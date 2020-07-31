"""
Un diccionario es una coleccion de datos, que
tiene un indice alfanumerico, a diferencia de las 
listas que su indice es numericco.
Es un array asociativo o un objeto json¡¡¡¡
"""

"""
#Diccionario normal
personas = {
    "nombre": "Juan",
    "apellido": "Perez",
    "email": "pjuan@email.com"
}

print(personas)
print(type(personas))
print(personas["email"])
"""

#Diccionario Bidimencional
contactos = [
    {'nombre': 'Victor',
    'apellido': 'Valenzuela',
    'email': 'vv@email.com'
    },
    {'nombre':'Enrrique',
    'apellido': 'Izaquirre',
    'email': 'ei@email.com'
    },
    {'nombre': 'nino',
    'apellido':'dicar',
    'email': 'nidicar@email.com'
    }
]
"""
contactos[2]['email'] = 'nino@email.com'
print(contactos[2]['email'])
"""
print("********Listados de Contactos*************")
for contacto in contactos:
    print(f"El nombre es: {contacto['nombre']}")
    print(f"El apellido es: {contacto['apellido']}")
    print(f"El correo es: {contacto['email']}")
    print("\n")


