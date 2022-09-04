"""
trabajarSets: ejercicio Crear dos sets (set1 y set2) con datos y unirlos en set3.
Volver a intentar unir set2 y ver que pasa. 
Eliminar set2 del set1 y preguntar si Perla que es el contenido de set2 
está en la lista de set3. Finalmente pasar set a lista ordenada.
"""
set1={"Clara","Diego","Jorge","Pepito"}
set2={"Perla"}
def unirSeparar():
    set3=set1.union(set2)
    print(set3)
    #Los datos de set2 no se van a volver a agregar porque los sets no aceptan datos repetidos
    set3=set3.union(set2)
    print(set3)
    set3=set3.difference(set2)
    #Se compara si Perla está dentro de set3
    if("Perla" in set3):
        print("La palabra está en la lista set3")
        print(set3)
    else:
        print("La palabra no está en la lista set3")
        print(set3)
    #Pasamos set a lista ordenada, ya que los set son datos no ordenados
    set3=list(set3)
unirSeparar()