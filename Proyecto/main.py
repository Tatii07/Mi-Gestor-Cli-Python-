import os
from archivos import cargar_datos, cargar_logs
from submenu import catalogo
from logs import log  # Importas la función logs desde logs.py

#===================================
# Inicio del Sistema
#===================================

lista = cargar_datos()
registro = cargar_logs()
ejecutando_principal = True

while ejecutando_principal:
    os.system("clear")
    print("=== SISTEMA GLOBAL V0.2 ===")
    print("1. Gestionar Entretenimiento")
    print("2. Registro de cambios")
    print("3. Salir del Sistema")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        catalogo(lista)

    elif opcion == "2":
        log(registro)
        
    elif opcion == "3":
         ejecutando_principal = False