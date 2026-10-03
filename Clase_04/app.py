import gradio as gr
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime


# ============================================================
# CONFIGURACIÓN
# ============================================================

GOOGLE_NEWS_URL = (
    "https://news.google.com/rss/search?"
    "q={}&hl=es-419&gl=AR&ceid=AR:es-419"
)


# ============================================================
# GENERAR CONSULTA DE NOTICIAS
# ============================================================

def construir_busqueda(profesion):

    profesion = profesion.lower().strip()

    categorias = {
        "developer": "software development programming technology artificial intelligence",
        "desarrollador": "software development programming technology artificial intelligence",
        "desarrolladora": "software development programming technology artificial intelligence",
        "programador": "programming software development technology AI",
        "programadora": "programming software development technology AI",
        "data scientist": "data science machine learning artificial intelligence",
        "cientifico de datos": "data science machine learning artificial intelligence",
        "científico de datos": "data science machine learning artificial intelligence",
        "ingeniero": "engineering technology innovation",
        "ingeniera": "engineering technology innovation",
        "abogado": "derecho jurisprudencia legislación justicia legaltech",
        "abogada": "derecho jurisprudencia legislación justicia legaltech",
        "derecho": "derecho jurisprudencia legislación justicia legaltech",
        "diseñador": "UX UI design technology",
        "diseñadora": "UX UI design technology",
        "marketing": "marketing digital publicidad negocios",
        "docente": "educación tecnología innovación enseñanza",
        "profesor": "educación tecnología innovación enseñanza",
        "profesora": "educación tecnología innovación enseñanza",
        "médico": "medicina salud tecnología innovación",
        "medico": "medicina salud tecnología innovación",
        "médica": "medicina salud tecnología innovación",
        "arquitecto": "arquitectura construcción diseño tecnología",
        "arquitecta": "arquitectura construcción diseño tecnología",
        "contador": "contabilidad finanzas impuestos tecnología",
        "contadora": "contabilidad finanzas impuestos tecnología",
        "periodista": "periodismo medios comunicación tecnología",
        "psicologo": "psicología salud investigación",
        "psicóloga": "psicología salud investigación",
        "ux": "UX UI diseño experiencia de usuario",
        "ui": "UX UI diseño interfaces",
    }

    for palabra, busqueda in categorias.items():

        if palabra in profesion:
            return busqueda

    return f'"{profesion}"'


# ============================================================
# OBTENER NOTICIAS
# ============================================================

def obtener_noticias(profesion):

    if not profesion or not profesion.strip():

        return """
## Noticias de tu profesión

Ingresá primero tu profesión u ocupación.
"""

    busqueda = construir_busqueda(profesion)

    query = urllib.parse.quote(busqueda)

    url = GOOGLE_NEWS_URL.format(query)

    try:

        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        with urllib.request.urlopen(
            request,
            timeout=10
        ) as respuesta:

            contenido = respuesta.read()

        root = ET.fromstring(contenido)

        noticias = root.findall(".//item")

        if not noticias:

            return f"""
## Noticias de {profesion.title()}

No encontramos noticias recientes para esta profesión.
"""

        resultado = f"""
## Actualidad profesional

### Noticias sobre {profesion.title()}

"""

        contador = 0

        for noticia in noticias:

            if contador >= 6:
                break

            titulo = noticia.findtext(
                "title",
                "Sin título"
            )

            enlace = noticia.findtext(
                "link",
                "#"
            )

            descripcion = noticia.findtext(
                "description",
                ""
            )

            fecha = noticia.findtext(
                "pubDate",
                ""
            )

            # ------------------------------------------------
            # FECHA
            # ------------------------------------------------

            fecha_formateada = ""

            if fecha:

                try:

                    fecha_dt = parsedate_to_datetime(fecha)

                    fecha_formateada = fecha_dt.strftime(
                        "%d/%m/%Y · %H:%M"
                    )

                except Exception:

                    fecha_formateada = fecha

            # ------------------------------------------------
            # LIMPIAR DESCRIPCIÓN
            # ------------------------------------------------

            descripcion = (
                descripcion
                .replace("<![CDATA[", "")
                .replace("]]>", "")
            )

            # ------------------------------------------------
            # NOTICIA
            # ------------------------------------------------

            resultado += f"""
### [{titulo}]({enlace})

{descripcion}

<span class="fecha-noticia">{fecha_formateada}</span>

---
"""

            contador += 1

        return resultado

    except Exception:

        return """
## Actualidad profesional

No pudimos cargar las noticias en este momento.

Intentá nuevamente con **Actualizar noticias**.
"""


