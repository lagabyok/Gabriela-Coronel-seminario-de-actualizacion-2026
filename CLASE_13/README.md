# ReciClass ♻️
### Clasificador de residuos mediante visión artificial y Machine Learning

**Proyecto integrador – Seminario de Actualización 2026**  
**Autora:** Gabriela Coronel  
**Institución:** IFTS N.º 18 – Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial

---

## 🌐 Aplicación y repositorio

- **Aplicación web:** https://reciclass.onrender.com
- **API – Estado del servicio:** https://reciclass.onrender.com/health
- **Documentación interactiva de la API:** https://reciclass.onrender.com/docs
- **Repositorio GitHub:** https://github.com/lagabyok/ReciClass/tree/main
- **Modelo entrenado:** https://huggingface.co/lagabyok/reciclass-model

El repositorio contiene el código fuente, la implementación del backend, el frontend y los archivos necesarios para comprender el desarrollo del proyecto.

## 1. Descripción del proyecto

**ReciClass** es una aplicación web que permite clasificar residuos a partir de una imagen utilizando técnicas de visión artificial y Machine Learning.

El usuario carga una fotografía de un residuo y el sistema procesa la imagen para identificar a qué categoría pertenece. Como resultado, muestra la clase predicha y las probabilidades estimadas para las distintas categorías.

El objetivo es desarrollar una herramienta accesible que permita explorar cómo los modelos de aprendizaje automático pueden aplicarse a la clasificación de residuos y contribuir a la educación y concientización sobre la separación de materiales.

### Categorías de clasificación

El modelo trabaja con nueve categorías:

1. Cardboard
2. Food Organics
3. Glass
4. Metal
5. Miscellaneous Trash
6. Paper
7. Plastic
8. Textile Trash
9. Vegetation

## 2. Dataset

Para el entrenamiento y evaluación se utilizó el dataset **RealWaste**, compuesto por 4.752 imágenes de residuos.

Se realizó una división estratificada de los datos para conservar la proporción de las clases en los distintos subconjuntos:

| Conjunto | Proporción |
|---|---:|
| Entrenamiento | 70 % |
| Validación | 15 % |
| Prueba | 15 % |

La separación permite entrenar el modelo, comparar alternativas y evaluar su desempeño sobre imágenes que no fueron utilizadas durante el entrenamiento.

## 3. Procesamiento de imágenes y extracción de características

El proyecto utiliza técnicas tradicionales de visión artificial para transformar las imágenes en vectores numéricos que puedan ser procesados por los algoritmos de Machine Learning.

Se implementó una extracción combinada de características:

- **HOG (Histogram of Oriented Gradients):** permite representar información relacionada con bordes, formas y gradientes de la imagen.
- **LBP (Local Binary Patterns):** captura patrones locales de textura.
- **HSV (Hue, Saturation, Value):** representa información del color.

La combinación genera un vector de **8.366 características** por imagen:

| Descriptor | Cantidad de características |
|---|---:|
| HOG | 8.100 |
| LBP | 10 |
| HSV | 256 |
| **Total** | **8.366** |

La extracción de características utilizada durante la predicción mantiene el mismo esquema que el empleado durante el entrenamiento, para asegurar la compatibilidad entre los datos de entrada y el modelo.

## 4. Entrenamiento y selección del modelo

Durante el desarrollo se compararon distintos algoritmos de clasificación:

- Support Vector Machine (SVM).
- Random Forest.
- Extra Trees.

A partir de las pruebas realizadas se seleccionó un modelo **Support Vector Machine con kernel RBF**.

Configuración utilizada:

| Parámetro | Valor |
|---|---|
| Algoritmo | SVM |
| Kernel | RBF |
| C | 10 |
| Gamma | scale |
| Class weight | balanced |
| Probability | True |

La configuración `class_weight=balanced` permite considerar el desequilibrio en la cantidad de imágenes de las distintas categorías durante el entrenamiento.

### Métricas de evaluación

Los resultados obtenidos fueron:

| Métrica | Validación | Prueba |
|---|---:|---:|
| Accuracy | 59,05 % | 57,22 % |
| F1 Macro | 58,16 % | 55,01 % |

Las métricas del conjunto de prueba representan la evaluación final sobre datos separados del entrenamiento.

El desempeño evidencia que el modelo logra reconocer patrones visuales en las imágenes, aunque todavía presenta limitaciones. Los resultados pueden variar ante fotografías externas al dataset, condiciones de iluminación diferentes, fondos complejos o residuos que pertenezcan a categorías visualmente similares.

