"""
ejercicio 44 crea clase vehiculo con atributos color y ruedas, 
la clase coche hereda de vehculo y tiene velocidad en km y cilindrada 
cc de atributos; la clase bicicleta hereda de vehículo con el atributo urbana.
De coche hereda camioneta con carga kg y de bicicleta
hereda motocicleta con atributos de velocidad km/h y cilindrada cc. 
Métodos catalogar que muestra el color del auto y en coche y bicicleta 
sobreescribir la función catalogar para que muestre las ruedas también.

"""
class Vehiculo():
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas
    
    def catalogar(self):
        print(f"El vehículo tiene el color {self.coche}")

class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad, cilindrada):
        super().__init__(color,ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    def catalogar(self):
        print(f"El Coche tiene el color {self.color}, su número de ruedas es {self.ruedas}, su velocidad es {self.velocidad} y la cilindrada es {self.cilindrada}")

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,urbana):
        super().__init__(color, ruedas)
        self.urbana=urbana

    def catalogar(self):
        print(f"La bici tiene el color {self.color}, su número de ruedas es {self.ruedas}, y es de tipo {self.urbana}")

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada,carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga=carga
    def catalogar(self):
        print(f"La camioneta tiene el color {self.color}, su número de ruedas es {self.ruedas}, la velocidad es {self.velocidad}, la cilindrada es {self.cilindrada} y la carga es {self.carga}")
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, urbana,velocidad, cilindrada):
        super().__init__(color, ruedas, urbana) 
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    def catalogar(self):
        print(f"La motocicleta es del color {self.color}, tiene {self.ruedas} ruedas, es de tipo {self.urbana}, tiene una velocidad de {self.velocidad} y una cilindrada de {self.cilindrada}")

moto=Motocicleta("rosa","2","urbana","50 km","50cc")
camion=Camioneta("rojo","4","100 km","100cc","grande")

moto.catalogar()
camion.catalogar()
