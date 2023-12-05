from sqlite3 import Connection
from db.connection import create_connection
from db.querys import execute_read_query
from db.utils import showRows, getTableFieldsMD, requestFieldData, requestDatabasePath, questionTable, getDatabaseTables, getForeignKeyList


def getForeignKeysName(fk_list: list):
    # Muestra los nombres de los campos a partir de los metadatos de este
    fk_name: list = []
    fk_referenced_table: list = []
    fk_referenced_field: list = []
    for field in fk_list:
        fk_name.append(field[3])
        fk_referenced_table.append(field[2])
        fk_referenced_field.append(field[4])
    return fk_name, fk_referenced_table, fk_referenced_field

def filterWithForeignKey(connection: Connection, table: str, fk_list: list):
    # Retorna una llista amb les dades filtrades
    fk_md: list = getForeignKeysName(fk_list)
    fk_names: list = fk_md[0]
    referenced_tables: list = fk_md[1]
    referenced_ids: list = fk_md[2]
    if len(fk_names) > 1:
        print(f'Esta tabla contiene varias claves foraneas: {fk_names}')
        fk_selected: str = input('Seleccione una: ')
    else:
        fk_name: str = fk_names[0]
        referenced_table: str = referenced_tables[0]
        referenced_id: str = referenced_ids[0]
        referenced_field: tuple = tuple(filter(lambda i: i[1] == referenced_id, getTableFieldsMD(connection, referenced_table)))
        showRows(connection, referenced_table)
        filter_value: str = requestFieldData(connection, referenced_table, referenced_field[0], referenced_id, 'Introduce pk: ', True)
    return list(execute_read_query(connection, f"SELECT * FROM {table} WHERE {fk_name} = '{filter_value}'"))
    


def main():
    db_path: str = requestDatabasePath()
    connection: Connection = create_connection(db_path)
    tables: list = getDatabaseTables(connection)
    table: str = questionTable(tables)
    fk_list: list = getForeignKeyList(connection, table)

    if fk_list != []:
        filtered_table: list = filterWithForeignKey(connection, table, fk_list)
        if filtered_table != []:
            for row in filtered_table:
                print(row)
        else:
            print('Vacío')
    else:
        print('La tabla seleccionada no contiene ninguna clave foranea que filtrar.')
    
main()
