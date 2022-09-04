"""
Los heterogramas son palabras de siete letras o más donde no se repite 
ninguna letra. Ejemplo: tulipán, libreta, corteza, murciélago, etc.
Decir si una cadena dada es heterograma o no; es heterogénea cuando 
ninguna palabra de la cadena tiene letras que se repitan.
En cuanto en una de sus palabaras tenga una letra que se repita ya no será heterograma.

"""
def esHeterograma(cadena):
    repe=False
    noRepe=set()
    palabra=""
    for i in range(len(cadena)):
        if(cadena[i]!=" "):
            noRepe.add(cadena[i])
            palabra+=cadena[i]
        
        elif(cadena[i]==" "):
            print(palabra)
            print(noRepe)
            if(len(palabra)!=len(noRepe)):
                repe=True
            noRepe.clear()
            palabra=""
    print(palabra)
    print(noRepe)
    if(len(palabra)!=len(noRepe)):
        repe=True
    if(repe==True):
        print("No es heterograma")
    else:
        print("Si es heterograma, ya que ninguna de las letras de cada una de sus palabras se repiten")
    

esHeterograma("tulipan libreta corteza murcielago coco")
