# Creamos el Diccionario
informacion_personal = {"nombre": "Selena", "edad": 26, "ciudad": "Quito", "profesion": "Ingeniero"}

# Acceder y Modificar Valores
# Accede al valor asociado con la clave "ciudad" y lo modifica con una ciudad diferente
informacion_personal["ciudad"] = "Cuenca"

# Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona
# En este caso, la clave "profesion" ya existe, así que la modificamos
informacion_personal["profesion"] = "Psicóloga"

# Verificar Existencia de Claves
# Verifica si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregamos un número de teléfono ficticio
    informacion_personal["telefono"] = "023038759"

# Eliminar una Clave
# Elimina la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el Diccionario Final
print("Información Personal:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")