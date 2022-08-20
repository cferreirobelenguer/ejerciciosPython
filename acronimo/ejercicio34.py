"""
Vamos a pedir al usuario que ingrese el significado
completo de una organización o concepto y con ello
como resultado obtendrá el acrónimo.

Entrada-> As Soon As Possible
Salida-> ASAP

"""
def buscarAcronimo(frase):
    acronimos=frase[0:1]
    for i in range(len(frase)):
        if (frase[i]==" "):
            acronimos+=frase[i+1]
    return(acronimos)
print(buscarAcronimo("Absent Without Leave"))


