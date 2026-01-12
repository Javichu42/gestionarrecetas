import json
import csv
import os
from recetas import lista_recetas, crear_receta

data = "data"

if not os.path.exists(data):
    os.makedirs(data)

def exportar_recetas():
    print("\nFormato de exportación:")
    print("1. JSON")
    print("2. CSV")
    print("3. TXT")

    opcion = input("Elige formato: ")
    nombre_archivo = input("Nombre del archivo (sin extensión): ")

    ruta = os.path.join(DATA_DIR, nombre_archivo)

    try:
        if opcion == "1":
            with open(ruta + ".json", "w", encoding="utf-8") as f:
                json.dump(lista_recetas, f, indent=4, ensure_ascii=False)
            print("Recetas exportadas en data/ correctamente (JSON).")

        elif opcion == "2":
            with open(ruta + ".csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["nombre", "ingredientes"])
                for receta in lista_recetas:
                    writer.writerow([
                        receta["nombre"],
                        ",".join(receta["ingredientes"])
                    ])
            print("Recetas exportadas en data/ correctamente (CSV).")

        elif opcion == "3":
            with open(ruta + ".txt", "w", encoding="utf-8") as f:
                for receta in lista_recetas:
                    f.write(receta["nombre"] + "\n")
                    f.write(",".join(receta["ingredientes"]) + "\n\n")
            print("Recetas exportadas en data/ correctamente (TXT).")

        else:
            print("Formato no válido.")

    except Exception as e:
        print(f"Error al exportar: {e}")

def importar_recetas():
    nombre_archivo = input("Nombre del archivo (con extensión): ")

    ruta = os.path.join(DATA_DIR, nombre_archivo)

    if not os.path.exists(ruta):
        print("Error: el archivo no existe en la carpeta data.")
        return

    try:
        if nombre_archivo.endswith(".json"):
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for receta in datos:
                    lista_recetas.append(
                        crear_receta(receta["nombre"], receta["ingredientes"])
                    )
            print("Recetas importadas desde JSON.")

        elif nombre_archivo.endswith(".csv"):
            with open(ruta, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for fila in reader:
                    ingredientes = fila["ingredientes"].split(",")
                    lista_recetas.append(
                        crear_receta(fila["nombre"], ingredientes)
                    )
            print("Recetas importadas desde CSV.")

        elif nombre_archivo.endswith(".txt"):
            with open(ruta, "r", encoding="utf-8") as f:
                bloques = f.read().strip().split("\n\n")
                for bloque in bloques:
                    lineas = bloque.split("\n")
                    nombre = lineas[0]
                    ingredientes = lineas[1].split(",")
                    lista_recetas.append(
                        crear_receta(nombre, ingredientes)
                    )
            print("Recetas importadas desde TXT.")

        else:
            print("Formato de archivo no soportado.")

    except Exception as e:
        print(f"Error al importar: formato incorrecto o archivo dañado.\n{e}")