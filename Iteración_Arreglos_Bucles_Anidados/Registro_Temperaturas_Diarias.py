# Crear una matriz 3D para almacenar los datos de temperaturas diarias
temperaturas = [
    # Quito
    [
        # Lunes
        [22, 20, 15,23],  # Semana 1, 2, 3, 4
        # Martes
        [23, 21, 19,20],
        # Miércoles
        [24, 22, 20,13],
        # Jueves
        [25, 23, 21,18],
        # Viernes
        [26, 24, 22,28],
        # Sábado
        [27, 25, 23,17],
        # Domingo
        [28, 26, 24,20]
    ],
    # Guayaquil
    [
        # Lunes
        [33, 22, 20, 35],
        # Martes
        [26, 23, 21, 29],
        # Miércoles
        [27, 24, 22, 31],
        # Jueves
        [28, 25, 23, 20],
        # Viernes
        [29, 26, 24, 33],
        # Sábado
        [30, 27, 25, 31],
        # Domingo
        [31, 28, 26, 24]
    ],
    # Cuenca
    [
        # Lunes
        [15, 12, 10, 8],
        # Martes
        [16, 13, 11, 20],
        # Miércoles
        [17, 14, 12, 19],
        # Jueves
        [18, 15, 13, 12],
        # Viernes
        [19, 16, 14, 22],
        # Sábado
        [20, 17, 15, 26],
        # Domingo
        [21, 18, 16, 12]
    ]
]

# Definición de la función calcular_temperatura_promedio
def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad durante cada semana.

    Parámetros:
    temperaturas (list): Matriz 3D que contiene las temperaturas diarias de cada ciudad.

    Retorna:
    dict: Diccionario que contiene la temperatura promedio de cada ciudad durante cada semana.
    """
    temperatura_promedio = {}
    ciudades = ["Quito", "Guayaquil", "Cuenca"]
    for ciudad in range(len(temperaturas)):
        ciudad_nombre = ciudades[ciudad]
        temperatura_promedio_ciudad = {}
        for semana in range(len(temperaturas[ciudad][0])):
            suma_temperaturas = 0
            for dia in range(len(temperaturas[ciudad])):
                suma_temperaturas += temperaturas[ciudad][dia][semana]
            promedio_temperatura = suma_temperaturas / len(temperaturas[ciudad])
            temperatura_promedio_ciudad[f"Semana {semana+1}"] = promedio_temperatura
        temperatura_promedio[ciudad_nombre] = temperatura_promedio_ciudad
    return temperatura_promedio

# Llamada a la función calcular_temperatura_promedio
temperatura_promedio = calcular_temperatura_promedio(temperaturas)

# Imprimir el resultado
for ciudad, semanas in temperatura_promedio.items():
    print(f"Temperatura promedio en {ciudad}:")
    for semana, temperatura in semanas.items():
        print(f"  {semana}: {temperatura:.2f}°C")