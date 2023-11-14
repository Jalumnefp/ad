#########################################
# UNIDAD 3                              #
# Ejercicio obligatorio (ESQUEMA)       #
#########################################
import random, csv, pickle, json

#################################################################    
# DEFINICIÓN DE FUNCIONES                                       #
#################################################################
def validar_credenciales():
    '''Pide usuario y contraseña y comprueba si está autorizado.
    
       Parámetros de salida:
         - autorizo: indica si está autorizado o no.
         - usuario: indica el nombre del usuario actual.
         - contras: indica la contraseña del usuario actual.
    '''
    
    autorizo = False
    
    print("ACCESO AL SISTEMA")
    usuario = input("\tUsuario: ")
    contras = input("\tContraseña: ")
    
    try:
        with open('data/credencials.txt', 'r') as fileReader:
            for linea in fileReader:
                linea = linea.rstrip('\n')
                credencials = linea.split('-')
                if usuario == credencials[0]:
                    if contras == credencials[1]:
                        print('Acceso permitido')
                        autorizo = True
                        break

    except:
        print('Error archivo')    
    
    return (autorizo, usuario, contras)

        
def valida_opcion():
    '''Función que muestra un menú y valida que la opción sea correcta
    
       Parámetros de salida:
         - opcion: opción seleccionada por el usuario.
    '''    

    opc_correctas = ['1', '2', '3', '4', '5', '0']
    
    #Mostramos el menú y solicitamos la operación al usuario
    opcion = ''
    while opcion not in opc_correctas:
        print()
        print("=============================")            
        print("   GAMIFICACIÓN EN EL AULA   ")
        print("=============================")
        print(" 1 - Cargar datos del fichero")
        print(" 2 - Imprimir datos ")
        print(" 3 - Jugar ")
        print(" 4 - Guardar datos ")
        print(" 5 - Cambiar contraseña ")
        print(" 0 - SALIR ")
        print("-----------------------------")    
        opcion = input("Dame la opción: ")
        if opcion not in opc_correctas:
            print("Por favor, vuelve a intentarlo.")
        else:
            print()       
    return opcion


def selec_formato():
    '''
    Muestra al usuario un menú donde seleccionar el tipo de formato.
    Retorna el formato seleccionado.
    '''
    formato = 0
    while(True):
        formato: int = int(input("Formatos disponibles:\n  1: txt\n  2: json\n  3: csv\n  4: pckl\nRespuesta: "))
        if formato == 1:
            return 'txt'
        elif formato == 2:
            return 'json'
        elif formato == 3:
            return 'csv'
        elif formato == 4:
            return 'pckl'

    
def cargar_jugadores():
    '''Carga los datos de los jugadores desde el fichero que el usuario seleccione" 
    
       Parámetros de salida: 
         - jugadores: lista con los datos de los jugadores. Los datos de cada jugador
           son de tipo diccionario y tienen el formato <nombre_jugador-nombre_personaje-lista_herramientas-vida>
    '''
    print("CARGAR DATOS")

    answ = selec_formato()

    if answ == 'txt': return carga_jugadores_txt()
    elif answ == 'json': return carga_jugadores_json()
    elif answ == 'csv': return carga_jugadores_csv()
    elif answ == 'pckl': return carga_jugadores_pckl()
    
    
def carga_jugadores_csv():
    '''
    Carga los datos de un fichero csv
    Retorna la lista con la informacion
    '''
    jugadores = []
    try:
        with open('data/dades_jugadors.csv', 'r', encoding='utf-8') as fileReader:
            lectura = csv.reader(fileReader, delimiter='-')
            for d in lectura:
                jugadores.append({
                        "nombre_jugador": d[0],
                        "personaje": d[1],
                        "herramientas": d[2].split(','),
                        "vida": d[3].split('\n')[0]
                    })
            print(jugadores)
    except Exception as e:
        print("El fichero 'datos_jugadores.csv' no se ha podido abrir:", e)
    finally:
        return jugadores

def carga_jugadores_json():
    '''
    Carga los datos de un fichero json
    Retorna la lista con la informacion
    '''
    jugadores = []
    try:
        with open('data/dades_jugadors.json', 'r', encoding='utf-8') as fileReader:
            jugadores = json.load(fileReader)
        print(jugadores)
    except Exception as e:
        print("El fichero 'datos_jugadores.json' no se ha podido abrir:", e)
    finally:
        return jugadores

