"""
LA CARRERA DE OBSTÁCULOS

Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
carrera de obstáculos.
La función recibirá dos parámetros:
    - Un array que sólo puede contener String con las palabras "run" o "jump"
    - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
    - La función imprimirá cómo ha finalizado la carrera:
    - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
variará el símbolo de esa parte de la pista.
    - Si hace "jump" en "_" (suelo), se variará la pista por "x".
    - Si hace "run" en "|" (valla), se variará la pista por "/".
    - La función retornará un Boolean que indique si ha superado la carrera.
Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""
carrera=("run","jump","run","run")
carreraGrafico="-|--"

def comprobarCarrera(carrera,carreraGrafico):
    
    resultados=[]
    #Si las longitudes de la lista y el string no coinciden se da como nula la carrera
    if(((len(carrera))!=(len(carreraGrafico)))):
        print("El corredor no ha finalizado la carrera correctamente")
    else:
        #Se va rellenando el resultado
        for i in range(len(carrera)):
                print("resultado: ",carrera[i]," grafico: ",carreraGrafico[i])
                # Si es jump y - se rellena x
                if((carrera[i]=="jump")and(carreraGrafico[i]=="-")):
                    resultados.append("x")
                elif((carrera[i]=="run")and(carreraGrafico[i]=="|")):
                #Si es run y | se rellena /
                    resultados.append("/")
        #Excepción que maneja el error que retorna cuando no se encuentra la cadena x o /, lo convierte en -1
        try:
            resultadosx=resultados.index("x")
            resultadosy=resultados.index("/")
        except:
            resultadosx=-1
            resultadosy=-1
        print("Estos son los resultados del jurado: ",resultados)
        #Si hay resultados se retorna una decisión del jurado en caso de que haya x e /
        #Si la lista de resultados está vacía es que la carrera es correcta
        if((len(resultados)>0)):
            if((resultadosx==-1)or(resultadosy==-1)):
                print("El corredor no ha finalizado la carrera correctamente")
        else:
            print("El corredor ha finalizado la carrera correctamente")
comprobarCarrera(carrera,carreraGrafico)