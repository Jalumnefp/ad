class Persona():
    color_sangre = 'rojo'

    def __init__ (self, nom, dni, edad):
        self.nom = nom
        self.dni = dni
        self.edad = edad

    def __str__(self):
        return f'[Nombre: {self.nom}, Dni: {self.dni}, Edad: {self.edad}, ColorSangre: {self.color_sangre}, VidaRestante: {self.__vida_restante(self.edad)}]'
    
    def dormir(self):
        print('zzzzzzzzzzz')

    def __vida_restante(self, edad: int):
        return 100-edad



p1 = Persona('Frodo', '12345678W', 23)

print(p1)
p1.dormir()