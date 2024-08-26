# Crear una matriz bidimensional (3x3)
matriz = [
    [83, 92, 78],
    [64, 50, 44],
    [39, 21, 12]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz_local, fila_numero):
    fila_a_ordenar = matriz_local[fila_numero]
    for i in range(len(fila_a_ordenar)):
        for j in range(len(fila_a_ordenar) - 1):
            if fila_a_ordenar[j] > fila_a_ordenar[j + 1]:
                fila_a_ordenar[j], fila_a_ordenar[j + 1] = fila_a_ordenar[j + 1], fila_a_ordenar[j]
    matriz_local[fila_numero] = fila_a_ordenar

# Ordenar la fila 1 (índice 1)
ordenar_fila(matriz, 1)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila 1 ordenada:")
for fila in matriz:
    print(fila)
