import streamlit as st
import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('Furniture.csv')

# Exibir o título no app
st.title("Exibindo Dados de Furniture")

# Exibir as primeiras linhas do DataFrame no Streamlit
st.write("Visualizando as primeiras 5 linhas do arquivo CSV:")
st.dataframe(df.head())

# Título da aplicação
st.title("Distribuição das Vendas e Margens de Lucro")

# Função para criar histogramas personalizados com Streamlit e Pandas
def plot_histogram(data, column, title, color):
    st.subheader(title)
    hist_data = data[column].dropna().value_counts(bins=10).sort_index()
    st.bar_chart(hist_data, use_container_width=True)

# Configuração das colunas para exibição lado a lado
col1, col2 = st.columns(2)

# Plotando o histograma de vendas na primeira coluna
with col1:
    plot_histogram(df, 'sales', 'Distribuição das Vendas', 'skyblue')

# Plotando o histograma de margens de lucro na segunda coluna
with col2:
    plot_histogram(df, 'profit_margin', 'Distribuição das Margens de Lucro', 'salmon')




# Título da aplicação
st.title("Receita Total por Categoria")

# Calculando a receita total por categoria
category_revenue = df.groupby('category')['revenue'].sum()

# Criar um DataFrame para visualização
category_revenue_df = category_revenue.reset_index()
category_revenue_df.columns = ['Category', 'Total Revenue']

# Exibir o gráfico de barras
st.bar_chart(category_revenue_df.set_index('Category'))

# Exibir a categoria com a maior receita
highest_revenue_category = category_revenue.idxmax()
highest_revenue_value = category_revenue.max()
st.write(f"A categoria que gerou a maior receita total é '{highest_revenue_category}' com uma receita de {highest_revenue_value:.2f}.")

# Título da aplicação
st.title("Vendas Totais por Estação")

# Calculando as vendas totais por estação
seasonal_sales = df.groupby('season')['sales'].sum()

# Criar um DataFrame para visualização
seasonal_sales_df = seasonal_sales.reset_index()
seasonal_sales_df.columns = ['Season', 'Total Sales']

# Exibir o gráfico de barras
st.bar_chart(seasonal_sales_df.set_index('Season'))

# Exibir a tabela de vendas totais por estação
st.write("Vendas totais por estação:")
st.dataframe(seasonal_sales_df)

# Título da aplicação
st.title("Média de Vendas por Localização")

# Calculando a média de vendas por localização
location_sales_mean = df.groupby('location')['sales'].mean()

# Criar um DataFrame para visualização
location_sales_df = location_sales_mean.reset_index()
location_sales_df.columns = ['Location', 'Average Sales']

# Exibir o gráfico de barras
st.bar_chart(location_sales_df.set_index('Location'))

# Exibir a localização com a maior média de vendas
max_sales_location = location_sales_mean.idxmax()
max_sales_value = location_sales_mean.max()
st.write(f"A localização com a maior média de vendas por produto é '{max_sales_location}' com uma média de {max_sales_value:.2f} vendas por produto.")

# Exibir a tabela de média de vendas por localização
st.dataframe(location_sales_df)

# Título da aplicação
st.title("Média e Mediana das Vendas e Margens de Lucro por Localização")

# Calculando a média e mediana das vendas por localização
sales_by_location = df.groupby('location')['sales'].agg(['mean', 'median'])

# Calculando a média e mediana das margens de lucro por localização
profit_margin_by_location = df.groupby('location')['profit_margin'].agg(['mean', 'median'])

# Configuração das colunas para exibição lado a lado
col1, col2 = st.columns(2)

# Exibindo a média e mediana das vendas por localização
with col1:
    st.subheader('Média e Mediana das Vendas por Localização')
    st.bar_chart(sales_by_location)

# Exibindo a média e mediana das margens de lucro por localização
with col2:
    st.subheader('Média e Mediana das Margens de Lucro por Localização')
    st.bar_chart(profit_margin_by_location)

# Exibir as tabelas com os resultados
st.write("Média e Mediana das Vendas por Localização:")
st.dataframe(sales_by_location)

st.write("Média e Mediana das Margens de Lucro por Localização:")
st.dataframe(profit_margin_by_location)
