"""
PREDICCIÓN INMOBILIARIA CON PANDAS, SKLEARN Y STATSMODELS
Crear un archivo llamado barrios.csv con los datos de precio,metros y barrio de viviendas.
En el que 0 es barrio de nivel medio o bajo y 1 es barrio de alto nivel.
    - Crear dataframe con los datos del csv
    - Crear variable x con datos de los metros y el barrio, estos datos son los que queremos predecir
    - Crear variable y con los datos del precio, a través de estos datos queremos saber el precio de predición de nuestra vivienda
    - Obteniendo unos metros y barrio predecir cuánto va a costar la vivienda mediante sklearn a través del dataframe obtenido del csv
"""
import pandas as pd
from sklearn import linear_model

def crearDataframe():
    datos=pd.read_csv("barrios.csv")
    dataframe=pd.DataFrame(datos)
    #Esto es lo que queremos predecir
    x=(dataframe[['metros',"barrio"]])
    #A través de estos datos queremos saber el precio
    y=(dataframe[['precio']])
    print(x)
    print(y)
    predecir(x,y)
    
def predecir(x,y):
    regr=linear_model.LinearRegression()
    regr.fit(x,y)
    #Prediccion con sklearn, mediante unos datos de metros y barrio se nos da un precio apróximado de lo que va a costar la vivienda
    metros = 100
    barrio = 0
    print ('Precio aproximado de: \n', regr.predict([[metros ,barrio]]))


crearDataframe()