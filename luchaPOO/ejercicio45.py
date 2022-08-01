"""
Ejercicio Herencia POO

Simular una pelea entre los guerreros Z, en el cual va a tener las siguientes clases:

- Luchador: clase concreta de la cual van a instanciar todos los guerreros y va a contener:

Atributos:
-Nombre (del luchador): str
-Kit: int
-SSJ: booleano
-Ataque: int
-Defensa:int
-Vida: int

Métodos:
-Atacar

-Batalla: clase que vamos a utilizar como menú, donde va a recibir dos luchadores
y va a empezar la batalla por turnos

-Ejemplos:

Goku:
-nombre: goku
-kit: 9000
-ssj: True
-ataque: 1000
-defensa: 500
-vida: 1000

Majinboo:
-nombre: majin boo
-kit: 7500
-ssj: False
-ataque: 700
-defensa: 700
-vida: 1500

Nota: en atacar hay que restarle a defensa el ataque, y esa diferencia se le resta a vida para restar las vidas
"""
import time
class Luchador():
    def __init__(self,nombre, kit, ssj, ataque,defensa, vida):
        self.nombre=nombre
        self.kit=kit
        self.ssj=ssj
        self.ataque=ataque
        self.defensa=defensa
        self.vida=vida

    def Atacar(self,enemigo):
        #pasamos por referencia el contrincante
        diferencia_ataque=self.ataque-enemigo.defensa
        enemigo.vida=enemigo.vida-diferencia_ataque
        print(f"{self.nombre} ha atacado a {enemigo.nombre} con una diferencia de ataque de {diferencia_ataque}")
        print(f"La vida del enemigo {enemigo.nombre} es {enemigo.vida}")

# clase Batalla que actúa de menú de la batalla llamando por atributos a los luchadores
class Batalla():
    turno="1"
    def __init__(self,Luchador1, Luchador2):
        self.Luchador1=Luchador1
        self.Luchador2=Luchador2
    def comienza_batalla(self):
        #Si los luchadores tienen vidas continúan peleando por turnos
        while(self.Luchador1.vida>0 and self.Luchador2.vida>0):
            time.sleep(0.5)
            if(self.turno=="1"):
                self.Luchador1.Atacar(self.Luchador2)
                self.turno="2"
            else:
                self.Luchador2.Atacar(self.Luchador1)
                self.turno="1"




Goku=Luchador("goku",9000,True,1000, 500,1000)
Majinboo=Luchador("majin boo",7500,False,700,700,1500)
Batalla(Goku,Majinboo).comienza_batalla()