# ============================================================
# GENERAR PERFIL
# ============================================================

def generar_perfil(
    nombre,
    edad,
    profesion,
    pais
):

    if not nombre.strip():

        return """
# Falta tu nombre

Ingresá tu nombre para generar tu perfil.
""", obtener_noticias("")

    if not profesion.strip():

        return """
# Falta tu profesión

Ingresá tu profesión u ocupación para personalizar
tu perfil y las noticias.
""", obtener_noticias("")

    # --------------------------------------------------------
    # CATEGORÍA
    # --------------------------------------------------------

    if edad < 18:

        categoria = "Etapa inicial"

    elif edad < 30:

        categoria = "Joven profesional"

    elif edad < 60:

        categoria = "Profesional"

    else:

        categoria = "Profesional senior"

    # --------------------------------------------------------
    # INFORME
    # --------------------------------------------------------

    informe = f"""
# Hola, {nombre}

Tu perfil profesional fue generado correctamente.

## Perfil profesional

**Nombre**

{nombre}

**Edad**

{edad} años

**Profesión / ocupación**

{profesion}

**País**

{pais}

**Etapa**

{categoria}

---

## Sobre tu perfil

Tu actividad profesional está relacionada con
**{profesion}**.

A partir de esta información seleccionamos
contenido y noticias relevantes para tu área.
"""

    noticias = obtener_noticias(profesion)

    return informe, noticias


# ============================================================
# LIMPIAR
# ============================================================

def limpiar():

    return (
        "",
        25,
        "",
        "Argentina",

        """
# Tu perfil

Completá tus datos para comenzar.
""",

        """
# Actualidad profesional

Las noticias relacionadas con tu profesión
aparecerán acá.
"""
    )


# ============================================================
# CSS
# ============================================================

