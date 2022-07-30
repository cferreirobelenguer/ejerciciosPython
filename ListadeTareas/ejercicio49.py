"""
Crear una clase llamada listaDeTareas donde no va 
a recibir ningún argumento en su constructor pero va a
tener un argumento definido como una lista, y va a 
contener los siguientes métodos:

Métodos:
    -mostrarTareas()
    -agregarTareas()
    -quitarTareas()

"""
tareas=[]
class listaDeTareas():
    def mostrarTareas(self,tareas):
        for i in tareas:
            print(f"Listado de tareas: {i}")

    def agregarTareas(self,tareas):
        print("Introduce una tarea")
        tarea=input()
        tareas.append(tarea)

    def quitarTareas(self,tareas):
        print("Escribe la tarea que quieres borrar")
        eliminado=False
        dato=input()
        contador=0
        for contenido in tareas:
            print("contenido ", contenido)
            contador+=1
            if(contenido==dato):
                print(contenido)
                tareas.pop(contador-1)
                eliminado=True
        if(eliminado==True):
            print("La tarea ha sido eliminada")


def gestionarTareas():
    contador=0
    while(contador!=10):
        rutina=listaDeTareas()
        print("Selecciona las siguientes opciones")
        print("Introduce 1 para mostrar las tareas")
        print("Introduce 2 para agregar tarea")
        print("Introduce 3 para quitar tarea")
        numero=input()
    
        if((numero!="1")and(numero!="2")and(numero!="3")):
            print("El número seleccionado no es correcto tiene que elegir 1, 2 o 3")
            contador+=1
        elif(numero=="1"):
            rutina.mostrarTareas(tareas)
            contador+=1
        elif(numero=="2"):
            rutina.agregarTareas(tareas)
            contador+=1
        elif(numero=="3"):
            rutina.quitarTareas(tareas)
            contador+=1
        
gestionarTareas()
