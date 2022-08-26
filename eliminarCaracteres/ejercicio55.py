"""
Enunciado: Crea dos funciones que reciban dos cadenas como parámetro (str1, str2) e impriman otras dos cadenas como salida (out1, out2).
    - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
    - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1
"""
str1="carmela y pepaz"
str2="sara y pepita"

def calcularOUT1(str1,str2):
    out1=""
    lista=[]
    str1=str1.lower()
    for i in str2:
        if(i!=" "):
            lista.append(i)
    for j in str1:
        if ((j not in lista)and(j!=" ")):
            out1+=j
    
    return out1
def calcularOUT2(str1,str2):
    out2=""
    str2=str2.lower()
    lista=[]
    for i in str1:
        if(i!=" "):
            lista.append(i)
    for j in str2:
        if ((j not in lista)and(j!=" ")):
            out2+=j
    return out2
print(calcularOUT1(str1,str2))
print(calcularOUT2(str1,str2))
