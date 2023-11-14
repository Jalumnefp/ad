from db.MariadbConnector import create_connection
from db.MariadbQuerys import execute_query, execute_read_query


def showMenu():
    print('---------------------------------------------------STAR WARS WIKI----------------------------------------------------')
    print()
    print(' 1 - Llistar informació de tots els planetes')
    print(' 2 - Insereix tres nous registres en la taula films amb les dades dels episodis VII, VIII i IX')
    print(' 3 - Llista la informació dels personatges (characters) que perteneixen a la Orden Jedi')
    print(' 4 - Llista el nom dels personatges que moren en el episodi III, junt al nom del seu assasí.')
    print(' 0 - Eixir del programa')
    print()
    print('---------------------------------------------------------------------------------------------------------------------')


def selectOption():
    while(True):
        answ: int = int(input('Escriure opció: '))
        if answ in range(5):
            return answ
        else:
            print('Selecciona una opción vàlida!')

def getTableFields(connection, table_name: str):
    query: str = f'''
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = 'starwars'
    AND TABLE_NAME = '{table_name}'
    ORDER BY ORDINAL_POSITION;
    '''
    return execute_read_query(connection, query)


def showRows(table: list, fields: list):
    print('\n-----------------------------------------------------------------------------------------------------------------------')
    for row in fields:
        row: str = str(row[0])
        if len(row) > 13:
            row = row[:13]
        elif len(row) < 6:
            row += "    "
        print(row.upper(), end='\t')
    print('\n-----------------------------------------------------------------------------------------------------------------------')
    for row in table:
        for field in row:
            field = str(field)
            if len(field) > 13:
                field = field[:13]
            elif len(field) < 8:
                field += "    "
            print(field, end='\t')
        print()
    print('-----------------------------------------------------------------------------------------------------------------------')


def listPlanets(connection):
    query: str = 'SELECT id, name FROM planets'
    return execute_read_query(connection, query)


def insertNewEpisodys(connection):
    episodeVII: str = "7, 'EpisodeVII', 'The Force Awakens'"
    episodeVIII: str = "8, 'EpisodeVIII', 'The Last Jedi'"
    episodeIX: str = "9, 'EpisodeIX', 'The Rise of Skywalker'"
    query: str = f'INSERT INTO films(id, episode, title) VALUES ({episodeVII}), ({episodeVIII}), ({episodeIX})'
    execute_query(connection, query)



def listJedisData(connection):
    query = '''
    SELECT c.* FROM characters c 
    INNER JOIN character_affiliations ca ON(c.id = ca.id_character) 
    INNER JOIN affiliations a on(ca.id_affiliation = a.id) 
    WHERE a.affiliation='Jedi Order'
    '''
    return execute_read_query(connection, query)


def listKillsEp3(connection): 
    query: str = '''
    SELECT c.name, k.name FROM characters c 
    INNER JOIN deaths d ON(c.id = d.id_character) 
    INNER JOIN characters k ON(k.id = d.id_killer) 
    INNER JOIN films f ON(d.id_film = f.id) 
    WHERE f.id = 3;
    '''
    return execute_read_query(connection, query)


def main():
    connection = create_connection('127.0.0.1', 'star', 'wars', 'starwars')
    print(execute_read_query(connection, 'SHOW TABLES'))
    
    while(True):
        showMenu()
        option: int = selectOption()
        if option == 1:
            result = listPlanets(connection)
            fields = [('id', ), ('name',)]
            showRows(result, fields)
        elif option == 2:
            insertNewEpisodys(connection)
        elif option == 3:
            result = listJedisData(connection)
            fields = getTableFields(connection, 'characters')
            showRows(result, fields)
        elif option == 4:
            result = listKillsEp3(connection)
            fields = [('char_name',), ('killer_name',)]
            showRows(result, fields)
        else:
            print('Eixint del programa.....')
            break
        

main()