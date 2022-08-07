
"""
Máquina expendedora

Primero se introducen monedas, sólo se permiten monedas de 0.10 (10 céntimos), 0.05 (5 céntimos), 0.20 (20 céntimos) y
0.50 (50 céntimos), 1 (1 euro) o 2 (2 euros)
Elegir el producto y comprar, en caso de que no se disponga de crédito suficiente mostrar mensaje
y si el crédito es superior dar el cambio correspondiente
"""
productos={"patatas fritas":1.20, "coca-cola":0.80, "doritos":1.30,"chocolatina": 1, "fanta":1.10, "sandwich":1.20}

    
def elegirProducto(productos):
    sumaMonedas=0
    #Sólo se permiten monedas de 5,20,20,50 céntimos o 1 euro o 2 euros y se suma el total de monedas
    monedas=-1
    while(monedas!=0):
        print("Introduce monedas")
        monedas=float(input())
        if(monedas==0):
            break;
        if((monedas==0.10)or(monedas==0.05)or(monedas==0.20)or(monedas==0.50)or(monedas==1)or(monedas==2)):
            
            sumaMonedas+=monedas
        else:
            print("Sólo se permiten monedas de 5,10,20,50 céntimos o 1 o 2 euros")
    sumaMonedas=round(sumaMonedas,2)
    print("La suma total de monedas es: ",sumaMonedas)
    print("Elige el producto")
    eleccion=input()
    for keys,values in productos.items():
        if(eleccion==keys):
            print(f"Ha elegido el producto: {keys} cuyo precio es {values} €")
            print("Su crédito es ",sumaMonedas,"€")
            #Si el valor del producto es superior o igual a lo que vale el producto se hace la compra
            if(sumaMonedas>=values):
                print("Producto comprado")
                #Si el crédito es superior al valor del producto se calculan las vueltas
                if(sumaMonedas>values):
                    vueltas=sumaMonedas-values
                    print(f"Su cambio es {vueltas} €")
            else:
                print("No dispone de suficiente crédito para comprar el producto, por favor introduzca más monedas")


elegirProducto(productos)
