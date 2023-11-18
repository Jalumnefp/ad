from sqlalchemy import create_engine, Engine, update
from sqlalchemy.orm import Session, aliased
from pathlib import Path
from db.db_models import Base, Clinic, Owner, Pet

def menu():
    print('-------FULLMETAL SQLALCHEMY------')
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
    return list(map(lambda model: model.__tablename__, tables))


def requestTable(tables: list, table_names: list):
    while(True):
        answ = input(f'Selecciona una tabla [{table_names}]: ')
        if answ in table_names:
            for table in tables:
                if table.__tablename__ == answ:
                    return table
        else:
            print('Seleccriona una tabla que existixca')

def createDatabase(engine: Engine):
    Base.metadata.create_all(engine)

def inserirDades(engine: Engine, tables: list):
    table_names: list = getNameTables(tables)
    table = requestTable(tables, table_names)
    newfields: list = [input(f'Dada camp [{field}]: ') for field in table.__fields__]
    fields_dict: dict = dict(zip(table.__fields__, newfields))
    
    with Session(engine) as session:

        stmt = table(**fields_dict)

        session.add(stmt)
        session.commit()

def modificarMascota(engine: Engine):
    nom = input('Pet name: ')
    breed = input('New breed: ')
    desc = input('New desc: ')
    with Session(engine) as session:
        
        pet = session.query(Pet).filter_by(name=nom).first()
        
        pet.breed = breed
        pet.descr = desc
        
        session.commit()
        
        

def modificarPropietari(engine: Engine):
    nom = input('Owner name: ')
    email = input('New email: ')
    with Session(engine) as session:
        
        owner = session.query(Owner).filter_by(name=nom).first()
        
        owner.email = email
        
        session.commit()
        
def modificarClinica(engine: Engine):
    nom = input('Clinic name: ')
    addr = input('New addr: ')
    with Session(engine) as session:
        
        clinic = session.query(Clinic).filter_by(name=nom).first()
        
        clinic.addr = addr
        
        session.commit()

def printAllStmt(stmt):
    for row in stmt:
        print(row)
        
def consultaUno(engine):
    with Session(engine) as session:
        p = aliased(Pet)
        c = aliased(Clinic)
        stmt = (session
            .query(c, p)
            .join(p, p.clinic_id == c.id)
            .all()
        )
        
        printAllStmt(stmt)
            
def consultaDos(engine):
    breed = input('Breed a filtrar: ')
    with Session(engine) as session:
        p = aliased(Pet)
        o = aliased(Owner)
        stmt = (session
            .query(o)
            .join(p, p.owner_id == o.id)
            .filter(p.breed == breed)
            .all()   
        )
        
        printAllStmt(stmt)

def visualitzarDades(engine: Engine):
    print('1. Llistat de totes les mascotes associades a cada clínica.\n2. Llistat de tots els propietaris de mascotes amb un breed determinat')
    answ = int(input('Resposta: '))
    while(True):
        if answ == 1:
            consultaUno(engine)
            break
        elif answ == 2:
            consultaDos(engine)
            break
        else:
            print('Resposta incorrecta')
            
def main():
    db_path: Path = requestDatabasePath()
    engine: Engine = create_engine(f'sqlite:///{db_path}', echo=False)
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