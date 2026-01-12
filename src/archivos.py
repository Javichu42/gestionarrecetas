import json
import csv
import os
from recetas import lista_recetas, crear_receta


def exportar_recetas():
    print("\nFormato de exportación:")
    print("1. JSON")
    print("2. CSV")
    print("3. TXT")

    opcion = input("Elige formato: ")
    nombre_archivo = input("Nombre del archivo (sin extensión): ")

    try:
        if opcion == "1":
            with open(nombre_archivo + ".json", "w", encoding="utf-8") as f:
                json.dump(lista_recetas, f, indent=4, ensure_ascii=False)
            print("Recetas exportadas a JSON correctamente.")

        elif opcion == "2":
            with open(nombre_archivo + ".csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["nombre", "ingredientes"])
                for receta in lista_recetas:
                    writer.writerow([
                        receta["nombre"],
                        ",".join(receta["ingredientes"])
                    ])
            print("Recetas exportadas a CSV correctamente.")

        elif opcion == "3":
            with open(nombre_archivo + ".txt", "w", encoding="utf-8") as f:
                for receta in lista_recetas:
                    f.write(receta["nombre"] + "\n")
                    f.write(",".join(receta["ingredientes"]) + "\n\n")
            print("Recetas exportadas a TXT correctamente.")

        else:
            print("Formato no válido.")

    except Exception as e:
        print(f"Error al exportar: {e}")
        