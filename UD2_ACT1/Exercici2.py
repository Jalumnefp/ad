from db.querys import execute_query, execute_read_query
from db.connection import connection

def insertar_dades():
    insertar_propietario = "INSERT INTO propietario VALUES (1, 'María Martínez', 'Desarrolladora de software', '01-01-1980');"
    insertar_mascota = "INSERT INTO mascota VALUES (1, 'sansón', 'ratonero', 1);"

    execute_query(connection, insertar_propietario)
    execute_query(connection, insertar_mascota)

insertar_dades()