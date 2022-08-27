"""
GENERADORES ENLAZADOS
Crear dos generadores que enlazan en una iteración 
cuando se itera un límite que viene dado por parámetro.
Iterar sólo los 4 primeros
"""
def generador2(i):
    for j in range(i+1):
        yield j
def generador1(limite):
    for i in range(limite):
        yield from generador2(i)

def iterar20():
    contador=0
    g=generador1(10000)
    while(contador!=4):
        print(next(g))
        contador+=1
iterar20()

