# 🎮 Jogo da Adivinhação de Números

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)

Este é um clássico jogo "Adivinhe o Número" desenvolvido em Python para ser executado no terminal. É um projeto focado em praticar conceitos fundamentais da linguagem, como loops, condicionais, funções e tratamento de erros.

### 🎬 Demonstração em Ação

*(**Dica para você, Lucas:** Grave um GIF rápido do jogo funcionando, salve-o como `demo.gif` dentro desta mesma pasta `JogodeAdivinhar`, e esta imagem aparecerá aqui automaticamente!)*

![Demonstração do Jogo de Adivinhação](./demo.gif)

---

## ✨ Funcionalidades Principais

O jogo inclui as seguintes características:

-   **Número Aleatório:** A cada nova partida, um número secreto entre 1 e 100 é sorteado.
-   **Dicas Interativas:** O jogador recebe dicas de "Mais alto!" ou "Mais baixo!" a cada palpite.
-   **Limite de Tentativas:** O jogador tem um limite de 10 tentativas para adivinhar o número.
-   **Contador de Tentativas:** O jogo informa o número da tentativa atual e, em caso de vitória, com quantas tentativas o jogador venceu.
-   **Validação de Entrada:** O programa não quebra se o usuário digitar um texto em vez de um número, pedindo uma entrada válida.
-   **Opção de Jogar Novamente:** Ao final de cada partida, o jogador pode escolher começar um novo jogo sem precisar executar o script novamente.

---

## 🛠️ Tecnologias e Conceitos Praticados

Este projeto foi construído utilizando:

-   **Python 3**
-   **Módulo `random`:** Para a geração do número secreto.

Os principais conceitos de programação explorados foram:

-   Estruturação de código em **Funções**.
-   Controle de fluxo com loops **`while`**.
-   Lógica com **`if/elif/else`**.
-   Tratamento de erros e exceções com **`try-except`**.
-   Captura de input do usuário com a função **`input()`**.
-   Manipulação de strings com os métodos **`.strip()`** e **`.upper()`**.

---

## 🚀 Como Executar o Jogo

Para jogar, siga os passos abaixo:

1.  **Pré-requisitos:**
    -   É necessário ter o **Python 3** instalado em sua máquina.

2.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/Lucas-715/python-scripts.git](https://github.com/Lucas-715/python-scripts.git)
    ```

3.  **Navegue até a Pasta do Projeto:**
    ```bash
    cd python-scripts/JogodeAdivinhar
    ```

4.  **Execute o Script:**
    ```bash
    python JogoAdivinha.py
    ```

Pronto! O jogo começará no seu terminal. Divirta-se!