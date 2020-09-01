"""
Crear un script que tenga 4 variables
-) Una lista, un entero, un string y un booleano y 
imprimir un mensaje segun el tipo de dato de cada variable.
Usar funciones
"""

def traducir(tipo):
    comprobar = ""

    if tipo == list:
        comprobar = "Lista"
    elif tipo == int:
        comprobar = "Entero"
    elif tipo == str:
        comprobar = "Cadena"
    elif tipo == bool:
        comprobar = "Booleano"
    return comprobar 


def checkVar(dato, tipo):
    resultado = isinstance(dato,tipo)
    mensaje = ""

    if resultado:
        mensaje = f"El dato'{dato}' es un '{traducir(tipo)}''"
    else:
        mensaje = f"El dato '{dato}' no es de tipo: {traducir(tipo)}"
    return mensaje

usuario = ["John", 42]
grupo = 40
titulo = "String"
status = True

print(checkVar(titulo,str))
print(checkVar(usuario,list))
print(checkVar(grupo,int))
print(checkVar(status,bool))
print(checkVar(titulo,bool))








