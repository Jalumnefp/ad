from db.querys import execute_read_query
from db.connection import connection

def show_metadata():
    tables: list = execute_read_query(connection, "SELECT t.name FROM sqlite_master t WHERE type = 'table'")

    for table in tables:
        print(table[0])
        table_info = execute_read_query(connection, f'PRAGMA table_info({table[0]})')
        for info in table_info:
            print(info[1])

show_metadata()
