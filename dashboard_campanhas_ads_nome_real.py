
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Título
st.title("📊 Dashboard de Anúncios - Custo x Lucro")

# Caminho para o arquivo Excel
file_path = os.path.join(os.path.dirname(__file__), "dashboard_campanhas_nome_real.xlsx")

# Carregando os dados
df = pd.read_excel(file_path)

# Calculando lucro e relação custo/lucro
df['lucro'] = df['roas'] * df['cost'] / 100
df['custo_x_lucro'] = df.apply(lambda row: row['cost'] / row['lucro'] if row['lucro'] > 0 else -1, axis=1)

# Exibindo a tabela
st.subheader("🗂️ Detalhamento das Campanhas")
st.dataframe(df)

# Gráfico de dispersão: Custo vs Lucro
st.subheader("💹 Relação Custo x Lucro")
fig, ax = plt.subplots()
ax.scatter(df['cost'], df['lucro'], color='green')
ax.set_xlabel('Custo')
ax.set_ylabel('Lucro')
ax.set_title('Dispersão: Custo vs Lucro')
st.pyplot(fig)
