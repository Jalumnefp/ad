from mariadb import connect, Error, Connection


def create_connection(host_name, user_name, user_password, db_name) -> Connection:
    connection = None
    try:
        connection = connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        connection.close()
    return connection