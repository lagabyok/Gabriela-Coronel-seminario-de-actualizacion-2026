# Portfolio - Proyecto Integrador

Repositorio correspondiente al proyecto integrador de la cursada.

## Contenido Clase 04 — Interfaz con Gradio Blocks

Objetivo
En esta clase reemplazamos gr.Interface por gr.Blocks para tener control sobre la disposición de la interfaz, y ampliamos la aplicación de la Clase 02:

Cambio a Blocks: la interfaz se construye con gr.Blocks, organizada en dos pestañas (gr.Tab).
Componentes nuevos: incorporamos gr.Slider, gr.Radio y gr.Number, que no se habían utilizado en clase (además de Textbox y Button).
Función propia: agregamos convertir_temperatura(celsius, unidad), conectada a sus propios inputs (slider y selector de unidad) y a su propio output (campo numérico).
Ejecución y enlace público: la aplicación se ejecuta localmente con share=True, que genera un enlace público temporal para compartirla.


#  Readme App

## Perfil Profesional

Aplicación web interactiva desarrollada con **Python + Gradio** que permite generar un perfil profesional personalizado a partir de datos básicos del usuario y consultar noticias relacionadas con su profesión u ocupación.

El proyecto combina una interfaz web simple y responsive con procesamiento de datos, generación dinámica de contenido y consumo de información mediante **Google News RSS**, sin necesidad de utilizar una API externa con clave.

---

##  Objetivo

El objetivo de la aplicación es crear una experiencia sencilla en la que una persona pueda:

* Ingresar sus datos personales y profesionales.
* Generar automáticamente un perfil profesional.
* Determinar una categoría según su edad.
* Obtener información relacionada con su profesión.
* Consultar noticias recientes de su área profesional.
* Interactuar con la aplicación desde una interfaz web.

El proyecto fue desarrollado como parte del **Seminario de Actualización 2026**.

---

##  Funcionalidades

###  Generación de perfil

El usuario puede ingresar:

* Nombre
* Edad
* Profesión u ocupación
* País

A partir de estos datos, la aplicación genera un perfil personalizado.

La edad también permite determinar automáticamente una categoría:

| Edad        | Categoría          |
| ----------- | ------------------ |
| Menor de 18 | Etapa inicial      |
| 18 – 29     | Joven profesional  |
| 30 – 59     | Profesional        |
| 60 o más    | Profesional senior |

---

###  Noticias profesionales

La aplicación genera una búsqueda relacionada con la profesión ingresada y obtiene noticias desde **Google News RSS**.

Se contemplan diferentes áreas profesionales, entre ellas:

* Desarrollo de software
* Programación
* Inteligencia Artificial
* Data Science
* Machine Learning
* Ingeniería
* Derecho
* UX/UI
* Marketing
* Educación
* Medicina
* Arquitectura
* Contabilidad
* Periodismo
* Psicología

También permite realizar búsquedas utilizando directamente la profesión ingresada por el usuario.

---

###  Actualización de noticias

El botón **"ACTUALIZAR NOTICIAS"** permite volver a consultar las noticias sin necesidad de regenerar todo el perfil.

---

### Limpieza de formulario

El botón **"LIMPIAR"** permite restablecer:

* Nombre
* Edad
* Profesión
* País
* Perfil generado
* Noticias

---

##  Tecnologías utilizadas

### Python

Lenguaje principal utilizado para desarrollar la lógica de la aplicación.

Se utiliza para:

* Procesamiento de datos.
* Generación del perfil.
* Clasificación según edad.
* Construcción de búsquedas.
* Obtención y procesamiento de noticias.
* Manejo de errores.
* Integración con Gradio.

---

### Gradio

Framework utilizado para construir la **interfaz web interactiva** de la aplicación.

Permite crear componentes como:

* Textbox
* Slider
* Dropdown
* Buttons
* Markdown
* Rows
* Columns

Además, permite conectar los componentes de la interfaz directamente con funciones Python mediante eventos.

---

### Google News RSS

Se utiliza el feed RSS de Google News para obtener noticias relacionadas con la profesión seleccionada.

Esto permite acceder a información actualizada sin implementar una API propia ni utilizar una API key.

---

### XML / ElementTree

La librería estándar `xml.etree.ElementTree` se utiliza para interpretar y procesar la información recibida desde el feed RSS.

Permite extraer:

* Título
* Enlace
* Descripción
* Fecha de publicación

---

### urllib

Se utiliza `urllib.request` y `urllib.parse`, ambas incluidas en la biblioteca estándar de Python.

Sus funciones principales son:

* Construir las consultas.
* Codificar parámetros.
* Realizar solicitudes HTTP.
* Descargar el feed RSS.

Por este motivo, el proyecto **no necesita `requests`**.

---

### HTML + CSS

La interfaz visual utiliza HTML y CSS personalizado dentro de Gradio.

El diseño busca una estética:

* Minimalista
* Editorial
* Monocromática
* Responsive
* Sin elementos visuales innecesarios

Se utilizan principalmente tonos:

* Negro
* Blanco
* Gris

La interfaz también adapta determinados elementos para dispositivos móviles.

---

##  Arquitectura de la aplicación

El funcionamiento general puede representarse de la siguiente manera:

