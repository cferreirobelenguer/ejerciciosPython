"""
Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
    - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
    - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1
"""
str1="carmela y pepa"
str2="sara y pepita"

def calcularOUT1(str1,str2):
    out1=""
    out2=""
    str1=str1.lower()
    str2=str2.lower()

    for j in str1:
        if ((j not in str2)and(j!=" ")):
            out1+=j
    for j in str2:
        if ((j not in str1)and(j!=" ")):
            out2+=j
    
    return out1,out2
print(calcularOUT1(str1,str2))
