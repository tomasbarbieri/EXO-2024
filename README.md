## Informe - Código de Gestión de Nombres de Pasantes

### **Resumen**

El código proporcionado es un script en Python diseñado para gestionar una lista de nombres de pasantes. Permite agregar y eliminar nombres en un archivo de texto llamado `pasantes_2024.txt`. La funcionalidad del código asegura que los nombres sean manejados de manera insensible a las diferencias entre mayúsculas y minúsculas, evitando duplicados y permitiendo la eliminación de entradas existentes.

### **Descripción del Código**

#### **1. Función `crear_archivo()`**

La función `crear_archivo` tiene el propósito de crear el archivo `pasantes_2024.txt` si aún no existe. La operación se realiza en modo de adición (`"a"`), lo que garantiza que el archivo se cree sin modificar su contenido si ya existe.

```python
def crear_archivo():
    with open("pasantes_2024.txt", "a") as archivo:
        pass
```

#### **2. Función `agregar_pasante(nombre, eliminar=False)`**

La función `agregar_pasante` maneja tanto la adición como la eliminación de nombres, dependiendo del valor del parámetro `eliminar`.

- **Agregar Nombre:** Si `eliminar` es `False` (o no se especifica), la función verifica si el nombre ya está en el archivo. Si no está, lo agrega al archivo en minúsculas para asegurar que las comparaciones sean insensibles a mayúsculas y minúsculas.
  
- **Eliminar Nombre:** Si `eliminar` es `True`, la función busca el nombre en el archivo y lo elimina si se encuentra. El archivo se reescribe excluyendo el nombre especificado.

```python
def agregar_pasante(nombre, eliminar=False):
    with open("pasantes_2024.txt", "r") as archivo:
        pasantes = archivo.readlines()
    nombres_existentes = [pasante.strip().lower() for pasante in pasantes]
    nombre = nombre.strip().lower()

    if eliminar:
        if nombre in nombres_existentes:
            with open("pasantes_2024.txt", "w") as archivo:
                for pasante in pasantes:
                    if pasante.strip().lower() != nombre:
                        archivo.write(pasante)
            print("Nombre eliminado")
        else:
            print("El nombre no se encuentra en la lista")
    else:
        if nombre in nombres_existentes:
            print("El nombre ya está")
        else:
            with open("pasantes_2024.txt", "a") as archivo:
                archivo.write(nombre + "\n")
            print("Nombre agregado")
```

#### **3. Menú de Opciones**

El menú interactivo permite al usuario seleccionar una de las siguientes opciones:
- **Agregar Nombre:** Solicita el nombre del pasante y lo añade al archivo si no está presente.
- **Eliminar Nombre:** Solicita el nombre del pasante y lo elimina del archivo si está presente.
- **Salir:** Termina el programa.

El menú utiliza un bucle `while` para seguir solicitando entradas hasta que el usuario elija salir.

```python
crear_archivo()

while True:
    opcion = input("Elige una opción: \n1. Agregar nombre \n2. Eliminar nombre \n3. Salir\n").strip()
    
    if opcion == "3":
        break
    
    if opcion in ["1", "2"]:
        nombre = input("Introduce el nombre y apellido del pasante: ").strip()
        if opcion == "1":
            agregar_pasante(nombre)
        elif opcion == "2":
            agregar_pasante(nombre, eliminar=True)
    else:
        print("Opción no válida. Inténtalo de nuevo.")
```

### **Consideraciones Adicionales**

- **Insensibilidad a Mayúsculas y Minúsculas:** Todos los nombres se manejan en minúsculas para evitar problemas de duplicación debido a variaciones en el uso de mayúsculas y minúsculas.
- **Integridad del Archivo:** La eliminación de nombres se maneja mediante la reescritura completa del archivo, lo que garantiza que solo los nombres no deseados se eliminen.

### **Conclusión**

El código proporciona una solución eficaz para gestionar una lista de nombres de pasantes, permitiendo tanto la adición como la eliminación de entradas de forma insensible a mayúsculas y minúsculas. La estructura modular y el menú interactivo facilitan la interacción del usuario y aseguran una correcta administración del archivo `pasantes_2024.txt`.

---