```text
                  USUARIO
                     │
                     ▼
             ┌───────────────┐
             │    Gradio     │
             │   Interface   │
             └───────┬───────┘
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
   Datos personales       Profesión
          │                     │
          ▼                     ▼
   generar_perfil()     construir_busqueda()
          │                     │
          │                     ▼
          │              Google News RSS
          │                     │
          │                     ▼
          │             obtener_noticias()
          │                     │
          └──────────┬──────────┘
                     ▼
             Resultados Gradio
```

---

##  Estructura del proyecto

Una estructura recomendada para el proyecto es:

```text
proyecto_integrador/
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

### `app.py`

Contiene:

* Lógica de la aplicación.
* Funciones de generación del perfil.
* Consulta de noticias.
* Interfaz Gradio.
* CSS personalizado.
* Eventos de los botones.

### `requirements.txt`

Contiene las dependencias externas necesarias para ejecutar el proyecto.

Ejemplo:

```text
gradio
```

Las demás librerías utilizadas pertenecen a la biblioteca estándar de Python.

### `.gitignore`

Permite evitar que archivos innecesarios sean subidos al repositorio, como:

```text
__pycache__/
*.pyc
.venv/
venv/
.env
```

---

##  Instalación

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta:

```bash
cd proyecto_integrador
```

---

### 2. Crear un entorno virtual

En Windows:

```bash
python -m venv .venv
```

Activarlo:

```bash
.venv\Scripts\activate
```

---

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Ejecutar la aplicación

```bash
python app.py 
o
py app.py
```

jecución y enlace público: la aplicación se ejecuta localmente mediante Python y utiliza share=True de Gradio para generar un enlace público temporal que permite compartir la aplicación.

```text
http://127.0.0.1:7860
Running on public URL:https://a84d78b13fc7856ca3.gradio.live
```

Abrir esa dirección en el navegador.

---

##  Flujo de uso

1. El usuario ingresa su nombre.
2. Selecciona o ingresa su profesión.
3. Indica su edad.
4. Selecciona su país.
5. Presiona **GENERAR MI PERFIL**.
6. La aplicación genera el perfil profesional.
7. Se realiza una búsqueda relacionada con la profesión.
8. Se muestran noticias obtenidas desde Google News RSS.
9. El usuario puede presionar **ACTUALIZAR NOTICIAS** para realizar una nueva consulta.
10. Puede utilizar **LIMPIAR** para comenzar nuevamente.

---

##  Obtención de noticias

La aplicación utiliza una URL de búsqueda RSS con parámetros regionales para Argentina y español:

```text
Google News RSS
hl=es-419
gl=AR
ceid=AR:es-419
```

Esto permite orientar los resultados hacia contenido en español y noticias relevantes para Argentina.

No se requiere:

* API Key
* Base de datos
* Servidor externo
* `requests`
* API propia

---

##  Diseño

La interfaz fue diseñada utilizando CSS personalizado sobre Gradio.

Características principales:

* Diseño monocromático.
* Tipografía de alto contraste.
* Estética editorial.
* Inputs rectangulares.
* Botones minimalistas.
* Eliminación de tarjetas visuales innecesarias.
* Diseño responsive.
* Jerarquía visual mediante títulos y separadores.

El objetivo es que la aplicación tenga una apariencia más cercana a una pequeña aplicación web profesional que a un formulario tradicional.

---

##  Manejo de errores

La aplicación contempla diferentes situaciones:

### Sin nombre

Se informa al usuario que debe ingresar su nombre.

### Sin profesión

Se solicita ingresar una profesión u ocupación para poder personalizar el perfil y realizar la búsqueda de noticias.

### Sin resultados

Si Google News no devuelve noticias, se muestra un mensaje indicando que no se encontraron noticias recientes.

### Error de conexión

Si no es posible acceder al feed RSS, la aplicación informa que las noticias no pudieron cargarse y permite intentar nuevamente.

---

##  Consideraciones

La aplicación no almacena permanentemente los datos ingresados por el usuario.

Los datos utilizados para generar el perfil se procesan durante la ejecución de la aplicación.

La consulta de noticias utiliza información pública disponible mediante Google News RSS.

---

##  Conceptos aplicados

Este proyecto permite aplicar conocimientos relacionados con:

* Python
* Programación funcional
* Funciones
* Condicionales
* Diccionarios
* Strings
* Manejo de excepciones
* HTTP requests
* URL encoding
* XML
* RSS
* Procesamiento de texto
* Interfaces web
* Eventos
* Componentes interactivos
* HTML
* CSS
* Diseño responsive
* Integración de fuentes externas

---

##  Posibles mejoras futuras

El proyecto puede evolucionar incorporando:

* Sistema de recomendaciones profesionales.
* Más categorías de profesiones.
* Filtros por país.
* Filtros por fecha.
* Clasificación de noticias por relevancia.
* Análisis de sentimiento de las noticias.
* Resumen automático mediante IA.
* Integración con modelos de lenguaje.
* Historial de consultas.
* Exportación del perfil a PDF.
* Persistencia de datos.
* Deploy en Hugging Face Spaces.
* Integración con APIs profesionales.
* Sistema de autenticación.

---

## 👩‍💻 Autora

**Gabriela Coronel**

Proyecto desarrollado en el marco del **Seminario de Actualización 2026**.

Tecnologías principales:

**Python · Gradio · HTML · CSS · XML · RSS**

---

## 📄 Licencia

Proyecto educativo desarrollado con fines académicos y de aprendizaje.


