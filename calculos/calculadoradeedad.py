#Calculadora de edad

from datetime import datetime

def calcular_edad(fecha_nacimiento):
    hoy = datetime.today()
    edad = hoy.year - fecha_nacimiento.year
    
    # Verificar si ya pasó el cumpleaños este año
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    
    return edad

# Solicitar fecha al usuario
while True:
    try:
        entrada = input("Ingresa tu fecha de nacimiento (AAAA-MM-DD): ")
        fecha_nac = datetime.strptime(entrada, "%Y-%m-%d")
        break
    except ValueError:
        print("Formato incorrecto. Usa AAAA-MM-DD")

edad_actual = calcular_edad(fecha_nac)
print(f"Tu edad es: {edad_actual} años")