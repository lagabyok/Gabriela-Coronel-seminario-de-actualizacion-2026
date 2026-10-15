---
title: BugTriage AI
emoji: 🐞
colorFrom: green
colorTo: purple
sdk: gradio
sdk_version: "5.49.1"
app_file: app.py
pinned: false
---

# BugTriage AI

**AI-assisted QA Bug Triage**

Aplicación de inteligencia artificial que asiste en la clasificación inicial de reportes de errores (*bugs*) de software mediante un modelo preentrenado de clasificación *zero-shot*.

## Probar la aplicación

**Demo online:** https://huggingface.co/spaces/lagabyok/bugtriage-ai

Podés ingresar un reporte de error directamente en la aplicación publicada, sin instalar Python ni configurar un entorno local.

## Problema que resuelve

Durante las pruebas de software, los equipos de QA reciben reportes de errores que deben analizar y organizar para facilitar su seguimiento y resolución.

BugTriage AI propone una categoría inicial a partir de una descripción escrita en lenguaje natural. Su objetivo es asistir en el primer triage y agilizar la organización de los reportes, sin reemplazar la evaluación humana.

## Categorías de clasificación

* **Funcional:** problemas relacionados con el comportamiento o funcionamiento de una funcionalidad.
* **UI/UX:** problemas de interfaz de usuario o experiencia de uso.
* **Autenticación:** problemas relacionados con el inicio de sesión o la validación de identidad.
* **Datos:** problemas relacionados con el registro, almacenamiento o tratamiento de datos.
* **Accesibilidad:** posibles barreras que dificultan el uso de la aplicación por distintas personas.

## ¿Cómo funciona?

1. La persona ingresa una descripción del bug.
2. La aplicación envía el texto al modelo de clasificación.
3. El modelo compara la descripción con las categorías candidatas.
4. La aplicación muestra la categoría sugerida, su puntuación, el nivel de confianza orientativo y las categorías alternativas.

La clasificación es una recomendación inicial. Los resultados deben ser revisados por una persona, especialmente cuando la puntuación es baja o las categorías son similares.

## Modelo de inteligencia artificial

