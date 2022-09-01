"""

Enunciado: Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
    - El .txt se corresponde con las entradas de una calculadora.
    - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
    - Soporta números enteros y decimales.
    - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
    - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
    - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.

"""
def operar(operacion):  

    print("El resultado es: ",operacion)
    #Calculamos las operaciones de suma y resta en el orden en el que están en la lista
    resultado=""
    for i in operacion:
        resultado+=str(i)
    #Se calcula el resultado con eval
    print("El resultado es ",eval(resultado))

def calcular():
    
    operacion=[]
    file=open("archivo.txt")
    #Hemos quitado el /n del archivo en función de la longitud y hemos pasado los datos a una lista para poder operar con ellos
    for linea in file:
            if(len(linea)==2):
                operacion.append(linea[0:1])
            else:
                operacion.append(linea[0:2])
    
    file.close()
    operar(operacion)

calcular()