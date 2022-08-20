"""
Dado un número, mostrar su serie de fibonacci.
La serie de fibonacci es un orden de números donde
cada número es la suma de los dos anteriores.

"""

def calcularFibonacci():
    print("Introduce un número")
    numero=int(input())
    serie=[0,1]
    for i in range(2,numero):
        serie.append(serie[i-1]+serie[i-2])
    return serie
print(calcularFibonacci())