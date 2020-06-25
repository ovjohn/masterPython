""" Bucle For """

contador = 0
resultado = 0

for contador in range(1,5):
    print(f"El contador va por el elemento : { contador }")

    resultado += contador # Es igual "resultado = resultado + contador"

print(f"El resulado es: { resultado }")


#Ejemplo tabala de Multiplicar

print("\ln############ Tabla de Multiplicar")

numero_usuario = int(input("De cual numero quiere tu tabla de Multiplicar:? "))
if numero_usuario < 1:
    numero_usuario = 1
    
print(f"\ln########### La Tabla del { numero_usuario} #######################")
    
for numero_tabla in range(1, 11):
    if numero_usuario == 50:
        print("Numero prohibido")
        break

    print(f"{numero_usuario} x { numero_tabla} = {numero_tabla * numero_usuario}")
else:
    print("Fin del ejercicio")

