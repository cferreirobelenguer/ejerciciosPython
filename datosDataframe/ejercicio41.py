"""
Dataframe
Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:

Mes	    Ventas	Gastos
Enero	30500	22000
Febrero	35600	23400
Marzo	28300	18100
Abril	33900	20700

Calculamos el total de ventas, total de gastos, el mínimo y máximo de ventas y el mínimo y máximo de gastos

"""
import pandas as pd

def crearData():
    data={"Mes":["Enero","Febrero","Marzo","Abril"],"Ventas":[30500,35600,28300,33900],"Gastos":[22000,23400,18100,20700]}
    #Creamos el dataframe
    datosTotales=pd.DataFrame(data)
    print(datosTotales)
    ventasTotales=0
    gastosTotales=0
    ventas=[]
    gastos=[]
    #Recorrer dataframe para calcular la suma de las ventas y la suma de los gastos
    for i in datosTotales.index:
        #Introducimos los datos de ventas y gastos en listas para calcular el valor máximo y mínimo
        ventas.append(int(datosTotales["Ventas"][i]))
        gastos.append(int(datosTotales["Gastos"][i]))
        #Vamos sumando el total de ventas y gastos en las iteraciones del dataframe
        ventasTotales+=int(datosTotales["Ventas"][i])
        gastosTotales+=int(datosTotales["Gastos"][i])
        
    print(f"Total ventas: ",ventasTotales)
    print(f"Total gastos: ",gastosTotales)

    #Calculamos el máximo y mínimo de ventas
    ventaMaxima=max(ventas)
    ventaMinima=min(ventas)
    print("Venta máxima: ",ventaMaxima)
    print("Venta mínima: ",ventaMinima)
    #Calculamos el máximo y mínimo de gastos
    gastoMaximo=max(gastos)
    gastoMinimo=min(gastos)
    print("Gasto máximo: ",gastoMaximo)
    print("Gasto mínimo: ",gastoMinimo)

crearData()
