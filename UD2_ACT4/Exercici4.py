from db.mariadb.querys import execute_read_query
from db.mariadb.utils import getDatabaseConnection
from db.sqlite.utils import getTableRowsColumn, returnIfExists

from mariadb import Connection


def main():
    connection: Connection = getDatabaseConnection()
    profesiones: list = getTableRowsColumn(connection, 'propietario', 'profesion')
    print(profesiones)
    profesion: str = returnIfExists(profesiones, 'Selecciona la profesión: ')
    result_raw = execute_read_query(connection, f"SELECT(num_mascotas_por_profesion('{profesion}'))")
    result = result_raw[0][0]
    print(result)
    
main()