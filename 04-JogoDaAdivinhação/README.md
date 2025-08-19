# 04 - Jogo da Adivinhação

Este é um clássico jogo "Adivinhe o Número" desenvolvido em Python para ser executado no terminal, com uma estrutura robusta que permite múltiplas partidas.

## ✨ Funcionalidades

-   **Número Aleatório:** Sorteia um número secreto entre 1 e 100 a cada nova partida.
-   **Dicas Interativas:** Fornece dicas de "Mais alto!" ou "Mais baixo!" a cada palpite.
-   **Limite e Contador de Tentativas:** O jogador tem 10 tentativas, e o jogo informa o andamento.
-   **Validação de Entrada:** O programa não quebra se o usuário digitar um texto, pedindo uma entrada válida.
-   **Opção de Jogar Novamente:** Ao final de cada partida, o jogador pode escolher começar um novo jogo.

## 🛠️ Tecnologias e Conceitos Praticados

-   **Python 3** e o módulo **`random`**.
-   Estrutura de jogo com um **loop `while` principal** e uma **função** para cada partida.
-   Tratamento de erros com **`try-except`**.

## 🚀 Como Executar

1.  Navegue até a pasta do projeto.
2.  Execute o script no terminal:
    ```bash
    python Adivinha.py
    ```
3.  Siga as instruções no terminal para jogar.