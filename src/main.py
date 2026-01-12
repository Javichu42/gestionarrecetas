def mostrarmenu():
    print("\n=== Gestor de Recetas ===")
    print("1. Añadir Receta")
    print("2. Listar Receta")
    print("3. Exportar Receta (TXT, CSV, JSON)")
    print("4. Importar Receta (TXT, CSV, JSON)")
    print("5. Buscar Receta online (API)")
    print("6. Ver Estadisticas")
    print("0. Salir")

def main():
    while True:
        mostrarmenu()
        option = input("Selecciona una opció: ")

        ##if option == "1":
            #añadirreceta()

        #elif option == "2":
            #listasrecetas()

        #elif option == "3":
            #exportarceteas()

        #elif option == "4":
            #importarecetas()

        #elif option == "5":
            #buscarrecetasapi()

        #elif option == "6":
            #verestadisticas()

        if option == "0":
            print("Saliendo del programa... 👋")
            break

        else:
            print("Opció no vàlida. Torna a intentar-ho.")


if __name__ == "__main__":
    main()