"""
La Tierra Media está en guerra! en ella lucharán razas leales
a Sauron contra otras bondadosas que no quieren que el mal reine
sobre sus tierras.
Cada raza tiene asociado un valor entre 1 y 5.
    - Razas bondadosas: Pelosos(1), Sureños buenos (2), Enanos(3),
    Númenóreanos (4), Elfos(5)
    - Razas malvadas: Sureños malos (2), Orcos(2), Goblins(2), Huargos(3), Trolls(5)
Crea un programa que calcule el resultado de la batalla entre los dos tipos de ejércitos:
- El resultado puede ser que gane el bien, el mal, o exista un empate.
Dependiento de la suma del valor del ejército y el número de integrantes.
- Cada ejército puede estar compuesto por un número de integrantes variable de cada raza.
- Tienes total libertad para modelar los datos del ejercicio.
Ej. 1 Peloso pierde contra 1 Orco
    2 Pelosos empatan contra 1 Orco
    3 Pelosos ganan a 1 Orco

"""
import random

bondadosos={"pelosos":1, "surenosbuenos":2,"enanos":3,"numenoreanos":4,"elfos":5}
malvados={"surenosmalos":2,"orcos":2,"goblins":2,"huargos":3,"trolls":5}

def batalla(bondadosos,malvados):
    listaBondadosos=[]
    listaMalvados=[]
    #Cogemos las claves y las metemos en unas listas de bondadosos y malvados
    for key in bondadosos.keys():
        listaBondadosos.append(key)
    for key in malvados.keys():
        listaMalvados.append(key)
    #calculamos la longitud de cada lista y con ese dato calculamos un random de jugadorBondadoso y de jugadorMalvado
    longitudBondadosos=len(listaBondadosos)-1
    longitudMalvados=len(listaMalvados)-1
    #random de los miembros de cada equipo de bondadosos y malvados
    randomBondadoso=random.randint(0,longitudBondadosos)
    randomMalvado=random.randint(0,longitudMalvados)
    jugadorBondadoso=listaBondadosos[randomBondadoso]
    jugadorMalvado=listaMalvados[randomMalvado]
    print("¡Comienza la batalla!...")
    #random del número de integrantes de cada equipo, ponemos límite de 0 a 100
    integrantesBondadoso=random.randint(0,100)
    integrantesMalvados=random.randint(0,100)
    #Se calcula el resultado sumando el valor del diccionario de cada clave de bondadoso y malvado más los integrantes
    resultadoBondadoso=int(bondadosos[jugadorBondadoso])+integrantesBondadoso
    resultadoMalvado=int(malvados[jugadorMalvado]+integrantesMalvados)
    if(resultadoBondadoso>resultadoMalvado):
        print(integrantesBondadoso, " ",jugadorBondadoso," gana/n a ",integrantesMalvados," ",jugadorMalvado)
    elif(resultadoBondadoso==resultadoMalvado):
        print(integrantesBondadoso, " ",jugadorBondadoso," empata/n contra ",integrantesMalvados," ",jugadorMalvado)
    elif(resultadoBondadoso<resultadoMalvado):
        print(integrantesBondadoso, " ",jugadorBondadoso," pierde/n contra",integrantesMalvados," ",jugadorMalvado)


batalla(bondadosos,malvados)

