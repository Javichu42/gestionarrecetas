# api.py

import requests

# Buscar recetas por ingrediente
def buscar_recetas_por_ingrediente(ingrediente):
    """
    Busca recetas usando la API de themealdb.com por ingrediente.
    Devuelve una lista de recetas encontradas.
    """
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingrediente}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        datos = response.json()
        if datos['meals']:
            return datos['meals']
        else:
            print("No se encontraron recetas con ese ingrediente.")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error en la petición: {e}")
        return []

# Mostrar resultados de la API
def mostrar_recetas_api(lista_recetas):
    """
    Muestra por pantalla los resultados devueltos por la API.
    """
    if not lista_recetas:
        print("No hay recetas para mostrar.")
        return
    for i, receta in enumerate(lista_recetas, start=1):
        print(f"{i}. {receta['strMeal']}")
