"""
Leer datos de un csv con la librería pandas
Mostrar lo siguiente: 1. todos los empleados, 2. nombre empleados, 3. sueldo empleados, 4. nombre y departamento de empleados
"""
import pandas as pd
import pandas as read_csv

dataframe= pd.read_csv("empleados.csv")

def mostrarTodo(dataframe):
    print("DATOS DE LOS EMPLEADOS: ")
    #mostrar todos los datos del csv
    print(dataframe)

def mostrarEmpleados(dataframe):
    print("NOMBRE DE LOS EMPLEADOS: ")
    #mostrar sólo los empleados
    print(dataframe['Empleado'])

def mostrarSueldos(dataframe):
    print("MOSTRAR SUELDO DE LOS EMPLEADOS: ")
    #mostrar sólo el sueldo de los empleados
    print(dataframe['Sueldo'])

def mostrarNombreDepartamento(dataframe):
    print("MOSTRAR NOMBRE Y DEPARTAMENTO DE LOS EMPLEADOS: ")
    #mostrar el nombre del empleado y su departamento
    print(dataframe[['Empleado','Departamento']])

mostrarTodo(dataframe)
mostrarEmpleados(dataframe)
mostrarSueldos(dataframe)
mostrarNombreDepartamento(dataframe)