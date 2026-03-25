# ============================================================
# CHASIDE • App completa con Módulo de Desviación Intrapersona
# ============================================================
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -----------------------
# Estilos y constantes UI
# -----------------------
PRIMARY = "#0F766E"
ACCENT = "#14B8A6"
MUTED = "#64748B"
SLATE = "#475569"

GREEN = "#22c55e"
AMBER = "#f59e0b"
RED = "#ef4444"
GRAY = "#6b7280"
LIGHT_GRAY = "#94a3b8"
BLUE = "#3b82f6"

AREAS = ["C", "H", "A", "S", "I", "D", "E"]

CAT_INT_TO_UI = {
    "Verde": "Elección de perfil correcto",
    "Amarillo": "Elección de perfil incorrecto",
    "Rojo": "No tiene un área predominante",
    "No aceptable": "Respondió al azar",
    "Sin sugerencia": "No tiene un área predominante",
}

CAT_UI_ORDER = [
    "Elección de perfil correcto",
    "Elección de perfil incorrecto",
    "No tiene un área predominante",
    "Respondió al azar",
]

CAT_UI_COLORS = {
    "Elección de perfil correcto": GREEN,
    "Elección de perfil incorrecto": AMBER,
    "No tiene un área predominante": LIGHT_GRAY,
    "Respondió al azar": RED,
}

DESC_CHASIDE = {
    "C": "Organización, supervisión, orden, análisis y síntesis, colaboración, cálculo.",
    "H": "Precisión verbal, organización, relación de hechos, justicia, persuasión.",
    "A": "Estético y creativo; detallista, innovador, intuitivo; habilidades visuales, auditivas y manuales.",
    "S": "Asistir y ayudar; investigación, precisión, percepción, análisis; altruismo y paciencia.",
    "I": "Cálculo y pensamiento científico/crítico; exactitud, planificación; enfoque práctico.",
    "D": "Justicia y equidad; colaboración, liderazgo; valentía y toma de decisiones.",
    "E": "Investigación; orden, análisis y síntesis; cálculo numérico, observación; método y seguridad.",
}

AREAS_LONG = {
    "C": "C = Administrativo",
    "H": "H = Humanidades y Sociales",
    "A": "A = Artístico",
    "S": "S = Ciencias de la Salud",
    "I": "I = Enseñanzas Técnicas",
    "D": "D = Defensa y Seguridad",
    "E": "E = Ciencias Experimentales",
}

INTERESES_ITEMS = {
    "C": [1, 12, 20, 53, 64, 71, 78, 85, 91, 98],
    "H": [9, 25, 34, 41, 56, 67, 74, 80, 89, 95],
    "A": [3, 11, 21, 28, 36, 45, 50, 57, 81, 96],
    "S": [8, 16, 23, 33, 44, 52, 62, 70, 87, 92],
    "I": [6, 19, 27, 38, 47, 54, 60, 75, 83, 97],
    "D": [5, 14, 24, 31, 37, 48, 58, 65, 73, 84],
    "E": [17, 32, 35, 42, 49, 61, 68, 77, 88, 93],
}

APTITUDES_ITEMS = {
    "C": [2, 15, 46, 51],
    "H": [30, 63, 72, 86],
    "A": [22, 39, 76, 82],
    "S": [4, 29, 40, 69],
    "I": [10, 26, 59, 90],
    "D": [13, 18, 43, 66],
    "E": [7, 55, 79, 94],
}

PERFIL_CARRERAS = {
    "Arquitectura": {"Fuerte": ["A", "I", "C"]},
    "Contador Público": {"Fuerte": ["C", "D"]},
    "Licenciatura en Administración": {"Fuerte": ["C", "D"]},
    "Ingeniería Ambiental": {"Fuerte": ["I", "C", "E"]},
    "Ingeniería Bioquímica": {"Fuerte": ["I", "C", "E"]},
    "Ingeniería en Gestión Empresarial": {"Fuerte": ["C", "D", "H"]},
    "Ingeniería Industrial": {"Fuerte": ["C", "D", "H"]},
    "Ingeniería en Inteligencia Artificial": {"Fuerte": ["I", "E"]},
    "Ingeniería Mecatrónica": {"Fuerte": ["I", "E"]},
    "Ingeniería en Sistemas Computacionales": {"Fuerte": ["I", "E"]},
}

