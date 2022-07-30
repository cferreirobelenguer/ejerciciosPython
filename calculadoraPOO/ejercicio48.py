"""
Crear una clase llamada calculadora con 
dos atributos que son los números,
va a contener los siguientes métodos:

Métodos:
    -sumar()
    -restar()
    -dividir()
    -multiplicar()
"""
class Calculadora:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    
    def sumar(self):
        suma=self.n1+self.n2
        print(f"SUMA: {suma}")
    def restar(self):
        resta=self.n1-self.n2
        print(f"RESTA: {resta}")
    def dividir(self):
        division=self.n1/self.n2
        print(f"DIVISIÓN: {division}")
    def multiplicar(self):
        multiplicacion=self.n1*self.n2
        print(f"MULTIPLICACIÓN: {multiplicacion}")

#método que crea el objeto y asigna los números y el operador
def crearObjeto():
    print("Introduce un número")
    numero1=int(input())
    print("Introduce otro número")
    numero2=int(input())
    calculo=Calculadora(numero1,numero2)
    print("Introduce el operador +,-,/,* ")
    operacion=input()

    if(operacion=="+"):
        calculo.sumar()
    elif(operacion=="-"):
        calculo.restar()
    elif(operacion=="/"):
        calculo.dividir()
    elif(operacion=="*"):
        calculo.multiplicar()
crearObjeto()
