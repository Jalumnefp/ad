vuelos = [
    {
        "origen": "valencia",
        "destinació": "menorca",
        "dia": "15-8",
        "classe": "turista"
    },
    {
        "origen": "extremadura",
        "destinació": "murcia",
        "dia": "12-9",
        "classe": "turista"
    },
    {
        "origen": "asturies",
        "destinació": "illes canaries",
        "dia": "22-1",
        "classe": "turista"
    }
]

barra = '========================='
menu = f'{barra}\n   GESTIÓN DE UN VUELO\n{barra}\n 1: Imprimir datos del vuelo\n 2: Imprimir un valor\n 3: Añadir <pasajeros>\n 4: Imprimir claves\n 5: Borrar clave\n 6: Imprimir todos los vuelos\n 0: SALIR\n{barra}\nDame la opción: '

while(True):
    answ = int(input(menu))
    print('\n')
    if answ == 0:
        print('EXIT...')
        break
    elif answ == 1:
        vuelo = int(input('Número de vuelo: '))
        print(vuelos[vuelo].items())
    elif answ == 2:
        vuelo = int(input('Número de vuelo: '))
        key_selected = input('Clau: ')
        if key_selected in vuelos[vuelo]:
            print(vuelos[vuelo].get(key_selected))
        else:
            print('La clau no existeix!')
    elif answ == 3:
        vuelo = int(input('Número de vuelo: '))
        num = int(input('Cantitat passatgers: '))
        vuelos[vuelo].setdefault('passatgers', num)
    elif answ == 4:
        vuelo = int(input('Número de vuelo: '))
        print(vuelos[vuelo].keys())
    elif answ == 5:
        vuelo = int(input('Número de vuelo: '))
        key_delete = input('Clau: ')
        if key_delete in vuelos[vuelo]:
            vuelos[vuelo].pop(key_delete)
        else:
            print('La clau no existeix!')
    elif answ == 6:
        for (n, v) in zip (range(len(vuelos)), vuelos):
            print('[{}] {}'.format(n, v))
    print('\n')
