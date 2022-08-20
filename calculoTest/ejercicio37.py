"""
Una empresa que realiza pruebas de selecció de personal,
necesita conocer el puntaje total obtenido por los candidatos que presenten las
pruebas técnicas a un determinado empleo. El puntaje total se calcula
del puntaje obtenido por respuestas correctas el obtenido por
respuestas incorrectas y en blanco.
Por cada respuesta correcta se obtienen 5 puntos, respuesta incorrecta -2 puntos
y respuesta en blanco -1 punto. La cantidad total de preguntas que tiene la evaluación
son 20.

"""

def introducirResultados():
    sumaCorrectos=0
    sumaIncorrectos=0
    sumaBlancos=0
    print("Introduce los resultados del test")
    contador=0
    while(contador!=20):
        resu=input()
        if((resu=="correcto")or(resu=="CORRECTO")):
            sumaCorrectos+=5
            contador+=1
        elif((resu=="incorrecto")or(resu=="INCORRECTO")):
            sumaIncorrectos+=2
            contador+=1
        elif((resu=="blanco")or(resu=="BLANCO")):
            sumaBlancos+=1
            contador+=1
        else:
            print("Formato no válido")
    print("La suma del puntuaje de respuestas correctas es: ",sumaCorrectos)
    print("La suma del puntuaje de respuestas incorrectas es: ",sumaIncorrectos)
    print("La suma del puntuaje de respuestas en blanco es: ",sumaBlancos)
    sumaFallos=sumaIncorrectos+sumaBlancos
    sumaTotal=sumaCorrectos-sumaFallos
    return("Puntaje total del test: ",sumaTotal)
print(introducirResultados())
