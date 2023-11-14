from db.querys import execute_query
from db.connection import connection


def crear_tables():
    crear_tabla_propietario = "CREATE TABLE IF NOT EXISTS propietario (id INT NOT NULL,nombre VARCHAR(50) NOT NULL,profesion VARCHAR(50) NOT NULL,fecha_nacimiento DATE,PRIMARY KEY (id));"

    crear_tabla_mascota = "CREATE TABLE IF NOT EXISTS mascota (id INT NOT NULL,nombre VARCHAR(50) NOT NULL,raza VARCHAR(50) NOT NULL,cliente INT NOT NULL,PRIMARY KEY (id),FOREIGN KEY (cliente) REFERENCES propietario(id));"

    execute_query(connection, crear_tabla_propietario)
    execute_query(connection, crear_tabla_mascota)

crear_tables()