Las probabilidades que devuelve SVM son estimaciones del modelo y no deben interpretarse como una certeza absoluta.

## 5. Arquitectura de la aplicación

ReciClass utiliza una arquitectura cliente-servidor:

- **Frontend:** interfaz web desarrollada con HTML, CSS y JavaScript.
- **Backend:** API desarrollada con Python y FastAPI.
- **Modelo:** archivo serializado `modelo.joblib`, utilizado para realizar las predicciones.
- **Despliegue:** servicio web alojado en Render.
- **Almacenamiento del modelo:** Hugging Face.

### Flujo de funcionamiento

1. El usuario ingresa a la aplicación web.
2. Selecciona una imagen desde su dispositivo.
3. El frontend convierte la imagen a Base64 y la envía al backend.
4. FastAPI recibe y valida los datos.
5. Se decodifica la imagen y se verifica su formato.
6. El backend ejecuta la extracción HOG, LBP y HSV.
7. El vector de características se envía al modelo SVM.
8. El modelo genera la categoría predicha y las probabilidades estimadas.
9. La API devuelve el resultado en formato JSON.
10. El frontend presenta la clasificación al usuario.

### Diagrama lógico

```text
              USUARIO
                 |
                 v
        NAVEGADOR WEB
                 |
                 v
       FRONTEND HTML / CSS / JS
                 |
                 | Imagen en Base64
                 v
          API FASTAPI
                 |
                 v
       VALIDACIÓN DE IMAGEN
                 |
                 v
     EXTRACCIÓN DE CARACTERÍSTICAS
          HOG + LBP + HSV
                 |
                 v
           MODELO SVM
          modelo.joblib
                 |
                 v
       PREDICCIÓN Y PROBABILIDADES
                 |
                 | Respuesta JSON
                 v
       FRONTEND / RESULTADO
                 |
                 v
              USUARIO
```

## 6. API

La API fue desarrollada con FastAPI y permite realizar predicciones a partir de imágenes enviadas mediante una solicitud HTTP.

### Endpoint de estado

**GET `/health`**

Permite verificar si el servicio está disponible y si el modelo fue cargado correctamente.

Ejemplo de respuesta:

```json
{
  "estado": "ok",
  "modelo_cargado": true
}
```

### Endpoint de predicción

**POST `/predecir`**

Recibe una imagen codificada en Base64 y devuelve la categoría predicha junto con las probabilidades estimadas.

Ejemplo de entrada:

```json
{
  "image_base64": "BASE64_DE_LA_IMAGEN",
  "filename": "residuo.jpg"
}
```

Ejemplo de respuesta:

```json
{
  "prediccion": "Plastic",
  "probabilidad": 0.82,
  "probabilidades": {
    "Cardboard": 0.02,
    "Food Organics": 0.01,
    "Glass": 0.03,
    "Metal": 0.02,
    "Miscellaneous Trash": 0.03,
    "Paper": 0.02,
    "Plastic": 0.82,
    "Textile Trash": 0.03,
    "Vegetation": 0.02
  },
  "archivo": "residuo.jpg"
}
```

Los valores del ejemplo son ilustrativos y no representan una predicción real.

### Validaciones

El backend contempla:

- Imágenes en formatos JPEG, PNG y WEBP.
- Tamaño máximo de imagen de 10 MB.
- Validación de la codificación Base64.
- Validación del contenido de la imagen.
- Verificación de la dimensión del vector de características antes de ejecutar el modelo.

### Códigos de respuesta

| Código | Descripción |
|---|---|
| 200 | Predicción realizada correctamente. |
| 422 | Datos de entrada inválidos o imagen mal formada. |
| 413 | La imagen supera el tamaño máximo permitido. |
| 500 | Error interno durante el procesamiento o la predicción. |
| 503 | Servicio no disponible o modelo no cargado, en el endpoint de estado. |

La documentación interactiva de los endpoints se encuentra en:

https://reciclass.onrender.com/docs

## 7. Despliegue

La aplicación se encuentra desplegada en **Render**, utilizando un único servicio web para alojar el backend FastAPI y servir el frontend estático.

Se eligió esta alternativa porque permite publicar la API y la interfaz dentro del mismo servicio, simplificando la comunicación entre ambas partes y evitando la necesidad de configurar dos dominios diferentes.

### Componentes del despliegue

