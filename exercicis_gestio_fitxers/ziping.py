from zipfile import ZipFile
from pathlib import Path

def print_menu():
    print('===========================')
    print('        ZIP MANAGER        ')
    print('===========================')
    print('1. Comprimir               ')
    print('2. Descomprimir            ')
    print('0. Eixir                   ')
    print('---------------------------')


while(True):

    print_menu()

    answ = int(input('Resposta: '))

    if(answ == 0):

        print('Eixint....')
        break

    elif(answ == 1):

        print('Escribe archivos de entrada: (Detener con "exit")')
        archivos_entrada = []
        while(True):
            entrada = input('Archivo de entrada: ')
            if len(archivos_entrada) == 0 and entrada == 'exit':
                print('Al menos pon un archivo')
            elif entrada == 'exit':
                break
            else:
                archivos_entrada.append(entrada)

        eixida = input('Archivo de salida: ')

        with ZipFile(file=f'{eixida}.zip', mode='a') as zipper:
            for file in archivos_entrada:
                zipper.write(file)

    elif(answ == 2):
        
        unzip_file = input('Archivo a descomprimir: ')
        
        with ZipFile(f'{unzip_file}.zip', 'r') as unzipper:
            unzipper.extractall(path=Path.cwd())


        
    