css = """

/* ============================================================
   VARIABLES DE COLOR
   ============================================================ */

:root {

    --fondo: #f2f2f2;
    --gris-formulario: #e8e8e8;
    --blanco: #ffffff;
    --negro: #000000;
    --texto: #212121;
    --gris-texto: #555555;
    --gris-medio: #888888;
    --gris-borde: #bdbdbd;
}


/* ============================================================
   FONDO GENERAL
   ============================================================ */

html,
body {

    background: #f2f2f2 !important;

    color: #111111 !important;

    min-height: 100vh !important;
}


body {

    margin: 0 !important;
}


.gradio-container {

    max-width: 1180px !important;

    margin: 0 auto !important;

    padding: 25px 45px 50px !important;

    background: #f2f2f2 !important;
}


/* ============================================================
   FORZAR FONDO GRIS DE GRADIO
   ============================================================ */

.gradio-container,
.gradio-container > div,
.gradio-container .main,
.gradio-container .contain {

    background: #f2f2f2 !important;
}


/* Evitar colores azulados del tema */

.gradio-container {

    --body-background-fill: #f2f2f2 !important;

    --background-fill-primary: #f2f2f2 !important;

    --background-fill-secondary: #e8e8e8 !important;

    --block-background-fill: #f2f2f2 !important;

    --panel-background-fill: #f2f2f2 !important;

    --border-color-primary: #bdbdbd !important;

    --border-color-accent: #111111 !important;

    --color-accent: #111111 !important;
}


/* ============================================================
   HERO
   ============================================================ */

.hero {

    padding: 35px 0 35px !important;

    border-bottom: 2px solid #111111 !important;
}


.hero h1 {

    font-size: clamp(58px, 9vw, 110px) !important;

    line-height: 0.86 !important;

    letter-spacing: -6px !important;

    font-weight: 900 !important;

    color: #000000 !important;

    margin: 0 0 22px !important;
}


/* CAMBIO 1: COLOR DEL SUBTÍTULO */

.hero-subtitle,
.hero-subtitle * {

    max-width: 650px !important;

    font-size: 18px !important;

    line-height: 1.5 !important;

    color: #111111 !important;
}


/* ============================================================
   TÍTULOS
   ============================================================ */

h1 {

    color: #000000 !important;

    font-weight: 800 !important;

    letter-spacing: -2px !important;
}


h2 {

    color: #111111 !important;

    font-weight: 750 !important;
}


h3 {

    color: #222222 !important;
}


/* ============================================================
   SECCIONES
   ============================================================ */

.section-title {

    font-size: 12px !important;

    text-transform: uppercase !important;

    letter-spacing: 2px !important;

    color: #666666 !important;
}


/* ============================================================
   FORMULARIO
   ============================================================ */

.form-section {

    background: #e8e8e8 !important;

    padding: 25px !important;

    margin: 10px 0 20px !important;

    border-radius: 0 !important;

    border: none !important;

    box-shadow: none !important;
}


label {

    color: #222222 !important;

    font-size: 12px !important;

    font-weight: 700 !important;

    text-transform: uppercase !important;

    letter-spacing: 1px !important;
}


/* ============================================================
   INPUTS
   ============================================================ */

input,
textarea {

    background: #ffffff !important;

    color: #111111 !important;

    border: 1px solid #999999 !important;

    border-radius: 0 !important;

    box-shadow: none !important;
}


input:focus,
textarea:focus {

    border-color: #111111 !important;

    box-shadow: none !important;
}


/* ============================================================
   DROPDOWN
   ============================================================ */

.gradio-dropdown {

    background: #ffffff !important;

    border: 1px solid #999999 !important;

    border-radius: 0 !important;

    box-shadow: none !important;
}


/* ============================================================
   SLIDER
   ============================================================ */

input[type="range"] {

    accent-color: #111111 !important;
}


/* ============================================================
   BOTONES
   ============================================================ */

button {

    border-radius: 0 !important;

    min-height: 46px !important;

    box-shadow: none !important;

    font-weight: 700 !important;

    letter-spacing: 1px !important;

    text-transform: uppercase !important;
}


button.primary {

    background: #000000 !important;

    color: #ffffff !important;

    border: 1px solid #000000 !important;
}


button.primary:hover {

    background: #333333 !important;
}


button.secondary {

    background: #ffffff !important;

    color: #111111 !important;

    border: 1px solid #111111 !important;
}


button.secondary:hover {

    background: #e8e8e8 !important;
}


/* ============================================================
   RESULTADO
   ============================================================ */

.resultado {

    background: transparent !important;

    border: none !important;

    box-shadow: none !important;

    padding: 0 !important;

    margin: 0 !important;
}


.resultado h1 {

    font-size: 48px !important;

    line-height: 0.95 !important;

    margin: 0 0 15px !important;
}


.resultado h2 {

    font-size: 25px !important;

    margin: 22px 0 8px !important;
}


.resultado p {

    margin: 5px 0 !important;

    line-height: 1.45 !important;
}


/* ============================================================
   CAMBIO 2: TODO EL TEXTO DEL RESULTADO EN NEGRO
   ============================================================ */

.resultado,
.resultado *,
.resultado .prose,
.resultado .prose * {

    color: #000000 !important;
}


.resultado p {

    color: #000000 !important;
}


.resultado h1,
.resultado h2,
.resultado h3 {

    color: #000000 !important;
}


.resultado strong {

    color: #000000 !important;
}


/* ============================================================
   NOTICIAS
   ============================================================ */

.noticias {

    background: transparent !important;

    border: none !important;

    box-shadow: none !important;

    padding: 0 !important;

    margin: 0 !important;
}


.noticias h2 {

    font-size: 12px !important;

    text-transform: uppercase !important;

    letter-spacing: 2px !important;

    color: #666666 !important;

    margin: 0 0 5px !important;
}


.noticias h3 {

    font-size: 21px !important;

    line-height: 1.15 !important;

    margin: 16px 0 5px !important;
}


.noticias p {

    line-height: 1.4 !important;

    margin: 5px 0 !important;
}


.noticias a {

    color: #111111 !important;

    text-decoration: none !important;

    border-bottom: 1px solid #111111 !important;
}


.noticias a:hover {

    color: #666666 !important;

    border-color: #666666 !important;
}


.fecha-noticia {

    color: #888888 !important;

    font-size: 11px !important;

    letter-spacing: 1px !important;
}


/* ============================================================
   SEPARADORES
   ============================================================ */

hr {

    border: none !important;

    border-top: 1px solid #bdbdbd !important;

    margin: 25px 0 !important;
}


/* ============================================================
   MARKDOWN
   ============================================================ */

.prose {

    color: #222222 !important;

    background: transparent !important;
}


.prose strong {

    color: #000000 !important;
}


/* ============================================================
   ELIMINAR ESTILO DE TARJETAS
   ============================================================ */

.block,
.panel,
.wrap {

    box-shadow: none !important;
}


.block {

    border-color: transparent !important;

    background: transparent !important;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer-text {

    padding-top: 25px !important;

    color: #888888 !important;

    font-size: 10px !important;

    letter-spacing: 1px !important;

    text-transform: uppercase !important;
}


/* ============================================================
   RESPONSIVE
   ============================================================ */

@media (max-width: 700px) {

    .gradio-container {

        padding: 20px !important;
    }

    .hero h1 {

        font-size: 60px !important;

        letter-spacing: -4px !important;
    }

    .hero-subtitle {

        font-size: 16px !important;
    }

    .resultado h1 {

        font-size: 38px !important;
    }
}

"""


