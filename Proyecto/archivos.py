import os
from datetime import date

# Obtener la fecha del día actual
fecha_hoy = str(date.today()) 

#=======================================
# Manejo de archivos
#=======================================

def cargar_datos():
    lista = []
    if os.path.exists("catalogo.txt"):
        archivo = open("catalogo.txt", "r")
        for linea in archivo:
            lista.append(linea.strip())
        archivo.close()
    return lista

def guardar_datos(lista):
    archivo = open("catalogo.txt", "w")
    for item in lista:
        archivo.write(item + "\n")
    archivo.close()

# --- FUNCIONES PARA EL REGISTRO DE CAMBIOS (LOGS) ---
def cargar_logs():
    registros = []
    try:
        with open("logs.txt", "r") as archivo:
            for linea in archivo:
                registros.append(linea.strip())
    except FileNotFoundError:
        # Si el archivo no existe todavía, no se cae el programa;
        # Si no encuentra el archivo crea uno nuevo
        print("Aviso: No se encontró archivo previo. Se creará uno nuevo.")
   
    return registros

def guardar_logs(registro):
    archivo = open("registro.txt", "w")
    for item in registro:
        archivo.write(item + "\n")
    archivo.close()