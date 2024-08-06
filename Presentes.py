import os
from datetime import datetime

def obtener_ubicacion_archivo(nombre_archivo):
    # Obtener la ubicación del archivo en la ruta actual
    ubicacion = os.path.abspath(nombre_archivo)
    return ubicacion

def calcular_horas_anuales(dias, turno):
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
    horas_anuales = horas_mensuales * 12 // 4  # Aproximadamente 12 meses en un año

    return horas_anuales

def buscar_y_sumar_horas(nombre, ubicacion):
    # Buscar el nombre en el archivo y sumar las horas correspondientes
    nombre = nombre.strip().lower()
    total_horas = 0
    
    with open(ubicacion, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split(";")
            nombre_archivo = partes[0].split(" ", 1)[1].strip().lower()
            if nombre == nombre_archivo:
                dias = partes[1]
                turno = partes[2]
                horas_anuales = calcular_horas_anuales(dias, turno)
                total_horas += horas_anuales
    return total_horas

def registrar_presentes(nombre):
    # Registrar los presentes en el archivo "Presentes"
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    nombre_archivo = "Presentes.txt"
    
    with open(nombre_archivo, "a") as archivo:
        archivo.write(f"\nFecha: {fecha_actual}\n")
        archivo.write(f"Nombre: {nombre}\n")

def main():
    ubicacion_archivo = obtener_ubicacion_archivo("ALTAS_pasantes_2024.txt")
    
    while True:
        nombre = input("Introduce el nombre y apellido del pasante (o 'salir' para terminar): ").strip()
        if nombre.lower() == "salir":
            break
        
        # Buscar y sumar horas
        total_horas = buscar_y_sumar_horas(nombre, ubicacion_archivo)
        if total_horas > 0:
            print(f"El total de horas anuales para {nombre} es: {total_horas} horas")
            registrar_presentes(nombre)
            print(f"{nombre} ha sido registrado en el archivo 'Presentes'")
        else:
            print(f"No se encontró a {nombre} en el archivo.")
            
if __name__ == "__main__":
    main()
