def crear_archivo():
    # Crear el archivo "pasantes_2024.txt" si no existe
    with open("pasantes_2024.txt", "a") as archivo:
        pass

def agregar_pasante(nombre, dias, eliminar=False):
    # Leer el archivo y verificar si el nombre ya está
    with open("pasantes_2024.txt", "r") as archivo:
        pasantes = archivo.readlines()

    # Convertir todos los nombres a minúsculas para la comparación
    nombres_existentes = [pasante.strip().lower().split(";")[0] for pasante in pasantes]

    # Convertir el nombre ingresado a minúsculas para la comparación
    nombre = nombre.strip().lower()

    if eliminar:
        if nombre in nombres_existentes:
            # Filtrar los nombres y eliminar el que coincide
            with open("pasantes_2024.txt", "w") as archivo:
                for pasante in pasantes:
                    if pasante.strip().lower().split(";")[0] != nombre:
                        archivo.write(pasante)
            print("Nombre eliminado")
        else:
            print("El nombre no se encuentra en la lista")
    else:
        if nombre in nombres_existentes:
            print("El nombre ya está")
        else:
            # Agregar el nombre con los días al archivo
            with open("pasantes_2024.txt", "a") as archivo:
                archivo.write(f"{nombre};{dias}\n")
            print("Nombre agregado")

crear_archivo()

while True:
    opcion = input("Elige una opción: \n1. Agregar nombre \n2. Eliminar nombre \n3. Salir\n").strip()
    
    if opcion == "3":
        break
    
    if opcion in ["1", "2"]:
        nombre = input("Introduce el nombre y apellido del pasante: ").strip()
        if opcion == "1":
            dias = input("Introduce los días que tiene que venir (ejemplo: 1,2,3 para Lunes, Martes, Miércoles): ").strip()
            agregar_pasante(nombre, dias)
        elif opcion == "2":
            agregar_pasante(nombre, "", eliminar=True)
    else:
        print("Opción no válida. Inténtalo de nuevo.")