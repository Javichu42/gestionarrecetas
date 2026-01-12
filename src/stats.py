import matplotlib.pyplot as plt
from recetas import lista_recetas
from collections import Counter


def grafico_ingredientes_por_receta():

    if not lista_recetas:
        print("No hay recetas para mostrar estadísticas.")
        return

    nombres = [receta["nombre"] for receta in lista_recetas]
    cantidades = [len(receta["ingredientes"]) for receta in lista_recetas]

    plt.figure()
    plt.bar(nombres, cantidades)
    plt.xlabel("Recetas")
    plt.ylabel("Número de ingredientes")
    plt.title("Ingredientes por receta")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def grafico_ingredientes_comunes():

    if not lista_recetas:
        print("No hay recetas para mostrar estadísticas.")
        return

    todos_ingredientes = []
    for receta in lista_recetas:
        todos_ingredientes.extend(receta["ingredientes"])

    contador = Counter(todos_ingredientes)

    ingredientes = list(contador.keys())
    cantidades = list(contador.values())

    plt.figure()
    plt.pie(cantidades, labels=ingredientes, autopct="%1.1f%%")
    plt.title("Ingredientes más comunes")
    plt.show()


def verestadisticas():

    print("\nMostrando estadísticas...")
    grafico_ingredientes_por_receta()
    grafico_ingredientes_comunes()