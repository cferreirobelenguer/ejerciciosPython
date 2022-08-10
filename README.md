# EJERCÍCIOS DE PYTHON

## EJERCÍCIOS DE PYTHON PARA REFORZAR LA LÓGICA DE PROGRAMACIÓN Y REPASAR CONCEPTOS
Versión usada de Python: Python3

# INDICE DE EJERCICIOS

## Estructuras de control y cadenas de caracteres

### invertirPalabra: ejercicio 1 de invertir una palabra que introduce el usuario
### numeroPrimo: ejercicio 2 dice si un número pasado por parámetro en la función es primo o no
### parImpar: ejercicio 5 pedir al usuario un número del 1 a 1000 y decir si es par o impar
### mayorDigito: ejercicio 17 introducir un valor y calcular el valor mayor de sus dígitos
### multiplos: ejercicio 18 dados tres números mostrar los múltiplos de A, menores que B y que no sean dividores de C usando estructuras de control
### FIZZBUZZ: ejercicio 19 EL FAMOSO "FIZZ BUZZ". Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
### combinaciones: ejercicio 20 sobre mostrar la combinación mayor de 3 números usando estructuras de control
### generosEdades: ejercicio 21 sobre hacer recuento de asistentes de un evento por género y edades usando estructuras de control
### numeroPerfecto: ejercicio 22 determinar si un número x es perfecto, si la suma de sus divisores es el mismo número, usando estructuras de control
### verificarEmail: ejercicio 31, se pide al usuario que introduzca un correo y se verifica si es correo o no, (es correo si tiene @)
### anagrama: ejercicio 16 Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas. Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial. NO hace falta comprobar que ambas palabras existan. Dos palabras exactamente iguales no son anagrama.



## Diccionario

### monedas: ejercicio 6 Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
### frutas: ejercicio 7 Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
### creditos: ejercicio 8 Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
### persona: ejercicio 9 Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
### maquinaExpendedora: ejercicio 10 Primero se introducen monedas, sólo se permiten monedas de 0.10 (10 céntimos), 0.05 (5 céntimos), 0.20 (20 céntimos) y 0.50 (50 céntimos), 1 (1 euro) o 2 (2 euros) .Elegir el producto y comprar, en caso de que no se disponga de crédito suficiente mostrar mensaje y si el crédito es superior dar el cambio correspondiente.
### traductor: ejercicio 11 Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
### traductorMorse: ejercicio15.py Crea un programa que sea capaz de transformar texto natural a código morse y viceversa. Debe detectar automáticamente de qué tipo se trata y realizar la conversión. En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ". El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse
### botEliza: ejercicio 46 sobre crear un bot mediante un diccionario

## Matrices

### ordenarMatriz: ejercicio 4 que pide ordenar cada una de las filas de una matriz primero de menor a mayor y luego de mayor a menor
### matrizDecimales: ejercicio 29 elegir el número de filas y columnas de una matriz, rellenarla con 1 o 0 (no permtir números que no sean 1 o 0). Pasar de binario a decimal cada una de las filas que componen la matriz
### calcularSubtotal: ejercicio 30 pide elegir 6 artículos de productos de una matriz (siempre y cuando el stock no sea 0) y cacular el subtotal y total

## Listas

### contadorVocales: ejercicio 12 , Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal. Contar también el número de consonantes que aparecen en la palabra. Mostrar todos los datos en matriz tabulada
### numerosInversos: ejercicio 13 Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
### consonantesVocales: ejercicio 26 , dada una lista con palabras contar las consonantes y vocales

## Tuplas

### contarLetras: ejercicio 3 que muestra la longitud de una tupla, añade un dato a esta y cuenta las letras de cada una de las palabras que forman la tupla
### segundoGrande: ejercicio 14 Dado una tupla de números encuentra el segundo más grande

## Programación orientada a objetos

### cochesMotosPOO: ejercicio 44 crea clase vehiculo con atributos color y ruedas, la clase coche hereda de vehculo y tiene velocidad en km y cilindrada cc de atributos; la clase bicicleta hereda de vehículo con el atributo urbana. De coche hereda camioneta con carga kg y de bicicleta hereda motocicleta con atributos de velocidad km/h y cilindrada cc. Métodos catalogar que muestra el color del auto y en coche y bicicleta sobreescribir la función catalogar para que muestre las ruedas también.
### luchaPOO: ejercicio 45 crear dos clases una de Luchadores cuyos atributos son nombre, kit, ssj, ataque, defensa y vida y el método es Atacar; y otra clase Batalla que actúa como menú llamando en sus atributos a los luchadores y comenzando la batalla por turnos. Si el jugador es atacado pierde vida
### personaPOO: ejercicio 47 crear clase persona con constructir con atributos nombre, edad y dni, y método que muestre la edad del objeto y otro que diga si es mayor de edad o no
### calculadoraPOO: ejercicio 48 crear calculadora con constructor que coge los números que introduce el usuario, el usuario también elige el operador y en función de eso se hace la operación que corresponda
### listadeTareas: ejercicio 49 crear lista de tareas sin constructor pasando por argumento una lista, creando una clase con los métodos de mostrar, agregar y quitar
### revertir: ejercicio 50 revertir una lista a través de POO tomando como atributo la lista y usando los métodos revertir y mostrarFrase.

## Dataframe, tratamiento de datos con librería Pandas

### cotizacionesBolsa: ejercicio 39 El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros). Construir una función que construya un DataFrame a partir del un fichero con el formato anterior y devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.
### datosDataframe: ejerccio 40 Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente. Calculamos el total de ventas, total de gastos, el mínimo y máximo de ventas y el mínimo y máximo de gastos:
Mes	Ventas	Gastos
Enero	30500	22000
Febrero	35600	23400
Marzo	28300	18100
Abril	33900	20700

### pandasExcel: ejercicio 41 leer los datos de nombre y correo de un excel con pandas
### pandasHtml: ejercicio 42 Leer los datos de una tabla html con Pandas
### proyectoPandas: ejercicio 43 Crear un archivo csv y leer el contenido de sus datos mediante creando un dataframe con pandas.

## Trabajando con bases de datos

## Django