# -----------------------
# Config de página
# -----------------------
st.set_page_config(page_title="CHASIDE • App", layout="wide")

st.markdown(
    f"""
<style>
.block-container {{ padding-top: 1.0rem; padding-bottom: 2rem; }}
.h1-title {{ font-size: 2.0rem; font-weight: 800; color: {PRIMARY}; margin-bottom: .25rem; }}
.subtitle {{ color: {MUTED}; margin-bottom: 1rem; }}
.section-title {{ font-weight: 700; font-size: 1.1rem; margin: 1rem 0 .35rem 0; color: {PRIMARY}; }}
.card {{ border: 1px solid #e5e7eb; border-radius: 14px; padding: 14px 16px; background: #ffffff; box-shadow: 0 2px 8px rgba(0,0,0,.04); }}
.badge {{ display:inline-block; padding: 4px 10px; border-radius: 999px; font-weight:700; font-size:.85rem; background: rgba(20,184,166,0.12); color:{PRIMARY}; }}
.puv {{ border-left: 6px solid {ACCENT}; padding: 12px 14px; background: #f8fffd; border-radius: 10px; font-size: 1.02rem; }}
.kpi {{ font-size: 1.02rem; }}
.kpi b {{ color: {SLATE}; }}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# Lógica de Procesamiento
# ============================================================

@st.cache_data(show_spinner=False)
def load_csv(url: str) -> pd.DataFrame:
    df = pd.read_csv(url)
    df.columns = [str(c) for c in df.columns]
    return df

@st.cache_data(show_spinner=False)
def process_chaside(df_raw: pd.DataFrame):
    df = df_raw.copy()
    columna_carrera = "¿A qué carrera desea ingresar?"
    columna_nombre = "Ingrese su nombre completo"

    if columna_carrera not in df.columns or columna_nombre not in df.columns:
        raise ValueError("Columnas faltantes en el CSV.")

    df[columna_carrera] = df[columna_carrera].astype(str)
    df[columna_nombre] = df[columna_nombre].astype(str)

    columnas_items = df.columns[5:103]
    df_items = (
        df[columnas_items].astype(str).apply(lambda c: c.str.strip().str.lower())
        .replace({"sí": 1, "si": 1, "s": 1, "1": 1, "no": 0, "n": 0, "0": 0, "nan": 0})
        .apply(pd.to_numeric, errors="coerce").fillna(0).astype(int)
    )
    df[columnas_items] = df_items

    def col_item(i: int) -> str:
        return columnas_items[i - 1]

    for a in AREAS:
        df[f"INTERES_{a}"] = df[[col_item(i) for i in INTERESES_ITEMS[a]]].sum(axis=1)
        df[f"APTITUD_{a}"] = df[[col_item(i) for i in APTITUDES_ITEMS[a]]].sum(axis=1)

    # --- CAMBIO: Desviación Intrapersona ---
    cols_intereses = [f"INTERES_{a}" for a in AREAS]
    df["Desviacion_Intrapersona"] = df[cols_intereses].std(axis=1)
    # Si la desviación < 1.0 (10% de la escala de 10), se asume azar/monotonía
    df["Informacion_No_Aceptable"] = df["Desviacion_Intrapersona"] < 1.0 

    peso_intereses, peso_aptitudes = 0.8, 0.2
    for a in AREAS:
        df[f"PUNTAJE_COMBINADO_{a}"] = (df[f"INTERES_{a}"] * peso_intereses + df[f"APTITUD_{a}"] * peso_aptitudes)
        df[f"TOTAL_{a}"] = df[f"INTERES_{a}"] + df[f"APTITUD_{a}"]

    df["Area_Fuerte_Ponderada"] = df.apply(lambda r: max(AREAS, key=lambda a: r[f"PUNTAJE_COMBINADO_{a}"]), axis=1)
    df["Score"] = df[[f"PUNTAJE_COMBINADO_{a}" for a in AREAS]].max(axis=1)

    def evaluar(area_chaside, carrera):
        perfil = PERFIL_CARRERAS.get(str(carrera).strip())
        if not perfil: return "Sin perfil definido"
        return "Coherente" if area_chaside in perfil.get("Fuerte", []) else "Neutral"

    df["Coincidencia_Ponderada"] = df.apply(lambda r: evaluar(r["Area_Fuerte_Ponderada"], r[columna_carrera]), axis=1)

    def carrera_mejor(r):
        if r["Informacion_No_Aceptable"]: return "Información no aceptable"
        a = r["Area_Fuerte_Ponderada"]
        c_actual = str(r[columna_carrera]).strip()
        sugeridas = [c for c, p in PERFIL_CARRERAS.items() if a in p.get("Fuerte", [])]
        return c_actual if c_actual in sugeridas else (", ".join(sugeridas) if sugeridas else "Sin sugerencia clara")

    df["Carrera_Mejor_Perfilada"] = df.apply(carrera_mejor, axis=1)

    def semaforo(r):
        if r["Carrera_Mejor_Perfilada"] == "Información no aceptable": return "No aceptable"
        if r["Carrera_Mejor_Perfilada"] == "Sin sugerencia clara": return "Sin sugerencia"
        return "Verde" if r["Coincidencia_Ponderada"] == "Coherente" else "Amarillo"

    df["Semáforo Vocacional"] = df.apply(semaforo, axis=1)
    df["Categoría_UI"] = df["Semáforo Vocacional"].map(CAT_INT_TO_UI).fillna("No tiene un área predominante")
    df["Categoría_UI"] = pd.Categorical(df["Categoría_UI"], categories=CAT_UI_ORDER, ordered=True)

    return df, columna_carrera, columna_nombre

# ============================================================
# Módulos de Renderizado (Simplificados para brevedad)
# ============================================================

def render_presentacion():
    st.markdown('<div class="h1-title">Diagnóstico Vocacional – Escala CHASIDE</div>', unsafe_allow_html=True)
    st.markdown('<div class="puv">Orientación vocacional personalizada basada en desviación intrapersona para asegurar calidad de datos.</div>', unsafe_allow_html=True)

def render_info_general(df, columna_carrera):
    st.header("Distribución General")
    fig = px.pie(df, names="Categoría_UI", color="Categoría_UI", color_discrete_map=CAT_UI_COLORS, hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

def render_info_individual(df, columna_carrera, columna_nombre):
    nombre = st.selectbox("Seleccione Estudiante:", df[columna_nombre].unique())
    al = df[df[columna_nombre] == nombre].iloc[0]
    st.metric("Resultado", al["Categoría_UI"])
    st.write(f"Desviación Intrapersona: {al['Desviacion_Intrapersona']:.2f}")

def main():
    st.sidebar.title("Navegación")
    modulo = st.sidebar.radio("Ir a:", ["Presentación", "General", "Individual"])
    url = st.sidebar.text_input("URL CSV:", "https://docs.google.com/spreadsheets/d/1BNAeOSj2F378vcJE5-T8iJ8hvoseOleOHr-I7mVfYu4/export?format=csv")

    try:
        df_raw = load_csv(url)
        df_proc, col_c, col_n = process_chaside(df_raw)
        if modulo == "Presentación": render_presentacion()
        elif modulo == "General": render_info_general(df_proc, col_c)
        elif modulo == "Individual": render_info_individual(df_proc, col_c, col_n)
    except Exception as e:
        st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
