#Variables Predefinidas

name = "John"

print(name) #Para imprimir por pantalla

print(type(name))

#Detectar el tipado
tipo = isinstance(name, str)

if tipo:
    print(f"{name}, es un string")
else:
    print("No es un string")