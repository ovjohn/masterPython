#Funciones y Metodos Predefenidas para tratar listas

cantantes = ["Julio", "Alice", "2pac", "Bunny"]
numeros = [1, 2, 5, 8, 3, 6, 4,8]

#Ordenar lista
print(numeros)
numeros.sort()#Metodo sort para Ordenar una lista
print(numeros)

#Añadir Elementos
cantantes.append("Alejandro")#Metodo append, para agregar un nuevo
cantantes.insert(2,"2do_Bolt")#Metodo para agregar un nuevo valor pero pasndo el indece tambien
print(cantantes)

#Eliminar Elementos
cantantes.pop(1)#Eleminar un objeto por el indice
cantantes.remove("Bunny")#Eliminar un obejeto por su nombre exacto
print(cantantes)

#Ordenar de forma invertida
print(numeros)
numeros.reverse()#Metodo para ordenar de forma inversa una Lista
print(numeros)

#Buscar dentro de una lista
print("Julio" in cantantes)#Buscar un elemento dentron de la lista con (in)

#Contar Elemento en una lista
print(len(cantantes))

#Contar cuantas veses aparece un elemento
print(numeros.count(8))

#Conseguir Indece
print(cantantes.index("Julio"))#Metodo para conseguir el indice de parametro

#Unir listas
cantantes.extend(numeros)
print(cantantes)