
print('VALIDANDO CREDENCIALES')
nom = input('Usuari: ')
passwd = input('Contrasenya: ')

try:
    with open('credenciales.txt', 'r') as fileReader:
        login = False
        for linea in fileReader:
            linea = linea.rstrip('\n')
            credencials = linea.split('-')
            if nom == credencials[0]:
                if passwd == credencials[1]:
                    print('Acceso permitido')
                    login = True
                    break
        if not login:
            print('Acceso denegado')       
except:
    print('File not found!')
        


