"""
DATAFRAME
    - Crear dataframe con datos de casas, precios y metros cuadrados e imprimir todos los datos
    - Imprimir los datos únicamente de precios y metros
    - Crear archivo csv con los mismos datos y crear dataframe desde esos datos del csv. Mostrar todos sus datos
    - Mostrar los datos de las casas y los precios del dataframe csv
    - Mostrar los 3 primeros datos del archivo css
    - Mostrar la media de los precios de las viviendas del dataframe del archivo css
    - Contar el número de viviendas que hay en el dataframe del archivo css
    - Máximo precio, mínimo precio, máximos metros y mínimos metros en el dataframe del archivo css
"""
import pandas as pd
import pandas as read_csv
from tabulate import tabulate

def mostrarPreciosMetros(dataframe):
    #Se muestran los precios y metros
    print("Datos de precios y metros:")
    print(dataframe[["Precios","Metros"]])

def crearDataframe():
    #Función que muestra todos los datos del dataframe
    print("Todos los datos del dataframe: ")
    dataframe=pd.DataFrame({'Casas':['chalet1','chalet2','piso3'],'Precios':[200000,300000,150000],'Metros':[400,700,700]})
    print(dataframe)
    print("________________")
    #Se muestran los precios y metros
    mostrarPreciosMetros(dataframe)

def mostrarCasasPrecios(dataframecsv):
    print("________________")
    #Se muestran las casas y precios
    print("Datos de casas y sus precios: ")
    print(dataframecsv[["Casas","Precios"]])

def mediaPrecios(dataframecsv):
    print("________________")
    #Media de precios de las casas:
    media=dataframecsv["Precios"].mean()
    print(f"Media de precios de las casas: {media}")

def contar(dataframecsv):
    print("________________")
    #contar el número de viviendas que hay en el dataframe:
    contar=dataframecsv.count()
    print(f"Número total de viviendas : {contar}")

def mostrarTres(dataframecsv):
    print("________________")
    #Mostrar los tres primeros datos del dataframe del archivo csv
    data=dataframecsv.head(3)
    print("Los tres primeros datos: ")
    print(data)

def maxMin(dataframecsv):
    print("________________")
    #Máximo y mínimo de precios y metros
    print("Máximo y mínimo de precios y metros:")
    minPrecio=dataframecsv["Precios"].min()
    maxPrecio=dataframecsv["Precios"].max()
    minMetros=dataframecsv["Metros"].min()
    maxMetros=dataframecsv["Metros"].max()
    print(tabulate([["Mínimo precio",minPrecio],["Máximo precio",maxPrecio],["Mínimos metros",minMetros],["Máximos metros",maxMetros]]))

def dataframeCSV():
    print("________________")
    print("Todos los datos del dataframe csv:")
    #Función que crea un dataframe desde un archivo csv y muestra todos los datos
    dataframecsv=pd.read_csv("casas.csv")
    print(dataframecsv)
    #Se muestran las casas y precios
    mostrarCasasPrecios(dataframecsv)
    #Mostrar los tres primeros datos del dataframe
    mostrarTres(dataframecsv)
    #Media de precios del dataframe
    mediaPrecios(dataframecsv)
    #Contar el número de viviendas del dataframe
    contar(dataframecsv)
    #Máximo y mínimo de precios y metros tabulados
    maxMin(dataframecsv)

crearDataframe()
dataframeCSV()