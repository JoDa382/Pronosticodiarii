import streamlit as st
import requests
import pandas as pd

# --- CONFIGURACIÓN ---
API_KEY = "236904abf5a7c2982d642f18959b355a" 
REGIONS = 'eu'
MARKETS = 'h2h'
ODDS_FORMAT = 'decimal'

DEPORTES = {
    '⚽ La Liga': 'soccer_spain_la_liga',
    '⚽ Premier League': 'soccer_england_league_1',
    '⚽ Serie A': 'soccer_italy_serie_a',
    '⚽ Super Liga Turquía': 'soccer_turkey_super_league',
    '主 Tenis ATP': 'tennis_atp_aus_open',
}

st.set_page_config(page_title="Estratega Interés Compuesto", page_icon="📈", layout="wide")

# --- INTERFAZ ---
st.title("🚀 Estratega: Interés Compuesto 1.50")

tabs = st.tabs(["🔍 Buscador de Picks", "📈 Calculadora de Crecimiento"])

with tabs[0]:
    st.sidebar.header("💰 Gestión de Banca")
    banca_inicial = st.sidebar.number_input("Banca Actual (€)", value=100.0)
    porcentaje_stake = st.sidebar.slider("% de Banca a apostar", 1, 100, 10)
    monto_apuesta = round(banca_inicial * (porcentaje_stake / 100), 2)
    
    if st.button('🔍 GENERAR COMBINADA'):
        # ... (Aquí va la lógica de búsqueda de cuotas de 1.20 que ya teníamos)
        st.info("Buscando cuotas de 1.20 en las APIs seleccionadas...")
        # Simulación para visualización
        cuota_final = 1.44 
        ganancia_neta = round(monto_apuesta * (cuota_final - 1), 2)
        st.success(f"Combinada Sugerida: Cuota {cuota_final}")
        st.metric("Inversión Hoy", f"{monto_apuesta}€", f"+{ganancia_neta}€ si aciertas")

with tabs[1]:
    st.header("Visualización del Reto 30 Días")
    st.write("Mira qué pasa si aciertas una cuota 1.50 diaria reinvirtiendo tus ganancias:")
    
    dias = st.slider("Días del reto", 1, 60, 30)
    cuota_objetivo = st.number_input("Cuota diaria promedio", value=1.50)
    
    datos_crecimiento = []
    banca_temporal = banca_inicial
    for d in range(1, dias + 1):
        ganancia = banca_temporal * (cuota_objetivo - 1)
        banca_temporal += ganancia
        datos_crecimiento.append({"Día": d, "Banca (€)": round(banca_temporal, 2)})
    
    df = pd.DataFrame(datos_crecimiento)
    st.line_chart(df.set_index("Día"))
    
    st.write(f"💰 Al final del día {dias}, tu banca sería de: **{round(banca_temporal, 2)}€**")
    st.caption("Nota: El interés compuesto es poderoso, pero recuerda que una sola pérdida reiniciará el progreso.")
    
