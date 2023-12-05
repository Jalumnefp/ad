barra = '======================='
menu = f'{barra}\n   DATOS DE UN JUEGO\n{barra}\n 1: Cargar datos\n 2: Modificar por clave\n 3: Guardar datos\n 0: SALIR\n{barra}\nDame la opción: '

jugadors = []

def valida_opcion(answ: int):
    options = [0, 1, 2, 3]
    return answ in options


def cargar_datos():
    try:
        with open('ad/datos_jugadors.txt', 'r', encoding='utf-8') as fileReader:
            for line in fileReader:
                temp = line.split('-')
                jugadors.append(
                    {
                        "nom": temp[0],
                        "personatge": temp[1],
                        "llista d'eines": temp[2].split(','),
                        "vida": int(temp[3].split('\n'))
                    }
                )
            print(jugadors)
    except:
        print('File not found')


def modificar_datos():
    if len(jugadors) == 0:
        print('No hay datos')
    else:
        print('\n', jugadors)
        jnom = input('Nom del jugador a modificar: ')
        for jmod in jugadors:
            if jnom == jmod.get('nom'):
                break
        clau = input('Clau: ')
        valor = input('Valor nou: ')
        print(jmod.update({clau: valor}))
    print(jugadors)
   
   
def get_format_playerdata():
    user_info = []
    for jugador in jugadors:
        nom = jugador.get('nom')
        clase = jugador.get('personatge')
        eines = ''
        for eina in jugador.get("llista d'eines"):
            if eina == jugador.get("llista d'eines")[len(jugador.get("llista d'eines"))-1]:
                eines += f'{eina}'
            else:
                eines += f'{eina},'
        vida = jugador.get('vida')
        user_info.append('{}-{}-{}-{}'.format(nom, clase, eines, vida))
    return ''.join(user_info)

     

def guardar_datos():  
    try:
        with open('ad/datos_jugadors.txt', 'w', encoding='utf-8') as fileWriter:
            fileWriter.writelines(get_format_playerdata())
    except:
        print('File error')
            

def main():
    while(True):
        answ = int(input(menu))
        if valida_opcion(answ):
            if answ == 0:
                print('Saliendo...')
                break
            elif answ == 1: 
                cargar_datos()
            elif answ == 2: 
                modificar_datos()
            elif answ == 3: 
                guardar_datos()
        else:
            print('Respuesta incorrecta')
        

main()




