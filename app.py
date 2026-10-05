import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Vendas - Nike",
    page_icon="👟",
    layout="wide"
)

# Carregar dados
@st.cache_data
def carregar_dados():
    return pd.read_csv('vendas_nike.csv')

df = carregar_dados()

# Título do Dashboard
st.title("👟 Dashboard Interativo de Vendas - Nike")
st.markdown("Análise de desempenho de vendas, produtos e regiões.")

# Barra Lateral (Filtros)
st.sidebar.header("🔍 Filtros")
regiao_selecionada = st.sidebar.multiselect(
    "Selecione a Região:",
    options=df['Regiao'].unique(),
    default=df['Regiao'].unique()
)

categoria_selecionada = st.sidebar.multiselect(
    "Selecione a Categoria:",
    options=df['Categoria'].unique(),
    default=df['Categoria'].unique()
)

# Filtrar o DataFrame
df_filtrado = df[
    (df['Regiao'].isin(regiao_selecionada)) & 
    (df['Categoria'].isin(categoria_selecionada))
]

# Indicadores (KPIs)
st.subheader("📊 Indicadores Principais")
col1, col2, col3 = st.columns(3)

faturamento_total = df_filtrado['Receita_Total'].sum()
total_unidades = df_filtrado['Quantidade'].sum()
ticket_medio = df_filtrado['Receita_Total'].mean() if len(df_filtrado) > 0 else 0

col1.metric("Faturamento Total", f"€{faturamento_total:,.2f}")
col2.metric("Produtos Vendidos", f"{total_unidades} un")
col3.metric("Ticket Médio", f"€{ticket_medio:,.2f}")

st.markdown("---")

# Gráficos
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("👟 Faturamento por Produto")
    fig_prod = px.bar(
        df_filtrado.groupby('Produto', as_index=False)['Receita_Total'].sum().sort_values(by='Receita_Total', ascending=True),
        x='Receita_Total',
        y='Produto',
        orientation='h',
        labels={'Receita_Total': 'Receita (€)', 'Produto': 'Modelo'},
        color='Receita_Total',
        color_continuous_scale='Reds'
    )
    st.plotly_chart(fig_prod, use_container_width=True)

with col_graf2:
    st.subheader("🌍 Vendas por Região")
    fig_reg = px.pie(
        df_filtrado,
        names='Regiao',
        values='Receita_Total',
        hole=0.4
    )
    st.plotly_chart(fig_reg, use_container_width=True)

# Tabela de Dados
st.subheader("📋 Dados Detalhados")
st.dataframe(df_filtrado, use_container_width=True)