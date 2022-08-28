"""
Crud de citas que permite crear cita, modificar cita, eliminar cita, ver cita
"""
import email
import sqlite3

def crearCita(data,cursor):
    error=False
    #Se piden los datos y se validan

    print("Introduce el nombre")
    #Se valida que nombre no sea numérico
    n=input()
    nombre=""
    if(n.isnumeric()):
        print("Nombre no debe tener caracteres numéricos")
        error=True
    else:
        nombre=n
        print(nombre)
    print("Introduce el apellido")
    #Se valida que apellido no sea numérico
    a=input()
    apellido=""
    if(a.isnumeric()):
        print("Apellidos no debe tener caracteres numéricos")
        error=True
    else:
        apellido=a
        print(apellido)
    print("Introduce mes de la citación")
    #Se valida que el mes sea comprendido entre 1 a 12
    mes=0
    m=input()
    if(m.isnumeric()):
        m=int(m)
        if((m<=1)or(m<=12)):
            mes=m
            print(mes)
        else:
            print("Debe introducir meses comprendidos entre enero y diciembre y en formato numérico")
            error=True
    else:
        print("Mes debe de ser numérico")
        error=True

    print("Introduce dia de la citación")
    #Se validan los días en función del mes anteriormente introducido
    d=input()
    if(d.isnumeric()):
        d=int(d)
        dia=0
        if(mes==1):
            if((d<=1)or(d<=31)):
                dia=d
                print(dia)
            else:
                print("Debe introducir un día entre 1 a 31")
                error=True
        elif(mes==2):
            if((d<=1)or(d<=28)):
                dia=d
                print(dia)
            else:
                print("Debe introducir un día entre 1 a 28")
                error=True
        elif(mes==3):
            if((d<=1)or(d<=31)):
                dia=d
                print(dia)
            else:
                print("Debe introducir un día entre 1 a 31")
                error=True
        elif(mes==4):
            if((d<=1)or(d<=30)):
                dia=d
                print(dia)
            else:
                print("Debe introducir un día entre 1 a 30")
                error=True
        elif(mes==5):
            if((d<=1)or(d<=31)):
                dia=d
                print(dia)
            else:
                print("Debe introducir un día entre 1 a 31")
                error=True
        elif(mes==6):
            if((d<=1)or(d<=30)):
                dia=d
                print(dia)
            else:
                print("Debe introducir un día entre 1 a 30")
                error=True
        elif(mes==7):
            if((d<=1)or(d<=31)):
                dia=d
                print(dia)
            else:
                print("Debe introducir un día entre 1 a 31")
                error=True
        elif(mes==8):
            if((d<=1)or(d<=31)):
                dia=d
                print(dia)
            else:
                print("Debe introducir un día entre 1 a 31")
                error=True
        elif(mes==9):
            if((d<=1)or(d<=30)):
                dia=d
                print(dia)
            else:
                print("Debe introducir un día entre 1 a 31")
                error=True
        elif(mes==10):
            if((d<=1)or(d<=31)):
                dia=d
                print(dia)
            else:
                print("Debe introducir un día entre 1 a 31")
                error=True
        elif(mes==11):
            if((d<=1)or(d<=30)):
                dia=d
                print(dia)
            else:
                print("Debe introducir un día entre 1 a 31")
                error=True
        elif(mes==12):
            if((d<=1)or(d<=31)):
                dia=d
                print(dia)
            else:
                print("Debe introducir un día entre 1 a 31")
                error=True
        else:
                print("Día no válido ya que el mes no es válido")
                error=True
    else:
        print("Día debe de ser numérico")

    print("Introduce teléfono de contacto")
    telefono=0
    phone=input()
    if(phone.isnumeric()):
        telefono=int(phone)
        print(telefono)
    else:
        print("Debe introducir un dato numérico en teléfono")
        error=True
    print("Introduce correo de contacto")
    #Se valida que correo contenga una @
    email=input()
    correo=""
    if('@' in email):
        correo=email
        print(correo)
    else:
        print("Opción no válida, correo debe contener @")
        error=True
    if(error==False):
        print("Se han introducido sus datos")
        registro=(nombre,apellido,dia,mes,telefono,correo)
        cursor.execute("INSERT INTO agenda (nombre,apellidos,dia,mes,telefono,correo) VALUES(?,?,?,?,?,?)",registro)
        data.commit()
    else:
        print("No se ha podido procesar su solicitud, datos errónes")

