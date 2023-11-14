import pickle

'''
Carrega les dades i les transforma en un pickle
'''

def carga_jugadores_txt():
    jugadores = []    
    try: 
        with open('backup/dades_jugadors.txt', 'r', encoding='utf-8') as fileReader:
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
    

with open('data/dades_jugadors.pckl', 'wb') as fileWriter:
    pickle.dump(obj=carga_jugadores_txt(), file=fileWriter)