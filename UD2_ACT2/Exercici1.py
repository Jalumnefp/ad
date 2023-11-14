from sqlite3 import Connection
from db.connection import create_connection
from db.querys import execute_query
from db.utils import getDatabaseTables, getFieldsName, getTableFieldsMD, questionTable, requestDatabasePath, showRows, requestFieldData, getTableRowsColumn


def getFormatDataFields(connection: Connection, table: str, table_fields: list):
    # Retorna los valores de los campos introducidos por el usuario formateados para la consulta
    table_fields_name: list = getFieldsName(table_fields)
    formated_names: list = []
    showRows(connection, table)
    print(f'Campos de la tabla: {table_fields_name}')
    for field, field_name in zip(table_fields, table_fields_name): 
        request_msg: str = f"Escribe el valor de {field_name}: "
        data_field: str = requestFieldData(connection, table, field, field_name, request_msg)
        formated_names.append(f"'{data_field}'")
    return ', '.join(formated_names)

def insertData(connection: Connection, table: str):
    # Inserta los datos preguntados al usuario
    table_fields: list = getTableFieldsMD(connection, table)
    table_fields_name: list = getFieldsName(table_fields)
    table_fields_format: str = ', '.join(table_fields_name)
    data_to_insert: str = getFormatDataFields(connection, table, table_fields)
    execute_query(connection, f'INSERT INTO {table}({table_fields_format}) VALUES ({data_to_insert});')

def main():
    db_path: str = requestDatabasePath()
    connection: Connection = create_connection(db_path)
    tables: list = getDatabaseTables(connection)
    table: str = questionTable(tables)
    '''insertData(connection, table)
    showRows(connection, table)'''
    
    print(getTableRowsColumn(connection, 'propietario', 'nombre'))

main()