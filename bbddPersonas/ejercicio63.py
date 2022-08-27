"""
UPDATE
Actualizar un dato de un registro en la tabla personas
"""
import sqlite3

def actualizar():
    db=sqlite3.connect("base.db")
    cursor=db.cursor()
    #Quiero que cambie Paula por Jose en el registro cuyo id es 2
    cursor.execute("UPDATE personas SET nombre='Paula' WHERE id=2")
    cursor.close()
    db.commit()
actualizar()