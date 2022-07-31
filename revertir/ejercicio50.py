"""
Crear una clase llamada Revertir donde va a recibir
una lista de palabras, y luego, podrá transformar esa
lista en un string pero con las palabras invertidas, ejemplo:

["Hola","como","estas"]->"estas como Hola"

Atributos:

-listaDePalabras

Métodos:

-revertir()
-mostrarFrase()

"""
listaNueva=[]
class Revertir():

    def __init__(self,listaDePalabras):
        self.listaDePalabras=listaDePalabras
    
    def revertir(self):
        
        
        for i in reversed(self.listaDePalabras):
            listaNueva.append(i)
        

    def mostrarFrase(self):
        print(listaNueva)
        
listaDePalabras=["Hola","como","estas"]
frase=Revertir(listaDePalabras)
frase.revertir()
frase.mostrarFrase()