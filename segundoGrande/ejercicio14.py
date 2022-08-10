"""
Dado una tupla de números encuentra el segundo más grande
"""
listado=(4,56,67,45,3,23,78,1,2)

def segundoGrande(listado):

    max=0
    segundoMax=0

    for i in listado:
        numero=int(i)
        if(numero>max):
            max=numero
    for i in listado:
        numero=int(i)
        if((numero>segundoMax)and(numero!=max)):
            segundoMax=numero
    
    print("Segundo más grande: ",segundoMax)

segundoGrande(listado)