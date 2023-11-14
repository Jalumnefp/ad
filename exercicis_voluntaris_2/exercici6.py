players = ['Antonio', 'Ana', 'Ramona']

barra = '========================='
menu = f'{barra}\n     JUGADORS ONLINE\n{barra}\n 1: Llega un jugador nuevo\n 2: Se va un jugador\n 3: FIN\n{barra}\nDame la opción: '

while(True):
    option = int(input(menu))

    if option not in range(1, 4):
        print('error')
    else:
        if option == 3:
            print('Adios!')
            break
        elif option == 1:
            players.append(input('¿Quien eres? '))
            print('Lista de jugadores: ', players)
        elif option == 2:
            print(f'El jugador {players[0]} se ha ido')
            players.pop(0)
