"""
El siguiente programa lee valores del teclado para crear una colección de contactos bajo
la forma de lista de diccionarios. Solo cuando se introducen valores no vacíos, se 
almacenan en el diccionario.
El número total de contactos es indefinido y depende del usuario, al que se le pregunta si
desea introducir más contactos después de cada uno de ellos.

"""
contactos={}
contactosTotales=[]

def introducirValores(contactos):
    valor=""
    while((valor!="no")or(valor!="NO")):
        print("¿Desea introducir datos? [si o no]")
        valor=str(input())
        if((valor=="si")or(valor=="SI")):
            print("Introduce un nombre de contacto: ")
            nombre=input()
            print("Introduce apellidos de contacto")
            apellidos=input()
            print("Introduce email de contacto")
            email=str(input())
            print("Introduce tlf")
            tlf=input()
            if((nombre!="")and(apellidos!="")and(email!="")and(tlf!="")):
                contactos.update({"nombre":nombre})
                contactos.update({"apellidos":apellidos})
                contactos.update({"email":email})
                contactos.update({"tlf":tlf})
                contactosTotales.append(contactos)
        elif((valor=="NO")or(valor=="no")):
            break;
    if(len(contactos)>0):
        print("El total de contactos es: ",contactosTotales)
    else:
        print("No se ha añadido contenido aún")

introducirValores(contactos)