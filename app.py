import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Green Fire Dashboard", page_icon="🌿")

st.title("🌿 Green Fire - Gestión de Fábrica")

# Conexión simplificada
conn = st.connection("gsheets", type=GSheetsConnection)

try:
    # Intentamos leer la pestaña de Insumos
    df = conn.read(worksheet="Insumos")
    
    st.subheader("📊 Precios de Insumos Actuales")
    st.table(df) # Usamos table para que cargue más rápido que dataframe
    st.success("¡Conexión exitosa con Google Sheets!")

except Exception as e:
    st.error(f"Error de conexión: {e}")
    st.info("Verificá que el nombre de la pestaña sea exactamente 'Insumos' y que los secretos estén bien cargados.")
