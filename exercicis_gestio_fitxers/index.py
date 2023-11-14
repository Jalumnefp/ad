from pathlib import Path


def getNomFitxer(path: Path):
    '''
    RETORNA EL NOM DEL FITXER
    '''
    if path.is_file():
        return Path(path.name)
    else:
        return None
    
def getFitxer(path_content, filename):
    '''
    RETORNA EL ARXIU EN CAS DE QUE EL CONTINGA I SI NO EL CONTÉ RETORNA NONE
    '''
    for file in path_content:
        if getNomFitxer(file) == filename:
            return Path(file)
    else:
        return None
    
def getFiles(path: Path):
    '''
    RETURNA UNA LLISTA AMB ELS FITXERS DEL DIRECTORI
    '''
    content = []
    for f in path.glob('*'):
        if Path(f).is_file():
            content.append(f)
    return content
    
def sameTime(path1: Path, path2: Path):
    print(path1.stat().st_mtime, path2.stat().st_mtime)
    return path1.stat().st_mtime == path2.stat().st_mtime

def sameSize(path1: Path, path2: Path):
    print(path1.stat().st_size, path2.stat().st_size)
    return path2.stat().st_size == path1.stat().st_size

def sameName(file1: str, file2: str):
    return file1 == file2
    

def compara(path1_content: Path, path2_content: Path):

    for file in all_files:

        file1 = getFitxer(path1_content, file)
        file2 = getFitxer(path2_content, file)

        if file1 == None:
            print(f'{file} NOMES EN 2')
        elif file2 == None:
            print(f'{file} NOMES EN 1')
        elif file1 and file2:
            if sameName(file1, file2) and sameTime(file1, file2) and sameSize(file1, file2):
                print(f'{file} IGUALES')
            else:
                if file1.stat().st_mtime > file2.stat().st_mtime:
                    print(f'{file} MES NOU EN 1')
                else:
                    print(f'{file} MES NOU EN 2')


print(f'Directiorio actual = {Path.cwd()}')
path1 = Path(input('Directori 1: '))
path2 = Path(input('Directori 2: '))

path1_content = getFiles(path1)
path2_content = getFiles(path2)
all_files = set(list(map(getNomFitxer, path1_content)) + list(map(getNomFitxer, path2_content)))

compara(path1_content, path2_content)

