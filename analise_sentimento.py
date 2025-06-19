# -*- coding: utf-8 -*-
"""
Análise de Sentimento de Reviews de Produtos.

Este script carrega dados de exemplo, aplica um modelo de IA da biblioteca
Transformers para classificar o sentimento de cada review e, ao final, exibe
a tabela com os resultados e gera um gráfico de barras com a distribuição
dos sentimentos.
"""

# 1. Importação das Bibliotecas Essenciais
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
import seaborn as sns

def criar_visualizacao(df):
    """
    Cria e salva um gráfico de barras a partir do DataFrame de resultados.
    """
    print("\n--- Gerando a Visualização dos Dados ---")

    # Contando os sentimentos
    contagem_sentimentos = df['sentimento'].value_counts()

    # Criando a figura do gráfico
    plt.figure(figsize=(8, 6))
    sns.set_style("darkgrid")
    sns.barplot(x=contagem_sentimentos.index, y=contagem_sentimentos.values, palette="viridis")

    # Adicionando títulos e legendas
    plt.title('Distribuição de Sentimentos das Reviews', fontsize=16)
    plt.xlabel('Sentimento', fontsize=12)
    plt.ylabel('Quantidade de Reviews', fontsize=12)

    # Salvando o gráfico como um arquivo de imagem
    plt.savefig('distribuicao_sentimentos.png')
    print("Gráfico salvo como 'distribuicao_sentimentos.png'")

    # Exibindo o gráfico em uma nova janela
    print("Exibindo gráfico...")
    plt.show()


def principal():
    """
    Função principal que orquestra toda a análise de sentimento.
    """
    print("--- Iniciando a Análise de Sentimento ---")

    # 2. Preparação dos Dados
    dados = {
        'produto': ['Smartphone XPTO', 'Fone de Ouvido Z', 'Teclado Mecânico K', 'Mouse Gamer W', 'Monitor Ultrawide'],
        'texto_review': [
            'Amei o celular! A bateria dura o dia todo e a câmera é incrível.',
            'O som é bom, mas o fone machuca a orelha depois de um tempo.',
            'Teclado barulhento e algumas teclas falham. Odiei.',
            'Este mouse é simplesmente perfeito para jogos, rápido e preciso.',
            'A tela é gigante, porém não achei as cores muito vibrantes.'
        ]
    }
    df_exemplo = pd.DataFrame(dados)
    print("Dados de exemplo carregados.")

    # 3. Carregamento e Aplicação do Modelo de IA
    print("Carregando o modelo de IA... (Isso pode levar um momento na primeira vez)")
    sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")

    def get_sentiment(text):
        """Aplica o pipeline de sentimento a um único texto."""
        result = sentiment_pipeline(text)[0]
        return result['label']

    df_exemplo['sentimento'] = df_exemplo['texto_review'].apply(get_sentiment)
    print("Análise concluída!")

    # 4. Exibição dos Resultados em tabela
    print("\n--- ✨ RESULTADO FINAL DA ANÁLISE ✨ ---")
    print(df_exemplo[['produto', 'texto_review', 'sentimento']])

    # 5. Chamada da função para criar o gráfico
    criar_visualizacao(df_exemplo)

# Este bloco especial garante que a função principal() só rode
# quando executamos este arquivo de script diretamente.
if __name__ == "__main__":
    principal()