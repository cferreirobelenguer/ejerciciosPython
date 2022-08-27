"""
    MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO
    Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD) 
    y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
    - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

def calcularMCD(num1,num2):
    temporal=0
    #Máximo común divisor
    while(num1!=0):
        temporal=num1
        num1=num1%num2
        num2=temporal
    mcd=num2
    print("El mínimo común divisor es: ",mcd)
    calcularMCM(mcd,20,6)

def calcularMCM(mcd,num1,num2):
    #Mínimo común múltiplo
    mcm=(num1*num2)/mcd
    print("El mínimo común múltiplo es: ",mcm)

calcularMCD(20,6)
