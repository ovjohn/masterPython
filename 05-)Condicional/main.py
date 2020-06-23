#Condicional IF

""" Operadores de Comparacion

    == Igual
    != Diferente
    > Mayor
    < Menor
    >= Mayor o Igual
    <= Menor o igual """

""" Operadores de Logicos

    and Y
    or  o
    !   Negacion
    not Negacion """

#Ejemplo 1
print("############## Ejempl-1 ##############")
#color = input("Adivina cual es mi color favorito?: ")
color = "verde"

if color == "verde":
    print("El color es verde")
else:
    print("NO haz adivinado, intentalo de nuevo por favor¡")


#Ejemplo 2
print("\n############## Ejempl-2 ##############")
#year = int(input("En que año estasmos:? "))
year =2022

if year >= 2021:
    print("El Año es mayor al 2021")
else:
    print("Estas por debajo de la actualidad o 2021")

#Ejempl3
print("\n#################### Ejemplo-3 #############")
nombre = input("Cual es tu nombre:? ")
pais = "venezuela"
continente = "america"
edad = int(input("Cual es tu edad?: "))
mayoria_edad = 18

if edad >= mayoria_edad:
    proviene = input("Cual es tu pais? :")
    if proviene == pais:
        print(f"Tu continente es: {continente}")
    else:
        print("No eres de America")    
else:
    print("No eres mayor de Edad")


#Ejempl4
print("\n#################### Ejemplo-4 #############")

dia = int(input("Introduzca Día de la Semana: "))

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es mastes")
elif dia == 3:
    print(" Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es Fin de semana")


#Ejempl5
print("\n#################### Ejemplo-5 #############")

edad_min = 17
edad_max = 65
edad_real = int(input("Cual es tu edad:? "))

if edad_real >= edad_min and edad_real <= edad_max:
    print(f"Tu edad es: {edad_real} y puedes trabajar")
else:
    print(f"Tu edad de {edad_real} no es apropiada y no puedes trabajar")

#Ejempl6
print("\n#################### Ejemplo-6 #############")

pais = input("Cual es tu Pais:? ")

if pais == "mexico" or pais == "venezuela" or pais == "colombia":
    print(f"Tu pais {pais}, es habla hispana")
else:
    print("El pais no es de Habla Hispana")
