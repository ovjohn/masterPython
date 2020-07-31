"""
Ejercicio 1
Hacer un programa que tenga una lista de 8 numeros enteros
y haga lo siguiente.
- Recorrer la lista y mostrarla
- Crear una funcion que sirva para mostar lista y que la devuelca como string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
"""
#Crenado la lista
numeros = [2,4,8,1,6,3,5,7]

#Recorriendo la Lista
print("###### Recorriendo la Lista###S")
for x in numeros:
    print(f"El numero es: {x}")
print("\n")

print("*********Ordenando la Lisa**********")
numeros.sort()
print(numeros)
print("\n")

print("*****Longitud de la Lista********")
print(len(numeros))
print("\n")

print("*****Buscando un Elemento*********")
b =int(input("Introduzca el numero que quieres buscar: "))
if b == b in numeros:
    print(f"Felitaciones tu numero esta en la lista y es {b}")
else:
    print(f"Tu numero no esta, por favor intente de nuevo.")

#Creando una funcion
def mostarLista(lista):
    resultado = ""
    for elemento in lista:
        resultado += "El elemento:" + str(elemento)
        resultado += "\n"
    return resultado

print(mostarLista(numeros))