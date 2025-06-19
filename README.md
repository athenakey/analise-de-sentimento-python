# Análise de Sentimento com Python e Transformers ✨

![Status do Projeto](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)

## Descrição do Projeto

Este projeto realiza uma análise de sentimento em um conjunto de reviews de produtos escritas em português. O objetivo é classificar cada review como Positiva, Negativa ou Neutra utilizando um modelo de Inteligência Artificial de ponta da biblioteca Transformers.

## Tecnologias Utilizadas

* **Linguagem:** `Python 3.11`
* **Análise de Dados:** `Pandas`
* **Visualização de Dados:** `Matplotlib` & `Seaborn`
* **Análise de Sentimento (IA):** `Transformers (Hugging Face)`
* **Ambientes de Desenvolvimento:** `Visual Studio Code`, `Google Colab`
* **Gerenciamento de Ambiente:** `venv` (Ambientes Virtuais do Python)

## ⚙️ Como Usar o Projeto

Existem duas maneiras de executar este projeto:

### Opção 1: Rodando no Google Colab (Método Fácil e Recomendado)

1.  Abra o notebook diretamente no ambiente do Google.
2.  Execute a primeira célula de código para instalar as bibliotecas necessárias:
    ```python
    !pip install pandas transformers matplotlib seaborn
    ```
3.  Execute as células restantes para ver a análise e os resultados.

### Opção 2: Rodando Localmente

Estas são as instruções para rodar o projeto em uma máquina local.

#### Pré-requisitos

É necessário ter o Python 3.11 (ou compatível) instalado na sua máquina.

#### Instalação

1.  Clone este repositório para a sua máquina.
2.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate
    ```
3.  Instale as dependências:
    ```bash
    pip install pandas transformers matplotlib seaborn
    ```

#### Execução

### Execução

Abra o notebook `analise_sentimento.ipynb` (ou o nome que você deu) em um ambiente como o VS Code ou Jupyter Lab e execute as células na ordem.

## O Que Aprendi?

A construção deste projeto foi uma jornada de aprendizado intensa, que foi muito além da simples análise de sentimento. Alguns dos principais aprendizados foram:

* **Configuração de Ambiente Profissional:** Aprendi na prática a importância de usar Ambientes Virtuais (`venv`) para isolar as dependências de um projeto, evitando conflitos.
* **Resolução de Problemas (Debugging):** Enfrentei e resolvi uma série de desafios de configuração, incluindo incompatibilidade entre versões de bibliotecas e do Python, políticas de execução do PowerShell e a importância de selecionar o 'Kernel' correto no VS Code.
* **Modelos de IA vs. Abordagens por Léxico:** Entendi a diferença fundamental entre uma análise de sentimento baseada em regras (como na biblioteca `LeIA`) e uma baseada em modelos de IA (Transformers), compreendendo as vantagens de precisão e contexto que os modelos modernos oferecem.
* **Manipulação de Dados e Visualização:** Aprimorei minhas habilidades com a biblioteca `Pandas` para aplicar funções e criar novas colunas, e com `Matplotlib`/`Seaborn` para gerar visualizações claras a partir dos resultados.

## Autor

Feito com ❤️ por **THENA**

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tfatimaa/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/athenakey)
