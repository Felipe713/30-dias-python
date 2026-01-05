# Día 02 - Variables y tipos de datos

nombre = "Felipe"
edad = 30
altura = 1.75
es_estudiante = True

print("Nombre: ", nombre)
print("Edad: ", edad)
print("Altura: ", altura)
print("¿Es estudiante?: ", es_estudiante)

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(es_estudiante))

# Entrada de datos desde teclado
nombre_usuario = input("Ingresa tu nombre: ") #input es para ingresar datos en la consola
edad_usuario = input("Ingresa tu edad: ")

print(nombre_usuario, type(nombre_usuario))
print(edad_usuario, type(edad_usuario))

edad_usuario = int(edad_usuario)
print(edad_usuario, type(edad_usuario))


