# Adicione estas importações no início do arquivo statistics_functions.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kendalltau, spearmanr, mannwhitneyu, chi2_contingency
from constants import ordinal_inverse_mappings

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
    """
    Analisa a relação entre duas colunas ordinais ou entre uma ordinal e uma numérica.
    
    Parâmetros:
        df: DataFrame pandas
        col1, col2: Nomes das colunas (strings) ou Series
    """

    # Garante que usamos nomes de colunas
    if isinstance(col1, pd.Series):
        col1 = col1.name
    if isinstance(col2, pd.Series):
        col2 = col2.name


    col1_ordinal = is_ordinal(df[col1])
    col2_ordinal = is_ordinal(df[col2])
    
    # Visualização
    plt.figure(figsize=(10, 5))
    
    try:
        if col1_ordinal and col2_ordinal:
            # Duas ordinais: Heatmap + Kendall's Tau
            contingency = pd.crosstab(df[col1], df[col2])
            sns.heatmap(contingency, annot=True, fmt='d', cmap='Blues')
            tau, p = kendalltau(df[col1], df[col2])
            plt.title(f"Relação Ordinal (Kendall's Tau)\nτ = {tau:.2f}, p = {p:.4f}")
        
        elif col1_ordinal or col2_ordinal:
            # Uma ordinal, uma numérica: Boxplot + Spearman
            ordinal_col = col1 if col1_ordinal else col2
            numeric_col = col2 if col1_ordinal else col1
            
            sns.boxplot(x=ordinal_col, y=numeric_col, data=df)
            rho, p = spearmanr(df[ordinal_col], df[numeric_col])
            plt.title(f"Correlação Ordinal-Numérica (Spearman)\nρ = {rho:.2f}, p = {p:.4f}")
        
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Erro durante a plotagem: {str(e)}")
        plt.close()

# Exemplo de uso:
# analyze_pair(df, 'Teve dor?', 'Nível de estresse')
# analyze_pair(df, 'Consultou médico?', 'Grau de incapacidade')