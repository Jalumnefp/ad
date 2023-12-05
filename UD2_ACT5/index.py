import datetime
from mariadb import Connection, Error
from db.mariadb.utils import getDatabaseConnection
from db.mariadb.query import execute_prepared_query, execute_read_prepared_query, execute_read_query


def menu():
    print('-------------------------------------------------------')
    print(' 1 -> Llistar planetes dins de tres rangues de diámetre')
    print(' 2 -> Insertar 3 personatges a l\'episodi 7            ')
    print(' 3 -> Llistar víctimes i assassins per episodi         ')
    print(' 0 -> Eixir                                            ')
    print('-------------------------------------------------------')

def filterPlanetsWithDiameterRange(connection: Connection, ranges: list):
    query: str = 'SELECT name, diameter FROM planets WHERE diameter BETWEEN %s AND %s'
    return execute_read_prepared_query(connection, query, ranges)

def insert3NewCharacter(connection: Connection, all_values: list):
    query: str = 'INSERT INTO characters(id, name, planet_id, created_date, updated_date) VALUES (%s, %s, %s, %s, %s)'
    execute_prepared_query(connection, query, all_values)
    insertCharacterToEpisodeVII(connection, all_values)
    
def insertCharacterToEpisodeVII(connection: Connection, raw_values: list):
    query: str = 'INSERT INTO character_films VALUES (%s, %s)'
    values: list = []
    for raw_value in raw_values:
        values.append((raw_value[0], 7))
    execute_prepared_query(connection, query, values)

def requestCharacters(connection: Connection):
    values_list: list = []
    planeta_id: int = 1
    create_date: str = '2014-12-20 21:17:56'
    update_date: str = '2014-12-20 21:17:56'
    for n in range(3):
        id: int = int(input('Id: '))
        name: str = input("Name: ")
        values_list.append((id, name, planeta_id, create_date, update_date))
    insert3NewCharacter(connection, values_list)

def showDiameters(ranges: list, results:list): 
    for rng, result in zip(ranges, results):
        print(rng)
        for row in result:
            print(f'\tName: {row[0]}, Diameter: {row[1]}')
            
def showVictimKillers(results: list):
    for result in results:
        for res in result:
            print(f'[{res[2].upper()}]  Víctima: [{res[0]}], Assassí: [{res[1]}]')

def requestDiameters(connection: Connection):
    ranges: list = []
    ranges_str: list = []
    for n in range(3):
        print(f'Rango número {n}:')
        diametre1: int = int(input("Diametre 1: "))
        diametre2: int = int(input("Diametre 2: "))
        ranges.append((diametre1, diametre2,))
        ranges_str.append(f'\nRANGE:[{diametre1}-{diametre2}]')
    results = filterPlanetsWithDiameterRange(connection, ranges)
    showDiameters(ranges_str, results)
    
def getEpisodes(connection: Connection):
    raw_episodes: list = execute_read_query(connection, 'SELECT episode FROM films')
    episodes: list = list(map(lambda it: it[0], raw_episodes))
    return episodes

def requestEpisodes(connection: Connection):
    episodes: list = []
    valid_episodes: list = getEpisodes(connection)
    print(f'Episodios: {valid_episodes} (Escriu EXIT per a eixir)')
    while(True):
        if len(episodes) == 6:
            break
        episode: str = input('Episodi: ')
        if episode.upper() == 'EXIT':
            break
        if episode in valid_episodes and episode not in episodes:
            episodes.append(episode)
        else:
            print('Seleccione un episodio existente y no repetido')
    return episodes

def showVictimAndKiller(connection: Connection):
    all_values: list = []
    query: str = '''
    SELECT c.name, k.name, f.episode FROM deaths d 
    JOIN characters c ON(c.id = d.id_character)
    JOIN characters k ON(k.id = d.id_killer)
    JOIN films f ON(f.id = d.id_film)
    WHERE f.episode = %s
    '''
    episodes: list = requestEpisodes(connection)
    for episode in episodes:
        all_values.append((episode,))
    result = execute_read_prepared_query(connection, query, all_values)
    showVictimKillers(result)

def main():
    connection: Connection = getDatabaseConnection()
    while(True):
        menu()
        option = int(input('Resposta: '))
        if option == 0:
            print('Eixint...')
            break
        elif option == 1:
            requestDiameters(connection)
        elif option == 2:
            requestCharacters(connection)
        elif option == 3:
            showVictimAndKiller(connection)
        else:
            print('Opción inválida')
    
main()