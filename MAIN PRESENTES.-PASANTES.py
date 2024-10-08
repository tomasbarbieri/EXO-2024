import os

def obtener_ubicacion_archivo():
    # Crear el archivo "ALTAS_pasantes_2024.txt" en la ubicación actual si no existe
    nombre_archivo = "ALTAS_pasantes_2024.txt"
    ubicacion = os.path.abspath(nombre_archivo)
    
    if not os.path.exists(ubicacion):
        with open(ubicacion, "w") as archivo:
            pass
    
    print(f"El archivo se ha creado en: {ubicacion}")
    return ubicacion

def crear_archivo(ubicacion):
    # Crear el archivo "ALTAS_pasantes_2024.txt" si no existe en la ubicación especificada
    with open(ubicacion, "a") as archivo:
        pass
    
    # Crear el archivo "ultimo_numero.txt" si no existe y establecer su valor inicial a 0
    try:
        with open("ultimo_numero.txt", "r") as archivo:
            pass
    except FileNotFoundError:
        with open("ultimo_numero.txt", "w") as archivo:
            archivo.write("0")

def obtener_ultimo_numero():
    # Leer el último número asignado del archivo "ultimo_numero.txt"
    with open("ultimo_numero.txt", "r") as archivo:
        ultimo_numero = int(archivo.read().strip())
    return ultimo_numero

def actualizar_ultimo_numero(nuevo_numero):
    # Actualizar el archivo "ultimo_numero.txt" con el nuevo número
    with open("ultimo_numero.txt", "w") as archivo:
        archivo.write(str(nuevo_numero))

def calcular_horas(dias, turno):
    # Determinar las horas según el turno
    if turno.lower() == "mañana":
        horas_por_dia = 4
    elif turno.lower() == "tarde":
        horas_por_dia = 3
    else:
        print("Turno no válido. Debe ser 'mañana' o 'tarde'.")
        return 0

    dias_lista = dias.split(',')
    cantidad_dias = len(dias_lista)
    horas_semanales = cantidad_dias * horas_por_dia
    horas_mensuales = horas_semanales * 4
    horas_anuales = 216  # Horas anuales fijas

    return horas_anuales

def agregar_pasante(ubicacion, nombre, dias, turno, eliminar=False):
    # Leer el archivo y verificar si el nombre ya está
    with open(ubicacion, "r") as archivo:
        pasantes = archivo.readlines()

    # Convertir todos los nombres a minúsculas para la comparación
    nombres_existentes = [pasante.strip().lower().split(";")[0].split(" ", 1)[1] for pasante in pasantes]
    
    # Convertir el nombre ingresado a minúsculas para la comparación
    nombre = nombre.strip().lower()

    if eliminar:
        if nombre in nombres_existentes:
            # Filtrar los nombres y eliminar el que coincide
            with open(ubicacion, "w") as archivo:
                for pasante in pasantes:
                    if pasante.strip().lower().split(";")[0].split(" ", 1)[1] != nombre:
                        archivo.write(pasante)
            print("Nombre eliminado")
        else:
            print("El nombre no se encuentra en la lista")
    else:
        if nombre in nombres_existentes:
            print("El nombre ya está")
        else:
            # Obtener el último número asignado y actualizarlo
            ultimo_numero = obtener_ultimo_numero()
            nuevo_numero = ultimo_numero + 1
            actualizar_ultimo_numero(nuevo_numero)

            # Calcular horas anuales
            horas_anuales = calcular_horas(dias, turno)

            # Agregar el nombre con los días, turno, horas y el número asignado al archivo
            with open(ubicacion, "a") as archivo:
                archivo.write(f"{nuevo_numero} {nombre};{dias};{turno};{horas_anuales} horas anuales\n")
            print("Nombre agregado")

ubicacion_archivo = obtener_ubicacion_archivo()
crear_archivo(ubicacion_archivo)

while True:
    opcion = input("Elige una opción: \n1. Agregar nombre \n2. Eliminar nombre \n3. Salir\n").strip()
    
    if opcion == "3":
        break
    
    if opcion in ["1", "2"]:
        nombre = input("Introduce el nombre y apellido del pasante: ").strip()
        if opcion == "1":
            dias = input("Introduce los días que tiene que venir (ejemplo: 1,2,3 para Lunes, Martes, Miércoles): ").strip()
            turno = input("Introduce el turno (mañana o tarde): ").strip().lower()
            agregar_pasante(ubicacion_archivo, nombre, dias, turno)
        elif opcion == "2":
            agregar_pasante(ubicacion_archivo, nombre, "", "", eliminar=True)
    else:
        print("Opción no válida. Inténtalo de nuevo.")