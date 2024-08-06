import os
from datetime import datetime

def obtener_ubicacion_archivo(nombre_archivo):
    # Obtener la ubicación del archivo en la ruta actual
    ubicacion = os.path.abspath(nombre_archivo)
    return ubicacion

def calcular_horas_cumplidas(dias, turno):
    # Determinar las horas diarias según el turno
    if turno.lower() == "mañana":
        horas_por_dia = 4
    elif turno.lower() == "tarde":
        horas_por_dia = 3
    else:
        print("Turno no válido. Debe ser 'mañana' o 'tarde'.")
        return 0

    dias_lista = dias.split(',')
    cantidad_dias = len(dias_lista)
    horas_cumplidas = cantidad_dias * horas_por_dia

    return horas_cumplidas

def buscar_y_sumar_horas(nombre, ubicacion):
    # Buscar el nombre en el archivo y sumar las horas correspondientes
    nombre = nombre.strip().lower()
    total_horas_cumplidas = 0
    
    with open(ubicacion, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split(";")
            nombre_archivo = partes[0].split(" ", 1)[1].strip().lower()
            if nombre == nombre_archivo:
                dias = partes[1]
                turno = partes[2]
                horas_cumplidas = calcular_horas_cumplidas(dias, turno)
                total_horas_cumplidas += horas_cumplidas

    horas_totales = 216
    horas_restantes = horas_totales - total_horas_cumplidas
    return total_horas_cumplidas, horas_restantes

def registrar_presentes(nombre, horas_cumplidas):
    # Registrar los presentes en el archivo "Presentes"
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    nombre_archivo = "Presentes.txt"
    
    with open(nombre_archivo, "a") as archivo:
        archivo.write(f"\nFecha: {fecha_actual}\n")
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Horas cumplidas: {horas_cumplidas}/216\n")

def main():
    ubicacion_archivo = obtener_ubicacion_archivo("ALTAS_pasantes_2024.txt")
    
    while True:
        nombre = input("Introduce el nombre y apellido del pasante (o 'salir' para terminar): ").strip()
        if nombre.lower() == "salir":
            break
        
        # Buscar y sumar horas
        horas_cumplidas, horas_restantes = buscar_y_sumar_horas(nombre, ubicacion_archivo)
        if horas_cumplidas > 0:
            print(f"El total de horas cumplidas para {nombre} es: {horas_cumplidas} horas")
            print(f"Horarios restantes para completar las 216 horas: {horas_restantes} horas")
            registrar_presentes(nombre, horas_cumplidas)
            print(f"{nombre} ha sido registrado en el archivo 'Presentes'")
        else:
            print(f"No se encontró a {nombre} en el archivo.")
            
if __name__ == "__main__":
    main()
