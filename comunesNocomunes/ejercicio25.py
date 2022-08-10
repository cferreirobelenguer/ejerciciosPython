"""
CONJUNTOS

Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
- Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
- Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

"""

lista1=[2,3,5,67,54,567,44]
lista2=[3,4,67,43,2,567,44]

comun=False


def calcularComunes(lista1,lista2,comun):
    listaComun=[]
    listaNoComun=lista1+lista2
    if(comun==True):
        #Si los elementos no están en la lista común (para evitar repeticiones) y coinciden en una lista y en otra se agregan a la lista común
        for i in lista1:
            try:
                resultado=listaComun.index(i)
            except:
                resultado=-1
            if(resultado==-1):
                for j in lista2:
                    try:
                        resultado2=listaComun.index(j)
                    except:
                        resultado2=-1
                    if((resultado2==-1)and(i==j)):
                        print(i)
                        listaComun.append(j)
        return "Lista común:",listaComun
            
    else:
        #Se hace otra vez la lista de comunes por si no se había elegido antes True; ya que en ese caso la lista saldría vacía
        listaComun2=[]
        for i in lista1:
            try:
                resultado=listaComun2.index(i)
            except:
                resultado=-1
            if(resultado==-1):
                for j in lista2:
                    try:
                        resultado2=listaComun2.index(j)
                    except:
                        resultado2=-1
                    if((resultado2==-1)and(i==j)):
                        print(i)
                        listaComun2.append(j)
        #Se compara la listaComun con la no común y si hay coincidencias se borran
        for i in listaComun2:
            for j in listaNoComun:
                if(i==j):
                    listaNoComun.remove(i)
        return "Lista no común: ",listaNoComun

print(calcularComunes(lista1,lista2,comun))