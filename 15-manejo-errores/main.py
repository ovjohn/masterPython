"""
Excepciones y manejo de errores 
y como capturarlos
"""

"""
try:
    nombre = input("Cual es tu Nombre: ?")

    if len(nombre) > 1:
        name = "El nombre es: " + nombre
    print(name)
except:
    print("Ha ocurrido un error, por favor mete bien el nombre")
else:
    print("Felicitaciones todo ha ido bien¡¡¡")
finally:
    print("Fin del programa")
"""
"""
#Multiples excepciones
try:
    numero = int(input("Intruduzca un numero para elevar a cuadrado: "))
    cuadrado = "El cuandrado es "+ str(numero * numero)
    print(cuadrado)
except TypeError:
    print("Debes de convertir tu cadena en entero en tu codigo")
except ValueError:
    print("Introduzco un numero correpto¡¡")
#except Exception as e:
#    print("Ha ocurrido un error", type(e).__name__)
"""

#Excepciones personalizadas

nombre = input("Introduzca tu monbre:")
edad = int(input("Cual es tu edad ?:"))

if edad < 5 or edad > 100:
    raise ValueError("La edad intruducidad no es Real")
elif len(nombre) <= 1:
    raise ValueError("El nombre no es real")
else:
    print("Bienvenido todo esta en orden¡")