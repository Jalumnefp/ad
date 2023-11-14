from db.mariadb.utils import getDatabaseConnection as getMariadbDatabaseConnection
from db.sqlite.querys import execute_read_query as sqlite_execute_read_query
from db.mariadb.querys import execute_query as mariadb_execute_query
from db.sqlite.utils import getDatabaseTables, getDatabaseConnection as getSqlite3DatabaseConnection

from sqlite3 import Connection as sqliteConnection
from mariadb import Connection as mariadbConnection


def formatFieldValues(table_data: list):
    table_rows: list = []
    
    for row_data in table_data:
        row_values: list = []
        for data in row_data:
            row_values.append(f"'{data}'")
        table_rows.append(', '.join(row_values))
    return table_rows

    
def insertTables(sqlite_connection: sqliteConnection, mariadb_connection: mariadbConnection, tables_names):
    for table_name in tables_names:
        table_data = sqlite_execute_read_query(sqlite_connection, f'SELECT * FROM {table_name}')
        formated_values: list = formatFieldValues(table_data)
        for values in formated_values:
            query: str = f'INSERT INTO {table_name} VALUES ({values})'
            mariadb_execute_query(mariadb_connection, query)


def main():
    sqlite_connection: sqliteConnection = getSqlite3DatabaseConnection()
    mariadb_connection: mariadbConnection = getMariadbDatabaseConnection()

    sqlite_tables: list = getDatabaseTables(sqlite_connection)
    
    sqlite_tables: list = getDatabaseTables(connection=sqlite_connection)
    insertTables(sqlite_connection, mariadb_connection, sqlite_tables)

main()