# EJERCÍCIOS DE PYTHON

## EJERCÍCIOS DE PYTHON PARA REFORZAR LA LÓGICA DE PROGRAMACIÓN Y REPASAR CONCEPTOS
Versión usada de Python: Python3
## CONTENIDO:
- Estructuras de control y cadenas de caracteres
- Diccionario
- Matrices
- Listas
- Tuplas
- Sets
- Programación orientada a objetos y herencia
- Generadores
- Archivos
- Dataframe, tratamiento de datos con librería Pandas
- Bases de datos sql

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
### Armstrong: ejercicio 23 Decir si un número es armstrong o no
### verificarEmail: ejercicio 31, se pide al usuario que introduzca un correo y se verifica si es correo o no, (es correo si tiene @)
### anagrama: ejercicio 16 Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas. Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial. NO hace falta comprobar que ambas palabras existan. Dos palabras exactamente iguales no son anagrama.
### acronimo: ejercicio 34 buscar acrónimo de una organización.
### infoCorreo: ejercicio 35 Extractor de información del correo electrónico
Recopile una dirección de correo electrónico del usuario y luego averigüe si el usuario tiene un nombre de dominio personalizado o un nombre de dominio popular. Por ejemplo

Recopilamos una dirección de correo electrónico del usuario y luego vamos a averiguar si ese email tiene nombre de dominio personalizado o un nombre de un dominio popular. Por ejemplo:

Entrada: mary.jane@gmail.com
Salida: Hola Mary, estoy viendo que tu email está registrado con Google. ¡Eso es genial!.
### calcularPropinas: ejercicio 36 Se pide la factura y se pide al cliente que elija la propina (18%,20% y 25%), se calcula la propina delegida, y el total de la factura incluida la propina
### calculoTest: ejercicio 37: Una empresa que realiza pruebas de selecció de personal, necesita conocer el puntaje total obtenido por los candidatos que presenten las pruebas técnicas a un determinado empleo. El puntaje total se calcula del puntaje obtenido por respuestas correctas el obtenido por respuestas incorrectas y en blanco. Por cada respuesta correcta se obtienen 5 puntos, respuesta incorrecta -2 puntos y respuesta en blanco -1 punto. La cantidad total de preguntas que tiene la evaluación son 20.
### mcdMcm: ejercicio 56 
    Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD) 
    y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
    - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
### areaPoligono: ejercicio 70 Crea una única función (importante que sea única) que sea capaz de calcular y retornar el área de un polígono:
- La función recibirá por parámetro sólo un polígono a la vez.
- Los polígonos soportados serán Triángulos, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo

## Diccionario

### monedas: ejercicio 6 Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
### frutas: ejercicio 7 Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
### creditos: ejercicio 8 Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
### persona: ejercicio 9 Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
### maquinaExpendedora: ejercicio 10 Primero se introducen monedas, sólo se permiten monedas de 0.10 (10 céntimos), 0.05 (5 céntimos), 0.20 (20 céntimos) y 0.50 (50 céntimos), 1 (1 euro) o 2 (2 euros) .Elegir el producto y comprar, en caso de que no se disponga de crédito suficiente mostrar mensaje y si el crédito es superior dar el cambio correspondiente.
### traductor: ejercicio 11 Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
### traductorMorse: ejercicio15.py Crea un programa que sea capaz de transformar texto natural a código morse y viceversa. Debe detectar automáticamente de qué tipo se trata y realizar la conversión. En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ". El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse
### contactos: ejercicio 27 El siguiente programa lee valores del teclado para crear una colección de contactos bajo la forma de lista de diccionarios. Solo cuando se introducen valores no vacíos, se almacenan en el diccionario. El número total de contactos es indefinido y depende del usuario, al que se le pregunta si desea introducir más contactos después de cada uno de ellos.
### botEliza: ejercicio 46 sobre crear un bot mediante un diccionario
### pokemon: ejercicio 69 Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
    - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
    - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
    - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
    (buscar su efectividad)
    - El programa recibe los siguientes parámetros:
    - Tipo del Pokémon atacante.
    - Tipo del Pokémon defensor.
    - Ataque: Entre 1 y 100.
    - Defensa: Entre 1 y 100.
    
## Matrices

