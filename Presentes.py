import os
from datetime import datetime

def obtener_ubicacion_archivo(nombre_archivo):
    # Obtener la ubicación del archivo en la ruta actual
    ubicacion = os.path.abspath(nombre_archivo)
    return ubicacion

def calcular_horas_por_dia(turno):
    # Determinar las horas diarias según el turno
    if turno.lower() == "mañana":
        return 4
    elif turno.lower() == "tarde":
        return 3
    else:
        print("Turno no válido. Debe ser 'mañana' o 'tarde'.")
        return None

def buscar_horas(nombre, ubicacion):
    # Buscar el nombre en el archivo y obtener las horas diarias correspondientes
    nombre = nombre.strip().lower()
    
    with open(ubicacion, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split(";")
            nombre_archivo = partes[0].split(" ", 1)[1].strip().lower()
            if nombre == nombre_archivo:
                dias = partes[1]
                turno = partes[2]
                horas_por_dia = calcular_horas_por_dia(turno)
                if horas_por_dia is not None:
                    return int(dias) * horas_por_dia
    
    return None

def actualizar_horas_cumplidas(nombre, ubicacion):
    horas_por_dia = buscar_horas(nombre, ubicacion)
    if horas_por_dia is None:
        return None
    
    horas_totales = 216
    archivo_presentes = "Presentes.txt"
    
    if not os.path.exists(archivo_presentes):
        with open(archivo_presentes, "w") as archivo:
            archivo.write("")

    # Leer el archivo de presentes y calcular el total actual de horas cumplidas
    total_horas_cumplidas = 0
    with open(archivo_presentes, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if "Horas cumplidas:" in linea:
                partes = linea.strip().split(":")
                total_horas_cumplidas = int(partes[1].split("/")[0].strip())
                break
    
    # Agregar las horas del nuevo ingreso
    total_horas_cumplidas += horas_por_dia
    
    # Actualizar el archivo con las nuevas horas
    with open(archivo_presentes, "a") as archivo:
        fecha_actual = datetime.now().strftime("%d-%m")
        hora_actual = datetime.now().strftime("%H:%M")
        archivo.write(f"{fecha_actual} / {nombre} / {hora_actual}\n")
        archivo.write(f"Horas cumplidas: {total_horas_cumplidas}/216\n")
    
    return total_horas_cumplidas

def actualizar_encabezado():
    # Actualizar el encabezado del archivo "Presentes.txt" según la fecha actual
    fecha_actual = datetime.now().strftime("%d-%m")
    hora_actual = datetime.now().strftime("%H:%M")
    
    # Determinar el turno según la hora actual
    if "07:30" <= hora_actual < "12:30":
        turno = "TM"
    elif "12:30" <= hora_actual <= "23:59":
        turno = "TT"
    else:
        turno = "FT"  # Fuera de horario

    encabezado = f"------ Presentes {fecha_actual} {turno} ------\n"

    # Verificar si el archivo existe y necesita actualización
    if not os.path.exists("Presentes.txt"):
        with open("Presentes.txt", "w") as archivo:
            archivo.write(encabezado)
    else:
        with open("Presentes.txt", "r") as archivo:
            lineas = archivo.readlines()
        
        # Verificar si el encabezado ya está presente y actualizarlo
        if lineas and lineas[0] != encabezado:
            with open("Presentes.txt", "w") as archivo:
                archivo.write(encabezado)
                archivo.writelines(lineas[1:])

def main():
    ubicacion_archivo = obtener_ubicacion_archivo("ALTAS_pasantes_2024.txt")
    
    while True:
        nombre = input("Introduce el nombre y apellido del pasante (o 'salir' para terminar): ").strip()
        if nombre.lower() == "salir":
            break
        
        # Actualizar el encabezado del archivo
        actualizar_encabezado()
        
        # Actualizar y mostrar las horas cumplidas
        horas_cumplidas = actualizar_horas_cumplidas(nombre, ubicacion_archivo)
        if horas_cumplidas is not None:
            horas_totales = 216
            horas_restantes = horas_totales - horas_cumplidas
            print(f"El total de horas cumplidas para {nombre} es: {horas_cumplidas} horas")
            print(f"Horarios restantes para completar las 216 horas: {horas_restantes} horas")
        else:
            print(f"No se encontró a {nombre} en el archivo o turno no válido.")

if __name__ == "__main__":
    main()
