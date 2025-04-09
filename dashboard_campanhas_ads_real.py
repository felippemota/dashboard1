
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Dashboard de Anúncios", layout="wide")

st.title("📊 Dashboard de Anúncios - Custo x Lucro")

# Caminho do arquivo Excel com os dados reais
file_path = os.path.join(os.path.dirname(__file__), "dashboard_campanhas_completas.xlsx")
df = pd.read_excel(file_path)

# Exibe tabela de dados
st.subheader("🗂️ Detalhamento das Campanhas")
st.dataframe(df)

# Gráfico de dispersão entre custo e lucro
st.subheader("🧮 Relação Custo x Lucro")
fig, ax = plt.subplots()
ax.scatter(df["cost"], df["lucro"], color="green")
ax.set_xlabel("Custo")
ax.set_ylabel("Lucro")
ax.set_title("Dispersão: Custo vs Lucro")
st.pyplot(fig)
