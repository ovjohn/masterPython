"""
Ejercicio 5.
Crear una lista con el contenido de la siguiente tabla:

ACCION      AVENTURA        DEPORTES
Gta         Assins          Fifa 21
Cod         Crash           Pro 21
Pugb        Prince Percia   Moto GP 21

Mostrar esta informacion de forma Ordenada
"""

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["Gta","Cod","Pugb"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["Assins","Crash","Prince Percia"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["Fifa21","Pro21","Moto GP21"]
    }
]

for i in tabla:
    print(f"........{i['categoria']}..........")
    for j in i['juegos']:
        print(f"{j}")
    print("\n")