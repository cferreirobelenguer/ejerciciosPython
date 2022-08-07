"""
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada 
asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de 
las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número 
total de créditos del curso.

"""
estudios={"Matemáticas":6, "Física":4, "Química":5, "Tecnología": 4}

def mostrarCreditos(estudios):
    sumaCreditos=0
    for keys,values in estudios.items():
        sumaCreditos+=values
        print(f"{keys} tiene {values} créditos")
    print(f"Total de créditos de todas las asignaturas: {sumaCreditos}")

mostrarCreditos(estudios)