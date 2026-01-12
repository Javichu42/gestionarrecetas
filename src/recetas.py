# recetas.py

# Lista para almacenar recetas
lista_recetas = []

# Crear una receta
def crear_receta(nombre, ingredientes):
    """Crea un diccionario con la receta"""
    return {"nombre": nombre, "ingredientes": ingredientes}

# Añadir receta desde el menú
def añadir_receta_menu():
    """Añade una receta desde la consola"""
    nombre = input("Nombre de la receta: ")
    ingredientes = input("Ingredientes (separados por coma): ").split(",")
    receta = crear_receta(nombre.strip(), [i.strip() for i in ingredientes])
    lista_recetas.append(receta)
    print(f"Receta '{nombre}' añadida correctamente.")

# Listar todas las recetas
def listar_recetas_menu():
    """Muestra todas las recetas guardadas"""
    if not lista_recetas:
        print("No hay recetas guardadas.")
        return
    for i, receta in enumerate(lista_recetas, start=1):
        print(f"\nReceta {i}: {receta['nombre']}")
        print("Ingredientes:")
        for ing in receta["ingredientes"]:
            print(f"- {ing}")

# Buscar receta por nombre
def buscar_receta(nombre):
    """Busca una receta por nombre y la devuelve"""
    for receta in lista_recetas:
        if receta["nombre"].lower() == nombre.lower():
            return receta
    return None

# Eliminar receta
def eliminar_receta(nombre):
    """Elimina una receta por nombre"""
    receta = buscar_receta(nombre)
    if receta:
        lista_recetas.remove(receta)
        print(f"Receta '{nombre}' eliminada.")
    else:
        print(f"No se encontró la receta '{nombre}'.")
