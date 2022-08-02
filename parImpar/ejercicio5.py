"""
Pedir al usuario un número entre 1 y 1000 y decir si es par o impar
"""
def parImmpar():

    contador=0

    while(contador!=10):

        print("Introduce un número:")
        numero=int(input())
        if((numero>=1)and(numero<=1000)):
            if(numero%2==0):
                print(f"Es par")
                contador+=1
            else:
                print("Es impar")
                contador+=1
        else:
            print("El número no está comprendido entre 1 y 1000")

parImmpar()
