#Print rango entre dos numeros

n1 = int(input("Indruduce el primer numero: "))
n2 = int(input("Introduce el segundo numero: "))

if n1 < n2:
    for i in range(n1,n2+1):
        print(i)
else:
    print("Introuzca el primer numero menor al segundo!!")