| Componente | Plataforma |
|---|---|
| Código fuente | GitHub |
| Frontend | Render |
| Backend / API | Render |
| Modelo entrenado | Hugging Face |
| Ejecución del servidor | Uvicorn |
| Framework de API | FastAPI |

El modelo se descarga desde Hugging Face durante el proceso de construcción del servicio mediante el script `download_model.py`.

El archivo `modelo.joblib` tiene un tamaño aproximado de 150 MB y no se incluye directamente en el repositorio GitHub. Esta decisión evita incorporar un archivo pesado al historial del repositorio y permite mantener separado el código fuente del artefacto entrenado.

### Configuración de Render

**Build Command:**

```bash
pip install -r requirements.txt && python download_model.py
```

**Start Command:**

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

La configuración del entorno utiliza variables de entorno para definir parámetros de ejecución y la ubicación de descarga del modelo.

## 8. CORS y comunicación entre frontend y backend

Durante el desarrollo se configuró CORS en FastAPI para permitir solicitudes desde los orígenes locales utilizados durante las pruebas.

En producción, el frontend y el backend se sirven desde el mismo dominio de Render. Por ese motivo, la aplicación utiliza rutas relativas para comunicarse con la API, sin necesitar una configuración CORS entre dominios diferentes.

Esta decisión simplifica el despliegue y reduce posibles problemas de comunicación entre el navegador y el servidor.

## 9. Limitaciones y mejoras futuras

ReciClass es un prototipo funcional y académico. Su desempeño y su infraestructura presentan limitaciones que deben considerarse antes de utilizarlo en un entorno de producción.

### Limitaciones actuales

- El modelo presenta una exactitud de 57,22 % en el conjunto de prueba.
- Las imágenes externas pueden tener características diferentes a las del dataset.
- Algunas categorías tienen similitudes visuales que pueden generar confusiones.
- Las probabilidades son estimaciones del modelo y no garantizan que la predicción sea correcta.
- El servicio utiliza el plan gratuito de Render, que puede suspenderse después de un período de inactividad.
- El primer acceso luego de la suspensión puede demorar mientras el servicio vuelve a iniciarse.
- La infraestructura gratuita no está diseñada para garantizar atención simultánea de grandes volúmenes de usuarios.

### Próximas mejoras

1. Ampliar y diversificar el dataset.
2. Analizar los errores por categoría mediante matrices de confusión.
3. Evaluar técnicas de aumento de datos.
4. Comparar el enfoque actual con redes neuronales convolucionales y modelos preentrenados.
5. Mejorar el rendimiento y la generalización del clasificador.
6. Incorporar mecanismos de monitoreo y registro de errores.
7. Realizar pruebas de carga y evaluar infraestructura escalable.
8. Mejorar la experiencia de usuario y la explicación de los resultados.

## 10. Ejecución local

Para ejecutar el proyecto en un entorno local se necesita Python y las dependencias declaradas en `requirements.txt`.

Desde la carpeta del backend:

```powershell
cd app/backend
```

Crear y activar un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```powershell
pip install -r requirements.txt
```

Configurar la ubicación del modelo según las instrucciones del proyecto y ejecutar el servidor:

```powershell
python -m uvicorn main:app --reload
```

La aplicación estará disponible en:

- Frontend: http://127.0.0.1:8000
- Documentación API: http://127.0.0.1:8000/docs
- Estado del servicio: http://127.0.0.1:8000/health

## 11. Uso de herramientas de inteligencia artificial generativa

Durante el desarrollo se utilizaron herramientas de inteligencia artificial generativa como apoyo para la resolución de dudas técnicas, revisión de código, análisis de errores, documentación y organización de tareas.

La implementación, las pruebas, la selección del modelo, la evaluación de resultados y las decisiones técnicas fueron revisadas durante el proceso de desarrollo.

Las herramientas generativas se utilizaron como asistencia y no como sustituto de la validación técnica del funcionamiento de la aplicación.

---

## 12. Autora

**Gabriela Coronel**  
Proyecto integrador – Seminario de Actualización 2026  
IFTS N.º 18 – Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial

**Repositorio del proyecto:**  
https://github.com/lagabyok/ReciClass/tree/main

**Aplicación desplegada:**  
https://reciclass.onrender.com

**Modelo:**  
https://huggingface.co/lagabyok/reciclass-model

**Colab_EDA_dataset:** 
https://colab.research.google.com/drive/1H5l7YQmET_Xnt5SaVIgXD6nWt_qhuOKF?usp=sharing

