import streamlit as st
import pandas as pd

# Configuración de la página para que parezca una App móvil
st.set_page_config(page_title="Pronóstico 1.50 Diarios", page_icon="⚽")

# Estilo personalizado (Modo Oscuro y Amigable)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #00ff41; color: black; font-weight: bold; }
    .card { padding: 20px; border-radius: 15px; background-color: #1e2130; border-left: 5px solid #00ff41; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 Pick del Día (Cuota 1.50)")
st.subheader("Dos selecciones de 1.20 combinadas")

# --- LÓGICA DE DATOS (Simulación de Flashscore) ---
# En una versión avanzada, aquí conectaríamos la API de Sportmonks o Football-API
datos_partidos = [
    {"evento": "Man. City vs Everton", "mercado": "Goles: +0.5", "cuota": 1.22, "confianza": "95%"},
    {"evento": "Alcaraz vs Sinner", "mercado": "Gana 1 Set (Alcaraz)", "cuota": 1.19, "confianza": "92%"},
    {"evento": "Real Madrid vs Valencia", "mercado": "Doble Oportunidad: 1X", "cuota": 1.15, "confianza": "96%"}
]

# --- INTERFAZ ---
st.write("### 🚀 Combinada Recomendada")

col1, col2 = st.columns(2)
p1 = datos_partidos[0]
p2 = datos_partidos[1]
cuota_total = round(p1['cuota'] * p2['cuota'], 2)

with st.container():
    st.markdown(f"""
    <div class="card">
        <h4>1. {p1['evento']}</h4>
        <p><b>Mercado:</b> {p1['mercado']} | <b>Cuota:</b> {p1['cuota']}</p>
        <p style='color: #00ff41;'>Probabilidad: {p1['confianza']}</p>
    </div>
    <div class="card">
        <h4>2. {p2['evento']}</h4>
        <p><b>Mercado:</b> {p2['mercado']} | <b>Cuota:</b> {p2['cuota']}</p>
        <p style='color: #00ff41;'>Probabilidad: {p2['confianza']}</p>
    </div>
    """, unsafe_allow_html=True)

st.metric(label="Cuota Total Combinada", value=f"{cuota_total}")

if st.button("Copiar Pronóstico"):
    st.success("¡Copiado al portapapeles! Suerte 🍀")

# --- HISTORIAL ---
with st.expander("Ver Historial Últimos 7 Días"):
    st.write("✅ Ayer: Ganada (Cuota 1.48)")
    st.write("✅ Martes: Ganada (Cuota 1.52)")
    st.write("❌ Lunes: Perdida (Cuota 1.45)")
