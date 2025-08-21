# ============================
# MÓDULO 1 · PRESENTACIÓN
# ============================
# Uso:
#   - Standalone:  streamlit run presentacion.py
#   - Integrado:   from presentacion import render_presentacion; render_presentacion()

import streamlit as st

# ---------- estilos (ligeros) ----------
PRIMARY = "#0F766E"      # teal-700
ACCENT  = "#14B8A6"      # teal-400
MUTED   = "#64748B"      # slate-500

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
.badge {{
  display:inline-block; padding: 4px 10px; border-radius: 999px;
  background: rgba(20,184,166,0.12); color:{PRIMARY}; font-weight: 600;
}}
.puv {{
  border-left: 6px solid {ACCENT}; padding: 12px 14px; background: #f8fffd;
  border-radius: 10px; font-size: 1.02rem;
}}
</style>
""", unsafe_allow_html=True)


def render_presentacion():
    # título
    st.markdown('<div class="h1-title">Diagnóstico Vocacional – Escala CHASIDE</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Aplicación de apoyo a la elección de carrera universitaria</div>', unsafe_allow_html=True)

    # autores e institución
    with st.container():
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
            st.markdown(f"""
<div class="card">
<b>Institución</b><br>
Tecnológico Nacional de México<br>
Instituto Tecnológico de Colima
</div>
            """, unsafe_allow_html=True)

    # objetivo de la aplicación
    st.markdown('<div class="section-title">¿Qué pretende esta aplicación?</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="card">
Esta herramienta orienta a estudiantes de bachillerato en el **descubrimiento de sus intereses y aptitudes**,
para apoyar una **elección de carrera informada y alineada** con sus fortalezas y aspiraciones.
Integra resultados de la escala CHASIDE y los presenta de forma clara para estudiantes, familias y docentes.
</div>
""", unsafe_allow_html=True)

    # madurez y personalidad
    st.markdown('<div class="section-title">Madurez y personalidad en el bachillerato</div>', unsafe_allow_html=True)
    st.markdown("""
La **personalidad** se encuentra en pleno desarrollo durante el bachillerato. La **madurez** permite al joven
empezar a definirse y reflexionar sobre su proyecto de vida, pero el proceso **aún está en construcción**.
En esta etapa es clave contar con **herramientas de orientación** que acompañen la toma de decisiones académicas.
""")

    # importancia de intereses y aptitudes
    st.markdown('<div class="section-title">Intereses y aptitudes: base de la formación académica</div>', unsafe_allow_html=True)
    st.markdown("""
Reconocer **lo que me interesa** y **para lo que tengo aptitud** ayuda a dirigir el esfuerzo,
sostener la motivación y **reducir el riesgo de abandono o frustración**. Estos factores son
determinantes para **persistir y desempeñarse** durante la vida universitaria.
""")

    # escala CHASIDE
    st.markdown('<div class="section-title">¿Qué es la escala CHASIDE?</div>', unsafe_allow_html=True)
    st.markdown("""
**CHASIDE** es una escala vocacional que integra **intereses** y **aptitudes** en siete áreas:

- **C** – Área Administrativa  
- **H** – Humanidades y Ciencias Sociales  
- **A** – Área Artística  
- **S** – Ciencias de la Salud  
- **I** – Enseñanzas Técnicas  
- **D** – Defensa y Seguridad  
- **E** – Ciencias Experimentales  

**Características generales:** aplicación rápida, reactivos tipo sí/no, interpretación sencilla y
**enfoque práctico** para vincular resultados con opciones de carrera.
""")

    # PUV
    st.markdown('<div class="section-title">Propuesta Única de Valor (PUV)</div>', unsafe_allow_html=True)
    st.markdown(f"""
<div class="puv">
<b>Orientación vocacional personalizada</b>, basada en evidencia (CHASIDE),
con visualizaciones claras (pastel de categorías, barras apiladas por carrera, boxplots y radar),
y reportes descargables para que los estudiantes identifiquen sus fortalezas y
las escuelas cuenten con **insumos objetivos** para el acompañamiento académico.
</div>
""", unsafe_allow_html=True)

# permitir uso standalone o como módulo
if __name__ == "__main__":
    # Nota: set_page_config suele declararse una sola vez en la app completa.
    # Si lo integras luego en una app multipágina, quita esta línea.
    st.set_page_config(page_title="Presentación • CHASIDE", layout="centered")
    render_presentacion()
