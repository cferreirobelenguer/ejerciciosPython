

#Decir si un número pasado por parámetro es primo o no

def esPrimo(num):
    esDivisible=False
    for i in range(2,num-1):
        if(num%i==0):
            esDivisible=True;
            
    print(esDivisible)
    if(esDivisible==False):
        if(num%num==0 and num%1==0):
            print(f"El número {num} es primo")
        else:
            print(f"El número {num} no es primo")
    else:
        print(f"El número {num} no es primo")
esPrimo(79)