
#Tenemos una matriz pasada por parámetro y se nos pide ordenar cada una de sus filas
#Ordenar al revés las filas

dato=[[5,67,43],[2,43,654],[34,1,6]]
#Ordenamos de menor a mayor las filas de la matriz
def ordenarFilas(dato):
    for filas in dato:
        filas.sort()
    print(f"Matriz con filas ordenadas de menor a mayor: {dato}")
#Ordenamos de mayor a menor la filas de la matriz
def ordenarReves(dato):
    datoNuevo=[]
    for filas in dato:
        datoNuevo.append(sorted(filas,reverse=True))
    print (f"Matriz con filas ordenadas de mayor a menor: {datoNuevo}")
    
ordenarFilas(dato)
ordenarReves(dato)

