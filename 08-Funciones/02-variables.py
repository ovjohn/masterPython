"""
Variables Globales y locales
"""

año = "Hola estamos en el año 2020 y vengo de una variable global"

def conseguir():
    #año = "Año 2020 provengo de una variable local"
    print(año)

    mes = "Julio"
    print(mes)

    global wed
    wed = "aprendiendopython.ve"


conseguir()
    
print("Esta es una Valiarble global : ", wed)