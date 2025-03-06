import math

# def es una funcion que recibe dos parametros, precio e interes, y retorna el resultado de multiplicar precio por interes
# precio: int
# interes: int
# float: int
def calcularInteres(precio, interes):

    return precio * interes

def calcularPrecio(precio, ganacia):

    return precio + (ganacia * precio)


def  precioVenta(precio, interes, ganacia):
    total = calcularPrecio(precio, ganacia)
    interes = calcularInteres(total, interes)
    return  total + interes
 
interes = float(input("Ingrese el interes: "))
precio = float(input("Ingrese el precio: "))    
ganacia = float(input("Ingrese la ganacia: "))

print(precioVenta(precio, interes, ganacia))

import random

def numero_aleatorio():
    print("Generador de Número Aleatorio")
    num = random.randint(1, 100)
    print(f"Número generado: {num}")

numero_aleatorio()

def comparar_cadenas():
    cadena1 = input("Ingrese la primera cadena: ")
    cadena2 = input("Ingrese la segunda cadena: ")
    
    if cadena1 == cadena2:
        print("Las cadenas son iguales.")
    else:
        print("Las cadenas son diferentes.")
        if cadena1 > cadena2:
            print(f'"{cadena1}" es mayor en orden alfabético que "{cadena2}".')
        else:
            print(f'"{cadena2}" es mayor en orden alfabético que "{cadena1}".')

comparar_cadenas()

print("Bienvenido dinos los precio, ganncia y impuesto")
#escribir  leer 
precio =  input("engrese el precio: ")
precio = float(precio)
ganacia =  input("engrese el ganancia: ")
ganacia = float(ganacia)
impuesto =  input("engrese el impuesto: ")
impuesto = float(impuesto)
#funcion nombre de l avariable()
def calcularImpuesto(impuesto, precio):
    return impuesto * precio
def calcularGanancia(ganacia, precio):
    return ganacia * precio

def calcularPrecioFinal(precio, impuesto, ganancia):
    precio1 = calcularGanancia(ganacia, precio) + precio
    impuestVenta = calcularImpuesto(impuesto, precio1)
    return precio1 + impuestVenta

print(calcularPrecioFinal(precio, impuesto, ganacia))