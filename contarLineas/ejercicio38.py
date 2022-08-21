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
        contadorLineas+=1
        for letra in linea:
            if(letra==" "):
                contadorPalabras+=1
    contadorPalabras=contadorPalabras+contadorLineas
    print("Total líneas: ",contadorLineas)
    print("Total de palabras: ",contadorPalabras)

contarArchivo()