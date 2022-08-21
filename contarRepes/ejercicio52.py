"""
JSON:
Pasar archivo json a diccionario.
Mostrar un listado con los toppings no repetidos, y mostrar
un listado con lostoppings repetidos
"""
import json
from multiprocessing.sharedctypes import Value

datos_JSON ="""{
	"tamano": "mediana",
	"precio": 15.67,
	"toppings": ["queso extra", "pepperoni", "albahaca","champiñones","queso extra","champiñones","champiñones"],
	"cliente": {
		"nombre": "Jane Doe",
		"telefono": "455-344-234",
		"correo": "janedoe@email.com"
	}
}"""
def pasarDiccionario(datos_JSON):
    listado=json.loads(datos_JSON)
    listaRepes=[]
    listaNoRepes=[]
    
    for key,values in listado.items():
        print("La clave es ",key," y el valor es ",values)
        if(key=="toppings"):
            for i in values:
                if i in listaNoRepes:
                    listaRepes.append(i)
                else:
                    listaNoRepes.append(i)
    print("Listado de ingredientes no repetidos: ",listaNoRepes)
    print("Lista de ingredientes repetidos: ",listaRepes)
pasarDiccionario(datos_JSON)