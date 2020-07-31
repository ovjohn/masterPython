"""
Sets, es una colaccion de datos que no tiene
ni indice ni orden. Se define con {}.
"""

personas = {
    "Pedro",
    "Alberto",
    "Juan"
}
personas.add("Paco")#Metodo para agregar un nuevo valor
personas.remove("Pedro")#Metodo para eleminar un valor

print(type(personas))
print(personas)

