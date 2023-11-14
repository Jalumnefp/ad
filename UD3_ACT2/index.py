from peewee import *
from db.models import*


def menu():
    print('-----------------------------------------------------------------')
    print('\n 0. Eixir')
    print(' 1. Llista la informació de tots els planetes.')
    print(' 2. Llista la informació dels personatges (characters) que\n    perteneixen a la Orden Jedi.')
    print(' 3. Llista el nom dels personatges que moren en el episodi\n    III, junt al nom del seu assasí.')
    print(' 4. Llista la informació de tots els planetes (planets) el\n    diàmetre dels quals estiga contingut entre dos valors\n    donats(els dóna l\'usuari).\n')
    print('-----------------------------------------------------------------')


def consulta1():
    query = Planets.select()
    for row in query:
        print(row.id, row.name)

def consulta2():
    query = Affiliations().select().where(Affiliations.affiliation=='Jedi Order')
    for row in query:
        print(row.id_characters)

def consulta3():
    ch = Characters.alias()
    kr = Characters.alias()
    fm = Films.alias()
    query = (Deaths().select(ch.name, kr.name)
                .join(ch, on=Deaths.id_character==ch.id)
                .join(kr, on=Deaths.id_killer==kr.id)
                .join(fm, Deaths.id_film==fm.id)
                .where(fm.id==3)
            )
    for chunk in chunked(query, 2):
        print('   '.join(value for value in chunk))

    
def consulta4():
    d1 = int(input('Diametre A: '))
    d2 = int(input('Diametre Z: '))
    query = Planets.select().where(Planets.diameter).between(d1, d2)
    for row in query:
        print(row.id, row.name, row.diameter)

def main():
    while(True):
        menu()
        answ = int(input('Resposta: '))
        if answ == 0:
            break
        elif answ == 1:
            consulta1()
        elif answ == 2:
            consulta2()
        elif answ == 3:
            consulta3()
        elif answ == 4:
            consulta4()


main()