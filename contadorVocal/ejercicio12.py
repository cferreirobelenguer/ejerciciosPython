"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
Contar también el número de consonantes que aparecen en la palabra. Mostrar todos los datos en matriz tabulada
"""
from tabulate import tabulate

def contarVocales():
    print("Introduce palabra")
    palabra=input()
    contadora=0;
    contadore=0;
    contadori=0;
    contadoro=0;
    contadoru=0;
    contadorNada=0
    tablaA=[]
    tablaE=[]
    tablaI=[]
    tablaO=[]
    tablaU=[]
    tablaConsonante=[]
    contadorConsonante=0

    for letra in palabra:
        if(letra=="a"):
            contadora+=1
        elif(letra=="e"):
            contadore+=1
        elif(letra=="i"):
            contadori+=1
        elif(letra=="o"):
            contadoro+=1
        elif(letra=="u"):
            contadoru+=1
        elif(letra==" "):
            contadorNada+=1
        else:
            contadorConsonante+=1
    total=[]
    tablaA.append("TOTAL A")
    tablaA.append(contadora)
    total.append(tablaA)
    tablaE.append("TOTAL E")
    tablaE.append(contadore)
    total.append(tablaE)
    tablaI.append("TOTAL I")
    tablaI.append(contadori)
    total.append(tablaI)
    tablaO.append("TOTAL O")
    tablaO.append(contadoro)
    total.append(tablaO)
    tablaU.append("TOTAL U")
    tablaU.append(contadoru)
    total.append(tablaU)
    tablaConsonante.append("TOTAL CONSONANTES")
    tablaConsonante.append(contadorConsonante)
    total.append(tablaConsonante)
    palabraMayus=palabra.upper()
    print("NÚMERO TOTAL DE VOCALES Y CONSONANTES DE LA PALABRA ", palabraMayus)
    print(tabulate(total))

contarVocales()