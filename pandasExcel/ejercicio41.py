"""
Leer los datos de un excel con pandas, mostrar nombre y correo
"""

import pandas as pd
import pandas as read_excel

dataframe=pd.read_excel("datos.xls")


def mostrarNombreCorreo(dataframe):
    print("Nombres de los sujetos: ")
    print(dataframe["NOMBRE"])
    print("Correos de los sujetos: ")
    print(dataframe["CORREO"])



mostrarNombreCorreo(dataframe)
