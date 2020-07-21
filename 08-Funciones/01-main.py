"""
Una funcion es un conjunto de instrucciones agrupadas
bajo un nombre en concreto y que se puede reulitizar
tantas veces sea necesariio

ejemplo:

def nombrePersona(parametros)
    #Aquí el conjunto de instrucciones

#Para llamarla se hace así: nombrePersona(mi-parametro)
"""
"""
#------------------ -----------------------Ejemplo1 -------------------
print("############ Ejemplo 1 - Funciones")

#Definiendo funcion
def muestraNombre():
    print("Juan")
    print("Perez")
    print("Almirca")
#Invocando o llamando la funcion
muestraNombre()


#---------------------------------------------  Ejemplo2-------------------------------
print("############ Ejemplo 2 - Funciones")
#Funciones con parametros
def mostrarNombre(nom, edad):
    print(f"Tu monbre es: {nom}")
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres Menor de edad!")

name = input("Introduce tu nombre: ")
ege = int(input("Introduzca tu edad: "))

mostrarNombre(name,ege)


#---------------------------   Ejemplo3 Tabla de multiplicar con una funcion ------------------

print("############ Ejemplo 3 - Tabla de Multiplicar con Funciones")

numTabla = int(input("De cual numero quiere la tabla de Multiplicar?: "))
def tablaMultiplicar(numTabla):
    for e in range(1,11):
        print(f"{e} x {numTabla} = {e * numTabla}")
    print("\n")

tablaMultiplicar(numTabla)

#----------> Ejemplo3.1 all table with upper funtion
for all in range(11):
    tablaMultiplicar(all)


#---------------------------   Ejemplo 4 ------------------

print("\n ############ Ejemplo 4 - Tabla de Multiplicar con Funciones")

#----------------> Parametros opcionales
def getEmpleado(name, ndi = None):
    print("EMPLEADO")
    print(f"{name}")
    if ndi != None:
        print(f"{ndi}")
getEmpleado("John")

#---------------------------   Ejemplo 4.1 ------------------
print("\n ############ Ejemplo 4 - OFERTA DE EMPLEO TELEGRAM")

oferta = input("Cual es tu oferta de Empleo: ")
def publicarEmpleo(oferta = None):
        while oferta != None:
                print(f"Oferta laboral para Developers: {oferta}")
                oferta = None
publicarEmpleo(oferta)

#---------------------------   Ejemplo 5 ------------------
print("\n ############ Ejemplo 5 - Return")
def saludame(saludo):
        name = f"Hola {saludo}"

        return name
print(saludame("Juan"))

#---------------------------   Ejemplo 6 ------------------
print("\n ############ Ejemplo 6 - Return")
def calculadora(n1,n2, operation = False):
        suma = n1 + n2
        resta = n1 - n2
        multi = n1 * n2
        divi = n1 / n2

        cadena =""

        if operation != False:
                cadena += "Suma: " + str(suma)
                cadena += "\n"
                cadena += "Resta: " + str(resta)
                cadena += "\n"
        else:
                cadena += "Multiplicacion: " + str(multi)
                cadena += "\n"
                cadena += "Division : " + str(divi)
                cadena += "\n"

        return cadena
print(calculadora(2,2, True))
"""
#---------------------------   Ejemplo 7 ------------------
print("\n ############ Ejemplo 7 - Funciones dentro de otras Funciones")
 
def getName(name):
         text = f"Tu monbres es: {name}"
         return(text)

def getLastname(lastname):
        text = f"Your Last Name is: {lastname}"
        return(text)

def getAll(name,lastname):
        text = getName(name) + "\n" + getLastname(lastname)
        return(text)

print(getAll("John","Oli"))

#------------------------ Ejemplo 8 ----------------------------
print("\n ################# Ejemplo 8 - Funcion lambda ")

get_year = lambda year: f"Dime el año: {year}" #Funcion anonima lambda - Se bede hacer en una sola linea

print(get_year(2020))








