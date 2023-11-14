from mariadb import Connection
from .connector import create_connection
from .querys import create_database


def requestDatabaseServer():
    # Retorna los datos para el conector de la base de datos
    default_ip = '127.0.0.1'
    default_username = 'star'
    default_password = 'wars'
    default_db_name = 'veterinaria'
    db_ip = input(f"Introducir ip del servidor [{default_ip}]: ") or default_ip
    db_name = input(f"Introducir nombre usuario [{default_username}]: ") or default_username
    db_passwd = input(f"Introducir contraseña usuario [{default_password}]: ") or default_password
    db = input(f"Introducir nombre base de datos [{default_db_name}]: ") or default_db_name
    
    return db_ip, db_name, db_passwd, db


def getDatabaseConnection():
    # Retorna una conexión a una base de datos (se asegura que la base de datos exista y si no la crea)
    mariadb_connection_info: list = requestDatabaseServer()
    mdb_ip: str = mariadb_connection_info[0]
    mdb_username: str = mariadb_connection_info[1]
    mdb_password: str = mariadb_connection_info[2]
    mdb_database: str = mariadb_connection_info[3]
    
    connection: Connection = create_connection(mdb_ip, mdb_username, mdb_password, None)
    create_database(connection, f"CREATE DATABASE IF NOT EXISTS {mdb_database}")
    connection = create_connection(mdb_ip, mdb_username, mdb_password, mdb_database)
    return connection



        