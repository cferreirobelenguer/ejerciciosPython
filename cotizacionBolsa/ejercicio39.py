"""
DATAFRAME CSV
El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: 
nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la 
acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), volumen (Volumen al cierre de bolsa),
Efectivo (capitalización al cierre en miles de euros). Construir una función que construya un DataFrame a partir del un 
fichero con el formato anterior y devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.

"""
import pandas as pd
import pandas as read_csv
#Creamos dataframe con valores de archivo csv
dataframe= pd.read_csv("cotizaciones.csv")
def calcularDataframe(dataframe):
    print("DATAFRAME CON LOS VALORES DEL ARCHIVO CSV: ")
    print(dataframe)
    contador=0;
    sumaFinal=0;
    sumaMaxima=0;
    sumaMinimo=0;
    sumaVolumen=0;
    sumaEfectivo=0;
    valoresFinal=[]
    valoresMaxima=[]
    valoresMinimo=[]
    valoresVolumen=[]
    valoresEfectivo=[]

    for data in dataframe.index:
        contador+=1
        #Añadimos los datos de las columnas en listas para calcular el máximo y mínimo de cada columna
        valoresFinal.append(int(dataframe["Final"][data]))
        valoresMaxima.append(int(dataframe["Máxima"][data]))
        valoresMinimo.append(int(dataframe["Mínimo"][data]))
        valoresVolumen.append(int(dataframe["Volumen"][data]))
        valoresEfectivo.append(int(dataframe["Efectivo"][data]))
        #calculamos la suma de cada uno para posteriormente calcular la media
        sumaFinal+=int(dataframe["Final"][data])
        sumaMaxima+=int(dataframe["Máxima"][data])
        sumaMinimo+=int(dataframe["Mínimo"][data])
        sumaVolumen+=int(dataframe["Volumen"][data])
        sumaEfectivo+=int(dataframe["Efectivo"][data])
    #Calculamos los valores máximos y mínimos de cada columna
    maxFinal=max(valoresFinal)
    minFinal=min(valoresFinal)
    maxMaxima=max(valoresMaxima)
    minMaxima=min(valoresMaxima)
    maxMinima=max(valoresMinimo)
    minMinima=min(valoresMinimo)
    maxVolumen=max(valoresVolumen)
    minVolumen=min(valoresVolumen)
    maxEfectivo=max(valoresEfectivo)
    minEfectivo=min(valoresEfectivo)
    #Calculamos las medias de cada columna
    mediaFinal=round(sumaFinal/contador)
    mediaMaxima=round(sumaMaxima/contador)
    mediaMinimo=round(sumaMinimo/contador)
    mediaVolumen=round(sumaVolumen/contador)
    mediaEfectivo=round(sumaEfectivo/contador)
    print("-------------------------------------------")
    #Creamos el dataframe con los máximos,mínimos y medias de cada columna
    print("DATAFRAME CON LOS VALORES DE MÁXIMOS MÍNIMOS Y MEDIAS: ")
    datos={"MÁXIMO FINAL":[maxFinal],"MÍNIMO FINAL":[minFinal],"MEDIA FINAL":[mediaFinal],"MÁXIMO MÁXIMA":[maxMaxima],"MÍNIMO MÁXIMA":[minMaxima],"MEDIA MÁXIMA":[mediaMaxima],"MÁXIMO MÍNIMA":[maxMinima],"MÍNIMO MÍNIMA":[minMinima],"MEDIA MÍNIMA":[mediaMinimo],"MÁXIMA VOLUMEN":[maxVolumen],"MÍNIMO VOLUMEN":[minVolumen],"MEDIA VOLUMEN":[mediaVolumen],"MÁXIMA EFECTIVO":[maxEfectivo],"MÍNIMO EFECTIVO":[minEfectivo],"MEDIA EFECTIVO":[mediaEfectivo]}
    datosMediasMaximos=pd.DataFrame(datos)
    #Devuelve el nuevo dataframe
    return datosMediasMaximos

print(calcularDataframe(dataframe))

