# Día 04 - Condicionales

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# Ejemplo con elif
nota = int(input("Ingresa tu nota (1 a 7): "))

if nota >= 6:
    print("Excelente")
elif nota >= 4:
    print("Aprobado")
else:
    print("Reprobado")


# Condiciones con booleanos
tiene_permiso = True

if edad >= 18 and tiene_permiso:
    print("Puede conducir")
else:
    print("No puede conducir")
