import clases #Importando Todas las Clases 

persona = clases.Persona()# creando el objeto persona de la calses Personas
persona.setNombre("John")
persona.setApellidos("Olivares")
persona.setAltura("170cm")
persona.setEdad("42 años")
print(f"La persona es: {persona.getNombre()} y su apellido es {persona.getApellidos()}")
print(persona.hablar())
print("\n**********************************************************************")

informatico = clases.Informatico()#Creando una persona de tipo informatico
informatico.setNombre("Alex")
informatico.setApellidos("Devs")
print(f"El informacio es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.programar())
print(informatico.getLenguajes())
print(informatico.hablar())
print(informatico.aprender("Python"))


print("\n**********************************************************************")

redes = clases.Tecnico()
print(redes.dominioRedes)
print(redes.auditoria2())




