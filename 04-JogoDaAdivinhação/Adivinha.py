import random

def jogo():
    print("\n--- Nova Partida! ---")
    print("Eu pensei em um número entre 1 e 100. Você tem 10 tentativas.")

    numero_secreto = random.randint(1, 100)
    tentativas = 0

    # Loop da partida
    while tentativas < 10:
        try:
            adivinhe = int(input("Qual o seu palpite? "))
            tentativas += 1

            if adivinhe < numero_secreto:
                print(f"Mais alto! Tentativa {tentativas} de 10.")
            elif adivinhe > numero_secreto:
                print(f"Mais baixo! Tentativa {tentativas} de 10.")
            else:
                print(f"Você acertou o número {numero_secreto} com {tentativas} tentativa(s)! ")
                return #Encerra a funçao

        except ValueError: # Valores Invalidos
            print("Entrada inválida! Por favor, digite apenas um número.")

    print(f"Fim das tentativas! O número era {numero_secreto}.")

while True:
    jogo()

    jogar_novamente = input("Deseja jogar novamente? [S/N]: ").strip().upper()

    if jogar_novamente != "S":
        break  # Encerra o loop

print("\nObrigado por jogar!")