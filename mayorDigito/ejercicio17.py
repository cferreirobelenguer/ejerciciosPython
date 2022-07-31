"""
Dado un número natural obtener el mayor de sus dígitos
"""

def calcular():

    print("Introduce un número")
    numero=int(input())
    max=0
    for i in range(numero):
        if(i>max):
            max=i
    print(f"El valor máximo de los dígitos de {numero} es {max}")

calcular()