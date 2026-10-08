import gradio as gr
import spaces
import torch
from transformers import pipeline


MODELO = "facebook/bart-large-mnli"

CATEGORIAS = [
    "Funcional",
    "UI/UX",
    "Autenticación",
    "Datos",
    "Accesibilidad"
]


# El modelo se carga una sola vez al iniciar la aplicación.
clasificador = pipeline(
    "zero-shot-classification",
    model=MODELO,
    device=0 if torch.cuda.is_available() else -1
)


@spaces.GPU
def clasificar_bug(texto):
    if not texto or not texto.strip():
        return "Ingresá un reporte de bug.", ""

    resultado = clasificador(
        texto,
        CATEGORIAS,
        multi_label=False
    )

    categoria = resultado["labels"][0]
    score = resultado["scores"][0]

    # Interpretación orientativa del score.
    if score >= 0.60:
        nivel = "Alto"
        advertencia = "La predicción presenta una confianza alta."
    elif score >= 0.40:
        nivel = "Medio"
        advertencia = "Se recomienda revisar la clasificación."
    else:
        nivel = "Bajo"
        advertencia = (
            "Se recomienda revisión humana antes de derivar el bug."
        )

    alternativas = "\n".join(
        f"- {label}: {score:.2%}"
        for label, score in zip(
            resultado["labels"],
            resultado["scores"]
        )
    )

    resultado_final = (
        f"Categoría sugerida: {categoria}\n"
        f"Nivel de confianza: {nivel}\n"
        f"Score: {score:.2%}\n\n"
        f"{advertencia}"
    )

    return resultado_final, alternativas


demo = gr.Interface(
    fn=clasificar_bug,
    inputs=gr.Textbox(
        label="Reporte del bug",
        placeholder="Ejemplo: El botón de guardar no funciona...",
        lines=5
    ),
    outputs=[
        gr.Textbox(
            label="Clasificación"
        ),
        gr.Textbox(
            label="Categorías alternativas"
        )
    ],
    title="BugTriage AI",
    description=(
        "Clasificación asistida por IA de reportes de bugs "
        "mediante zero-shot classification. "
        "La herramienta funciona como apoyo al primer triage "
        "y no reemplaza la revisión humana."
    ),
    submit_btn="Analizar bug",
    clear_btn="Limpiar"
)


if __name__ == "__main__":
    demo.launch()