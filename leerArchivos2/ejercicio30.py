"""
Crear archivo mediante cmd y leer todo su contenido de golpe mediante python
"""
# El archivo se crea mediante COPY con archivo2.text, se escribe el contenido y con ctrl- C se guarda

def leer():
    fichero=open("archivo2.txt")
    print(fichero.read())
    fichero.close()
leer()
