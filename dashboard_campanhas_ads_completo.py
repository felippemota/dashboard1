
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard de Anúncios", layout="wide")

st.title("📊 Dashboard de Anúncios - Custo x Lucro")

# Carregar dados
df = pd.read_excel("dashboard_campanhas_com_recomendacoes.xlsx")

# Exibir tabela
st.subheader("📝 Detalhamento das Campanhas")
st.dataframe(df)

# Gráfico: Custo vs Lucro
st.subheader("🧮 Relação Custo x Lucro")

fig, ax = plt.subplots(figsize=(5, 3))  # Reduzido
ax.scatter(df["cost"], df["lucro"], color='green')
ax.set_xlabel("Custo")
ax.set_ylabel("Lucro")
ax.set_title("Dispersão: Custo vs Lucro")
st.pyplot(fig)

# Justificativas de custo x lucro
st.subheader("📌 Justificativas de Custo x Benefício")
for index, row in df.iterrows():
    st.markdown(f"**{row['name']}**: {row['justificativa']}")
