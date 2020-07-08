"""
Programa que pide la nota de 10 alumno y 
que dice cuantos han aprobado y cuantos no!
"""
ciclo = 1
aprobados = 0
reprobados = 0


while ciclo < 11:
    nota = int(input(f"Introduzca nota del alumno-{ciclo}: "))
    if nota >= 1 and nota <= 10:
        if nota >= 5:
            aprobados += 1
        else:
            reprobados += 1
        

        ciclo += 1
    else:
        print("Introduzca una nota valida entre 0 y 10 !")
else:
    print(f"El numero de Aprobados es:{aprobados} ")
    print(f"El numero de Reprobados es:{reprobados} ")

