from sqlite3 import Connection
from db.connection import create_connection
from db.querys import execute_query
from db.utils import returnIfExists, getTableRowsColumn, getTableFieldsMD, getFieldsName, getPrimaryKey, requestFieldData, requestDatabasePath, getDatabaseTables, questionTable, showRows


def questionDataField(table_fields_name: list):
    # Pregunta el campo a modificar y lo retorna
    print(f'Campos de la tabla: {table_fields_name}')
    request_msg: str = "Selecciona el campo a modificar: "
    field: str = returnIfExists(table_fields_name, request_msg)
    return field


def requestKeyValue(connection: Connection, table: str, pk_field: str):
    pk_list: list = getTableRowsColumn(connection, table, pk_field)
    while(True):
        pk_value: str = input('Introduce la clave del campo a modificar: ')
        if pk_value in pk_list:
            return pk_value
        else:
            print('No has introducido el campo correcto o la clave ya existe')


def updateData(connection: Connection, table: str):
    # Actualiza el campo con los datos proporcionados
    table_fields: list = getTableFieldsMD(connection, table)
    table_fields_name: list = getFieldsName(table_fields)
    pk_field_raw: tuple = getPrimaryKey(table_fields)
    pk_field: str = pk_field_raw[1]
    pk_field_value: str = requestKeyValue(connection, table, pk_field)
    field_to_mod: str = questionDataField(table_fields_name)
    request_msg: str = f"Nuevo valor del campo {field_to_mod}: "
    field_mod: tuple = tuple(filter(lambda i: i[1] == field_to_mod, table_fields))
    value: str = requestFieldData(connection, table, field_mod[0], field_to_mod, request_msg)
    execute_query(connection, f"UPDATE {table} SET {field_to_mod}='{value}' WHERE {pk_field} = '{pk_field_value}';")
    
def main():
    db_path: str = requestDatabasePath()
    connection: Connection = create_connection(db_path)
    tables: list = getDatabaseTables(connection)
    table: str = questionTable(tables)
    showRows(connection, table)
    updateData(connection, table)
    showRows(connection, table)

main()