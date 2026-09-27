import os
from archivos import guardar_logs
from archivos import cargar_logs

def log(registro):
    en_log = True
    while en_log:
        os.system("clear")
        print("=== REGISTRO DE CAMBIOS ===")
        print("1. Ver Registro")
        print("2. Agregar registro")
        print("3. Buscar Registro")
        print("4. Borrar registro")
        print("5. Editar registro")
        print("6. Volver al menú principal")
            
        opcion_log = input("\nSelecciona una opción: ")
      
        if opcion_log == "1":
            print("\n--- ELEMENTOS REGISTRADOS (" + str(len(registro)) + ") ---")
            for item in registro:
                print("- " + item)
            input("\nPresiona Enter para volver al menú...")          
                
        elif opcion_log == "2":
            nuevo = input("Agrega informacion: ")
            registro.append(nuevo)
            guardar_logs(registro)
            input("\n'" + nuevo + "' guardado con éxito. Presiona Enter para continuar...")
                
        elif opcion_log == "3":
            fecha_buscar = input("\nIngresa la fecha a buscar (AAAA-MM-DD): ")
            encontrados = False
            
            print("\n--- REGISTROS DEL DÍA " + fecha_buscar + " ---")
            for item in registro:
                if fecha_buscar in item:  # Revisa si la fecha está escrita en esa línea
                    print("- " + item)
                    encontrados = True
                    
            if not encontrados:
                print("No se encontraron registros para esa fecha.")
            input("\nPresiona Enter para continuar...")           

        elif opcion_log == "4":
            fecha_borrar = input("\nIngresa la fecha cuyos registros quieres borrar (AAAA-MM-DD): ")
            
            # Creamos una lista nueva guardando solo los elementos que NO coinciden con la fecha
            lista_nueva = []
            borrados = 0
            
            for item in registro:
                if fecha_borrar in item:
                    borrados += 1  # Lo ignoramos (lo borramos)
                else:
                    lista_nueva.append(item)  # Conservamos los demás
                    
            if borrados > 0:
                registro = lista_nueva  # Reemplazamos la lista antigua por la nueva
                guardar_logs(registro) # Guardamos los cambios en el teléfono
                input("\nSe borraron " + str(borrados) + " registro(s) de la fecha. Presiona Enter...")
            else:
                input("\nNo se encontraron registros con esa fecha. Presiona Enter...")

        elif opcion_log == "5":
            print("\n--- EDITAR REGISTRO ---")
            busqueda = input("Ingresa el texto exacto del registro a editar: ")
    
            if busqueda in registro:
                # Encontramos la posición del elemento en la lista
                posicion = registro.index(busqueda)
                
                # Pedimos el nuevo nombre
                nuevo_nombre = input("Ingresa la nueva información: ")
                
                # Reemplazamos en la lista
                registro[posicion] = nuevo_nombre
                
                # Guardamos en el archivo de logs
                guardar_logs(registro)
                
                input("\n¡Registro actualizado con éxito! Presiona Enter...")
            else:
                input("\nEl registro no existe. Presiona Enter...")
                  
        elif opcion_log == "6":
            en_log = False  # Regresa al menú global