def carga_jugadores_pckl():
    '''
    Carga los datos de un fichero pckl
    Retorna la lista con la informacion
    '''
    jugadores = []
    try:
        with open('data/dades_jugadors.pckl', 'rb') as fileReader:
            jugadores = pickle.load(fileReader)
        print(jugadores)
    except Exception as e:
        print("El fichero 'datos_jugadores.pckl' no se ha podido abrir:", e)
    finally:
        return jugadores
    

def carga_jugadores_txt():
    '''
    Carga los datos de un fichero txt
    Retorna la lista con la informacion
    '''
    jugadores = []    
    try: 
        with open('data/dades_jugadors.txt', 'r', encoding='utf-8') as fileReader:
            for line in fileReader:
                temp = line.split('-')
                jugadores.append(
                    {
                        "nombre_jugador": temp[0],
                        "personaje": temp[1],
                        "herramientas": temp[2].split(','),
                        "vida": temp[3].split('\n')[0]
                    }
                )
            print(jugadores)
        print("Datos cargados correctamente.")
    except:
        print("El fichero 'datos_jugadores.txt' no se ha podido abrir.")
    finally:
        return jugadores


def lee_jugador(jugadores, usuario):
    '''Crea un diccionario con los datos del jugador actual.
    
       Parámetros de entrada:
        - jugadores: lista con los datos de todos los jugadores.
        - usuario: nombre del jugador validado en el sistema.
        
       Salida:
         - diccionario con los datos del jugador actual.
    '''
    jugador = {}
    
    for jug in jugadores:        
        if jug['nombre_jugador'] == usuario:            
            jugador = jug.copy()
            break
    print(jugador)
    return jugador


def imprimir_datos(jugador):
    '''Imprime los datos del jugador actual.
    
       Parámetros de entrada:
         - jugador: diccionario con los datos del jugador actual.
    '''
    if jugador == {}:
        print("Actualmente no hay ningún jugador cargado.")
    else:
        print("DATOS DEL JUGADOR ACTUAL")
        print("\tJugador: ", jugador['nombre_jugador'])
        print("\tPersonaje: ", jugador['personaje'])

        print("\tHerramientas: ", end="")
        for herramienta in jugador['herramientas']:
            print(herramienta, end=', ')

        print("\n\tVida: ", jugador['vida'], '\n')        


def pide_herramienta(lista_herramientas):
    '''Solicita por pantalla la herramienta que quiere utilizar el jugador.
    '''
    sigue = True
    while sigue:
        print("Herramientas disponibles: ", lista_herramientas)
        herramienta = input("¿Qué herramienta vas a utilizar? ")
        if herramienta in lista_herramientas:
            sigue = False
    return herramienta


def jugar(jugadores_anterior, jugador_actual):
    '''El jugador utiliza una herramienta y gana/pierde vida.
    
       Parámetros de entrada:
         - jugadores_anterior: lista original de jugadores antes de modificarla.
         - jugador_actual: diccionario con los datos del jugador actual.
         
       Parámetros de salida:
         - jugadores: lista con los datos modificados del jugador actual.
    '''    
    if jugadores_anterior == []:
        print("Actualmente no hay ningún jugador cargado.")
        jugadores = []
    else:
        jugadores = jugadores_anterior.copy()
                
        print("¡A JUGAR!")
        print("Vida: {}\n".format(jugador_actual["vida"]))
        
        if len(jugador_actual["herramientas"]) == 0:
            print("No te quedan herramientas disponibles.")
        else:
            #PROFE - Mostrar las herramientas disponibles.
            print('Herramientas: ', jugador_actual['herramientas'])
            #PROFE - Pedir la herramienta que se va a utilizar (usa "pide_herramienta")
            objeto = pide_herramienta(jugador_actual['herramientas'])
            #PROFE - Calcular la vida disponible usando el resultado de "gana_pierde".
            gana_pierde = random.randint(-5, +5)
            vida = int(jugador_actual['vida']) + gana_pierde 
            #PROFE - Informar de la herramienta utilizada y la vida disponible.
            print(f'Has usado esto: {objeto}.\nTe faltan {vida} puntos de vida ({gana_pierde}).')
            #PROFE - Actualizar la lista de jugadores.
            jugador_actual['herramientas'].remove(objeto)
            jugador_actual.update({"vida": f"{vida}"})
            for jug in jugadores:
                if jug['nombre_jugador'] == jugador_actual['nombre_jugador']:            
                    jug.update({"vida": f"{vida}"})
                    break
                    
    return jugadores       
    
    
