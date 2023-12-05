from sqlite3 import Connection, Error, connect

def create_connection(path):
    connection: Connection = None
    try:
        connection = connect(path)
        print('Connection SQLite DB successfull')
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection