# Crear una matriz bidimensional (3x3)
matriz = [
    [83, 92, 78],
    [64, 50, 44],
    [39, 21, 12]
]

# Búsqueda de un valor específico en la matriz
valor_buscado = 50

# Inicializar variables para rastrear la posición del valor
fila_encontrada = -1
columna_encontrada = -1

# Recorrer la matriz para buscar el valor
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break  # Detener la búsqueda una vez que se encuentra el valor
    if fila_encontrada != -1:
        break  # Salir del bucle exterior si se encuentra el valor

# Verificar si se encontró el valor y mostrar la posición
if fila_encontrada != -1:
    print(f"Valor {valor_buscado} encontrado en la posición ({fila_encontrada}, {columna_encontrada})")
else:
    print(f"Valor {valor_buscado} no se encontró en la matriz")
