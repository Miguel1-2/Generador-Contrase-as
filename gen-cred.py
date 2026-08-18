import secrets
import string
import os

banner =r"""
    __ ___ _  _      ___ ___ ___ ___  
  / __| __| \| |___ / __| _ \ __|   \ 
 | (_ | _|| .` |___| (__|   / _|| |) |
  \___|___|_|\_|    \___|_|_\___|___/ 
                                      """
def generador_user(nombre, apellido):
    nombre = nombre.strip().lower()
    apellido = apellido.strip().lower()

    apellido_cort = apellido[:3]
    numero_random = "".join(secrets.choice(string.digits) for _ in range (2))

    return nombre + apellido_cort + numero_random

def generador_password(longitud):
    caracteres = (string.ascii_letters + string.digits + string.punctuation)

    return "".join(secrets.choice(caracteres) for _ in range(longitud))


def crear_credencial():
    os.system("clear")
    print(banner)
    nombre = input("ingresa tu primer nombre: ")
    apellido = input("ingresa tu primer apellido: ")

    while True:
        try: 
            longitud = int(input("Longitud de contraseña(min:8 | max:20): "))
                
            if 8<= longitud <=20:
                break
            else:
                print("fuera de rango")
        except ValueError:
                print("Debes ingresar un numero.")

    usuario = generador_user(nombre, apellido)
    password = generador_password(longitud)
    print()
    print(f"tu nombre de User: {usuario.capitalize()}@corp.pe")
    print()
    print(f"tu contraseña es: {password}")

while True:
    try:
        crear_credencial()
        while True:
            continuar = input(
                "\nGenerar otra credencial [s/n]: ").lower()

            if continuar == "s":
                break
            
            elif continuar == "n":
                print("Saliendo...")
                exit()

            else:
                print("Opción inválida. Escribe solamente s o n.")

    except KeyboardInterrupt:
        print("\nPrograma cancelado.")
        break
