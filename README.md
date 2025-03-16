# Prefect ETL con JSONPlaceholder

Este proyecto es una implementación de un flujo ETL (Extract, Transform, Load) utilizando Prefect, una herramienta de orquestación de flujos de trabajo en Python. El flujo extrae datos desde la API de JSONPlaceholder, los transforma y los almacena en una base de datos SQLite.

## Descripción de la Actividad

La actividad consiste en:

1. Seguir el tutorial original sobre Prefect y su uso en flujos ETL.
2. Modificar el código para obtener datos desde JSONPlaceholder en lugar de la fuente original.
3. Implementar un flujo ETL con Prefect para extraer publicaciones, transformarlas y almacenarlas en SQLite.

## Instalación y Ejecución

### Prerrequisitos

Asegúrate de tener instalado Python y los siguientes paquetes:

```bash
pip install prefect requests sqlite3
```

### Ejecución

Clona el repositorio y ejecuta el script principal:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
python script.py
```

## Código

El código principal implementa las siguientes funciones:

- **Extracción**: Obtiene datos de publicaciones desde `https://jsonplaceholder.cypress.io/posts`.
- **Transformación**: Organiza los datos en una estructura definida.
- **Carga**: Almacena los datos en una base de datos SQLite llamada `posts.db`.