# ============================================================
# INTERFAZ
# ============================================================

with gr.Blocks(

    title="Perfil Profesional",

    theme=gr.themes.Base(
        primary_hue="gray",
        secondary_hue="gray",
        neutral_hue="gray"
    ),

    css=css

) as demo:


    # ========================================================
    # HERO
    # ========================================================

    gr.Markdown(
        """
<div class="hero">

<h1>
PERFIL<br>
PROFESIONAL
</h1>

<div class="hero-subtitle">

Conocé tu perfil y descubrí qué está pasando
en tu área profesional.

Completá tus datos y generá una experiencia
personalizada.

</div>

</div>
"""
    )


    # ========================================================
    # DATOS
    # ========================================================

    gr.Markdown(
        """
## Comenzá acá

Contanos un poco sobre vos.
"""
    )


    with gr.Row(elem_classes="form-section"):

        with gr.Column():

            nombre = gr.Textbox(
                label="Nombre",
                placeholder="Ej. Gabriela"
            )

            profesion = gr.Textbox(
                label="Profesión u ocupación",
                placeholder="Ej. Developer"
            )

        with gr.Column():

            edad = gr.Slider(
                minimum=1,
                maximum=100,
                value=25,
                step=1,
                label="Edad"
            )

            pais = gr.Dropdown(
                choices=[
                    "Argentina",
                    "Brasil",
                    "Chile",
                    "Uruguay",
                    "Paraguay",
                    "México",
                    "España",
                    "Otro"
                ],
                value="Argentina",
                label="País"
            )


    # ========================================================
    # BOTONES
    # ========================================================

    with gr.Row():

        boton_generar = gr.Button(
            "GENERAR MI PERFIL",
            variant="primary"
        )

        boton_limpiar = gr.Button(
            "LIMPIAR",
            variant="secondary"
        )


    # ========================================================
    # RESULTADO
    # ========================================================

    gr.Markdown("---")


    salida = gr.Markdown(
        """
# Tu perfil

Completá tus datos para comenzar.
""",
        elem_classes="resultado"
    )


    # ========================================================
    # NOTICIAS
    # ========================================================

    gr.Markdown("---")


    noticias = gr.Markdown(
        """
# Actualidad profesional

Las noticias relacionadas con tu profesión
aparecerán acá.
""",
        elem_classes="noticias"
    )


    boton_noticias = gr.Button(
        "ACTUALIZAR NOTICIAS"
    )


    # ========================================================
    # FOOTER
    # ========================================================

    gr.Markdown(
        """
<div class="footer-text">

PERFIL PROFESIONAL · PYTHON + GRADIO

</div>
"""
    )


    # ========================================================
    # EVENTOS
    # ========================================================

    boton_generar.click(

        fn=generar_perfil,

        inputs=[
            nombre,
            edad,
            profesion,
            pais
        ],

        outputs=[
            salida,
            noticias
        ]
    )


    boton_noticias.click(

        fn=obtener_noticias,

        inputs=profesion,

        outputs=noticias
    )


    boton_limpiar.click(

        fn=limpiar,

        inputs=[],

        outputs=[
            nombre,
            edad,
            profesion,
            pais,
            salida,
            noticias
        ]
    )


# ============================================================
# EJECUTAR
# ============================================================

if __name__ == "__main__":

    demo.launch()