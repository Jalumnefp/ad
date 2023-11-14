vuelos = {
    "origen": "valencia",
    "destinació": "menorca",
    "dia": "15-8",
    "classe": "turista"
}

barra = '========================='
menu = f'{barra}\n   GESTIÓN DE UN VUELO\n{barra}\n 1: Imprimir datos del vuelo\n 2: Imprimir un valor\n 3: Añadir <pasajeros>\n 4: Imprimir claves\n 5: Borrar clave\n 0: SALIR\n{barra}\nDame la opción: '

while(True):
    answ = int(input(menu))
    if answ == 0:
        print('EXIT...')
        break
    elif answ == 1:
        print(vuelos.items())
    elif answ == 2:
        key_selected = input('Clau: ')
        print(ifKeyExistsIn(key_selected, vuelos))
    elif answ == 3:
        num = int(input('Cantitat passatgers: '))
        vuelos.setdefault('passatgers', num)
    elif answ == 4:
        print(vuelos.keys())
    elif answ == 5:
        key_delete = input('Clau: ')
        print(ifKeyExistsIn(key_delete, vuelos))