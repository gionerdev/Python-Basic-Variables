"""Las variables son contenedoras de datos que ocupan un espacio en la memoria 
La dirección que ocupan en la memoria se puede verificar con la función id()"""
"la variable se declare, no obstante se crea al momento de definirle un valor"

name = "Agatha"
surname = "Christie"
age = 85
book = "Muerte En El Nilo" 
category = "Crime, Police"

"""Las variables pueden ir variando de datos a lo largo del programa,
esto es debido a su tipado dinámico en donde puede tomar distintos datos sin necesidad de
especificar"""

name = "Howard Phillip"
surname = "Lovecraft"
book = "Los Gatos de Ulthar"
category = "Terror, Sci-Fi"

"Creando otras variables"

color = "Rojo"
color2 = "Verde"
color3 = "Azul"
color4 = "Amarillo"
color5 = "Magenta"

"Variables que contienen información personal"

country = "Venezuela"
state = "Miranda"
kind_of_blood = 'B'

"Variables con cadenas largas"

message = """Hello, can you give me a frapuccino with extra cream?\nand a candy bread."""

"El \n se utiliza para hacer un salto de linea. \ Se usa para tabular."

message2 = """Hello World, my name is Gioner and this is a test in Python."""  

"Variables agrupadas"
"No es recomendada esta sintaxis."

x, y, z = 'Coffe', 'Cream', 'Milk'

"""Desempaquetar un dato, los datos de una colección o un string pueden ser
vinculados a otra variable""" 

"Dependiendo la cantidad de datos, se añaden las variables."

lista = [1, 1, 2, 3, 5, 8]

uno, dos, tres, cuatro, cinco, seis = lista 

print() 
