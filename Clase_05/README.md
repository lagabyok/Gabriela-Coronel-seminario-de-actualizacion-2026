# Portfolio - Proyecto Integrador

Repositorio correspondiente al proyecto integrador de la cursada
Seminario de Actualización · IFTS N.º 18



# Clase 05

## Actividad: Publicá tu app y documentala

En esta actividad se realizó el **deploy de la aplicación desarrollada con Gradio** y se creó una versión equivalente utilizando **Streamlit**.

El objetivo fue comprobar que una aplicación desarrollada en Python puede ser publicada en un servidor real y que el procedimiento de despliegue puede adaptarse a diferentes herramientas de interfaz.

---

## 1. Deploy en Render

La aplicación original fue desarrollada utilizando **Python y Gradio**.

La aplicación permite ingresar datos personales y profesionales para generar un perfil personalizado. Además, utiliza el RSS de Google News para obtener noticias relacionadas con la profesión ingresada.

### Funcionalidades

- Ingreso del nombre.
- Selección de edad.
- Ingreso de profesión u ocupación.
- Selección del país.
- Generación de un perfil profesional.
- Clasificación de la etapa profesional según la edad.
- Búsqueda de noticias relacionadas con la profesión.
- Actualización de noticias.
- Botón para limpiar los datos.

La interfaz fue desarrollada con `gr.Blocks()` y cuenta con estilos CSS personalizados. La aplicación utiliza funciones independientes para generar el perfil, obtener noticias y limpiar los datos.

### Configuración para Render

Para que Gradio pueda funcionar correctamente en Render, se configuró el servidor para escuchar en todas las interfaces de red y utilizar el puerto correspondiente.

```python
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )
```

##  Deploy

### Aplicación Gradio publicada en Render

[PEGAR AQUÍ EL LINK DE RENDER]

---

##  Versión equivalente en Streamlit

Como parte de la actividad se desarrolló una versión mínima de la aplicación utilizando **Streamlit**.

Esta versión mantiene la idea principal del proyecto, pero utiliza los componentes y la forma de interacción propios de Streamlit.

No es necesario que la versión de Streamlit tenga exactamente la misma interfaz que la versión de Gradio. El objetivo es comprobar que la misma aplicación puede llevarse a otra herramienta de interfaz y posteriormente publicarse.

### Deploy en Streamlit

**Aplicación Streamlit publicada:**

[PEGAR AQUÍ EL LINK DE STREAMLIT]

---

##  Diferencias entre Gradio y Streamlit

La principal diferencia observada fue la forma de construir la interfaz.

Con **Gradio**, la aplicación se organiza mediante componentes y eventos, utilizando elementos como `Textbox`, `Slider`, `Dropdown` y botones asociados a funciones mediante `.click()`.

Con **Streamlit**, la interfaz se construye de manera más directa mediante instrucciones de Python que generan los componentes en pantalla y ejecutan el código según la interacción del usuario.

A pesar de estas diferencias, el proceso general de publicación es similar: preparar las dependencias, configurar el proyecto, conectarlo con el repositorio y realizar el deploy en un servicio externo.

---

## Tecnologías utilizadas

- **Python**
- **Gradio**
- **Streamlit**
- **Render**
- **Google News RSS**
- **Git**
- **GitHub**

---

## Estructura del proyecto

```text
proyecto_integrador/
│
├── Clase_05/
│   └── README.md
│
├── app.py
├── app_streamlit.py
├── requirements.txt
├── .gitignore
└── README.md
```

##  Resultado

# Al finalizar la actividad se obtuvieron:

Una aplicación de Gradio publicada en Render.
Una versión mínima de la aplicación desarrollada con Streamlit.
Ambas aplicaciones documentadas.
El README general del proyecto actualizado para incluir la Clase 05.
Entrega

La entrega corresponde al enlace del repositorio de GitHub.6. Resultado


## Autor/a

Gabriela Coronel