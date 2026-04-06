import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("🌿 Green Fire - Gestión de Fábrica")

# Creamos la conexión
conn = st.connection("gsheets", type=GSheetsConnection)

# Leemos la pestaña de Insumos
df = conn.read(worksheet="Insumos")

st.subheader("Precios de Insumos Actuales")
st.dataframe(df)

st.success("¡Conexión exitosa con Google Sheets!")
