"""

CÓDIGO MORSE

Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse
"""

alfabeto={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"}

def traducirMorse(alfabeto):
    print("Introduce palabra")
    palabra=input()
    contador=0
    traduccion=""
    #Reemplazamos los espacios por asteriscos
    palabra=palabra.replace(" ","*")
    print(palabra)
    #Vamos traduciendo creando dos iteraciones, una de la palabra y otra del diccionario buscando letra por letra
    for letra in palabra:
        if(letra=="*"):
            traduccion+="*"
        for keys, values in alfabeto.items():
            #Si el contador no llega al final se incluye un espacio entre caracter y caracter
            if(contador<len(palabra)-1):
                
                if(letra==keys):
                    contador+=1
                    morse=values
                    traduccion+=morse+" "
            else:
            #En caso de que se llegue al final no se incluye espacio
                if(letra==keys):
                    contador+=1
                    morse=keys
                    traduccion+=morse
    #Se reemplaza el asterisco por un espacio, como ya había un espacio creado por el for con este ya habría doble espacio entre palabra y palabra
    traduccion=traduccion.replace("*"," ")
    print("Traducción a morse: ",traduccion)
traducirMorse(alfabeto)