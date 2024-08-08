import os
from datetime import datetime

def obtener_ubicacion_archivo(nombre_archivo):
    return os.path.abspath(nombre_archivo)

def calcular_horas_por_dia(turno):
    if turno.lower() == "mañana":
        return 4
    elif turno.lower() == "tarde":
        return 3
    else:
        print("Turno no válido. Debe ser 'mañana' o 'tarde'.")
        return None

def buscar_datos(nombre, ubicacion):
    nombre = nombre.strip().lower()
    with open(ubicacion, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split(";")
            nombre_archivo = partes[0].strip().lower()
            if nombre == nombre_archivo:
                dias = partes[1]
                turno = partes[2]
                return dias, turno
    return None, None

def agregar_nuevo_ingreso(nombre, ubicacion):
    print("Este nombre no está en el archivo.")
    dias = input("Indique los días según números (por ejemplo, Martes y Jueves = 2,4): ").strip()
    turno = input("Indique el turno (mañana o tarde): ").strip()
    
    horas_por_dia = calcular_horas_por_dia(turno)
    if horas_por_dia is None:
        return None
    
    with open(ubicacion, "a") as archivo:
        archivo.write(f"{nombre} ; {dias} ; {turno}\n")
    
    # Actualizar archivo de nombres ingresados
    with open("Nombres_ingresados.txt", "a") as archivo:
        archivo.write(f"{nombre}\n")
    
    return horas_por_dia

def actualizar_horas_cumplidas(nombre, ubicacion):
    dias, turno = buscar_datos(nombre, ubicacion)
    if dias is None or turno is None:
        return None, None
    
    horas_por_dia = calcular_horas_por_dia(turno)
    if horas_por_dia is None:
        return None, None
    
    horas_totales = 216
    archivo_presentes = "Presentes.txt"
    
    if not os.path.exists(archivo_presentes):
        with open(archivo_presentes, "w") as archivo:
            archivo.write("")
    
    total_horas_cumplidas = 0
    with open(archivo_presentes, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if "Horas cumplidas:" in linea:
                partes = linea.strip().split(":")
                total_horas_cumplidas = int(partes[1].split("/")[0].strip())
                break
    
    horas_cumplidas = horas_por_dia
    total_horas_cumplidas += horas_cumplidas
    
    with open(archivo_presentes, "a") as archivo:
        fecha_actual = datetime.now().strftime("%d-%m")
        hora_actual = datetime.now().strftime("%H:%M")
        archivo.write(f"{fecha_actual} / {nombre} / {hora_actual}\n")
        archivo.write(f"Horas cumplidas: {total_horas_cumplidas}/216\n")
    
    return horas_cumplidas, total_horas_cumplidas

def actualizar_encabezado():
    fecha_actual = datetime.now().strftime("%d-%m")
    hora_actual = datetime.now().strftime("%H:%M")
    
    if "07:30" <= hora_actual < "12:30":
        turno = "TM"
    elif "12:30" <= hora_actual <= "23:59":
        turno = "TT"
    else:
        turno = "FT"  # Fuera de horario

    encabezado = f"------ Presentes {fecha_actual} {turno} ------\n"

    if not os.path.exists("Presentes.txt"):
        with open("Presentes.txt", "w") as archivo:
            archivo.write(encabezado)
    else:
        with open("Presentes.txt", "r") as archivo:
            lineas = archivo.readlines()
        
        if lineas and lineas[0] != encabezado:
            with open("Presentes.txt", "w") as archivo:
                archivo.write(encabezado)
                archivo.writelines(lineas[1:])

def nombre_existe(nombre):
    nombre = nombre.strip().lower()
    if not os.path.exists("Nombres_ingresados.txt"):
        return False
    
    with open("Nombres_ingresados.txt", "r") as archivo:
        nombres = archivo.read().splitlines()
    
    return nombre in nombres

def main():
    ubicacion_archivo = obtener_ubicacion_archivo("ALTAS_pasantes_2024.txt")
    
    while True:
        nombre = input("Introduce el nombre y apellido del pasante (o 'salir' para terminar): ").strip().lower()
        if nombre == "salir":
            break
        
        actualizar_encabezado()
        
        if not nombre_existe(nombre):
            horas_cumplidas = agregar_nuevo_ingreso(nombre, ubicacion_archivo)
            if horas_cumplidas is not None:
                print(f"Horas cumplidas en este ingreso: {horas_cumplidas}")
                print(f"Horas restantes: {216 - horas_cumplidas}")
        else:
            horas_cumplidas, total_horas_cumplidas = actualizar_horas_cumplidas(nombre, ubicacion_archivo)
            if horas_cumplidas is not None:
                horas_totales = 216
                horas_restantes = horas_totales - total_horas_cumplidas
                print(f"El total de horas cumplidas para {nombre} es: {total_horas_cumplidas} horas")
                print(f"Horas restantes para completar las 216 horas: {horas_restantes} horas")
            else:
                print(f"No se encontró a {nombre} en el archivo o turno no válido.")

if __name__ == "__main__":
    main()
