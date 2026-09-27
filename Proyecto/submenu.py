import os
from archivos import guardar_datos
from archivos import cargar_datos

def catalogo(lista):
    en_catalogo = True
    while en_catalogo:
        os.system("clear")
        print("=== MÓDULO ENTRETENIMIENTO ===")
        print("1. Agregar elemento")
        print("2. Ver lista")
        print("3. Buscar Elemento")
        print("4. Eliminar Elemento")
        print("5. Editar Elemento")
        print("6. Volver al Menú Principal")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            nuevo = input("Agrega el nombre del nuevo elemento: ")
            lista.append(nuevo)
            guardar_datos(lista)
            input("\n'" + nuevo + "' guardado con éxito. Presiona Enter para continuar...")
            
        elif opcion == "2":
            print("\n--- TUS ELEMENTOS ---")
            for item in lista:
                print("- " + item)
            input("\nPresiona Enter...")
            
        elif opcion == "3":
            busqueda = input("¿Qué elemento quieres buscar?: ")
            if busqueda in lista:
                print("¡ENCONTRADO! '" + busqueda + "' está registrado en el sistema.")
            else:
                print("NO ENCONTRADO. '" + busqueda + "' no existe en el registro.")
            input("\nPresiona Enter para volver al menú...")
           
        elif opcion == "4":
            borrar = input("\nIngresa el nombre exacto del elemento a borrar: ")
            if borrar in lista:
                lista.remove(borrar)
                guardar_datos(lista)
                input("\n'" + borrar + "' ha sido eliminado con éxito! Presiona Enter...")
            else:
                input("\nNO ENCONTRADO. No se pudo borrar porque no existe en la lista. Presiona Enter...")   
                    
        elif opcion == "5":
            print("\n--- EDITAR ELEMENTO ---")
            busqueda = input("Ingresa el nombre exacto del elemento a editar: ")
    
            if busqueda in lista:
                # Encontramos la posición del elemento en la lista
                posicion = lista.index(busqueda)
                
                # Pedimos el nuevo nombre
                nuevo_nombre = input("Ingresa el nuevo nombre:  ")
                
                # Reemplazamos en la lista
                lista[posicion] = nuevo_nombre
                
                # Guardamos en el archivo .txt
                guardar_datos(lista)
                
                input("\n¡Elemento actualizado con éxito! Presiona Enter...")
            else:
                input("\nEl elemento no existe en el registro. Presiona Enter...")           
             
        elif opcion == "6":
            en_catalogo = False
