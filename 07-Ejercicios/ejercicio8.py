"""
Ejercicio 8, Cuanto es el X Porciento
del Numero que se pida?
"""

num = int(input("Introduzca el numero: "))
porcentaje = int(input("Diga que porcentaje quiere sacar: "))

p = (num * porcentaje/100)

print(f"El {porcentaje}% de {num} es: {p}%")