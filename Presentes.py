import os
import json

while True:
    with open("usuarios.txt", "r") as archivo_usuarios:
        listaUsuarios = archivo_usuarios.readlines()
        print(listaUsuarios)
    if listaUsuarios:
        ultimoUsuario = listaUsuarios[-1].rstrip().replace("'",'"')
        diccionarioUltimoUsuario=json.loads(ultimoUsuario)
        ultimoNumeroIdentificacion = diccionarioUltimoUsuario.get("numeroIdentificacion")
    else:
        ultimoNumeroIdentificacion = 0

    opcion = input("Elige una opción: \n1. Agregar nombre \n2. Eliminar nombre \n3. Salir\n").strip()
    
    
    if opcion =="1":
        nombre = input("Ingrese nombres: ")
        apellido = input("Ingrese apellido: ")
        dni = input("Ingrese dni: ")
        cuil = input ("Ingrese Cuil: ")
        fechaNacimiento= input("Ingrese nacimiento: ")
        cargo = input("Ingrese cargo: ")
        dias = input("Introduce los días que tiene que venir (ejemplo: 1,2,3 para Lunes, Martes, Miércoles): ").strip()
        turno = input("Introduce el turno (mañana o tarde): ").strip().lower()
        nuevoUsuario={
            "numeroIdentificacion": ultimoNumeroIdentificacion + 1,
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "cuil": cuil,
            "fechaNacimiento": fechaNacimiento,
            "cargo":cargo,
            "turno":turno,
        }
        existe = False
        for persona in listaUsuarios:
            if dni in pe ona:
                print(f"La persona {nombre} {apellido} ya ha sido ingresada")
                existe = True
        
        if existe == False:
            with open ("usuarios.txt","a") as archivoUsuarios:
                archivoUsuarios.write(str(nuevoUsuario)+ "\n") 
        

        

    
