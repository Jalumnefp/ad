from mariadb import Connection, Error


def create_database(connection: Connection, query: str):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_query(connection: Connection, query: str):
    with connection.cursor() as cursor:
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred.", "Probablemen les dades ja s'han insertat")


def execute_prepared_query(connection: Connection, query: str, values: list):
    with connection.cursor(prepared=True) as cursor:
        try:
            for v in values:
                cursor.execute(query, v)
            connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred.", "Probablemen les dades ja s'han insertat")


def execute_read_query(connection: Connection, query: str):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_prepared_query(connection: Connection, query: str, values: list):
    cursor = connection.cursor(prepared=True)
    result = []
    try:
        for v in values:
            cursor.execute(query, v)
            result.append(cursor.fetchall())
        return result
    except Error as e:
        print(f"The error '{e}' occurred")