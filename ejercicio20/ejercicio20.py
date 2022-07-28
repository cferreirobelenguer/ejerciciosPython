#Dados tres números mostrar la combinación mayor en su conjunto; ej 200 002 020 la combinación mayor es 200

def combinacionNumeros(a,b,c):
    
    valores=[]
    a=str(a)
    b=str(b)
    c=str(c)
    
    valores.append(int(a+b+c));
    valores.append(int(a+c+b));
    valores.append(int(c+a+b));
    valores.append(int(c+b+a));
    valores.append(int(b+a+c));
    valores.append(int(b+c+a));

    maximo=max(valores)
    minimo=min(valores)
    print(f"El valor máximo es: {maximo} ")
    print(f"El valor mínimo es: {minimo} ")
combinacionNumeros(4,3,7)