# Gestor de Recetas
Participantes del Equipo: Javier López y Petar Petrov

## Descripción del proyecto
Aplicación en Python para gestionar recetas de cocina, con funcionalidades para añadir, listar, buscar y eliminar recetas.  
Incluye integración con la API pública de themealdb.com para buscar recetas online. Se usa una libreria externa para traducir los ingredientes del Español a Ingles para buscar en la API mas facilmente.

## Instrucciones de instalación
1. Clonar el repositorio:
2. Instalar librerías externas: pip install googletrans==4.0.0-rc1
3. Abrir los archivos en Python (VS Code, PyCharm, etc.)  

## Uso
- Ejecutar `main.py`
- Funciones disponibles en `archivos.py`:
  - `exportar_recetas()`
  - `importar_recetas()`
- Funciones disponibles en `api.py`:
  - `traducir_ingrediente(ingrediente)`
  - `buscar_recetas_por_ingrediente(ingrediente)`
  - `mostrar_recetas_api(ingrediente)`
  - `buscarrecetasapi()`
- Funciones disponibles en `recetas.py`:
  - `crear_receta(nombre, ingrediente)`
  - `listar_recetas_menu()`
  - `añadir_receta_menu()`
- Funciones disponibles en `stats.py`:
  - `grafico_ingredientes_por_receta()`
  - `grafico_ingredientes_comunes()`
  - `grafico_media_ingredientes()`
  - `verestadisticas()`

## Archivos
- `recetas.py`: gestión de recetas
- `api.py`: funciones para la API de recetas
- `archivos.py`: exportar/importar recetas
- `stats.py`: estadisticas de las recetas
- `main.py`: menú principal
- `README.md`: documentación del proyecto

## Capturas y gráficos
(Los gráficos se pueden ver en `data/`)
