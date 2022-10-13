# Hacer diagrama de flujo y codigo en python que calcule e imprima el factorial de un numero n

print("\n---------------------------------------------")
print("----- Calcular el factorial de un numero -----")
print("---------------------------------------------\n")

#input
n=int(input("Ingrese el numero para calcular su factorial: "))

#processing
fact=1

for i in range(n):
    i=i+1
    fact=fact*i

print("\nEl factorial de "+str(n)+" es: "+str(fact)+" \n")