### ordenarMatriz: ejercicio 4 que pide ordenar cada una de las filas de una matriz primero de menor a mayor y luego de mayor a menor
### matrizDecimales: ejercicio 29 elegir el número de filas y columnas de una matriz, rellenarla con 1 o 0 (no permtir números que no sean 1 o 0). Pasar de binario a decimal cada una de las filas que componen la matriz
### calcularSubtotal: ejercicio 30 pide elegir 6 artículos de productos de una matriz (siempre y cuando el stock no sea 0) y cacular el subtotal y total

## Listas

### contadorVocales: ejercicio 12 , Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal. Contar también el número de consonantes que aparecen en la palabra. Mostrar todos los datos en matriz tabulada
### numerosInversos: ejercicio 13 Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
### comunesNoComunes: ejercicio 25 Crea una función que reciba dos array, un booleano y retorne un array.
- Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
- Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
### consonantesVocales: ejercicio 26 , dada una lista con palabras contar las consonantes y vocales
### fibonacci: ejercicio 33 , Dado un número, mostrar su serie de fibonacci. La serie de fibonacci es un orden de números donde cada número es la suma de los dos anteriores.
### numerosPerdidos: ejercicio 53 Dado un array de enteros ordenado y sin repetidos, crea una función que calcule  y retorne todos los que faltan entre el mayor y el menor. Lanza un error si el array de entrada no es correcto (si está vacío o contiene repetidos).
### eliminarCaracteres: ejercicio 55 Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
    - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
    - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1
### ordenarLista: ejercicio 65, Ordenar lista sin usar el método sort

## Tuplas

### contarLetras: ejercicio 3 que muestra la longitud de una tupla, añade un dato a esta y cuenta las letras de cada una de las palabras que forman la tupla
### segundoGrande: ejercicio 14 Dado una tupla de números encuentra el segundo más grande
### carreraObstaculos: ejercicio 24 Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente la carrera. Para ello tiene que realizar la opción correcta en cada tramo de la pista.: La función recibirá dos parámetros:
    - Un array que sólo puede contener String con las palabras "run" o "jump"
    - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
    - La función imprimirá cómo ha finalizado la carrera:
    - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
variará el símbolo de esa parte de la pista.
    - Si hace "jump" en "_" (suelo), se variará la pista por "x".
    - Si hace "run" en "|" (valla), se variará la pista por "/".
    - La función retornará un Boolean que indique si ha superado la carrera.

## Sets

### trabajarSets: ejercicio 71 trabajarSets: ejercicio Crear dos sets (set1 y set2) con datos y unirlos en set3. Volver a intentar unir set2 y ver que pasa. Eliminar set2 del set1 y preguntar si Perla que es el contenido de set2 está en la lista de set3. Eliminar Jorge de set3.Finalmente pasar set a lista ordenada.

## Programación orientada a objetos y herencia

### cochesMotosPOO: ejercicio 44 crea clase vehiculo con atributos color y ruedas, la clase coche hereda de vehculo y tiene velocidad en km y cilindrada cc de atributos; la clase bicicleta hereda de vehículo con el atributo urbana. De coche hereda camioneta con carga kg y de bicicleta hereda motocicleta con atributos de velocidad km/h y cilindrada cc. Métodos catalogar que muestra el color del auto y en coche y bicicleta sobreescribir la función catalogar para que muestre las ruedas también.
### luchaPOO: ejercicio 45 crear dos clases una de Luchadores cuyos atributos son nombre, kit, ssj, ataque, defensa y vida y el método es Atacar; y otra clase Batalla que actúa como menú llamando en sus atributos a los luchadores y comenzando la batalla por turnos. Si el jugador es atacado pierde vida
### personaPOO: ejercicio 47 crear clase persona con constructir con atributos nombre, edad y dni, y método que muestre la edad del objeto y otro que diga si es mayor de edad o no
### calculadoraPOO: ejercicio 48 crear calculadora con constructor que coge los números que introduce el usuario, el usuario también elige el operador y en función de eso se hace la operación que corresponda
### listadeTareas: ejercicio 49 crear lista de tareas sin constructor pasando por argumento una lista, creando una clase con los métodos de mostrar, agregar y quitar
### revertir: ejercicio 50 revertir una lista a través de POO tomando como atributo la lista y usando los métodos revertir y mostrarFrase.

## Archivos

