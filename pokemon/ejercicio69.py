"""
Enunciado: Crea un programa que calcule el daño de un ataque durante
una batalla Pokémon.
    - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
    - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
    - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
    (buscar su efectividad)
    - El programa recibe los siguientes parámetros:
    - Tipo del Pokémon atacante.
    - Tipo del Pokémon defensor.
    - Ataque: Entre 1 y 100.
    - Defensa: Entre 1 y 100.
"""
import random

def batalla():
    #diccionarios de efectividades de los pokemon
    Agua={'agua':0.5,'fuego':1,'planta':2,'electrico':2}
    Fuego={'agua':2,'fuego':0.5,'planta':0.5,'electrico':1}
    Planta={'agua':0.5,'fuego':2,'planta':0.5,'electrico':1}
    Electrico={'agua':1,'fuego':1,'planta':1,'electrico':0.5}

    pokemon=['Agua','Fuego','Planta','Electrico']
    jugar="SI"
    #Mientras que jugador siga que si se produce una batalla, si dice que no o se introduce otro comando se para el programa
    while((jugar=="SI")or(jugar=="si")):
        print("¿Quieres jugar [SI o NO]")
        jugar=input()
        #pokemon aleatorios de jugadores
        luchador1=random.choice(pokemon)
        luchador2=random.choice(pokemon)
        luchador2lower=luchador2.lower()
        #ataque aleatorio de 1 a 100 de jugador 2
        ataqueJugador2=int(random.randint(1,100))
        #defensa aleatoria de 1 a 100 del jugador 1
        defensaJugador1=int(random.randint(1,100))
        if(luchador1=="Agua"):
            #Se calcula el daño del jugador 2 al jugador 1
            danoJugador1=50*(ataqueJugador2/defensaJugador1)*float(Agua[luchador2lower])
        elif(luchador1=="Fuego"):
            #Se calcula el daño del jugador 2 al jugador 1
            danoJugador1=50*(ataqueJugador2/defensaJugador1)*float(Fuego[luchador2lower])
        elif(luchador1=="Planta"):
            #Se calcula el daño del jugador 2 al jugador 1
            danoJugador1=50*(ataqueJugador2/defensaJugador1)*float(Planta[luchador2lower])
        elif(luchador1=="Electrico"):
            #Se calcula el daño del jugador 2 al jugador 1
            danoJugador1=50*(ataqueJugador2/defensaJugador1)*float(Electrico[luchador2lower])
        if((jugar=="SI")or(jugar=="si")):
            #batalla
            print("Bienvenido al gimnasio pokemon")
            print("¡Comienza la batalla!")
            print("Jugador 1 de tipo: ",luchador1)
            print("Jugador 2 de tipo: ",luchador2)
            print("Ataque de jugador 2 a jugador 1\nAtaque de jugador 2: ",ataqueJugador2,"\nDefensa de jugador 1: ",defensaJugador1)
            print("El daño del jugador 1 por el ataque del jugador 2 es: ",danoJugador1)
        elif((jugar=="NO")or(jugar=="no")):
            print("Se ha acabado el juego")
            break;
        else:
            print("Error de comando introducido, debe introducir SI o NO")
batalla()    



