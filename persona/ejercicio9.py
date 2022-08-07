"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

persona={}

def pedirNombre(persona):
    print("Introduce nombre ")
    nombre=input()
    persona.update({'Nombre':nombre})
    print("Datos de persona:")
    for keys,values in persona.items():
        print(f"{keys}: {values}")

def pedirEdad(persona):
    print("Introduce edad ")
    edad=input()
    persona.update({'Edad':edad})
    print("Datos de persona:")
    for keys,values in persona.items():
        print(f"{keys}: {values}")
def pedirSexo(persona):
    print("Introduce sexo ")
    sexo=input()
    persona.update({'Sexo':sexo})
    print("Datos de persona:")
    for keys,values in persona.items():
        print(f"{keys}: {values}")
def pedirTelefono(persona):
    print("Introduce teléfono de contacto ")
    tlf=input()
    persona.update({'Teléfono':tlf})
    print("Datos de persona:")
    for keys,values in persona.items():
        print(f"{keys}: {values}")
def pedirCorreo(persona):
    print("Introduce correo electrónico ")
    correo=input()
    persona.update({'Correo':correo})
    print("Datos de persona:")
    for keys,values in persona.items():
        print(f"{keys}: {values}")

pedirNombre(persona)
pedirEdad(persona)
pedirSexo(persona)
pedirTelefono(persona)
pedirCorreo(persona)