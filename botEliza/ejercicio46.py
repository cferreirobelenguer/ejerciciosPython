# Realizar una versión del programa Eliza sobre consola
#  Se pide desarrollar un método que realice una aproximación muy sencilla
#  a la funcionalidad que proporcionaba Eliza, En concreto el método debe realizar lo siguiente:
#  
#  Recibir frases tecleadas por un humano desde el ordenador(hasta que llegue a 10 el contador)
# Comprobar para cada frase que teclea el humano si existen en la misma
#  una serie de palabras clave.
#  Responder con un texto por pantalla a cada frase del humano en función de que la misma contuviera
#  o no una determinada palabra clave.
# En la siguiente tabla se resumen las palabras claves posibles y la frase de respuesta del ordena:
# Palabras clave:      Frase de respuesta:
# hola						hola,qué tal?
# encantado				encantado de conocerte yo también
# adiós 					adiós, espero conocerte
# hora						lo siento no llevo reloj
# nombre					Mi nombre es Eliza
# Yo he añadido al ejercicio que se trabaje con JOptionPane dando
# opción al sistema de elegir si hablar con Eliza o no, si es no se cierra el sistema.
# Y si cuando se habla con Eliza se dice adiós Eliza contesta y cierra el sistema.
# En caso de que no entienda lo que se le dice, poner un mensaje de default fallback.
intents={};
def crearIntents():
    #Creamos los intents en un diccionario
    intents.update({"hola":"hola,¿qué tal?"})
    intents.update({"encantado":"encantado de conocerte yo también"})
    intents.update({"adiós":"adiós,espero conocerte"})
    intents.update({"hora":"Lo siento no llevo reloj"})
    intents.update({"nombre":"Mi nombre es Eliza"})

def conversarEliza():
    contador=0;
    palabra=""
    print("Bienvenido, soy el asistente virtual Elisa, ¿En qué puedo ayudarte?")
    
    while(contador!=10):
        entiende=False;
        palabra=input()
        print(f"User: {palabra}")
        for keys,value in intents.items():
            if(palabra==keys):
                entiende=True;
                print(f"Eliza: {value}")
            
        if(entiende==False):
            print(f"Eliza: Ups, no te entiendo. Prueba a decirme otra cosa")
        
        contador+=1
crearIntents()
conversarEliza()