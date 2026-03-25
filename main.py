# ============================
# MÓDULO 1 · PRESENTACIÓN
# ============================

import streamlit as st

# ---------- estilos ----------
PRIMARY = "#0F766E"
ACCENT = "#14B8A6"
MUTED = "#64748B"

st.set_page_config(page_title="Presentación • CHASIDE", layout="centered")

st.markdown(f"""
<style>
.block-container {{ padding-top: 1.5rem; padding-bottom: 2.5rem; }}
.h1-title {{
  font-size: 2.0rem; font-weight: 800; color: {PRIMARY}; margin-bottom: .25rem;
}}
.subtitle {{ color: {MUTED}; margin-bottom: 1.25rem; }}
.section-title {{
  font-weight: 700; font-size: 1.1rem; margin: 1.2rem 0 .2rem 0; color: {PRIMARY};
}}
.card {{
  border: 1px solid #e5e7eb; border-radius: 16px; padding: 16px 18px;
  background: #ffffff; box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}}
.puv {{
  border-left: 6px solid {ACCENT}; padding: 12px 14px; background: #f8fffd;
  border-radius: 10px; font-size: 1.02rem;
}}
</style>
""", unsafe_allow_html=True)


def render_presentacion():
    st.markdown(
        '<div class="h1-title">Diagnóstico Vocacional – Escala CHASIDE</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="subtitle">Aplicación de apoyo a la elección de carrera universitaria</div>',
        unsafe_allow_html=True
    )

    # Autores e institución
    st.markdown('<div class="section-title">Autores e institución</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1.2])

    with col1:
        st.markdown("""
<div class="card">
<b>Autores</b><br>
• Dra. Elena Elsa Bricio Barrios<br>
• Dr. Santiago Arceo-Díaz<br>
• Psic. Martha Cecilia Ramírez Guzmán
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div class="card">
<b>Institución</b><br>
Tecnológico Nacional de México<br>
Instituto Tecnológico de Colima
</div>
""", unsafe_allow_html=True)

    # Objetivo
    st.markdown('<div class="section-title">¿Qué pretende esta aplicación?</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="card">
Esta herramienta orienta a estudiantes de bachillerato en el <b>descubrimiento de sus intereses y aptitudes</b>,
para apoyar una <b>elección de carrera informada y alineada</b> con sus fortalezas y aspiraciones.
Integra resultados de la escala CHASIDE y los presenta de forma clara para estudiantes, familias y docentes.
</div>
""", unsafe_allow_html=True)

    # Madurez y personalidad
    st.markdown('<div class="section-title">Madurez y personalidad en el bachillerato</div>', unsafe_allow_html=True)
    st.markdown("""
La <b>personalidad</b> se encuentra en pleno desarrollo durante el bachillerato. La <b>madurez</b> permite al joven
empezar a definirse y reflexionar sobre su proyecto de vida, pero el proceso <b>aún está en construcción</b>.
En esta etapa es clave contar con <b>herramientas de orientación</b> que acompañen la toma de decisiones académicas.
""", unsafe_allow_html=True)

    # Intereses y aptitudes
    st.markdown('<div class="section-title">Intereses y aptitudes: base de la formación académica</div>', unsafe_allow_html=True)
    st.markdown("""
Reconocer <b>lo que me interesa</b> y <b>para lo que tengo aptitud</b> ayuda a dirigir el esfuerzo,
sostener la motivación y <b>reducir el riesgo de abandono o frustración</b>. Estos factores son
determinantes para <b>persistir y desempeñarse</b> durante la vida universitaria.
""", unsafe_allow_html=True)

    # Escala CHASIDE
    st.markdown('<div class="section-title">¿Qué es la escala CHASIDE?</div>', unsafe_allow_html=True)
    st.markdown("""
<b>CHASIDE</b> es una escala vocacional que integra <b>intereses</b> y <b>aptitudes</b> en siete áreas:

- <b>C</b> – Área Administrativa  
- <b>H</b> – Humanidades y Ciencias Sociales  
- <b>A</b> – Área Artística  
- <b>S</b> – Ciencias de la Salud  
- <b>I</b> – Enseñanzas Técnicas  
- <b>D</b> – Defensa y Seguridad  
- <b>E</b> – Ciencias Experimentales  

<b>Características generales:</b> aplicación rápida, reactivos tipo sí/no, interpretación sencilla y
enfoque práctico para vincular resultados con opciones de carrera.
""", unsafe_allow_html=True)

    # PUV
    st.markdown('<div class="section-title">Propuesta Única de Valor (PUV)</div>', unsafe_allow_html=True)
    st.markdown(f"""
<div class="puv">
<b>Orientación vocacional personalizada</b>, basada en evidencia (CHASIDE),
con visualizaciones claras y reportes descargables para que los estudiantes identifiquen sus fortalezas
y las instituciones cuenten con insumos objetivos para el acompañamiento académico.
</div>
""", unsafe_allow_html=True)


if __name__ == "__main__":
    render_presentacion()
