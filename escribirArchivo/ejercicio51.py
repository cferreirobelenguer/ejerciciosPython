"""
Escribir un programa para gestionar un listín telefónico con los nombres 
y los teléfonos de los clientes de una empresa. El programa incorporar 
funciones crear el fichero con el listín si no existe, para consultar el 
nombre de un cliente y mostrar su teléfono, añadir el teléfono de un nuevo
cliente,consultar el teléfono de un cliente y mostrar su nombre o eliminar
contacto. El listín debe estar guardado en el fichero de texto archivo.txt
donde el nombre del cliente y su teléfono deben aparecer separados por comas
y cada cliente en una línea distinta.(en proceso sin terminar)

"""
def anadirContacto():
    esta=False
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
        file.write(contactoNuevo+","+numNuevo+"\n")
    else:
        print("Ya está añadido el contacto")
        file.close()

def buscaNumero():
    #Busca el número de teléfono en el listín y muestra el nombre del contacto
    esta=False
    palabra=""
    print("Introduce el número de teléfono a buscar")
    numeroBusqueda=input()
    file=open("archivo.txt","r+")
    archivo=file.readlines()
    for i in archivo:
        if(numeroBusqueda in i):
            esta=True
            posicion=i.index(",")
            palabra=i[0:posicion]
    if(esta==True):
        print("El número "+numeroBusqueda+" está dentro del listín, y el contacto es "+palabra)
    else:
        print("El contacto no está en el listín")
    file.close()

def buscaContacto():
    estaBusqueda=False
    #se busca un contacto por nombre y muestra el número de teléfono
    print("Introduce el contacto a buscar")
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

def eliminar():
    #Se elimina el contacto por nombre
    esta=False
    lista=[]
    print("Introduce el contacto a eliminar del listín telefónico")
    contacto=input()
    file=open("archivo.txt","r+")
    archivo=file.readlines()
    for i in archivo:
        if(contacto not in i):
            lista.append(i)
        else:
            esta=True
            file.close()
    if(esta==True):
        file=open("archivo.txt","w+")
        file.truncate()
        for j in lista:
            print(j)
            file.write(j)
                
        file.close()

def gestionListin():
    try:
        #En caso de que exista el archivo de listin se abre
        file=open("archivo.txt","r+")
        contador=0
        #5 oportunidades para escoger opción
        while(contador!=5):
            #Menú de opciones
            print("¿Qué quieres hacer?")
            print("Pulsa 1 si quieres agregar un contacto por nombre de contacto")
            print("Pulsa 2 si quieres buscar un contacto por nombre")
            print("Pulsa 3 si quieres buscar un contacto por número de teléfono")
            print("Pulsa 4 si quieres eliminar un contacto por nombre de contacto")
            decision=input()
            esta=False
            estaBusqueda=False
            palabra=""
            if(decision=="1"):
                contador+=1
                anadirContacto()
            elif(decision=="2"):
                contador+=1
                buscaContacto()
            elif(decision=="3"):
                contador+=1
                buscaNumero()
            elif(decision=="4"):
                contador+=1
                eliminar()
            else:
                print("Debe introducir una opción válida")
            

    except FileNotFoundError:
        #En caso de que no exista el archivo del listin se crea con permisos de escritura
        print("El archivo no se encuentra")
        fileNew=open("archivo.txt","w")

        
gestionListin()