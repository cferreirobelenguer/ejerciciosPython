"""
Diccionario español inglés traductor:
Escribir un programa que cree un diccionario de traducción español-inglés. 
El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
y cada par <palabra>:<traducción> separados por comas. 
El programa debe crear un diccionario con las palabras y sus traducciones. 
Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
Si una palabra no está en el diccionario debe dejarla sin traducir.
"""


diccionarioEspanolIngles={"hola":"hello","mundo":"world","estoy":"am","nosotros":"we","vosotros":"you","ellos":"they","estáis":"are","están":"are","estamos":"are","estas":"are","estamos":"are","esta":"is","tu":"you","programando":"programming","yo":"i","ella":"he"}

def introducePalabra(diccionarioEspanolIngles):
    print("Introduce una frase en español")
    frase=input()
    #la pasamos a minúsculas porque python es camel case
    frase=frase.lower()
    palabra=""
    traduccion=""
    fraseTraducida=""
    for i in frase:
        palabra+=i
        for keys,values in diccionarioEspanolIngles.items():
            if(palabra==keys):
                #Si encuentra la palabra concatenamos la palabra traducida en un string
                traduccion=values
                fraseTraducida+=traduccion+" "
        #Si i es espacio en blanco se reinicia todo
        if(i==" "):
            palabra=""
            traduccion=""
    #Ponemos la primera letra en mayúsculas para construir la frase
    fraseTraducida=fraseTraducida.capitalize()
    print("Frase traducida: ",fraseTraducida)
    
introducePalabra(diccionarioEspanolIngles)