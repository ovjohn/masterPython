"""
LISTAS (arrays).
Son una coleccion de datos/valores, bajo un unico nombre.
Para acceder a esos valores, podemos usar u indice númerico.
"""

pelicula = "Batman"

#Definir Lista
pelicula = ["Sansan", "La vida es Bella", "Hombre Araña"]
canciones = list(("One", "Jupiter", "Estreñita"))#Aqui se uso la funcion list, pero hay que pasar una tupla
variadas = ["string", 2.2, 7, True]

#print(f"Primera lista: {pelicula},Segunda lista: {canciones}, Tercera lista: {variadas}")

#Indices
pelicula[1] = "New Pelicula" # Modificar el elemento Uno de la lista
print(pelicula[1]) #Por numero d Indice
print(canciones[0:2])# Por rango
print(pelicula)