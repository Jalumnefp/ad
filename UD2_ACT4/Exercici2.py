from db.mariadb.querys import execute_query as mariadb_execute_query
from db.mariadb.utils import getDatabaseConnection as getMariadbDatabaseConnection
from db.sqlite.utils import getTableFieldsMD, getDatabaseTables, getDatabaseConnection as getSqlite3DatabaseConnection, createMariadbTableRows

from sqlite3 import Connection as sqliteConnection
from mariadb import Connection as mariadbConnection


def createTables(sqlite_connection: sqliteConnection, mariadb_connection: mariadbConnection, tables_names):
    for table_name in tables_names:
        table_fields: list = getTableFieldsMD(sqlite_connection, table=table_name)
        table_rows: str = createMariadbTableRows(sqlite_connection, table_name, table_fields)
        query: str = f'CREATE TABLE IF NOT EXISTS {table_name} ({table_rows});'
        mariadb_execute_query(mariadb_connection, query)

def main():
    sqlite_connection: sqliteConnection = getSqlite3DatabaseConnection()
    mariadb_connection: mariadbConnection = getMariadbDatabaseConnection()
        
    sqlite_tables: list = getDatabaseTables(sqlite_connection)
    
    sqlite_tables: list = getDatabaseTables(connection=sqlite_connection)
    createTables(sqlite_connection, mariadb_connection, sqlite_tables)

main()