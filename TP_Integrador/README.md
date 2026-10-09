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

## AI-assisted QA Bug Triage

Aplicación de inteligencia artificial para asistir en la clasificación inicial de reportes de bugs de software.

BugTriage AI utiliza un modelo de **zero-shot classification** preentrenado para sugerir una categoría a partir de un reporte escrito en lenguaje natural.

### Categorías

- Funcional
- UI/UX
- Autenticación
- Datos
- Accesibilidad

### Tecnologías

- Python
- Hugging Face Transformers
- BART Large MNLI
- Gradio
- Hugging Face Spaces
- ZeroGPU

### Modelo

Se utiliza `facebook/bart-large-mnli`, evaluado previamente frente a un segundo modelo mediante un benchmark de 12 casos de prueba.

El modelo seleccionado obtuvo el mejor equilibrio entre precisión y tiempo de inferencia dentro del conjunto evaluado.

### Uso

Ingresá un reporte de bug y presioná **Analizar bug**.

La aplicación devuelve:

- categoría sugerida;
- nivel de confianza orientativo;
- score;
- categorías alternativas.

La clasificación es una asistencia para el primer triage y **no reemplaza la revisión humana**.

### Proyecto académico

Trabajo Práctico Integrador — Seminario de Actualización

Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial — IFTS N.º 18

Autora: Gabriela Coronel