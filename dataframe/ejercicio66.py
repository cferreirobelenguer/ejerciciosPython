"""
DATAFRAME
    - Crear dataframe con datos de casas, precios y metros cuadrados e imprimir todos los datos
    - Imprimir los datos únicamente de precios y metros
    - Crear archivo csv con los mismos datos y crear dataframe desde esos datos del csv. Mostrar todos sus datos
    - Mostrar los datos de las casas y los precios del dataframe csv
"""
import pandas as pd
import pandas as read_csv

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

def dataframeCSV():
    print("________________")
    print("Todos los datos del dataframe csv: ")
    #Función que crea un dataframe desde un archivo csv y muestra todos los datos
    dataframecsv=pd.read_csv("casas.csv")
    print(dataframecsv)
    #Se muestran las casas y precios
    mostrarCasasPrecios(dataframecsv)

crearDataframe()
dataframeCSV()