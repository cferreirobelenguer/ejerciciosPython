
"""
EJERCICIO MATRICES: FACTURA COMPRA
Dada una tabla que contiene los artículos
y los precios de un negocio y cantidad de stock.
Simular generar una factura de a lo sumo 6 artículos,
en la cual el usuario solo debe ingresar el artículo 
y la cantidad de artículos que quiere. El programa 
debería calcular los subtotales y el total general de
la factura.

"""
from tabulate import tabulate

table = [["leche","1.70","50"],["cocacola","2","100"],["tomate","1","20"],["aceite","4","10"],["arroz","1.10","50"],["pack cruasanes","2.10","0"],["cereales","1.70","10"],["pack filetes pollo", "5.10","0"]]
def comprarArticulos(table):
    compra=[]
    contador=0;
    #Se añaden los artículos, como máximo 6
    while(contador!=6):
        print("Escribe el artículo que quieres comprar: ")
        articulo=input()
        print("Escribe la cantidad que quieres comprar")
        cantidad=int(input())
        for filas in table :
            for columnas in range(len(filas)):
                if(articulo==filas[columnas]):
                    stock=int(filas[2])
                    if((cantidad<=stock)and (cantidad!=0)):
                        for i in range(cantidad):
                            #Si hay stock y se coge ese artículo se reduce el stock
                            #Sólo se pueden coger artículos cuando la cantidad solicitada es menor o igual que el stock disponible
                            if(cantidad<=stock):
                                stock=stock-cantidad
                                filas[2]=str(stock)
                            compra.append(filas)

                    
        contador+=1
    #Se imprime el ticket de compra
    print("--TICKET DE COMPRA--")
    print(tabulate(compra))
    subtotal=0
    precio=0
    iva=0.21
    #Se calculan los totales y subtotales teniendo en cuenta la cantidad de stock
    for filas in compra:
        for columnas in range(len(filas)):
            if(columnas==1):
                precio=float(filas[columnas])
                subtotal+=precio
    
    subtotal=round(subtotal)
    print(f"SUBTOTAL SIN IVA: {subtotal} €")
    iva=subtotal*iva
    print(f"IVA: {iva}")
    total=subtotal+iva
    print(f"--TOTAL DE LA COMPRA--: {total}")


comprarArticulos(table)