"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""

from optparse import Values


monedas={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

def mostrarDivisa(monedas):
    valor=""
    encontrado=False
    print(f"Introduzca una divisa y se mostrará su símbolo: ")
    divisa= input()
    for key,values in monedas.items():
        if(key==divisa):
            valor=values
            encontrado=True
    if(encontrado==True):
        print(f"El símbolo de la divisa es {valor}")
    else:
        print("No se ha encontrado el valor")
mostrarDivisa(monedas)