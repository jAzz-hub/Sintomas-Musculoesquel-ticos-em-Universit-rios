# Adicione estas importações no início do arquivo statistics_functions.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kendalltau, spearmanr, mannwhitneyu, chi2_contingency
from constants import ordinal_inverse_mappings, ordinal_mappings
from matplotlib.colors import LinearSegmentedColormap


# Casos de variável categórica nominal x variável númerica
def Boxplot(df, x_axis, y_numerical_axis):
    sns.boxplot(x=df[x_axis], y=df[y_numerical_axis], data=df)
    plt.xticks(rotation=45)  # Rotaciona rótulos para legibilidade    
    plt.show()


def is_ordinal(series):
    """Verifica se uma série é ordinal (numérica com <= 5 valores únicos)"""
    return pd.api.types.is_numeric_dtype(series) and series.nunique() <= 5


def is_binary(series):
    """Verifica se uma série é binária (apenas 2 valores únicos)"""
    return series.nunique() == 2


def analyze_ordinal_pair(df, col1, col2):
    # Verificação inicial
    if col1 not in ordinal_inverse_mappings or col2 not in ordinal_inverse_mappings:
        raise ValueError("Verifique os nomes das colunas nos mapeamentos!")
    
    # Pré-processamento
    df_clean = df[[col1, col2]].dropna().copy()
    
    # Mapeia valores para texto
    df_clean[f'{col1}_label'] = df_clean[col1].map(ordinal_inverse_mappings[col1])
    df_clean[f'{col2}_label'] = df_clean[col2].map(ordinal_inverse_mappings[col2])

    # Ordem categórica explícita
    ordem_col1 = [ordinal_inverse_mappings[col1][i] for i in sorted(ordinal_inverse_mappings[col1].keys())]
    ordem_col2 = [ordinal_inverse_mappings[col2][i] for i in sorted(ordinal_inverse_mappings[col2].keys())]
    
    # Cria categorias ordenadas
    df_clean[f'{col1}_label'] = pd.Categorical(
        df_clean[f'{col1}_label'], 
        categories=ordem_col1, 
        ordered=True
    )
    df_clean[f'{col2}_label'] = pd.Categorical(
        df_clean[f'{col2}_label'], 
        categories=ordem_col2, 
        ordered=True
    )
    
    # Tabela de contingência
    contingency = pd.crosstab(
        df_clean[f'{col1}_label'], 
        df_clean[f'{col2}_label']
    )
    
    
        # Configuração do Seaborn
    sns.set_theme(font_scale=2.2)  # Aumenta a escala geral das fontes

#     custom_cmap = LinearSegmentedColormap.from_list(
#     "custom_fade", ["#D4145A", "#6A1B9A", "#0D47A1"]
#   )

    #  custom_cmap = LinearSegmentedColormap.from_list(
    #     "custom_fade", ["#0D47A1", "#6A1B9A","#D4145A"]
    # )
    # custom_cmap = LinearSegmentedColormap.from_list(
    # "custom_fade_exact", ['#622460', '#4d2a68', '#393174', '#263a83', '#154394']
    # )

    # custom_cmap = LinearSegmentedColormap.from_list(
    #     "custom_fade_exact", ['#6f215e', '#3c2f71', '#263982', '#552765', '#871f5c']

    # )

    custom_cmap = LinearSegmentedColormap.from_list(
        "custom_fade_reversed", ['#263982', '#3c2f71', '#552765', '#6f215e', '#871f5c']
    )
    # Plotagem
    plt.figure(figsize=(20, 20))
    ax = sns.heatmap(
        contingency, 
        annot=True, 
        fmt='d', 
        cmap=custom_cmap,#'YlOrBr', 
        cbar_kws={'label': 'Contagem'}
    )
    
    # Configurações do gráfico
    plt.title(f"Relação entre '{col1}' e '{col2}'", pad=15)
    plt.xlabel(col2, fontsize = 22)
    plt.ylabel(col1, fontsize = 22)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    # Adiciona estatísticas
    tau, p = kendalltau(df_clean[col1], df_clean[col2])
    plt.figtext(
        0.5, -0.2, 
        f"Kendall's Tau = {tau:.2f} (p = {p:.4f})\n",
        ha='center', 
        fontsize=23
    )
    
    plt.tight_layout()
    plt.show()