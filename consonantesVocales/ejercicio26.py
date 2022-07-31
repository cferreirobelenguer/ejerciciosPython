"""
EJERCICIO DE LISTAS Y MATRICES
Dada una lista de palabras, contar cuantas 
vocales y consonantes tiene cada palabra

"""
palabras=["hola","mundo","estoy","programando","con","Python","holamundo"]
vocales=[]
consonantes=[]
    
def contar(palabras):
    #Contamos las vocales y las consonantes de cada palabra y las metemos en una lista de vocales y consonantes
    for i in palabras:
        contadorVocales=0
        contadorConsonantes=0
        palabra=i.lower()
        for j in palabra:
            if((j=="a")or(j=="e")or(j=="i")or(j=="o")or(j=="u")):
                contadorVocales+=1
            else:
                contadorConsonantes+=1
        vocales.append(contadorVocales)
        consonantes.append(contadorConsonantes)
    

def mostrarResultados(palabras,consonantes,vocales):
    from tabulate import tabulate
    #Vamos a crear una tabla con los datos para mostrar los resultados
    #Insertamos un título a cada fila
    palabras.insert(0,"PALABRAS: ")
    consonantes.insert(0,"Nº DE CONSONANTES: ")
    vocales.insert(0,"Nª DE VOCALES: ")
    #Creamos una matriz con los resultados y lo tabulamos con la librería tabulate
    resultados=[]
    resultados.append(palabras)
    resultados.append(consonantes)
    resultados.append(vocales)
    print("--RESULTADOS--")
    print(tabulate(resultados))


contar(palabras)
mostrarResultados(palabras,consonantes,vocales)