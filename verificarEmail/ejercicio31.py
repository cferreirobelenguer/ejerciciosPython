
"""
Se pide al usuario que introduzca un email y se verifica
si es un email o no. El programa entiende que es un email
cuando contiene @

"""

def verificarEmail():
    print("Por favor introduzca un email: ")
    email=input()
    contiene=False
    for i in email:
        if(i=="@"):
            contiene=True
    if(contiene!=True):
        print("El correo introducido no es válido. Por favor introduzca un correo correcto")
    else:
        print("Correo verificado")

verificarEmail()