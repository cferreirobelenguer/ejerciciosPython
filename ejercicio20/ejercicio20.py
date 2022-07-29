#Dados tres números mostrar la combinación mayor en su conjunto; ej 200 002 020 la combinación mayor es 200

def combinacionNumeros(a,b,c):
    primera=0
    segunda=0
    tercera=0
    #primeras posiciones
    if((a>b)and(a>c)):
        primera=a
    elif((b>a)and(b>c)):
        primera=b
    elif((c>a)and(c>b)):
        primera=c
    #segunda posición a
    if((a>c)and(a<b)):
        segunda=a
    elif((a>b)and(a<c)):
        segunda=a
    #segunda posición b
    elif((b>c)and(b<a)):
        segunda=b
    elif((b>a)and(b<c)):
        segunda=b
    #segunda posición c
    elif((c>a)and(c<b)):
        segunda=c
    elif((c>b)and(c<a)):
        segunda=c
    #terceras posiciones
    if((a<b)and(a<c)):
        tercera=a
    elif((b<a)and(b<c)):
        tercera=b
    elif((c<a)and(c<b)):
        tercera=c

    numero=str(primera)+str(segunda)+str(tercera)
    print(f"La combinación mayor es {numero}")
combinacionNumeros(4,3,7)