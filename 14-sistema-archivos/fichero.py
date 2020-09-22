from io import open #Importando del paquete io el modulo open
import pathlib

#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero-texto.txt"
archivo = open(ruta,"a+")

#Escribir
archivo.write("*********Soy un texto creado por python************\n")

#Cerrar archivo
archivo.close()