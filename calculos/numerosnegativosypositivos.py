#Determinar si un número es positivo, negativo o cero

numero = float(input("Ingrese un número: "))
if numero > 0:
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print("El número es cero")