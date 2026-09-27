import os
from archivos import cargar_datos, cargar_logs
from submenu import catalogo
from logs import log

def pedir_numero():
    try:
        opcion = int(input("Selecciona un número: "))
        return opcion
    except ValueError:
        print("❌ Error: Debes ingresar un número entero, no texto.")
        input("\nPresiona Enter para continuar...") 
        return None

# Inicio del Sistema
lista = cargar_datos()
registro = cargar_logs()
ejecutando_principal = True

while ejecutando_principal:
    os.system("clear")
    print("=== SISTEMA GLOBAL V0.2 ===")
    print("1. Gestionar Entretenimiento")
    print("2. Registro de cambios")
    print("3. Salir del Sistema")
    
    opcion = pedir_numero()

    if opcion == 1:
        catalogo(lista)
    elif opcion == 2:
        log(registro)
    elif opcion == 3:
        ejecutando_principal = False