def formatea_herramientas(mi_lista):
    '''Recibe una lista de herramientas y devuelve una cadena con las
       herramientas separadas por una coma.
       
       Parámetros de entrada:
         - mi_lista: lista de herramientas
         
       Parámetros de salid:
         - cadena: cadena de texto que contiene las herramientas separadas por comas.
    '''
    cadena = ''
    for h in mi_lista:
        if cadena == '':
            cadena = h
        else:
            cadena = cadena + ',' + h
    return cadena


def get_format_playerdata_txt(jugadors):
    '''Recibe una lista de jugadores y devuelve una cadena con los datos de cada jugador
       formateados.

       Formato: nombre-tipo-herramientas_lista-vida

       Parámetros de entrada
         - jugadors: lista de jugadores
        
       Parámetros de salida:
         - ''.join(user_info): transformación de la lista user_info a string, la cual contiene strings de los jugadores formateados
    
    
    '''
    user_info = []
    
    for jugador in jugadors:
        nom = jugador.get('nombre_jugador')
        clase = jugador.get('personaje')
        eines = formatea_herramientas(jugador.get('herramientas'))
        vida = jugador.get('vida')
        user_info.append(f'{nom}-{clase}-{eines}-{vida}\n')
    
    return ''.join(user_info)
    

def guardar_datos(jugadores):
    '''Guarda los datos de un diccionario en el fichero "datos_jugadores.txt" 
    
       Parámetros de entrada:
         - jugadores: lista con los datos de los jugadores.
         
       Salida:
         - Actualiza el fichero "datos_jugadores.txt"         
    '''
    print("GUARDAR DATOS")
    
    if (len(jugadores) == 0):
        print("Actualmente no hay ningún jugador cargado.")
    else:
        answ = selec_formato()
        if answ == 'txt': return guardar_datos_txt(jugadores);
        elif answ == 'json': return guardar_datos_json(jugadores)
        elif answ == 'csv': return guardar_datos_csv(jugadores)
        elif answ == 'pckl': return guardar_datos_pckl(jugadores)
    print("Datos guardados en el fichero.") 
        

def guardar_datos_csv(jugadores):
    '''
    Guarda los datos en un fichero csv
    Parametro list con los jugadores
    '''
    try:
        with open('data/dades_jugadors.csv', 'w', encoding='utf-8') as fileWrite:
            writer =csv.writer(fileWrite, delimiter='-')
            for data in jugadores:
                row = [data['nombre_jugador'], data['personaje'], ','.join(data['herramientas']), data['vida']]
                writer.writerow(row)
            
    except Exception as e:
        print("El fichero 'datos_jugadores.csv' no se ha podido abrir:", e)

def guardar_datos_json(jugadores):
    '''
    Guarda los datos en un fichero json
    Parametro list con los jugadores
    '''
    try:
        with open('data/dades_jugadors.json', 'w', encoding='utf-8') as fileWrite:
            obj_json = json.dumps(jugadores, ensure_ascii=False)
            fileWrite.write(obj_json)
            
    except Exception as e:
        print("El fichero 'datos_jugadores.json' no se ha podido abrir:", e)

def guardar_datos_pckl(jugadores):
    '''
    Guarda los datos en un fichero pckl
    Parametro list con los jugadores
    '''
    try:
        with open('data/dades_jugadors.pckl', 'wb') as fileWrite:
            pickle.dump(file=fileWrite, obj=jugadores)
    except Exception as e:
        print("El fichero 'datos_jugadores.pckl' no se ha podido abrir:", e)

def guardar_datos_txt(jugadores):
    '''
    Guarda los datos en un fichero txt
    Parametro list con los jugadores
    '''
    try:
        #PROFE - Abrimos el fichero "datos_jugadores.txt" para sobreescribir.
        with open('data/dades_jugadors.txt', 'w', encoding='utf-8') as fileWriter:
        #PROFE - Para cada jugador de la lista, escribimos línea con sus datos respetando el formato utilizado originalmente.
            fileWriter.writelines(get_format_playerdata_txt(jugadores))
    except:
        print("El fichero 'datos_jugadores.txt' no se ha podido abrir.")



