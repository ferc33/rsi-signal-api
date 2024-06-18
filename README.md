
# 📈 RSI Signal API

![GitHub](https://img.shields.io/github/license/ferc33/rsi-signal-api)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.70.0-green)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)
![Status](https://img.shields.io/badge/status-Active-success)

## 🚀 Descripción del Proyecto

**RSI Signal API** es una API diseñada para calcular la **señal RSI (Relative Strength Index)**, una herramienta popular en el análisis técnico de mercados financieros. Esta API proporciona a los desarrolladores una manera fácil de integrar el cálculo del RSI en sus aplicaciones de trading y análisis de datos financieros.

## 🌟 Características

- 📊 **Cálculo del RSI**: Genera el índice de fuerza relativa (RSI) a partir de los datos de precios.
- 📦 **Facilidad de Integración**: API RESTful construida con FastAPI para una integración sencilla.
- 🔄 **Soporte para Docker**: Implementación simplificada utilizando Docker.
- 📉 **Análisis Financiero**: Herramienta esencial para traders y analistas de mercado.

## 🛠️ Tecnologías Utilizadas

- **Lenguaje de Programación**: ![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
- **Framework**: ![FastAPI](https://img.shields.io/badge/FastAPI-0.70.0-green)
- **Contenedorización**: ![Docker](https://img.shields.io/badge/Docker-Supported-blue)

## 🧩 Instalación y Uso

### Prerrequisitos

- Docker instalado en tu máquina. Puedes descargar Docker [aquí](https://www.docker.com/get-started).

### Paso a Paso

1. **Clona el repositorio**:
    ```bash
    git clone https://github.com/ferc33/rsi-signal-api.git
    cd rsi-signal-api
    ```

2. **Construye la imagen Docker**:
    ```bash
    docker build -t rsi-signal-api .
    ```

3. **Ejecuta el contenedor Docker**:
    ```bash
    docker run -p 8000:8000 rsi-signal-api
    ```

4. **Accede a la API**:
    Abre tu navegador y dirígete a `http://localhost:8000/docs` para ver la documentación interactiva de la API proporcionada por Swagger UI.

## 📚 Documentación

La documentación detallada de la API está disponible en la interfaz interactiva Swagger UI una vez que la API está en ejecución: `http://localhost:8000/docs`.

## 👥 Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los pasos indicados a continuación para contribuir:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## 📧 Contacto

Para cualquier pregunta o sugerencia, por favor contacta al mantenedor del proyecto:

- **Fernando Carrillo** - [ferc33@gmail.com](mailto:ferc33@gmail.com)
