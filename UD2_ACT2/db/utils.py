from sqlite3 import Connection
from .querys import execute_read_query
from pathlib import Path
from datetime import datetime


def requestDatabasePath():
    # Retorna una ruta existente introducida por el usuario
    default_db_path = Path('db', 'veterinaria.db')
    while(True):
        db_path = Path(input(f"Introducir ruta de la base de datos [{default_db_path}]: ") or default_db_path)
        if(db_path.exists()):
            break
        else:
            print('La ruta no existe!')
    return str(db_path)

def getDatabaseTables(connection: Connection):
    # Retorna una lista con las tablas de la base de datos
    tables_raw: list = execute_read_query(connection, "SELECT name FROM sqlite_master WHERE type = 'table'")
    tables: list = list(map(lambda x: x[0], tables_raw))
    return tables

def getTableFieldsMD(connection: Connection, table: str):
    # Retorna una lista con los metadatos de los campos de una tabla
    table_fields: list = execute_read_query(connection, f'PRAGMA table_info({table})')
    return table_fields


def getTableRowsColumn(connection: Connection, table:str, field_name: str):
    # Retorna los valores de un determinado campo de todas las filas de la tabla
    fields_raw: list = execute_read_query(connection, f'SELECT {field_name} FROM {table};')
    fields: list = list(map(lambda x: x[0], fields_raw))
    return fields
    

def getFieldsName(fields: list):
    # Muestra los nombres de los campos a partir de los metadatos de este
    fields_name: list = []
    for field in fields:
        fields_name.append(field[1])
    return fields_name


def getForeignKeyList(connection: Connection, table: str):
    # Retorna una lista con las claves foraneas de la tabla
    return execute_read_query(connection, f'PRAGMA foreign_key_list({table})')

def getPrimaryKey(table_fields: list):
    # Retorna el nombre del campo PK de la tabla
    for field in table_fields:
        if isPrimaryKey(field):
            return field
        

def questionTable(tables: list):
    # Pregunta al usuario la tabla a modificar y la retorna
    print(f'Tablas disponibles: {tables}')
    table: str = None
    while(True):
        table = input('Selecciona la tabla a modificar: ')
        if table in tables:
            break
        else:
            print('Selecciona una tabla que exista')
    return table


def __drawLine(table: str):
    # Retorna una línea con la longitud del nombre de la tabla para hacer simetria
    line: list = []
    for x in range(len(table)):
        line.append('-')
    return ''.join(line)

def showRows(connection: Connection, table: str):
    # Muestra las filas de la tabla
    rows: list = execute_read_query(connection, f'SELECT * FROM {table}')
    print(f'{__drawLine(table)*2}{table.upper()}{__drawLine(table)*3}')
    for row in rows:
        print(row)
    print(f'{__drawLine(table)*2}{__drawLine(table)}{__drawLine(table)*3}')
    

def validatePrimaryKey(connection: Connection, table: str, field_name: str, field_value):
    # Comprueba que la clave primaria no existe en ningún otro campo
    pk_fields_raw: list = getTableRowsColumn(connection, table, field_name)
    pk_fields: list = list(map(str, pk_fields_raw))
    return field_value not in pk_fields

def getReferenceFields(connection: Connection, table: str, field_name: str):
    # Retorna una lista con los valores referenciados y el nombre de la tabla referenciada
    fk_list: list = execute_read_query(connection, f'PRAGMA foreign_key_list({table})')
    fk_md_raw: tuple = tuple(filter(lambda fk_md: fk_md[3] == field_name, fk_list))
    fk_md = fk_md_raw[0]
    reference_table: str = fk_md[2]
    reference_table_field: str = fk_md[4]
    reference_values: list = getTableRowsColumn(connection, reference_table, reference_table_field)
    return reference_values, reference_table


def returnIfExists(list: list, request_msg: str):
    # Comprueba si existe el elemento introducida por el usuario en la lista
    while(True):
        element: str = input(request_msg)
        if element in list:
            return element
        else:
            print('Selecciona un campo existente')
    

def returnIfNotExists(list: list, request_msg: str):
    # Comprueba si existe el elemento introducida por el usuario en la lista
    while(True):
        element: str = input(request_msg)
        if element not in list:
            return element
        else:
            print('Selecciona un campo existente')
    

def requestFieldData(connection: Connection, table: str, field: tuple, field_name: str, request_msg: str, inversion: bool = False):
    # Pregunta al usuario el valor del campo y lo retorna
    field_is_pk: bool = isPrimaryKey(field)
    field_is_fk: bool = isForeignKey(connection, table, field_name)
    condition: bool = None
    
    while(True):
        if field_is_fk: 
            reference_values: list = getReferenceFields(connection, table, field_name)
            showRows(connection, reference_values[1])
            
        value: str = input(request_msg)
        
        if isIntegerType(field): 
            condition = requestIntegerInt(value)
        if isVarcharType(field): 
            size: int = int(field[2][8:10])
            condition = requestVarcharSize(value, size)
        if isDateType(field): 
            condition = requestDateFormat(value)
            
        if condition:
            if field_is_pk:
                if (validatePrimaryKey(connection, table, field_name, value)):
                    if inversion: print('Seleccione un campo existente para filtrarlo')
                    else: return value
                else:
                    if inversion: return value
                    else: print('Este campo es una clave primaria, y debe ser única')
            elif field_is_fk:
                if (value in reference_values[0]):
                    return value
                else:
                    print('Este campo es una clave foranea, y debe recibir un campo referenciado')
            else:
                return value
        else:
            print('Asegurate de introducir datos acordes al tipo de campo')


def requestIntegerInt(integer: str):
    return integer.isdigit()
    
               
def requestVarcharSize(varchar: str, size: int):
    # Comprueba el tamaño del str introducido por el usuario
    return len(varchar) <= size


def requestDateFormat(date: str):
    # Comprueba el formato de la fecha introducida por el usuario
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except:
        print('Asegurate de respetar el formato YYYY-MM-DD')
        return False


def isPrimaryKey(field: tuple):
    # Comprueba si field es clave primaria
    # Parametros: tuple con los metadatos de un campo
    return field[5] == 1

def isForeignKey(connection: Connection, table: str, field_name: str):
    # Comprueba si el campo es una clave foranea
    fk_list: list = getForeignKeyList(connection, table)
    return any(fk[3] == field_name for fk in fk_list)

def isIntegerType(field: tuple):
    # Comprueba si field es un integer o int
    return field[2] == 'INT'

def isVarcharType(field: tuple):
    # Comprueba si field es un varchar
    return field[2][:7] == 'VARCHAR'
    
def isDateType(field: tuple):
    # Comprueba si field es una fecha
    return field[2] == 'DATE'
