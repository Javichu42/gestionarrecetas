import requests
from googletrans import Translator

translator = Translator()

def traducir_ingrediente(ingrediente):
    traduccion = translator.translate(ingrediente, src="es", dest="en")
    return traduccion.text

# Buscar recetas por ingrediente
def buscar_recetas_por_ingrediente(ingrediente):
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
    if not lista_recetas:
        print("No hay recetas para mostrar.")
        return
    for i, receta in enumerate(lista_recetas, start=1):
        print(f"{i}. {receta['strMeal']}")


def buscarrecetasapi():
    ingrediente_es = input("Ingrediente a buscar: ")
    ingrediente_en = traducir_ingrediente(ingrediente_es)

    recetas = buscar_recetas_por_ingrediente(ingrediente_en)
    mostrar_recetas_api(recetas)