"""
Eliminar un registro de la tabla de personas
"""
import sqlite3
db=sqlite3.connect("base.db")

def eliminar(db):
    cursor=db.cursor()
    #Queremos eliminar el registro cuyo nombre es Jose
    cursor.execute("DELETE from personas WHERE nombre='Jose'")
    cursor.close()
    db.commit()

eliminar(db)