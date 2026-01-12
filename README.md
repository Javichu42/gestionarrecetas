# gestionarrecetas

Javier López
Petar Petrov
# Gestor de Recetas

## Descripción del proyecto
Aplicación en Python para gestionar recetas de cocina, con funcionalidades para añadir, listar, buscar y eliminar recetas.  
Incluye integración con la API pública de themealdb.com para buscar recetas online.

## Instrucciones de instalación
1. Clonar el repositorio:
2. Instalar librerías externas:
3. Abrir los archivos en Python (VS Code, PyCharm, etc.)  

## Uso
- Ejecutar `main.py` (cuando el menú esté listo)  
- Funciones disponibles en `recetas.py`:
  - `añadir_receta_menu()`
  - `listar_recetas_menu()`
  - `buscar_receta(nombre)`
  - `eliminar_receta(nombre)`
- Funciones disponibles en `api.py`:
  - `buscar_recetas_por_ingrediente(ingrediente)`
  - `mostrar_recetas_api(lista_recetas)`

## Archivos
- `recetas.py`: gestión de recetas
- `api.py`: funciones para la API de recetas
- `archivos.py`: exportar/importar recetas (hecho por otro compañero)
- `main.py`: menú principal (hecho por otro compañero)
- `README.md`: documentación del proyecto

## Capturas y gráficos
(Los gráficos se mostrarán en `estadisticas.py`, realizados por otro compañero)