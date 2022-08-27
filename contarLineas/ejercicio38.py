"""
Files exercise
Write a function which count number of lines and number of words in a text. 
All the files are in the data the folder: 
a) Read obama_speech.txt file and count number of lines and words 

"""

def contarArchivo():
    df=open('obama_speech.txt')
    texto=df.readlines()
    print("Texto:",texto)
    contadorLineas=0
    contadorPalabras=0

    for linea in texto:
        #Se cuentan las lineas
        contadorLineas+=1
        for letra in linea:
            #Se cuentan las palabras partiendo del espacio y de los saltos de línea
            if((letra==" ")or(letra in "\n")):
                contadorPalabras+=1
    #Le añadimos la palabra del final al contador de palabras, ya que al final del texto no hay espacio ni salto de línea
    #y sino no lo computa como palabra
    contadorPalabras=contadorPalabras+1
    
    print("Total líneas: ",contadorLineas)
    print("Total de palabras: ",contadorPalabras)

contarArchivo()