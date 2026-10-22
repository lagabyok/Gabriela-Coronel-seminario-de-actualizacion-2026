
# Seminario de Actualización 2026 — Portfolio de Proyectos

Repositorio académico de trabajos prácticos, ejercicios y aplicaciones desarrolladas durante el Seminario de Actualización 2026 del IFTS N.º 18.

El objetivo es documentar el proceso de aprendizaje y reunir en un solo lugar las actividades realizadas, las aplicaciones desarrolladas y el proyecto integrador, aplicando buenas prácticas de programación, control de versiones, organización del código y documentación técnica.

## 📚 Contenido del repositorio

El repositorio está organizado por clases y actividades. Cada carpeta contiene los archivos correspondientes a su actividad y, cuando corresponde, un README con la documentación y las instrucciones necesarias para trabajar con ella.

```text
Gabriela-Coronel-seminario-de-actualizacion-2026/
│
├── Clase_02/
│   ├── .gitignore
│   ├── README.md
│   ├── app.py
│   ├── image.png
│   └── requirements.txt
│
├── Clase_03/
│   ├── README.md
│   └── image-1.png
│
├── Clase_04/
│   ├── .gradio/
│   ├── .gitignore
│   ├── README.md
│   ├── app.py
│   └── requirements.txt
│
├── Clase_05/
│   ├── .gradio/
│   ├── .gitignore
│   ├── README.md
│   ├── app.py
│   ├── app_streamlit.py
│   └── requirements.txt
│
├── Clase_6TS.pdf
│
├── TP_Integrador/
│   ├── .gradio/
│   │   └── flagged/
│   ├── informe/
│   ├── notebook/
│   ├── presentacion/
│   ├── .gitignore
│   ├── README.md
│   ├── app.py
│   └── requirements.txt
│
└── README.md
```

### Organización de las actividades

- **Clase 02:** preparación del entorno de desarrollo, Python, entornos virtuales, dependencias y primeros pasos con Git.
- **Clase 03:** ejercicios de Git y GitHub, seguimiento de cambios, ramas e interacción con repositorios.
- **Clase 04:** desarrollo de interfaces interactivas con Gradio.
- **Clase 05:** desarrollo y despliegue de aplicaciones con Gradio y Streamlit.
- **Clase 06 — Revisión de pares:** evaluación del repositorio de un compañero o compañera mediante una rúbrica, con foco en la documentación, la organización, la reproducibilidad y el historial de commits. La entrega se encuentra en `Clase_6TS.pdf`.
- **TP Integrador:** desarrollo de BugTriage AI, proyecto de inteligencia artificial realizado como trabajo integrador del seminario.

## 🚀 Requisitos previos

Para trabajar con las actividades que incluyen código, se recomienda contar con:

- Python, en la versión indicada por cada actividad.
- Git instalado.
- Visual Studio Code u otro editor de código.
- Conexión a Internet para clonar el repositorio e instalar las dependencias.

Los requisitos pueden variar entre actividades. Consultá la documentación individual antes de comenzar.

## 📥 1. Clonar el repositorio

La clonación se realiza una sola vez. Abrí una terminal y ejecutá:

```bash
git clone https://github.com/lagabyok/Gabriela-Coronel-seminario-de-actualizacion-2026.git
```

Ingresá a la carpeta del repositorio:

```bash
cd Gabriela-Coronel-seminario-de-actualizacion-2026
```

Si utilizás Visual Studio Code, podés abrir el proyecto completo con:

```bash
code .
```

Una vez clonado, podés navegar por las carpetas y trabajar con cada actividad de manera independiente.

## 🐍 2. Preparar el entorno de trabajo

Cada actividad puede tener sus propios requisitos y dependencias. Por eso, **no existe un único procedimiento de instalación que deba aplicarse automáticamente a todas las carpetas**.

Si una actividad utiliza Python y cuenta con un archivo `requirements.txt`, seguí las instrucciones de su README para crear y activar el entorno virtual e instalar las dependencias correspondientes.

Como referencia, la configuración habitual en Windows PowerShell consiste en:

1. Ingresar a la carpeta de la actividad.
2. Crear un entorno virtual con la versión de Python requerida.
3. Activar el entorno virtual.
4. Instalar las dependencias declaradas en su `requirements.txt`.

Los comandos exactos, las versiones necesarias y cualquier configuración adicional deben consultarse en la documentación de cada actividad.

## ▶️ 3. Abrir y ejecutar las actividades

Para ejecutar una actividad, seguí los pasos indicados en su README individual. Allí se especifican los requisitos, la configuración del entorno, la instalación de dependencias y el comando de ejecución, cuando corresponda.

### Documentación de las actividades

- [Clase 02 — README](Clase_02/README.md)
- [Clase 03 — README](Clase_03/README.md)
- [Clase 04 — README](Clase_04/README.md)
- [Clase 05 — README](Clase_05/README.md)
- [Clase 06 — Revisión de pares](Clase_6TS.pdf)
- [TP Integrador — README](TP_Integrador/README.md)

El README principal funciona como índice general del repositorio. La documentación individual de cada actividad es la referencia para instalar, configurar y ejecutar sus archivos.

## 🌐 Aplicaciones desplegadas

Algunas actividades cuentan con versiones publicadas que se pueden consultar directamente desde el navegador.

### Clase 05 — Perfil Profesional

- **Versión Gradio en Render:** [Abrir aplicación](https://perfil-profesional-app.onrender.com/)
- **Versión Streamlit:** [Abrir aplicación](https://gabriela-coronel-seminario-portfolio-app-perfilpro.streamlit.app/)

### TP Integrador

- **BugTriage AI en Hugging Face Spaces:** [Abrir aplicación](https://huggingface.co/spaces/lagabyok/bugtriage-ai)

La disponibilidad de las aplicaciones depende de las condiciones del servicio de alojamiento.

## 🛠️ Tecnologías y herramientas

Entre las herramientas y tecnologías utilizadas a lo largo del seminario se encuentran:

- **Python:** desarrollo de aplicaciones y procesamiento de datos.
- **Git y GitHub:** control de versiones y gestión del código fuente.
- **Gradio:** creación de interfaces web interactivas.
- **Streamlit:** desarrollo de aplicaciones interactivas.
- **Hugging Face Spaces:** publicación de aplicaciones.
- **Render:** despliegue de aplicaciones web.
- **Modelos preentrenados de inteligencia artificial:** utilizados en actividades de inferencia y clasificación.

Las tecnologías y dependencias específicas varían según los objetivos de cada actividad.

## 📌 Buenas prácticas de organización

- Mantener cada actividad dentro de su carpeta correspondiente.
- Documentar los proyectos y ejercicios mediante sus README.
- Registrar las dependencias de cada aplicación en su `requirements.txt`, cuando corresponda.
- Utilizar `.gitignore` para excluir entornos virtuales y archivos locales que no deban versionarse.
- No publicar tokens, contraseñas, claves privadas ni datos sensibles.
- Evitar incluir archivos temporales o registros que no sean necesarios para comprender o reproducir el proyecto.

## 👩‍💻 Autora

**Gabriela Coronel**

Estudiante de la Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial — IFTS N.º 18.

Repositorio académico del Seminario de Actualización 2026.
