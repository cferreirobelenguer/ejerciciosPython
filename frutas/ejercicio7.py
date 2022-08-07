"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de 
ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

"""
frutas={}

def calcularFrutas(frutas):
    frutas.update({'Plátano':1.35})
    frutas.update({'Manzana':0.80})
    frutas.update({'Pera':0.85})
    frutas.update({'Naranja':0.70})
    encontrado=False
    valor=0
    precio=0
    print("Introduce la fruta que quieres comprar")
    fruta=input()
    
    for keys,values in frutas.items():
        if(fruta==keys):
            print("Introduce los kilos")
            kilos=int(input())
            encontrado=True
            valor=values
            precio=round(kilos*valor)
            
    if(encontrado==True):
        print(f"El usuario quiere comprar la fruta {fruta} cuyo precio por kilo es {valor}, quiere {kilos} kilos y el precio total es {precio}")
    else:
        print("El valor introducido no se encuentra")
calcularFrutas(frutas)
