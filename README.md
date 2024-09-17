# Análise de Dados Imobiliários

Este projeto consiste na análise de dados de um conjunto imobiliário fornecido pelo site [Kaggle](https://www.kaggle.com). A análise foi realizada utilizando as bibliotecas **Pandas** e **Streamlit**, com foco na visualização dos resultados de vendas e margens de lucro em diferentes estações e localizações.

## Descrição do Dataset

O dataset contém as seguintes colunas:

- **price**: Preço do produto
- **cost**: Custo do produto
- **sales**: Quantidade de vendas
- **profit_margin**: Margem de lucro
- **inventory**: Estoque disponível
- **discount_percentage**: Percentual de desconto aplicado
- **delivery_days**: Dias para entrega
- **category**: Categoria do produto
- **material**: Material do produto
- **color**: Cor do produto
- **location**: Localização (Rural, Suburban, Urban)
- **season**: Estação (Spring, Summer, Fall, Winter)
- **store_type**: Tipo de loja (Online, Retail)
- **brand**: Marca do produto
- **revenue**: Receita gerada pelo produto

## Perguntas Respondidas na Análise

1. **Qual é a distribuição das vendas e margens de lucro?**  
   A análise mostra a distribuição das vendas e margens de lucro por categoria, revelando quais produtos geram mais receita e lucro.
   
2. **Qual categoria gerou a maior receita total?**  
   A categoria com maior receita foi determinada pela soma total das receitas para cada categoria.

3. **Existe algum padrão sazonal nas vendas?**  
   As vendas foram analisadas com base nas estações do ano (primavera, verão, outono e inverno) para verificar se há um padrão sazonal nas vendas.

4. **Qual estação teve o maior total de vendas?**  
   A estação com o maior volume total de vendas foi identificada, auxiliando na análise de períodos de alta demanda.

5. **Qual localização tem a maior média de vendas por produto?**  
   A média de vendas por localização (rural, suburbana, urbana) foi calculada para identificar onde os produtos têm um desempenho superior.

6. **Existem diferenças nas vendas ou margens de lucro com base na localização?**  
   Foram investigadas as diferenças entre as vendas e margens de lucro com base na localização, destacando variações regionais.

## Principais Resultados

- **Distribuição das Vendas e Margens de Lucro**:  
  Produtos de **camas** e **mesas** têm vendas mais expressivas, enquanto **cadeiras** e **sofás** apresentaram margens de lucro mais altas.

- **Categoria com Maior Receita Total**:  
  A categoria "Mesas" gerou a maior receita total, com uma soma significativa em várias estações do ano.

- **Padrão Sazonal nas Vendas**:  
  As vendas têm uma leve variação sazonal, com **inverno** e **outono** apresentando os maiores totais de vendas.

- **Estação com Maior Total de Vendas**:  
  O **inverno** registrou o maior total de vendas.

- **Localização com Maior Média de Vendas**:  
  A localização **urbana** registrou a maior média de vendas por produto, com aproximadamente **25,21** vendas por produto.

- **Diferenças de Vendas e Margens de Lucro por Localização**:  
  As localizações urbanas apresentaram tanto uma maior média de vendas quanto margens de lucro mais consistentes, enquanto regiões rurais mostraram margens de lucro mais variáveis.

## Tecnologias Utilizadas

- **Python** para manipulação e análise de dados.
- **Pandas** para o processamento de dados.
- **Streamlit** para visualização de dados interativa.
- **Jupyter Notebook** para experimentação e desenvolvimento.

## Dashboard da Análise
[Streamlit](https://d4thjrkuuwd3mvy56lcnxq.streamlit.app/).
