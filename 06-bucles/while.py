""" BUCLE WHILE """

contador = 1
while contador <= 2:
    print(f"El numero del contador es: {contador}")
    contador += 1

#Ejercicio2
contador2 = 1
muestrame = str(0)
while contador2 <= 10:
    muestrame = muestrame +", "+ str(contador2)
    contador2 += 1
print(muestrame)

#Ejercicio Tabla de Multiplicar
print("\n########## Tabla de Multiplicar")

numero = int(input("¿De que numero quiere la tabla de multiplicar: ?"))
contador3 = 1

if numero < 1:
    numero = 1
while contador3 <= 10:
    print(f"{numero} x {contador3} = {numero*contador3}")
    contador3 += 1
        
    

