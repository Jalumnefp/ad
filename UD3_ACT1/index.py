from peewee import *
from pathlib import Path
from db.db_models import Clinic, Owner, Pet

def menu():
    print('-------------PEEWEE--------------')
    print('  1. Inserir dades               ')
    print('  2. Modificar mascota           ')
    print('  3. Modificar propietari        ')
    print('  4. Modificar clinica           ')
    print('  5. Visualitzar dades           ')
    print('  0. Eixir                       ')
    print('---------------------------------')

def requestDatabasePath():
    while(True):
        db_path = Path(input('Database path [db/database.db]: ') or 'db/database.db')
        
        if db_path.resolve().exists():
            return db_path
        else:
            print('The path no exists')

def getNameTables(tables: list):
    return list(map(lambda model: model._meta.name, tables))

def requestTable(tables: list, table_names: list):
    while(True):
        answ = input('Selecciona una tabla: ')
        if answ in table_names:
            for table in tables:
                if table._meta.name == answ:
                    return table
        else:
            print('Seleccriona una tabla que existixca')

def createDatabase(sqlite_db: SqliteDatabase, tables: list):
    sqlite_db.connect()
    sqlite_db.create_tables(tables)
    sqlite_db.close()

def inserirDades(sqlite_db: SqliteDatabase, tables: list):
    sqlite_db.connect()
    print('\n>>Inserció de dades <<')
    table_names = getNameTables(tables)
    print('Tables disponibles: ', table_names)
    table: Model = requestTable(tables, table_names)
    table_fields: list = table._meta.fields_list
    values: list = []
    for field in table_fields:
        if field != 'id':
            values.append(input(f'Nou valor de {field}: '))
    if table._meta.name == 'Clinic':
        Clinic(addr = values[0], name = values[1]).save()
    elif table._meta.name == 'Owner':
        Owner(email = values[0], name = values[1]).save()
    elif table._meta.name == 'Pet':
        Pet(id_clin = values[0], id_ownr = values[1], breed = values[2], desc = values[3], name = values[4]).save()
    sqlite_db.close()

def modificarMascota(sqlite_db: SqliteDatabase):
    sqlite_db.connect()
    id = input('Id pet: ')
    breed = input('New breed: ')
    desc = input('New desc: ')
    Pet.update(breed = breed, desc = desc).where(Pet.id == id).execute()
    sqlite_db.close()

def modificarPropietari(sqlite_db: SqliteDatabase):
    sqlite_db.connect()
    name = input('Owner name: ')
    email = input('New email: ')
    Owner.update(email = email).where(Owner.name == name).execute()
    sqlite_db.close()

def modificarClinica(sqlite_db: SqliteDatabase):
    sqlite_db.connect()
    name = input('Clinic name: ')
    addr = input('New addr: ')
    Clinic.update(addr = addr).where(Clinic.name == name).execute()
    sqlite_db.close()


def visualitzarDades(sqlite_db: SqliteDatabase):
    with sqlite_db.connection_context():
        print('1.- Mostrar mascotes i clinica')
        print('2.- Filtrar els propietaris de una raça')
        answ = int(input('Resposta: '))
        if answ == 1:
            clinic = Clinic.alias()
            query = Pet.select(Pet, clinic.id).join(clinic, on=clinic.id == Pet.id_clin)
            for row in query:
                print(f'\nMascota [\n\tid = {row.id},\n\tid_clinica = {row.id_clin},\n\tid_propietari = {row.id_ownr},\n\tbreed = {row.breed},\n\tdesc = {row.desc},\n\tname = {row.name},\n\tclinica asociada = {row.id_clin_id}\n]')
        elif answ == 2:
            breed = input('Breed: ')
            query = Owner.select().join(Pet).where(Pet.breed == breed).distinct()
            for row in query:
                print(f'\nOwner [\n\tid = {row.id},\n\taddr = {row.email},\n\tname = {row.name}\n]')


def main():
    db_path: Path = requestDatabasePath()
    sqlite_db = SqliteDatabase(db_path)
    tables = [Clinic, Owner, Pet]
    createDatabase(sqlite_db, tables)

    while(True):
        menu()
        answ = int(input('Resposta: '))
        if answ == 0:
            break
        elif answ == 1:
            inserirDades(sqlite_db, tables)
        elif answ == 2:
            modificarMascota(sqlite_db)
        elif answ == 3:
            modificarPropietari(sqlite_db)
        elif answ == 4:
            modificarClinica(sqlite_db)
        elif answ == 5:
            visualitzarDades(sqlite_db)
        else:
            print('Resposta invàlida!')

main()