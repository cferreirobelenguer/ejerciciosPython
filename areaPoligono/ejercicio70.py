"""
Crea una única función (importante que sea única) que sea capaz de calcular y retornar el área
de un polígono
- La función recibirá por parámetro sólo un polígono a la vez.
- Los polígonos soportados serán Triángulos, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo

"""
def calcularPoligono(tipo,b,a):
    if(tipo=="triangulo"):
        area=float(b*a/2)
        return "El área del triángulo es ",area," cm cuadrados"
    elif(tipo=="cuadrado"):
        area=float(b**2)
        return "El área de un cuadrado es ",area," cm cuadrados"
    elif(tipo=="rectangulo"):
        area=float(b*a)
        return "El área de un cuadrado es ",area," cm cuadrados"
    else:
        return "El tipo de polígono debe ser triangulo, cuadrado o rectangulo"
    pass

print(calcularPoligono("triangulo",20,50))
print(calcularPoligono("cuadrado",12,0))
print(calcularPoligono("rectangulo",10,67))