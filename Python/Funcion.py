valor = type(False)
print(valor) # <class 'bool'>
print("-------------------------") # False
bool(1)
print(bool(1)) # True
print(bool(0)) # False
print(bool(2)) # True
print(bool(-1)) # True
print(bool(0.0)) # False
print(bool(0.1)) # True
print(bool('')) # False
print(bool(' ')) # True
print(bool('Hola')) # True
print(bool([])) # False
print(bool([1,2,3])) # True
print(bool({})) # False
print(bool({'a':1})) # True
print("-------------------------") # False
print(True + True) # True
print(True + False) # False
print(False + False) # False
print(False + True) # False
print("-------------------------") # False
print(True * True) # True
print(True * False) # False
print(False * False) # False
print(False * True) # False
print("-------------------------") # False
print(True and True) # True
print(True and False) # False
print(False and False) # False
print(False and True) # False   
print("-------------------------") # False
print(True or True) # True
print(True or False) # True
print(False or False) # False
print(False or True) # True
print("-------------------------") # False

print(1 == 1) # True
print(1 == 2) # False
print(1 != 1) # False
print(1 != 2) # True
print(1 < 2) # True
print(1 > 2) # False
print(1 <= 2) # True
print(1 >= 2) # False

usuario = list()
usuario.append("EverSorto")
usuario.append("1234")
usuario.append(500)

reciboLista = list()
reciboLista.append(["123", 500])
reciboLista.append(["124", 600])
reciboLista.append(["125", 700])
reciboLista.append(["126", 800])
reciboLista.append(["127", 900])

acciones = list()
acciones.append("Deposito")
acciones.append("Pago de recibo")   
acciones.append("Retiro")

usuario2 = list()
usuario2.append("Ricardo.J.Milos")
usuario2.append("1234-55-88")
usuario2.append(100)

def registro (): 
    lista = list()
    user = input("Ingrese su usuario: ")
    passW = input("Ingrese su contraseña: ")

    lista.append(user)
    lista.append(passW)

    if usuario[0] == user and usuario[1] == passW:
        print("Bienvenido")
        return lista
    else:
        print("Usuario o contraseña incorrecta")
def oportunidad(registro):
    intentos = 0
    while intentos < 3:
        print("Intento: ", 3 - intentos)
        esValido = registro()
        if esValido:
            return esValido
        else:
            intentos += 1
def operacion():
    seleccion = list()
    cantidadOperaciones = ""
    print("Seleccione la operación que desea realizar: ")
    print("1. Deposito")
    print("2. Pago de recibo")
    print("3. Retiro")

    seleccion.append(input("Seleccione el nuemro de la operación: "))

    if seleccion[0] == "1":
        print("Deposito")
        cantidadOperaciones = float( input ("Ingrese la cantidad "))
        seleccion.append(cantidadOperaciones)

    elif seleccion[0] == "2":
        print("Pago de recibo")
        cantidadOperaciones = input("Ingrese el número de NIC ")
        seleccion.append(cantidadOperaciones) 
       

    elif seleccion[0] == "3":
        print("Retiro")
        cantidadOperaciones = float( input ("Ingrese la cantidad "))
        seleccion.append(cantidadOperaciones)
        
    else:
        print("Opción no válida")
    
    return seleccion
def retiro(operacion): 
    saldo = operacion()
    if(saldo[1] <=  usuario[2]):
        usuario[2] = usuario[2] - saldo[1]
        print("Retiro exitoso")
        print("Saldo actual: ", usuario[2])
        return True
    else:
        print("Cantidad  no admitida")
        return False
def deposito(operacion): 
    saldo = operacion()
    if(saldo[1] > 0):
        usuario[2] = usuario[2] + saldo[1]
        print("Deposito exitoso")
        print("Saldo actual: ", usuario[2])
    else:
        print("Cantidad no admitida")

def pagoRecibo(operacion):
    op = operacion()
    
    for i in range(len(reciboLista)):
        if(reciboLista[i][0] == op[1]):
           ingresarMonto = input(
               f"Pago de NIC : {reciboLista[i][0]} , ¿Desea realizar un pago {reciboLista[i][1]} ?  S/N")
           
           if(ingresarMonto.lower() =="s"):
                if(reciboLista[i][1] <= usuario[2]):
                 usuario[2] = usuario[2] - reciboLista[i][1]
                 print("Pago exitoso")
                 print("Saldo actual: ", usuario[2])   
        else:
            print("Pago no exitoso")
            print("Saldo actual: ", usuario[2])
            return False
             
             
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