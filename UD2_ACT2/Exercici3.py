from sqlite3 import Connection
from db.connection import create_connection
from db.utils import requestDatabasePath, showRows, questionTable, getDatabaseTables

def main():
    db_path: str = requestDatabasePath()
    connection: Connection = create_connection(db_path)
    tables: list = getDatabaseTables(connection)
    table: str = questionTable(tables)
    showRows(connection, table)
    
main()
    