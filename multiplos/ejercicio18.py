#Dados tres números mostrar los múltiplos de A, menores que B y que no sean dividores de C

def buscarNumeros(a,b,c):
    longitud=10
    valores=[];
    for i in range(10):
        print(a*i)
        if ((a*i<b) and (a*i%c!=0)):
            print(a*i)
            valores.append(a*i)
    print(valores)
buscarNumeros(2,18,3)