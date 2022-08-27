"""
BBDD

Crear una tabla personas con datos de id (autoincrementable, not null, y clave primaria), nombre (texto, not null), apellidos (texto, not null),
documento (texto not null), fecha (integer, not null, única); e introduce datos en DB Browser for SQLite
Una vez hecho esto:
- Conectar con la bbdd
- Mostrar el primer registro de la bbdd
- Mostrar todos los registros de la bbdd

"""
import sqlite3

def mostrarDatos():
    db=sqlite3.connect("base.db")
    cursor= db.cursor()
    #Vamos a mostrar todos los datos de la tabla personas
    datos=cursor.execute("SELECT * FROM personas")
    print("Primer registro de la tabla personas: ")
    #Fetchone muestra el primer registro de la bbdd
    print(datos.fetchone())
    print("Todos los registros de la tabla personas: ")
    #Fetchall muestra todos los registros de la tabla
    print(datos.fetchall())

    cursor.close()
mostrarDatos()