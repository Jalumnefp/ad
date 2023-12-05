nom = input('Hola, ¿como te llamas? ').capitalize()
print(nom, ',encantad@ de hablar contigo!')

option_cita = True
option_dada = True
option_anec = True

while(True):
    action = input(f'¿Que quieres hacer {nom}? (CITA, DADA, ANÉCDOTA) ')
    if action == '':
        print(f'Hasta la vista, {nom}.')
        break
    elif action.upper() == 'CITA':
        if option_cita:
            print('“Si penses que els usuaris dels teus programes són idiotes, només els idiotes usaran els teus programes” - Linus Torvalds')
        else:
            print('Segunda cita')
        option_cita = not option_cita
    elif action.upper() == 'DADA':
        if option_dada:
            print('“El codi binari és el llenguatge de les màquines.')
        else:
            print('Segunda dada')
        option_dada = not option_dada
    elif action.upper() == 'ANECDOTA':
        if option_anec:
            print('Ada Lovelace va ser una matemàtica britànica considerada la primera persona que va escriure un algorisme destinat a ser processat per una màquina.')
        else:
            print('Segunda anecdota')
        option_anec = not option_anec
    else:
        print('Opció incorrecta, prova un altra vegada.')

