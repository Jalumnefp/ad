from sqlite3 import Error, connect

def create_connection(path):
    connection = None
    try:
        connection = connect(path)
        print("Connection to SQLite DB successfull")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

