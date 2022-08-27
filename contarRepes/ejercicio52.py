"""
JSON:
Pasar archivo json a diccionario.
Mostrar un listado con los toppings que hay sin repeticiones
Mostrar un listado con los toppings no repetidos, y mostrar
un listado con lostoppings repetidos
"""
import json


datos_JSON ="""{
	"tamano": "mediana",
	"precio": 15.67,
	"toppings": ["queso extra", "pepperoni", "albahaca","champiñones","queso extra","champiñones","champiñones","nata","nata"],
	"cliente": {
		"nombre": "Jane Doe",
		"telefono": "455-344-234",
		"correo": "janedoe@email.com"
	}
}"""

def pasarDiccionario(datos_JSON):
    #Importamos el json para poder leerlo
    listado=json.loads(datos_JSON)
    #Trabajamos con set para que no se repitan datos
    listaRepes=set()
    listaNoRepes=set()
    lista=[]

    for key,values in listado.items():
        if(key=="toppings"):
            for i in values:
                print(i)
                #Mostramos los repetidos creando un set y comparándolo con la lista de ingredientes
                if i in lista:
                    listaRepes.add(i)
                else:
                #Se crea una lista con los datos del archivo de json
                    lista.append(i)
    # En caso de que los datos de la lista no estén en la lista de repetidos, son no repetidos
    for i in lista:
        if(i not in listaRepes):
            listaNoRepes.add(i)
        
    
    print("Listado de todos los ingredientes sin repetir: ",lista)
    print("Listado de ingredientes no repetidos: ",listaNoRepes)
    print("Lista de ingredientes repetidos: ",listaRepes)
pasarDiccionario(datos_JSON)