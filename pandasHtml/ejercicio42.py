"""
Leer los datos de una tabla de html con pandas
"""

import pandas as pd
import pandas as read_html

dataframe=pd.read_html("form.html")


def recorrerDatos(dataframe):
    print(f"Total de tablas: {len(dataframe)}")
    print(dataframe)

recorrerDatos(dataframe)