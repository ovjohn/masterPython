#Calculadora

num_1 = int(input("Numero 1: ? "))
num_2 = int(input("Numero 2: ?"))

suma = num_1 + num_2
resta = num_1 - num_2
multipilacion = num_1 * num_2
divicion = num_1 / num_2

operacion = int(input(" Que quieres hacer: ? \n Precione 1 para -> Suma.\n Precione 2 para->Resta.\n Precione 3 para ->Multiplicacion. \n Precione 4 para ->Divicion>"))

if operacion == 1:
    print(f"La suma es: {suma}")
elif operacion == 2:
    print(f"La resta es: {resta}")
elif operacion == 3:
    print(f"La multiplicacion es: {multipilacion}")
elif operacion == 4:
    print(f"La divicion es: {divicion}")
else: 
    print("Por favor escoja una opcion valida!") 