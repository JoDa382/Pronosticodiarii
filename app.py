import streamlit as st
import requests
import pandas as pd

# --- CONFIGURACIÓN ---
API_KEY = "236904abf5a7c2982d642f18959b355a" 
REGIONS = 'eu'
MARKETS = 'h2h'
ODDS_FORMAT = 'decimal'

# Ligas que pediste
LIGAS = {
    '🇪🇸 La Liga': 'soccer_spain_la_liga',
    '🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League': 'soccer_england_league_1',
    '🇮🇹 Serie A': 'soccer_italy_serie_a',
    '🇹🇷 Super Liga': 'soccer_turkey_super_league'
}

st.set_page_config(page_title="Estratega 1.50", page_icon="🚀", layout="wide")

st.title("🚀 Estratega: Interés Compuesto 1.50")

tabs = st.tabs(["🔍 Buscador de Picks", "📈 Calculadora de Crecimiento"])

with tabs[0]:
    st.sidebar.header("💰 Gestión de Banca")
    banca_inicial = st.sidebar.number_input("Banca Actual (€)", value=100.0)
    porcentaje_stake = st.sidebar.slider("% de Banca a apostar", 1, 100, 10)
    monto_apuesta = round(banca_inicial * (porcentaje_stake / 100), 2)
    
    if st.button('🔍 GENERAR COMBINADA REAL'):
        hallados = []
        with st.spinner('Escaneando ligas de España, Inglaterra, Italia y Turquía...'):
            for nombre_liga, sport_key in LIGAS.items():
                url = f'https://api.the-odds-api.com/v4/sports/{sport_key}/odds/?apiKey={API_KEY}&regions={REGIONS}&markets={MARKETS}&oddsFormat={ODDS_FORMAT}'
                try:
                    res = requests.get(url)
                    if res.status_code == 200:
                        data = res.json()
                        for partido in data:
                            for outcome in partido['bookmakers'][0]['markets'][0]['outcomes']:
                                # Buscamos cuotas en tu rango ideal de 1.18 a 1.25
                                if 1.18 <= outcome['price'] <= 1.25:
                                    hallados.append({
                                        "liga": nombre_liga,
                                        "equipo": outcome['name'],
                                        "partido": f"{partido['home_team']} vs {partido['away_team']}",
                                        "cuota": outcome['price']
                                    })
                except:
                    continue

        if len(hallados) >= 2:
            # Seleccionamos los dos con mayor probabilidad (cuota más baja dentro del rango)
            hallados.sort(key=lambda x: x['cuota'])
            p1, p2 = hallados[0], hallados[1]
            
            cuota_final = round(p1['cuota'] * p2['cuota'], 2)
            ganancia_neta = round(monto_apuesta * (cuota_final - 1), 2)
            
            st.balloons()
            st.success(f"✅ ¡Combinada Encontrada! Cuota Total: {cuota_final}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.info(f"**{p1['liga']}**\n\n{p1['equipo']}\n\n{p1['partido']} (@{p1['cuota']})")
            with col2:
                st.info(f"**{p2['liga']}**\n\n{p2['equipo']}\n\n{p2['partido']} (@{p2['cuota']})")
            
            st.metric("Retorno Estimado", f"{round(monto_apuesta + ganancia_neta, 2)}€", f"+{ganancia_neta}€ de beneficio")
        else:
            st.warning("No hay suficientes favoritos con cuota 1.20 en este momento. Prueba más tarde.")

with tabs[1]:
    st.header("Visualización del Reto 30 Días")
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
