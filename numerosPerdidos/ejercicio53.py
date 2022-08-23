"""
Ejercicio listas
Dado un array de enteros ordenado y sin repetidos,
crea una función que calcule  y retorne todos los que faltan entre
el mayor y el menor.
Lanza un error si el array de entrada no es correcto (si está vacío o contiene repetidos).
"""
lista=[4,5,12,1,30]
noRepes=[]


def tieneRepes(lista):
    tiene=False
    #Se verifica si lista tiene repetidos creando otra nueva lista
    for i in lista:
        if(i not in noRepes):
            noRepes.append(i)
        else:
            tiene=True
    if(tiene==True):
        #Si la lista contiene repetidos se muestra error
        print("Error, la lista no puede contener repetidos")
    else:
        print(calcular(lista))
    

def calcular(lista):
    listaNumeros=[]
    if (len(lista)>0):
        #Calculamos el máximo y mínimo
        maximo=max(lista)
        minimo=min(lista)
        print(maximo)
        print(minimo)
        #Recorremos de máximo a minimo, y mostramos los digitos que no estén en la lista
        #En caso de que algún dígito dentro del rango esté en la lista no se muestra
        for i in reversed(range(minimo,maximo)):
            if( i not in lista):
                listaNumeros.append(i)

    else:
        #Si la lista está vacía se muestra error
        print("Error, la lista debe contener datos")
    return listaNumeros
tieneRepes(lista)