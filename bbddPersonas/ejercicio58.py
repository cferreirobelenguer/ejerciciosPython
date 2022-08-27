"""
Insertar datos dentro de la bbdd personas
"""
import sqlite3

def insertarDatos():
    db=sqlite3.connect("base.db")
    #Forma de insertar los datos introduciéndolos directamente en el insert into
    cursor=db.cursor()
    cursor.execute("INSERT INTO personas (nombre,apellido,documento,nacimiento) VALUES( 'Jose','Perez',123,'05/05/1978')")
    db.commit()

def insertarDatos2():
    #Forma de insertar datos creando un registro externo
    db=sqlite3.connect("base.db")
    cursor=db.cursor()
    registro=('Sandra','Hernandez',5656556,'07/06/1996')
    cursor.execute("INSERT INTO personas (nombre,apellido,documento,nacimiento) VALUES(?,?,?,?)",registro)
    db.commit()

insertarDatos()
insertarDatos2()
