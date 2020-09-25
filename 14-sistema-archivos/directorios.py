import os, shutil

#Crear una Carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
    print("Directorio creado con exito¡¡¡")
else:
    print("El directorio ya existe")

#Eliminar una carpeta
#os.rmdir("./mi_carpeta")

#Copiar Carpeta
"""
carpeta_original = "./mi_carpeta"
carpeta_copia = "./mi_carpeta_copia"
shutil.copytree(carpeta_original, carpeta_copia)
"""

#Listar el contenido de una carpeta
contenido_carpeta = os.listdir("./mi_carpeta")
print(contenido_carpeta)

for contenido in contenido_carpeta:
    print("Fichero: " + contenido)




