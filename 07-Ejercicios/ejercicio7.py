#Paragama que imprime los numeros impares

num1 = int(input("Primer Nuemro: ?"))
num2 = int(input("Segundo Numero: ?"))

if num1 < num2:
    for e in range(num1,num2):
        resto = e % 2
        if resto != 0:
            print(f"El numero impar es: {e}")
else:
    print("El primer Numero debe ser menor que el segundo")