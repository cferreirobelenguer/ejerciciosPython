"""
GENERADORES
Crear una función generadora para
Iterar un límite con generadores.
Llamar a esta función generadora 10 veces
usando un contador.
"""
def generador(limite):
    for i in range(limite):
        #Estado de suspensión
        yield i

#Llama a la función generadora 10 veces usando un contador
def llamada():
    contador=0
    g=generador(10000)
    while(contador!=10):
        print(next(g))
        contador+=1
llamada()




