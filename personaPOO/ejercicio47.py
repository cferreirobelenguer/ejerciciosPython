"""
Crear una clase llamada Persona donde sus atributos van a ser:
Atributos:
- Nombre
-Edad
-DNI

Y van a tener los siguientes métodos:
-mostrarEdad(): devuelve la edad de la persona
- esMayordeEdad(): devuelve True si es mayor o igual de 18,
y False si es menor de 18

Realizar su respectivo constructor, métodos y atributos
"""

from mailbox import NoSuchMailboxError


class Persona:
    
    def __init__(self,nombre,edad,dni):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni

    def mostrarEdad(self):
        print(f"La edad de {self.nombre} es {self.edad}")
    
    def esMayordeEdad(self):
        if(self.edad>18):
            print(f"{self.nombre} es mayor de edad con {self.edad} años")
        else:
            print(f"{self.nombre} no es mayor de edad con {self.edad} años")

chica=Persona('Carla',20,"5674635")
chico=Persona("Pablo",12,"5435644")
chica.mostrarEdad()
chica.esMayordeEdad()
chico.mostrarEdad()
chico.esMayordeEdad()
    

