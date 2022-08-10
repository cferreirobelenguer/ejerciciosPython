"""
¿ES UN ANAGRAMA?
Dificultad: MEDIA

Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
NO hace falta comprobar que ambas palabras existan.
Dos palabras exactamente iguales no son anagrama.
"""
def esAnagrama():
    print("Introduce una palabra")
    palabra1=input()
    print("Introduce otra palabra")
    palabra2=input()
    #El reverso de una de ellas tiene que ser igual a la otra para que sean anagramas
    reverso=""
    for letra in reversed(palabra1):
        reverso+=letra

    if(reverso==palabra2):
        print("Son anagramas")
    else:
        print("No son anagramas")
esAnagrama()
