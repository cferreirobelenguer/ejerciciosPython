"""
Enunciado: Crea dos funciones que reciban dos cadenas como parámetro (str1, str2) e impriman otras dos cadenas como salida (out1, out2).
    - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
    - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1
"""
str1="carmelahy"
str2="sarayuee"

def calcularOUT1(str1,str2):
    out1=""
    lista=[]
    for i in str2:
        lista.append(i)
    for j in str1:
        if j not in lista:
            out1+=j
    
    return out1
def calcularOUT2(str1,str2):
    out2=""
    lista=[]
    for i in str1:
        lista.append(i)
    for j in str2:
        if j not in lista:
            out2+=j
    return out2
print(calcularOUT1(str1,str2))
print(calcularOUT2(str1,str2))
