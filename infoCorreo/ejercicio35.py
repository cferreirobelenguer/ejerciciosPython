"""
Extractor de información del correo electrónico
Recopile una dirección de correo electrónico del usuario y luego averigüe si el usuario tiene un nombre de dominio personalizado o un nombre de dominio popular. Por ejemplo

Recopilamos una dirección de correo electrónico del usuario y luego vamos a averiguar si ese email tiene nombre de dominio personalizado o un nombre de un dominio popular. Por ejemplo:

Entrada: mary.jane@gmail.com
Salida: Hola Mary, estoy viendo que tu email está registrado con Google. ¡Eso es genial!.
"""
def infoCorreo():
    print("Introduzca su nombre")
    nombre=input()
    print("Por favor introduzca un email")
    email=str(input())
    posicionArroba=0
    posicionPunto=0
    for i in range(len(email)):
        if email[i]=="@":
            posicionArroba=i
            print(posicionArroba)
        if email[i]==".":
            posicionPunto=i
            print(posicionPunto)
    letra=email[posicionArroba+1:posicionPunto]
    print(letra)
    if letra in "gmail":
        return "Hola ",nombre," estoy viendo que tu email está registrado con Google. ¡Esto es genial!"
    elif letra in "yahoo":
        return "Hola ",nombre," estoy viendo que tu email está registrado con Yahoo. ¡Esto es genial!"
    elif letra in "hotmail":
        return "Hola ",nombre," estoy viendo que tu email está registrado con Hotmail. ¡Esto es genial!"
    elif letra in "outlock":
        return "Hola ",nombre," estoy viendo que tu email está registrado con Outlock. ¡Esto es genial!"
    else:
        return "Hola ",nombre, " estoy viendo que tu email está registrado con un dominio personalizado de ",letra,". ¡Impresionante!"

print(infoCorreo())