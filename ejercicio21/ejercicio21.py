#A una fiesta asistieron personas de diferentes
#edades y sexos. Construir un algoritmo dadas las 
#edades y generos de las personas
#Calcular :
#- Cantidad de personas que asistieron a la fiesta
#- Cantidad de hombres y mujeres
#-La edad de la persona más jóven que asistirá
#Ingresar datos hasta que la edad sea cero

def agregarDatos():
    edades=[]
    contador=0;
    contadorh=0;
    contadorm=0;
    sexo="";
    edad="";
    edadd=7;
    #Se produce el bucle hasta que edad sea 0
    while edadd!=0:
        print("Introduce una edad")
        edad=input();
        edadd=int(edad)

        if(edadd!=0):

            #Ingresamos los datos de edad en lista para calcular el más joven
            edades.append(int(edad))
            sexo=input("Introduce género");
            #calculamos la cantidad de hombres y mujeres
            if(sexo=="hombre"):
                contadorh+=1;
            elif(sexo=="mujer"):
                contadorm+=1;
            #Con este contador calculamos la cantidad total de todos
            contador+=1
    
    print(edades)
    maximo=max(edades)
    minimo=min(edades)

    print(f"Hombres: {contadorh}")
    print(f"Mujeres: {contadorm}")
    print(f"El más mayor: {maximo}")
    print(f"El más jóven: {minimo}")
    print(f"Personas que asistieron al evento: {contador}")

agregarDatos()

    