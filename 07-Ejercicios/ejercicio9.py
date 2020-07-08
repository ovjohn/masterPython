"""
Hacer un programa que pide un numero indifenidamente hast que introduzcan 111
"""

n = int

while n != 111:
    n = int(input("Introzca un numero: "))
    print(f"El numero que introduzjo es: {n}")
else:
    print("FIN")