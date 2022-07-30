#Determinar si un número X es perfecto,
#un número es perfecto si la suma de sus divisores es el
#mismo número. Ej. El 6 es perfecto ya que 1+2+3=6

def numeroPerfecto(num):
    
    suma=0;
    for i in range(1,num):
        
        if((num%i==0)or(i==num)):
            print(i)
            suma+=i;
    if(suma==num):
        print(f"{num} es un número perfecto ya que la suma de sus divisores es {suma}")
    else:
        print(f"{num} no es un número perfecto; ya que la suma de sus divisores es {suma}")

numeroPerfecto(496)