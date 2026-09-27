import os
from datetime import date

# Obtiene la fecha del día actual
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
    registro = [] 
    if os.path.exists("registro.txt"):
        archivo = open("registro.txt", "r")
        for linea in archivo:
            registro.append(linea.strip())
        archivo.close()
    return registro

def guardar_logs(registro):
    archivo = open("registro.txt", "w")
    for item in registro:
        archivo.write(item + "\n")
    archivo.close()