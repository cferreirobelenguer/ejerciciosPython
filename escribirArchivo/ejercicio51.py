"""
Escribir un programa para gestionar un listín telefónico con los nombres 
y los teléfonos de los clientes de una empresa. El programa incorporar 
funciones crear el fichero con el listín si no existe, para consultar el 
nombre de un cliente y mostrar su teléfono, añadir el teléfono de un nuevo
cliente y eliminar el teléfono de un cliente. El listín debe estar guardado
en el fichero de texto listin.txt donde el nombre del cliente y su teléfono
deben aparecer separados por comas y cada cliente en una línea distinta.
(en proceso sin terminar)

"""

def gestionListin():
    try:
        #En caso de que exista el archivo de listin se abre
        file=open("archivo.txt","r+")
        contador=0
        #5 oportunidades para escoger opción
        while(contador!=5):
            #Menú de opciones
            print("¿Qué quieres hacer?")
            print("Pulsa 1 si quieres agregar un contacto")
            print("Pulsa 2 si quieres buscar un contacto")
            print("Pulsa 3 si quieres eliminar un contacto")
            decision=input()
            esta=False
            estaBusqueda=False
            palabra=""
            if(decision=="1"):
                #Se añade un nuevo contacto
                file=open("archivo.txt","r+")
                print("Introduce el contacto a añadir")
                contactoNuevo=input()
                archivo=file.readlines()
                print(archivo)
                for i in archivo:
                    if(contactoNuevo not in i):
                        print("No esta")
                    else:
                        esta=True
                if(esta!=True):    
                    print("Introduce el número a añadir")
                    numNuevo=input()
                    print("Contacto añadido")
                    contador+=1
                    file.write(contactoNuevo+","+numNuevo+"\n")
                else:
                    print("Ya está añadido el contacto")
                file.close()
            elif(decision=="2"):
                #se busca un contacto
                print("Introduce el contacto a buscar")
                contador+=1
                contactoBusqueda=input()
                file=open("archivo.txt","r+")
                archivo=file.readlines()
                for i in archivo:
                    if(contactoBusqueda not in i):
                        print("No esta")
                    else:
                        posicion=i.index(",")
                        palabra=i[posicion+1::]
                        estaBusqueda=True
                print(estaBusqueda)
                if(estaBusqueda==True):
                    print("El contacto ",contactoBusqueda,"está dentro del listín, y el número es ",palabra)
                else:
                    print("El contacto no está en el listín")
                file.close()
            elif(decision=="3"):
                elimina=False
                file=open("archivo.txt","r+")
                lista=[]
                print("Introduce el contacto a eliminar")
                contador+=1
                contactoElimina=input()
                for palabra in file:
                    if(contactoElimina not in palabra):
                        print("No se elimina")
                        lista.append(palabra)
                    else:
                        print("Se elimina")
                        elimina=True
                if(elimina==True):
                    file.truncate()
                    print(lista)
                    for i in lista:
                        print(i)
                        file.write(i+"\n")
                    print("Contacto eliminado")
            
                
                
                file.close()
                
            else:
                print("Debe introducir una opción válida")
            

    except FileNotFoundError:
        #En caso de que no exista el archivo del listin se crea con permisos de escritura
        print("El archivo no se encuentra")
        fileNew=open("archivo.txt","w")

        
gestionListin()