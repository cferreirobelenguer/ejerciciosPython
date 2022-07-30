#Invertir el orden de una palabra que introduce el usuario : ej. hola sería aloh

def invertir():
    print("Introduza una palabra: ")
    palabra=input();
    palabraNueva="";
    for i in reversed(palabra):
        palabraNueva+=i
    print(f"La palabra al revés es {palabraNueva}")

invertir()