def get_format_passwd(data):
    '''Recibe una lista de los usuarios y contraseñas y devuelve estos datos formateados
    
        Formato: nombre-contraseña

       Parámetros de entrada:
        - data: lista de listas con los usuarios y contraseñas

       Parámetros de salida:
        - ''.join(result): transformación de la lista result a string, la cual contiene strings de los usuarios y contraseñas formateados
    '''
    result = []
    for d in data:
        result.append(f'{d[0]}-{d[1]}\n')
    return ''.join(result)
        

def cambiar_contrasenya(usuario, vieja_contra):
    '''Función que permite cambiar la contraseña de un usuario.  
    
       Parámetros de entrada: 
         - Usuario actual
         - Contraseña actual
         
       Salida:
         - Actualiza el fichero "credenciales.txt"
         - Devuelve la nueva contraseña, o la vieja si no se ha cambiado.
    '''
    print("CAMBIO DE CONTRASEÑA")

    intentos = 3
    while(intentos != 0):
    #PROFE - Pide contraseña vieja.
        old_passwd = input('Contraseña: ')
    #PROFE -   Si no es correcta, tiene dos intentos más.
        if old_passwd == vieja_contra:
            #PROFE -   Si es correcta, pide contraseña nueva.
            while(True):
                new_passwd = input('Nueva contraseña: ')
                if new_passwd == old_passwd:
                    print('No pongas la misma contraseña')
                else:
                    break
            break
        else:
            intentos -= 1
            print(f'Contraseña incorrecta.\nIntentos restantes: {intentos}')
            
    #PROFE - Devuelve la contraseña actual.
    try:
        data = []
        with open('data/credencials.txt', 'r', encoding='utf-8') as fileReader: 
            
            for linea in fileReader:
                linea = linea.rstrip('\n')
                temp = linea.split('-')
                if temp[0] == usuario:
                    temp[1] = new_passwd
                data.append(temp)
        with open('data/credencials.txt', 'w', encoding='utf-8') as fileWriter:
            fileWriter.writelines(get_format_passwd(data))              
    except:
        print('Error')
    
    
#################################################################   
# PROGRAMA PRINCIPAL                                            #
################################################################    

jugadores = [] #Creamos la lista que contendrá los datos
jugador = {} #Creamos el diccionario vacío del jugador actual
#Validamos las credenciales
credencial = validar_credenciales()
autorizo = credencial[0]
usuario = credencial[1]
contras = credencial[2]
if autorizo == True:
    print("\n\tBienvenid@ al sistema " + usuario.upper() + ".")
    opcion = valida_opcion()
    while opcion != '0':
        if opcion == '1': #Cargar datos del fichero
            #Carga en la lista "jugadores" los datos del fichero "jugadores.txt"
            #PROFE - Llama a la función cargar_jugadores() y recoge el valor de salida.
            jugadores = cargar_jugadores()
            #Lee los datos del jugador actual y los guarda en el diccionario "jugador"
            jugador = lee_jugador(jugadores, usuario)
        elif opcion == '2': #Imprime los datos del jugador actual
            #PROFE - Llama a la función imprimir_datos() pasándole el parámetro de entrada.
            imprimir_datos(jugador)
        elif opcion == '3': #Jugar
            #PROFE - Llama a la función jugar() pasándole la lista de jugadores y los datos del jugador actual.
            #PROFE - Además, recibe la lista de jugadores modificada.
            jugadores = jugar(jugadores, jugador)
        elif opcion == '4': #Guardar datos
            #PROFE - Llama a la función guardar_datos() pasándole la lista de jugadores.
            guardar_datos(jugadores)
        elif opcion == '5': #Cambiar contraseña
            #PROFE - Llama a la función cambiar_contrasenya() pasándole el usuario y contraseña original.
            #PROFE - Además, recibe la contraseña actual del usuario.
            cambiar_contrasenya(usuario, contras)
        opcion = valida_opcion()
else:
    input("Usuario no autorizado.")