def modificarCita(data,cursor):
    print("Introduce el id")
    numero=input()
    if(numero.isnumeric()):
        id=0
        id=int(numero)
        error=False
        #Se piden los datos y se validan

        print("Introduce el nombre")
        #Se valida que nombre no sea numérico
        n=input()
        nombre=""
        if(n.isnumeric()):
            print("Nombre no debe tener caracteres numéricos")
            error=True
        else:
            nombre=n
            print(nombre)
        print("Introduce el apellido")
        #Se valida que apellido no sea numérico
        a=input()
        apellido=""
        if(a.isnumeric()):
            print("Apellidos no debe tener caracteres numéricos")
            error=True
        else:
            apellido=a
            print(apellido)
        print("Introduce mes de la citación")
        #Se valida que el mes sea comprendido entre 1 a 12
        mes=0
        m=input()
        if(m.isnumeric()):
            m=int(m)
            if((m<=1)or(m<=12)):
                mes=m
                print(mes)
            else:
                print("Debe introducir meses comprendidos entre enero y diciembre y en formato numérico")
                error=True
        else:
            print("Mes debe de ser numérico")
            error=True

        print("Introduce dia de la citación")
        #Se validan los días en función del mes anteriormente introducido
        d=input()
        if(d.isnumeric()):
            d=int(d)
            dia=0
            if(mes==1):
                if((d<=1)or(d<=31)):
                    dia=d
                    print(dia)
                else:
                    print("Debe introducir un día entre 1 a 31")
                    error=True
            elif(mes==2):
                if((d<=1)or(d<=28)):
                    dia=d
                    print(dia)
                else:
                    print("Debe introducir un día entre 1 a 28")
                    error=True
            elif(mes==3):
                if((d<=1)or(d<=31)):
                    dia=d
                    print(dia)
                else:
                    print("Debe introducir un día entre 1 a 31")
                    error=True
            elif(mes==4):
                if((d<=1)or(d<=30)):
                    dia=d
                    print(dia)
                else:
                    print("Debe introducir un día entre 1 a 30")
                    error=True
            elif(mes==5):
                if((d<=1)or(d<=31)):
                    dia=d
                    print(dia)
                else:
                    print("Debe introducir un día entre 1 a 31")
                    error=True
            elif(mes==6):
                if((d<=1)or(d<=30)):
                    dia=d
                    print(dia)
                else:
                    print("Debe introducir un día entre 1 a 30")
                    error=True
            elif(mes==7):
                if((d<=1)or(d<=31)):
                    dia=d
                    print(dia)
                else:
                    print("Debe introducir un día entre 1 a 31")
                    error=True
            elif(mes==8):
                if((d<=1)or(d<=31)):
                    dia=d
                    print(dia)
                else:
                    print("Debe introducir un día entre 1 a 31")
                    error=True
            elif(mes==9):
                if((d<=1)or(d<=30)):
                    dia=d
                    print(dia)
                else:
                    print("Debe introducir un día entre 1 a 31")
                    error=True
            elif(mes==10):
                if((d<=1)or(d<=31)):
                    dia=d
                    print(dia)
                else:
                    print("Debe introducir un día entre 1 a 31")
                    error=True
            elif(mes==11):
                if((d<=1)or(d<=30)):
                    dia=d
                    print(dia)
                else:
                    print("Debe introducir un día entre 1 a 31")
                    error=True
            elif(mes==12):
                if((d<=1)or(d<=31)):
                    dia=d
                    print(dia)
                else:
                    print("Debe introducir un día entre 1 a 31")
                    error=True
            else:
                    print("Día no válido ya que el mes no es válido")
                    error=True
        else:
            print("Día debe de ser numérico")

        print("Introduce teléfono de contacto")
        telefono=0
        phone=input()
        if(phone.isnumeric()):
            telefono=int(phone)
            print(telefono)
        else:
            print("Debe introducir un dato numérico en teléfono")
            error=True
        print("Introduce correo de contacto")
        #Se valida que correo contenga una @
        email=input()
        correo=""
        if('@' in email):
            correo=email
            print(correo)
        else:
            print("Opción no válida, correo debe contener @")
            error=True
        if(error==False):
            print("Se han introducido sus datos")
            registro=(nombre,apellido,dia,mes,telefono,correo,id)
            cursor.execute("UPDATE agenda SET nombre=?,apellidos=?,dia=?,mes=?,telefono=?,correo=? WHERE id=?",registro)
            data.commit()
        else:
            print("No se ha podido procesar su solicitud, datos errónes")
        
    else:
        print("Debe introducir un número")
def eliminarCita(data,cursor):
    print("Introduce el id")
    numero=input()
    if(numero.isnumeric()):
        id=0
        id=int(numero)
        cursor.execute("DELETE from agenda WHERE id=?",(id,))
        data.commit()
        print("La cita ha sido eliminada")
    else:
        print("Debe introducir un número")
    

def verCita(cursor):
    print("Introduce el nombre de la persona")
    nombre=input()
    datos=cursor.execute("SELECT * FROM agenda where nombre=?",(nombre,))
    resultado=datos.fetchall()
    if(len(resultado)>0):
        print("A continuación se mostrarán las citas que tengas registradas: ",resultado)
    else:
        print("No hay resultados para esta búsqueda")


def menuCitas():
    data=sqlite3.connect("citas.db")
    cursor=data.cursor()
    opcion=False
    while(opcion!=True):
        print("Bienvenido al servicio de petición de citas, por favor elija una opción")
        print("1. Pulse 1 para introducir una cita")
        print("2. Pulse 2 para modificar una cita")
        print("3. Pulse 3 para eliminar una cita")
        print("4. Pulse 4 para ver su cita")
        print("5. Pulse 5 para salir")
        eleccion=input()
        if(eleccion=="1"):
            crearCita(data,cursor)
        elif(eleccion=="2"):
            modificarCita(data,cursor)
        elif(eleccion=="3"):
            eliminarCita(data,cursor)
        elif(eleccion=="4"):
            verCita(cursor)
        elif(eleccion=="5"):
            print("Hasta pronto")
            opcion=True
            break;
        else:
            print("El dato introducido no es correcto")
    cursor.close()
menuCitas()

