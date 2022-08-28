"""
LISTAS
Ordenar lista sin usar el método sort
"""
lista=[45,3,23,6,5,1,78]

def ordenar(lista):
    contador=0
    listaOrdenada=[]
    posicion=0
    longitud=len(lista)
    #Se realiza el bucle mientras contador sea diferente a la longitud de la lista
    while(contador!=longitud):
        #Se calcula el valor mínimo
        minimo=min(lista)
        for i in range(len(lista)):
            if (lista[i]==minimo):
                posicion=i
                contador+=1
        #Obtenemos la posición del valor mínimo para eliminarlo de la lista y así poder ir obteniendo otros valores mínimos
        lista.pop(posicion)    
        
        #Se añaden los valores mínimos a la lista a medida que se recorre la lista
        listaOrdenada.append(minimo)
    
    print(f"La lista ordenada es: {listaOrdenada}")

ordenar(lista)