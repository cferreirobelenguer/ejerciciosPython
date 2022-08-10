"""

¿ES UN NÚMERO DE ARMSTRONG?

Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
En la teoría de los números, un número de Armstrong o también llamado un número narcisista, un invariante digital 
pluscuamperfecto y un número perfecto más es básicamente un número que es la suma de sus propios dígitos, 
cada uno elevado a la potencia del número de dígitos. 

"""

def esArmstrong():
    print("Introduce un número")
    numero=input()
    num=int(numero)
    longitud=len(numero)
    suma=0

    for i in numero:
        digito=int(i)
        suma+=digito**longitud
    
    if(suma==num):
        print("Es armstrong")
    else:
        print("No es armstrong")

esArmstrong()