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
canciones[2] = "New Movie"#Cambio de la pelicula en indice 2

pelicula[1] = "New Pelicula" # Modificar el elemento Uno de la lista
print(pelicula[1]) #Por numero d Indice
print(canciones[0:2])# Por rango
print(pelicula[1:])# Apartir del indice 1 hasta el final
print(canciones)

#Añadir elementos a una lista
canciones.append("Fly to the Moon")
print(canciones)

#Recorrer Lista
new_movie = ""
while new_movie != "stop":
    new_movie = input("Introduce Nueva Pelicula: ")
    if new_movie != "stop":
        pelicula.append(new_movie)
print("\n**********Listas de Canciones***********")
for x in pelicula:
    print(f"{pelicula.index(x)}. {x}")