### leerArchivos: ejercicio 28 crear un archivo en cmd , escribir contenido mendiante comandos y leer su contenido linea por linea y pasarlo a una lista
### leerArchivos2: ejercicio 30 crear un archivo en cmd , escribir contenido mediante comandos y leer su contenido de golpe
### contarLineas: ejercicio 38 Files exercise. Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words
### contarRepes: ejercicio 52 JSON:
    - Pasar archivo json a diccionario.
    - Mostrar un listado con los toppings que hay sin repeticiones
    - Mostrar un listado con los toppings no repetidos, y mostrar
    - un listado con lostoppings repetidos
### escribirArchivo: ejercicio 51 Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa. El programa incorporar funciones crear el fichero con el listín si no existe, para consultar el nombre de un cliente y mostrar su teléfono, añadir el teléfono de un nuevo cliente,consultar el teléfono de un cliente y mostrar su nombre o eliminar contacto. El listín debe estar guardado en el fichero de texto archivo.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.(en proceso sin terminar)
### calcularoraTXT: ejercicio 54 Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
    - El .txt se corresponde con las entradas de una calculadora.
    - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
    - Soporta números enteros y decimales.
    - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
    - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
### quitarSalto ejercicio 61. Dado un archivo txt quitar los saltos de línea

## Generadores

### listaGenerador: ejercicio 59 Crear una función generadora para iterar un límite que viene dado por parámetro con generadores. Llamar a esta función generadora 10 veces usando un contador.
### generadoresEnlazados: ejercicio 60 Crear dos generadores que enlazan en una iteración cuando se itera un límite que viene dado por parámetro. Iterar sólo los 4 primeros.

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
### dataframe: ejercicio 66 DATAFRAME
    - Crear dataframe con datos de casas, precios y metros cuadrados e imprimir todos los datos
    - Imprimir los datos únicamente de precios y metros
    - Crear archivo csv con los mismos datos y crear dataframe desde esos datos del csv. Mostrar todos sus datos
    - Mostrar los datos de las casas y los precios del dataframe csv
    - Mostrar los 3 primeros datos del archivo css
    - Mostrar la media de los precios de las viviendas del dataframe del archivo css
    - Contar el número de viviendas que hay en el dataframe del archivo css
    - Máximo precio, mínimo precio, máximos metros y mínimos metros en el dataframe del archivo css
### prediccionInmobiliaria: ejercicio 67, PREDICCIÓN INMOBILIARIA CON PANDAS Y SKLEARN
Crear un archivo llamado barrios.csv con los datos de precio,metros y barrio de viviendas.
En el que 0 es barrio de nivel medio o bajo y 1 es barrio de alto nivel.
    - Crear dataframe con los datos del csv
    - Crear variable x con datos de los metros y el barrio, estos datos son los que queremos predecir
    - Crear variable y con los datos del precio, a través de estos datos queremos saber el precio de predición de nuestra vivienda
    - Obteniendo unos metros y barrio predecir cuánto va a costar la vivienda mediante sklearn a través del dataframe obtenido del csv

## Bases de datos

### bbddPersonas: ejercicio 57 BBDD. Crear una tabla personas con datos de id (autoincrementable, not null, y clave primaria), nombre (texto, not null), apellidos (texto, not null), documento (texto not null), fecha (integer, not null, única); e introduce datos en DB Browser for SQLite. Una vez hecho esto:
- Conectar con la bbdd
- Mostrar el primer registro de la bbdd
- Mostrar todos los registros de la bbdd
### bbddPersonas: ejercicio 58. Insertar datos dentro de la bbdd personas
### bbddPersonas: ejercicio 62. Eliminar un registro de la tabla de personas
### bbddPersonas: ejercicio 63. Actualizar un dato de un registro en la tabla personas
### bbddPadresHijos: ejercicio 65. CLAVE FORÁNEA Y CONSULTAS DE VARIAS TABLAS
    - Crear una bbdd de con las tablas de Padres e Hijos cuya clave foránea sea el id del padre,
    - Rellenar la tabla con datos.
    - Mostrar el nombre, apellidos del padre; nombre y apellidos de los hijos cuyo id de padre sea 3
    - Tabular los resultados con titulo de cabecera
### CRUDCitas: ejercicio 68, Crud de citas que permite crear cita, modificar cita, eliminar cita, ver cita


