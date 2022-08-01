# Aulas

## 0 Apresentação da disciplina

## 1 Introdução

### 1.1 Introdução à ciência de dados

Aulas:

- Skienna, Cap 1: What is Data Science?

- Bruce, 1.1 Elements of Structured Data

### 1.2 Introdução ao Python para ciência de dados

Aulas:

- McKinney, Cap. 4 - NumPy Basics: Arrays and Vectorized Computation.
- McKinney, Cap. 5 - Getting Started with pandas.
- Bruce, 1.2 Rectangular data
- VanderPlas, [3 Data Manipulation with Pandas](https://jakevdp.github.io/PythonDataScienceHandbook/03.00-introduction-to-pandas.html)

Material de revisão:

- McKinney, Cap. 2 - Python Language Basics, IPython, and Jupyter Notebooks.
- McKinney, Cap. 3 - Built-in Data Structures, Functions, and Files

### 1.3 Tratamento de dados

Aulas:

- McKinney, 6 Data Loading, Storage, and File Formats
- McKinney, 7 Data Cleaning and Preparation
- McKinney, 8 Data Wrangling: Join, Combine, and Reshape
- Skienna, 3 Data Munging.

### 1.4 Visualização básica de dados em Python

- McKinney, 9 Plotting and Visualization

- VanderPlas, [4 Visualization with Matplotlib](https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html)

## 2 Análise exploratória de dados

### 2.1 Estatística descritiva

- Skienna, 2.2 Descriptive Statistics
    - Centrality Measures
    - Variability Measures
    - Interpreting Variance

- Bruce, 1.3 Estimates of Location
- Bruce, 1.4 Estimates of Variability

### 2.2 Correlação

- Skienna, 2.3 Correlation Analysis.
- Bruce, 1.7 Correlation

### 2.3 Exploratory Data Analysis (EDA)

- Wickham, 7 Exploratory Data Analysis

- Skienna, 6.1 Exploratory Data Analysis

- Bruce, 1.5 Exploring the data distribution
- Bruce, 1.6 Exploring binary and categorical data
- Bruce, 1.7 Correlation
- Bruce, 1.8 Exploring two or more variables

- McKinney, 10 Data Aggregation and Group Operations

- Downey, 7 Relationships between variables

## 3 Inferência

### 3.1 Significância estatística

- Skienna, 5.3 Statistical significance
    - T-test, coeficiente de variação (correlação)

- Skienna, 5.5 Permutation Tests and P-values
    - Bootstrap e p-valor

- Bruce, 2 Data and Sampling Distributions

- Bruce, 3 Statistical Experiments and Significance Testing
    - A/B Testing
    - Hypothesis Tests
    - Resampling (Permutation and Bootstrap)
    - Statistical Significance and p-Values
    - t-Tests
    - ANOVA
    - Chi-Square Test
    - Power and Sample Size

- Downey, 9 Hypothesis testing

- Slides de Raquel
    - Testes de hipótese (fpcc2 slide 05 a 07)
    - Testes em variáveis categóricas (fpcc2 slide 18, )


## 4 Regressão

- Bruce, 4 Regression and Prediction

- Skienna, 9 Linear and Logistic Regression

- McKinney, 12.4 Introduction to scikit-learn

- VanderPlas, [5.6 In Depth: Linear Regression](
https://jakevdp.github.io/PythonDataScienceHandbook/05.06-linear-regression.html)

- Downey, 11 Regression

## 5 Visualização avançada?

- Teoria, visualização interativa?
    - Pegar aulas do minicurso de DataViz

## Agrupamento?

## Scraping?

# Projeto?

Deixar livre para o aluno explorar um dataset e construir uma análise em notebook ou dashboard

# Datasets para práticas

## Câmara dos deputados (API)

URL: https://dadosabertos.camara.leg.br/swagger/api.html

### Ideias

- Alinhamento de partidos com governo nas votações (endpoint `/votacao/{id}/orientacoes`)

- Alinhamento de deputados com governo nas votações (endpoint `/votacao/{id}/votos`)

- Partidos/deputados com mais proposições realizadas/votadas/ aprovadas (endpoint `/proposicoes/{id}`)

- Partidos com mais deputados

- Deputados com mais mandatos

#### Gênero

- Partidos/estados com mais mulheres eleitas

- Evolução de deputadas mulheres ao longo do tempo

- Proporção de proposições realizadas/votadas/aprovadas por gênero


## Casos e óbitos de Covid-19 no Brasil

URL: https://github.com/wcota/covid19br

Ideias:
- Estados e cidades mais afetados (incidência, mortalidade e letalidade)
- 

## Vacinação de Covid-19 no Brasil

URL: https://github.com/wcota/covid19br-vac

Ideias:
- Cidades/estados com maior cobertura vacinal por dose

## Dados eleitorais TSE

URL: https://dadosabertos.tse.jus.br/dataset/

Ideias:

- Qual é o padrão de mulheres candidatas / eleitas ao longo do tempo?

- Quais estados / municípios possuem maior/menor proporção de mulheres eleitas?

- Candidatas "laranja"? Encontrar candidatos com votação muito abaixo do esperado e identificar a proporção de mulheres



# Referências

- [P4DS] McKinney, W. Python for Data Analysis, 3rd Edition, 2022. Open Access: https://wesmckinney.com/book/

- [TDSDM] Skienna, S. The Data Science Design Manual. Springer. 2017.

- [R4DS] Wickhan, H. R for Data Science. Open Access: http://r4ds.had.co.nz

- [PS4DS] Bruce, P. et al. Practical Statistics for Data Scientists (O’Reilly).

- [PDSH] VanderPlas, J. Python Data Science Handbook. 2022. Open URL: https://jakevdp.github.io/PythonDataScienceHandbook/

- [TK] Downey, A. Think Stats - Exploratory Data Analysis in Python. 

- https://github.com/yurimalheiros/icd
- https://github.com/nazareno/fpcc2
- https://github.com/nazareno/ciencia-de-dados-1