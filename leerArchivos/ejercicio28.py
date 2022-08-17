"""
Ejercicio archivos

Crear un archivo de texto mediante comandos de cmd y leer su contenido mediante python
- Leer todas las líneas de un texto y convertirlos en una lista


"""
#El archivo se ha creado en cmd mediante COPY con archivo.txt, se introducen los datos y con ctrl C se guardan

def leer():
    fichero=open('archivo.txt')
    lineas=fichero.readlines()
    #Con esto leemos línea a línea
    for linea in lineas:
        print (linea)
    fichero.close()
leer()