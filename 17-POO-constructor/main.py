from coche import Coche

auto = Coche("Rojo","Doge","Ram",190,6,4)

#print(auto.getMarca())
print(auto.getInfo())

if type(auto) == Coche:
    print("Auto es un Objeto de tipo Coche")
else:
    print("Auto no es de tipo coche")

#Visibilidad de las Variasbles
print(auto.soy_publico)
#print(auto.__soy_privada)
print(auto.getPrivada())