# 1. Escritura de Archivo de Texto
# Abrimos el archivo en modo escritura ('w')
# Si el archivo no existe, se crea. Si existe, se sobrescribe.
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales usando el metodo write()
    file.write('Nota 1: Recordar cita médica\n')
    file.write('Nota 2: Repasar unidad 6 de Ingles\n')
    file.write('Nota 3: Recordar el lunch de 13:15 a 14:00\n')

print("Archivo creado y notas escritas con éxito.")

# 2. Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido del archivo línea por línea utilizando readline()
    linea = file.readline()
    while linea:
        # Mostramos cada línea leída en la consola
        # strip() elimina espacios en blanco y saltos de línea al inicio y al final
        print(linea.strip())
        linea = file.readline()

print("\nLectura del archivo completada.")

# 3. Cierre de Archivos
# Nota: No es necesario cerrar explícitamente el archivo cuando se usa 'with'
# Python se encarga automáticamente de cerrar el archivo al salir del bloque 'with'