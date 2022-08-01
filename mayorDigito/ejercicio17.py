"""
Dado un número natural obtener el mayor de sus dígitos

"""

def calcular():

    print("Introduce un número")
    numero=input()
    max=0
    lista=[]
    for i in numero:
        lista.append(i)

    for j in lista:
        valor=int(j)
        if (valor>max):
            max=valor

    print(f"El valor máximo de los dígitos de {numero} es {max}")

calcular()