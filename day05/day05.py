# Día 05 - Listas

# Crear listas
numeros = [1, 2, 3, 4, 5]
nombres = ["Ana", "Luis", "Felipe"]

print(numeros)
print(nombres)

# Acceder a elementos (índices empiezan en 0)
print(numeros[0])
print(nombres[2])

# Último elemento
print(numeros[-1])

# Modificar elementos
numeros[0] = 10
print(numeros)

# Agregar elementos
numeros.append(6) #apend es agregar
print(numeros)

# Eliminar elementos
numeros.remove(3) #remove es remover
print(numeros)

# Longitud de la lista
print("Cantidad de elementos:", len(numeros)) #len es el tamaño

frutas = ["pera", "platano", "frutilla"]

frutas.append("manzana")
frutas.append("banana")
frutas.append("naranja")

print(frutas)

frutas.remove("banana")
print(frutas)

print("¿manzana está en la lista?", "manzana" in frutas)

