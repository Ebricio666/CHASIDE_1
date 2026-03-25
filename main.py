import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def process_chaside(df_raw: pd.DataFrame):
    df = df_raw.copy()

    columna_carrera = "¿A qué carrera desea ingresar?"
    columna_nombre = "Ingrese su nombre completo"

    if columna_carrera not in df.columns or columna_nombre not in df.columns:
        raise ValueError(f"Columnas faltantes. Se requieren: '{columna_carrera}' y '{columna_nombre}'.")

    df[columna_carrera] = df[columna_carrera].astype(str)
    df[columna_nombre] = df[columna_nombre].astype(str)

    # Procesamiento de ítems (columnas 5 a 103)
    columnas_items = df.columns[5:103]
    df_items = (
        df[columnas_items]
        .astype(str)
        .apply(lambda c: c.str.strip().str.lower())
        .replace({
            "sí": 1, "si": 1, "s": 1, "1": 1, "true": 1, "verdadero": 1, "x": 1,
            "no": 0, "n": 0, "0": 0, "false": 0, "falso": 0, "": 0, "nan": 0,
        })
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0)
        .astype(int)
    )
    df[columnas_items] = df_items

    def col_item(i: int) -> str:
        return columnas_items[i - 1]

    # Intereses y aptitudes por área
    for a in AREAS:
        df[f"INTERES_{a}"] = df[[col_item(i) for i in INTERESES_ITEMS[a]]].sum(axis=1)
        df[f"APTITUD_{a}"] = df[[col_item(i) for i in APTITUDES_ITEMS[a]]].sum(axis=1)

    # ============================================================
    # NUEVO: Módulo de Desviación Intrapersona
    # ============================================================
    cols_intereses = [f"INTERES_{a}" for a in AREAS]
    df["Desviacion_Intrapersona"] = df[cols_intereses].std(axis=1)
    
    # Marcamos como no aceptable si la desviación es muy baja (monotonía/azar)
    # Un umbral de 1.0 es adecuado para detectar falta de discriminación en 10 ítems
    df["Informacion_No_Aceptable"] = df["Desviacion_Intrapersona"] < 1.0
    # ============================================================

    # Ponderación y puntajes
    peso_intereses, peso_aptitudes = 0.8, 0.2
    for a in AREAS:
        df[f"PUNTAJE_COMBINADO_{a}"] = (df[f"INTERES_{a}"] * peso_intereses + df[f"APTITUD_{a}"] * peso_aptitudes)
        df[f"TOTAL_{a}"] = df[f"INTERES_{a}"] + df[f"APTITUD_{a}"]

    # Área fuerte y score máximo
    df["Area_Fuerte_Ponderada"] = df.apply(lambda r: max(AREAS, key=lambda a: r[f"PUNTAJE_COMBINADO_{a}"]), axis=1)
    df["Score"] = df[[f"PUNTAJE_COMBINADO_{a}" for a in AREAS]].max(axis=1)

    # Coherencia
    def evaluar(area_chaside, carrera):
        perfil = PERFIL_CARRERAS.get(str(carrera).strip())
        if not perfil: return "Sin perfil definido"
        if area_chaside in perfil.get("Fuerte", []): return "Coherente"
        if area_chaside in perfil.get("Baja", []): return "Requiere Orientación"
        return "Neutral"

    df["Coincidencia_Ponderada"] = df.apply(lambda r: evaluar(r["Area_Fuerte_Ponderada"], r[columna_carrera]), axis=1)

    # Lógica de Carrera Mejor Perfilada (Integrando Desviación)
    def carrera_mejor(r):
        if r["Informacion_No_Aceptable"]:
            return "Información no aceptable"
        a = r["Area_Fuerte_Ponderada"]
        c_actual = str(r[columna_carrera]).strip()
        sugeridas = [c for c, p in PERFIL_CARRERAS.items() if a in p.get("Fuerte", [])]
        return c_actual if c_actual in sugeridas else (", ".join(sugeridas) if sugeridas else "Sin sugerencia clara")

    # Diagnóstico y Semáforo
    def diagnostico(r):
        if r["Carrera_Mejor_Perfilada"] == "Información no aceptable": return "Información no aceptable"
        if str(r[columna_carrera]).strip() == str(r["Carrera_Mejor_Perfilada"]).strip(): return "Perfil adecuado"
        if r["Carrera_Mejor_Perfilada"] == "Sin sugerencia clara": return "Sin sugerencia clara"
        return f"Sugerencia: {r['Carrera_Mejor_Perfilada']}"

    def semaforo(r):
        diag = r["Diagnóstico Primario Vocacional"]
        if diag == "Información no aceptable": return "No aceptable"
        if diag == "Sin sugerencia clara": return "Sin sugerencia"
        match = r["Coincidencia_Ponderada"]
        return {"Coherente": "Verde", "Neutral": "Amarillo", "Requiere Orientación": "Rojo"}.get(match, "Sin sugerencia")

    df["Carrera_Mejor_Perfilada"] = df.apply(carrera_mejor, axis=1)
    df["Diagnóstico Primario Vocacional"] = df.apply(diagnostico, axis=1)
    df["Semáforo Vocacional"] = df.apply(semaforo, axis=1)

    df["Categoría_UI"] = df["Semáforo Vocacional"].map(CAT_INT_TO_UI).fillna("No tiene un área predominante")
    df["Categoría_UI"] = pd.Categorical(df["Categoría_UI"], categories=CAT_UI_ORDER, ordered=True)

    return df, columna_carrera, columna_nombre
