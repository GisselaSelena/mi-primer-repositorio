# Crear una matriz 3D para almacenar los datos de temperaturas diarias
temperaturas = [
    # Quito
    [
        # Lunes
        [22, 20, 15],  # Semana 1, 2, 3
        # Martes
        [23, 21, 19],
        # Miércoles
        [24, 22, 20],
        # Jueves
        [25, 23, 21],
        # Viernes
        [26, 24, 22],
        # Sábado
        [27, 25, 23],
        # Domingo
        [28, 26, 24]
    ],
    # Guayaquil
    [
        # Lunes
        [33, 22, 20],
        # Martes
        [26, 23, 21],
        # Miércoles
        [27, 24, 22],
        # Jueves
        [28, 25, 23],
        # Viernes
        [29, 26, 24],
        # Sábado
        [30, 27, 25],
        # Domingo
        [31, 28, 26]
    ],
    # Cuenca
    [
        # Lunes
        [15, 12, 10],
        # Martes
        [16, 13, 11],
        # Miércoles
        [17, 14, 12],
        # Jueves
        [18, 15, 13],
        # Viernes
        [19, 16, 14],
        # Sábado
        [20, 17, 15],
        # Domingo
        [21, 18, 16]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in range(len(temperaturas)):
    ciudad_nombre = ["Quito", "Guayaquil", "Cuenca"][ciudad]
    for semana in range(len(temperaturas[ciudad][0])):
        suma_temperaturas = 0
        for dia in range(len(temperaturas[ciudad])):
            suma_temperaturas += temperaturas[ciudad][dia][semana]
        promedio_temperatura = suma_temperaturas / len(temperaturas[ciudad])
        print(f"Promedio de temperatura en {ciudad_nombre} en la semana {semana+1}: {promedio_temperatura:.2f}°C")