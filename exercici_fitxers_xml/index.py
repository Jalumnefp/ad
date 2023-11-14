from bs4 import BeautifulSoup


def menu():
    '''
    Mostra per pantalla el menu
    '''
    print('<== XML MANAGER ==>')
    print(' 1.- Cargar archivo')
    print(' 2.- Añadir persona')
    print(' 3.- Borrar persona')
    print(' 4.- Mostra persona')
    print(' 5.- Modificar campo')
    print(' 6.- Guardar archivo')
    print(' 0.- Salir')


def seleccionarOpción():
    '''
    Retorna la opció seleccionada en cas de que siga correcta
    Return int amb la resposta
    '''
    menu()
    while(True):
        answ = int(input('Respuesta: '))
        if answ not in range(7):
            print('Proporcione una respuesta válida.')
        else:
            return answ


def mostrarPersonas(persones: list):
    '''
    Mostra per pantalla les persones carregades
    Parametre list amb les persones carregades
    '''
    print('==>PERSONAS<==')
    for persona in persones:
        print(persona)


def formatearDatos(bs_data: BeautifulSoup):
    '''
    Guarda les dades obtingudes del fitxer en una llista de diccionaris
    Parametre BeautifulSoup amb les dades de les persones
    Retorna list amb diccionaris que contenen les dades de les persones
    '''
    
    persones_formatejades: list = []
    persones = bs_data.find_all('persona')

    for persona in persones:
        persones_formatejades.append({
            "dni": persona.dni.text,
            "nom": persona.nom.text,
            "cognoms": persona.cognoms.text
        })
        
    return persones_formatejades

     
def cargarDatos():
    '''
    Llig la informacio del fitxer xml i el retorna en forma de llista de diccionaris
    Retorna list amb diccionaris que contenen les dades de les persones
    '''

    persones_data_temp: list = []
    
    with open('data/persones.xml', 'r', encoding='utf-8') as fileReader:
        data = fileReader.read()

    bs_data = BeautifulSoup(data, 'xml')
        
    persones_data_temp = formatearDatos(bs_data)
    
    print('==>CARGA DE DATOS COMPLETADA<==')
    
    return persones_data_temp


def modificarDatos(persones_data: list):
    '''
    Modifica les dades obtingudes
    Parametre list amb la informacio de les persones
    Retorna list amb la informacio de les persones actualitzada
    '''
    
    persones_data_temp = list.copy(persones_data)
    
    if len(persones_data_temp) == 0:
        print('No se han encontrado personas. Asegurate de cargar datos antes de modificarlos.')
    else:
        mostrarPersonas(persones_data_temp)
    
        key_mod = input('Selecciona la clave a modificar: ')     
        dni = input(f'Selecciona el {key_mod} de la persona a modificar: ')
        new_dni = input(f'Nuevo {key_mod}: ')
        
        for persona in persones_data_temp:
            if persona[key_mod] == dni:
                persona[key_mod] = new_dni
        
    return persones_data_temp


def añadirPersona(persones_data: list):
    '''
    Afegix una persona a les dades obtingudes
    Parametre list amb la informacio de les persones
    Retorna list amb la informacio actualitzada
    '''

    persones_data_temp = list.copy(persones_data)
    
    if len(persones_data_temp) == 0:
        print('No se han encontrado personas. Asegurate de cargar datos antes de modificarlos.')
    else:
        mostrarPersonas(persones_data_temp)
        
        print('==>Creación de persona<==')
        key_dni = input('Dni: ')
        key_nom = input('Nombre: ')
        key_cognoms = input('Apellidos: ')
        
        persones_data_temp.append({
            "dni": key_dni,
            "nom": key_nom,
            "cognoms": key_cognoms
        })
    
    return persones_data_temp


def validateKeyDni(dni: str, persones: list):
    '''
    Comprova que la clau dni proporcionada existixca en la llista
    Parametres str amb el dni i list amb les persones a comprovar
    Retorna boolean
    '''

    persones_dni: list = []
    for persona in persones:
        persones_dni.append(persona.get('dni'))
    return dni in persones_dni


def mostrarPersona(persones: list):
    '''
    Mostra les dades de una persona en concret
    Parametre list persones
    '''
    if len(persones) == 0:
        print('No se han encontrado personas. Asegurate de cargar datos antes de querer fitrarlos.')
    else:
        mostrarPersonas(persones)

        print('==>PERSONA<==')

        while(True):
            key_dni = input('Dni: ')
            if validateKeyDni(key_dni, persones): break
            else: print('Seleccione un dni existente.')

        for persona in persones:
            if persona['dni'] == key_dni:
                key_nom = persona['nom']
                key_cognom = persona['cognoms']
                print(f'  DNI: {key_dni}\n  Nom: {key_nom}\n  Cognoms: {key_cognom}')


def borrarPersona(persones_data: list):
    '''
    Borra una persona de les dades obtingudes
    Parametre list amb la informacio de les persones
    Retorna list amb la informacio actualitzada
    '''

    persones_data_temp = list.copy(persones_data)
    
    if len(persones_data_temp) == 0:
        print('No se han encontrado personas. Asegurate de cargar datos antes de modificarlos.')
    else:
        mostrarPersonas(persones_data_temp)
        
        print('==>Borración de persona<==')
        
        while(True):
            key_dni = input('Dni: ')
            if validateKeyDni(key_dni, persones_data_temp): break
            else: print('Seleccione un dni existente.')
        
        for persona in persones_data_temp:
            if persona['dni'] == key_dni:
                persones_data_temp.remove(persona)
                
    return persones_data_temp        
    

def crearXml(persones_data: list):
    '''
    Crea un arxiu xml amb la informacio de la llista de diccionaris
    Parametre list amb la informacio de les persones
    Retorna str amb el xml
    '''

    xml_builder = []

    for persona in persones_data:
        dni = persona['dni']
        nom = persona['nom']
        cognoms = persona['cognoms']
        xml_builder.append(f'<persona><dni>{dni}</dni><nom>{nom}</nom><cognoms>{cognoms}</cognoms></persona>')
        
    xml = str(BeautifulSoup('<persones>{}</persones>'.format(''.join(xml_builder)), 'xml'))
        
    return xml


def guardarDatos(persones_data: list):
    '''
    Guarda la informacio en el fitxer xml
    Parametre list amb la informacio de les persones
    '''
    
    if len(persones_data) == 0:
        print('No se han encontrado personas. Asegurate de cargar datos antes de modificarlos.')
    else:
        xml = crearXml(persones_data)

        with open('data/persones.xml', 'w', encoding='utf-8') as fw:
            fw.writelines(xml)
    
    print('==>GUARDADO COMPLETADO<==')


def main():
    '''
    Funcio principal del programa
    '''

    persones_data = []
    
    while(True):
        option = seleccionarOpción()
    
        if option == 0:
            print('Fin del programa.')
            break
        elif option == 1:
            persones_data = cargarDatos()
        elif option == 2:
            persones_data = añadirPersona(persones_data)
        elif option == 3:
            persones_data = borrarPersona(persones_data)
        elif option == 4:
            mostrarPersona(persones_data)
        elif option == 5:
            persones_data = modificarDatos(persones_data)
        elif option == 6:
            guardarDatos(persones_data)
        
        print('------------------------------------------')
        mostrarPersonas(persones_data)
        
        
main()