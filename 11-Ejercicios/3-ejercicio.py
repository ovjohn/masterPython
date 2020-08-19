"""
Hacer un programa que evalue si una variable esta vacia
y de ser positivo, llenarla con lestras en minuscula
 y mostrala en Mayuscala """

letras = " sebas "
if len(letras.strip()) <= 0:
     letras = "hola soy un string minuscula"
     print(letras.upper())
else:
    print("La variable tiene contenido y es:" + "'"+letras+"'")