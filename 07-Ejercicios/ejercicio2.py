"""
Imprimir los numeros pares del 1 al 120
"""

for num in range(1,120):
    if num % 2 == 0:
        print(f"{num}")
    num += num