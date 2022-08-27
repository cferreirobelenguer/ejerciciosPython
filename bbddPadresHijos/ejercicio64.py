"""
CLAVE FORÁNEA Y CONSULTAS DE VARIAS TABLAS
Crear una bbdd de con las tablas de Padres e Hijos cuya clave foránea sea el id del padre,
rellenar la tabla con datos.
    - Mostrar el nombre, apellidos del padre; nombre y apellidos de los hijos cuyo id de padre sea 3
    - Tabular los resultados con titulo de cabecera
"""
import sqlite3
from tabulate import tabulate

def mostrarHijos():
    db=sqlite3.connect("data.db")
    cursor=db.cursor()
    datos=cursor.execute("SELECT Padre.nombre AS 'NOMBRE PADRE',Padre.apellido AS 'APELLIDO PADRE', Hijo.nombre_hijo AS 'NOMBRE HIJO', Hijo.apellido_hijo AS 'APELLIDO HIJO' FROM Padre,Hijo  where Padre.idPadre=3 and Hijo.id_Padre=3")
    print(tabulate(datos.fetchall(),headers=["NOMBRE PADRE", "APELLIDO PADRE", "NOMBRE HIJO","APELLIDO HIJO"]))
    cursor.close()
    db.commit()
mostrarHijos()