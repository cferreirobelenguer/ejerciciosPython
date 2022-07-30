
#Ejercicio 3 tuplas

# Introducir una nueva palabra a la tupla introducida por el usuario
# Contar las letras de cada palabra que forma una tupla ya dada
# Mostrar la longitud de la tupla

dato=("Ana","Pepa","Clara","Marta","Carla","Veronica")
#Función que muestra la longitud de la tupla
def longitudTupla(dato):
    longitud=len(dato)
    print(f"La longitud de la tupla es {longitud}")

#Función que modifica la tupla
#La tuplas no pueden modificarse con lo cual para poder modificarla hay que pasarla a lista
def introducirDatos(dato):
    listaDato=list(dato)
    print("Introduce un nombre nuevo para añadir a la tupla: ")
    nombre=input()
    listaDato.append(nombre)
    #Pasamos la lista a tupla otra vez
    dato=tuple(listaDato)
    print(f"Los nuevos datos modificados de la tupla son: {dato}")
    contar(dato)

#Contar letras de cada una de las palabras de la tupla

def contar(dato):
    
    for i in dato:
        contador=0;
        for j in i:
            contador+=1
        print(f"El nombre {i} tiene {contador} letras")


longitudTupla(dato)
introducirDatos(dato)
