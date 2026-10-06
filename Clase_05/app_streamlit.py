
import streamlit as st
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime


GOOGLE_NEWS_URL = (
    "https://news.google.com/rss/search?"
    "q={}&hl=es-419&gl=AR&ceid=AR:es-419"
)


def construir_busqueda(profesion):
    profesion = profesion.lower().strip()

    categorias = {
        "developer": "software development programming technology artificial intelligence",
        "desarrollador": "software development programming technology artificial intelligence",
        "programador": "programming software development technology AI",
        "data scientist": "data science machine learning artificial intelligence",
        "cientifico de datos": "data science machine learning artificial intelligence",
        "ingeniero": "engineering technology innovation",
        "abogado": "derecho jurisprudencia legislación justicia legaltech",
        "diseñador": "UX UI design technology",
        "marketing": "marketing digital publicidad negocios",
        "docente": "educación tecnología innovación enseñanza",
        "médico": "medicina salud tecnología innovación",
    }

    for palabra, busqueda in categorias.items():
        if palabra in profesion:
            return busqueda

    return f'"{profesion}"'


def obtener_noticias(profesion):

    if not profesion.strip():
        return []

    busqueda = construir_busqueda(profesion)
    query = urllib.parse.quote(busqueda)
    url = GOOGLE_NEWS_URL.format(query)

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        with urllib.request.urlopen(request, timeout=10) as respuesta:
            contenido = respuesta.read()

        root = ET.fromstring(contenido)
        noticias = root.findall(".//item")

        resultado = []

        for noticia in noticias[:6]:

            titulo = noticia.findtext(
                "title",
                "Sin título"
            )

            enlace = noticia.findtext(
                "link",
                "#"
            )

            fecha = noticia.findtext(
                "pubDate",
                ""
            )

            fecha_formateada = fecha

            if fecha:
                try:
                    fecha_dt = parsedate_to_datetime(fecha)
                    fecha_formateada = fecha_dt.strftime(
                        "%d/%m/%Y · %H:%M"
                    )
                except Exception:
                    pass

            resultado.append(
                {
                    "titulo": titulo,
                    "enlace": enlace,
                    "fecha": fecha_formateada
                }
            )

        return resultado

    except Exception:
        return []


# -----------------------------
# CONFIGURACIÓN DE PÁGINA
# -----------------------------

st.set_page_config(
    page_title="Perfil Profesional",
    page_icon="💼",
    layout="centered"
)


# -----------------------------
# ESTILOS
# -----------------------------

st.markdown(
    """
    <style>

    /* Fondo general */
    .stApp {
        background-color: #F5F5F5;
        color: #111111;
    }

    /* Contenedor principal */
    .block-container {
        max-width: 850px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    /* Títulos */
    h1 {
        color: #111111 !important;
        font-weight: 800 !important;
        letter-spacing: -1px;
    }

    h2, h3 {
        color: #222222 !important;
        font-weight: 700 !important;
    }

    p, label {
        color: #333333 !important;
    }

    /* Inputs */
    input {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border: 1px solid #BDBDBD !important;
        border-radius: 8px !important;
    }

    /* Selectbox */
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border: 1px solid #BDBDBD !important;
        border-radius: 8px !important;
    }

    /* Slider */
    div[data-baseweb="slider"] {
        color: #111111 !important;
    }

    /* Botón */
    .stButton > button {
        width: 100%;
        background-color: #111111 !important;
        color: #FFFFFF !important;
        border: 1px solid #111111 !important;
        border-radius: 8px !important;
        padding: 0.65rem 1rem !important;
        font-weight: 700 !important;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        background-color: #333333 !important;
        border-color: #333333 !important;
        color: #FFFFFF !important;
    }

    /* Línea divisoria */
    hr {
        border-color: #D0D0D0 !important;
    }

    /* Links de noticias */
    a {
        color: #222222 !important;
        text-decoration: none !important;
    }

    a:hover {
        color: #000000 !important;
        text-decoration: underline !important;
    }

    /* Fecha de noticias */
    .stCaption {
        color: #777777 !important;
    }

    /* Alertas */
    div[data-testid="stAlert"] {
        background-color: #EAEAEA !important;
        color: #222222 !important;
        border: 1px solid #CFCFCF !important;
    }

    /* Ocultar elementos innecesarios de Streamlit */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# INTERFAZ
# -----------------------------

st.title("PERFIL PROFESIONAL")

st.write(
    "Conocé tu perfil y descubrí qué está pasando "
    "en tu área profesional."
)

st.subheader("Comenzá acá")

nombre = st.text_input(
    "Nombre",
    placeholder="Ej. Gabriela"
)

profesion = st.text_input(
    "Profesión u ocupación",
    placeholder="Ej. Developer"
)

edad = st.slider(
    "Edad",
    min_value=1,
    max_value=100,
    value=25
)

pais = st.selectbox(
    "País",
    [
        "Argentina",
        "Brasil",
        "Chile",
        "Uruguay",
        "Paraguay",
        "México",
        "España",
        "Otro"
    ]
)


if st.button("GENERAR MI PERFIL"):

    if not nombre.strip():
        st.warning("Ingresá tu nombre.")

    elif not profesion.strip():
        st.warning("Ingresá tu profesión u ocupación.")

    else:

        if edad < 18:
            categoria = "Etapa inicial"
        elif edad < 30:
            categoria = "Joven profesional"
        elif edad < 60:
            categoria = "Profesional"
        else:
            categoria = "Profesional senior"

        st.divider()

        st.header(f"Hola, {nombre}")

        st.subheader("Perfil profesional")

        st.write(f"**Nombre:** {nombre}")
        st.write(f"**Edad:** {edad} años")
        st.write(f"**Profesión / ocupación:** {profesion}")
        st.write(f"**País:** {pais}")
        st.write(f"**Etapa:** {categoria}")

        st.divider()

        st.subheader("Actualidad profesional")

        noticias = obtener_noticias(profesion)

        if noticias:

            for noticia in noticias:

                st.markdown(
                    f"### [{noticia['titulo']}]"
                    f"({noticia['enlace']})"
                )

                st.caption(noticia["fecha"])

        else:

            st.info(
                "No pudimos cargar noticias en este momento."
            )
