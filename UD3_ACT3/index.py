from sqlalchemy import create_engine, Engine
from pathlib import Path
from db.db_models import Base, Clinic, Owner, Pet

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
        db_path = Path(input('Database path [db/veterinaria.db]: ') or 'db/veterinaria.db')
        
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

def createDatabase(engine: Engine):
    Base.metadata.create_all(engine)

def inserirDades(engine: Engine, tables: list):
    pass

def modificarMascota(engine: Engine):
    pass

def modificarPropietari(engine: Engine):
    pass

def modificarClinica(engine: Engine):
    pass


def visualitzarDades(engine: Engine):
    pass


def main():
    db_path: Path = requestDatabasePath()
    engine: Engine = create_engine(f'sqlite:///{db_path}')
    tables: list = [Clinic, Owner, Pet]
    createDatabase(engine)

    while(True):
        menu()
        answ = int(input('Resposta: '))
        if answ == 0:
            break
        elif answ == 1:
            inserirDades(engine, tables)
        elif answ == 2:
            modificarMascota(engine)
        elif answ == 3:
            modificarPropietari(engine)
        elif answ == 4:
            modificarClinica(engine)
        elif answ == 5:
            visualitzarDades(engine)
        else:
            print('Resposta invàlida!')

main()