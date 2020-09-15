def holaMundo(name):
    p = print(f"Hola {name}, este es parte de un modulo:")
    return p

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