
"""
EJERCICIO MATRICES:

Dada una matriz de NxM elementos,
compuesta de 0 y 1, recorrer cada una de las
filas y mostrar el valor decimal equivalente
ej
3 filas
5 columnas
[
    [1,1,1,0,1],[1,0,1,0,0],[1,0,0,0,1]
]
Resultado en decimal
[29,20,17]
"""
matriz=[]
columnas=0;
#Se eligen las filas y las columnas y los datos
def crearMatriz():
    print("Introduce el número de filas")
    filas=int(input())
    print("Introduce el número de columnas")
    columnas=int(input())

    
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            print("Introduce datos para el contenido de las columnas")
            datos=int(input())
            while((datos!=0)or(datos!=1)):
                #No se permite introducir datos que no sean o 0 o 1
                print("Los datos son incorrectos, debe introducir 0 o 1.")
                datos=int(input())
                if((datos==1)or(datos==0)):
                    matriz[i].append(datos)
                    break
            
                
    
def filasDecimal(matriz,columnas):
    print(matriz)
    decimales=[]
    suma=0;
    contador=len(matriz[0])-1
    for filas in matriz:
        for info in range(len(filas)):
            if(contador==-1):
                decimales.append(suma)
                suma=0
                contador=len(matriz[0])-1
            potencia=float(2**contador)
            suma+=float((float(filas[info])*potencia))
            contador-=1
    decimales.append(suma)       
    print(decimales)

crearMatriz()
filasDecimal(matriz, columnas)