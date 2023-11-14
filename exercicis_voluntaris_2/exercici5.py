print('Por favor, introduce una lista de numeros.')
lista = []
numero = 10
while(True):
    numero = int(input('Número (negativo para salir): '))
    if numero < 0:
        break
    else:
        lista.append(numero)

print(lista)