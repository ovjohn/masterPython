from io import open #Importando del paquete io el modulo open
import pathlib
import shutil #Modulo para copiar y pegar ficheros

#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero-texto.txt"
archivo = open(ruta,"a+")

#Escribir
archivo.write("*********Soy un texto creado por python************\n")

#Cerrar archivo
archivo.close()

#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero-texto.txt"
archivo_contenido = open(ruta,"r") #Con el atributo "r" para abrir solo lectura

# Leer contenido
#contenido = archivo_contenido.read() #Aqui se usa el metodo read para leer
#print(type(contenido))

#Leer contenido y guardar en Lista
lista = archivo_contenido.readlines()
archivo_contenido.close

for e in lista:
    print("- "+e.center(10))

#Copiando Fichero
rutaOriginal = str(pathlib.Path().absolute()) + "/fichero-texto.txt"
rutaNueva = str(pathlib.Path().absolute()) + "/fichero-nuevo.txt"

shutil.copyfile(rutaOriginal, rutaNueva) #modulo que sireve para copiar un fichero a otro lugar
