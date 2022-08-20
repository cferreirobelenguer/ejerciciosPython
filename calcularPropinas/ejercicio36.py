"""
Se pide la factura y se pide al cliente que elija la propina (18%,20% y 25%)
se calcula la propina delegida
y el total de la factura incluida la propina

"""
def calcularPropina():
    print("¿Cuál la factura de hoy?")
    factura=float(input())
    print("Elija la propina 18, 20 o 25")
    propina=input()
    print("propina:",propina)
    if(propina=="18"):
        propina=int(propina)
        propinaCalculo=18/100
        print(propinaCalculo)
        incrementoPrecio=factura*propinaCalculo
        facturaTotal=factura+incrementoPrecio
        print(facturaTotal)
        return "La propina elegida es del ",propina," %, "," la factura total incluida la propina es ",facturaTotal," €"

    elif(propina=="20"):
        propina=int(propina)
        propinaCalculo=20/100
        incrementoPrecio=factura*propinaCalculo
        facturaTotal=factura+incrementoPrecio
        return "La propina elegida es del ",propina," %, "," la factura total incluida la propina es ",facturaTotal," €"
    elif(propina=="25"):
        propina=int(propina)
        propinaCalculo=25/100
        incrementoPrecio=factura*propinaCalculo
        facturaTotal=factura+incrementoPrecio
        return "La propina elegida es del ",propina," %, "," la factura total incluida la propina es ",facturaTotal," €"
    else:
        return "No se ha podido calcular, la propina elegida debe ser de 18, 20 o 25%"
print(calcularPropina())