Se utiliza el modelo preentrenado [`facebook/bart-large-mnli`](https://huggingface.co/facebook/bart-large-mnli), disponible en Hugging Face Hub.

La aplicación utiliza la tarea `zero-shot-classification`, que permite comparar un texto con un conjunto de categorías candidatas sin entrenar un clasificador específico desde cero para este proyecto.

### Evaluación de modelos

Durante el desarrollo se compararon dos modelos mediante un conjunto exploratorio de 12 casos de prueba.

| Modelo                                          | Exactitud observada | Tiempo promedio por caso |
| ----------------------------------------------- | ------------------: | -----------------------: |
| `facebook/bart-large-mnli`                      |                50 % |                   0,90 s |
| `MoritzLaurer/mDeBERTa-v3-base-xnli-mnli-2mil7` |             16,67 % |                   4,15 s |

En ese conjunto de evaluación, BART obtuvo mayor exactitud y menor tiempo promedio de inferencia. Estos resultados corresponden únicamente a los casos evaluados y no garantizan el mismo rendimiento con otros reportes.

La puntuación devuelta por el modelo no debe interpretarse como una probabilidad calibrada de que la categoría sea correcta.

## Tecnologías utilizadas

* Python
* Hugging Face Transformers
* PyTorch
* Gradio
* Hugging Face Spaces
* ZeroGPU de Hugging Face Spaces

## Ejecutar el proyecto localmente

### Requisitos previos

Antes de comenzar, instalá:

* Python 3.10 o 3.11, según la compatibilidad de las dependencias del proyecto.
* Git.
* Una conexión a Internet para instalar las dependencias y descargar el modelo.

Los comandos siguientes están escritos para Windows PowerShell.

### 1. Clonar el repositorio

Abrí PowerShell y ejecutá:

```powershell
git clone https://github.com/lagabyok/Gabriela-Coronel-seminario-de-actualizacion-2026.git
```

Ingresá a la carpeta de la aplicación:

```powershell
cd Gabriela-Coronel-seminario-de-actualizacion-2026/TP_Integrador
```

### 2. Crear un entorno virtual

El entorno virtual permite instalar las dependencias del proyecto de forma aislada.

```powershell
python -m venv .venv
```

### 3. Activar el entorno virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación por la política de ejecución, podés habilitarla temporalmente para la sesión actual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Después, volvé a ejecutar el comando de activación.

### 4. Instalar las dependencias

Actualizar `pip`:

```powershell
python -m pip install --upgrade pip
```

Instalar las dependencias declaradas en `requirements.txt`:

```powershell
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene:

```text
gradio==5.49.1
transformers
torch
spaces
```

* `gradio`: crea la interfaz web.
* `transformers`: permite cargar y ejecutar el modelo de clasificación.
* `torch`: proporciona las operaciones de cálculo utilizadas por el modelo.
* `spaces`: proporciona funcionalidades específicas de Hugging Face Spaces utilizadas por la aplicación.

### 5. Ejecutar la aplicación

Desde la carpeta `TP_Integrador`, ejecutá:

```powershell
python app.py
```

Abrí en el navegador la dirección local que indique Gradio en la terminal. Habitualmente es:

http://127.0.0.1:7860

La primera ejecución puede tardar más porque el entorno necesita descargar el modelo y preparar sus dependencias.

Para detener la aplicación, regresá a la terminal y presioná `Ctrl+C`.

## Token de Hugging Face y variables de entorno

### ¿Es obligatorio configurar `HF_TOKEN`?

No es obligatorio para el funcionamiento previsto de la versión final si se utiliza el modelo público `facebook/bart-large-mnli` mediante `pipeline` de Transformers y no se realizan operaciones que requieran autenticación.

Durante el desarrollo también se probó `InferenceClient`, una herramienta que permite consultar servicios remotos de inferencia de Hugging Face. Esas pruebas presentaron errores de autenticación y disponibilidad del servicio. La implementación final utiliza `pipeline` como mecanismo principal de inferencia.

### ¿Cómo configurar un token sin escribirlo en el código?

Si necesitás un token para alguna operación adicional, podés crearlo desde tu cuenta de Hugging Face y almacenarlo como una variable de entorno.

En Windows PowerShell, ejecutá:

```powershell
$env:HF_TOKEN = Read-Host "Ingresá tu token de Hugging Face"
```

El valor queda disponible para los procesos iniciados desde esa terminal durante la sesión actual.

Para comprobar si está configurado sin mostrar el secreto:

```powershell
if ($env:HF_TOKEN) {
    Write-Output "HF_TOKEN está configurado"
} else {
    Write-Output "HF_TOKEN no está configurado"
}
```

Desde Python, la variable puede leerse así:

```python
import os

hf_token = os.getenv("HF_TOKEN")
```

Esta instrucción solamente lee la variable; no crea el token ni comprueba sus permisos.

**Importante:** nunca escribas el token directamente en `app.py`, lo subas al repositorio ni lo compartas en capturas de pantalla. Si la aplicación publicada necesitara una credencial para acceder a un servicio remoto, configurala en los secretos del entorno correspondiente.

## Estructura del proyecto

```text
TP_Integrador/
├── app.py
├── requirements.txt
├── README.md
└── notebook/
    └── 01_evaluacion_modelos.ipynb
```

* `app.py`: implementación de la aplicación Gradio y la clasificación de reportes.
* `requirements.txt`: dependencias necesarias para ejecutar el proyecto.
* `README.md`: documentación e instrucciones de instalación y uso.
* `notebook/01_evaluacion_modelos.ipynb`: evaluación exploratoria y comparación de modelos.

## Limitaciones y uso responsable

* El sistema propone una categoría; no determina de forma definitiva la causa del error.
* No reproduce el bug ni analiza automáticamente el código fuente de la aplicación afectada.
* Las puntuaciones no son probabilidades calibradas de acierto.
* La evaluación realizada con 12 casos es exploratoria y limitada.
* La clasificación debe ser revisada por una persona antes de tomar decisiones importantes de QA.

## Proyecto académico

**Trabajo Práctico Integrador — Seminario de Actualización 2026**

Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial — IFTS N.º 18

**Autora:** Gabriela Coronel

### Enlaces del proyecto

* **Aplicación online:** https://huggingface.co/spaces/lagabyok/bugtriage-ai

* **Modelo utilizado:** https://huggingface.co/facebook/bart-large-mnli
