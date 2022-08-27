"""
Dado un archivo txt quitar los saltos de línea
"""
def quitar():
    file=open("texto.txt","r+")
    texto=file.readlines()
    #Se leen los datos con salto de línea
    print("Texto con saltos: ",texto)
    #Se reemplaza \n por nada
    for i in range(len(texto)):
        texto[i]=texto[i].replace("\n","")
    #Se leen los datos sin salto de línea
    print("Texto sin saltos: ",texto)
    file.close
quitar()


