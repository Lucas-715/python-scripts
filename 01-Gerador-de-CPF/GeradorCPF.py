#gerador de cpfs 
import random # Necessário para gerar números aleatórios.

# Cria uma lista com 9 números aleatórios de 0 a 9.
digitos = [random.randint(0, 9) for _ in range(9)]

# Define uma função que transforma a lista de dígitos em texto.
def gerar_cpf():
    CPF = ""
    # Junta cada dígito da lista em uma string.
    for i in range(9):
        CPF = CPF + str(digitos[i])
    return CPF

# Chama a função para criar a base do CPF.
CPF = gerar_cpf()

# Calcula o primeiro dígito verificador (DV1).
DV1 = ((int(CPF[0]) * 10 + int(CPF[1]) * 9 + int(CPF[2]) * 8 + int(CPF[3]) * 7 + int(CPF[4]) * 6 + int(CPF[5]) * 5 + int(CPF[6]) * 4 + int(CPF[7]) * 3 + int(CPF[8]) * 2 )) * 10 % 11

# Se o resultado for 10 ou 11, o dígito vira 0.
if DV1 >= 10:
    DV1 = 0

# Adiciona o DV1 ao final do CPF.
CPF = CPF + str(DV1)
    
# Calcula o segundo dígito verificador (DV2), agora com 10 dígitos.
DV2 = ((int(CPF[0]) * 11 + int(CPF[1]) * 10 + int(CPF[2]) * 9 + int(CPF[3]) * 8 + int(CPF[4]) * 7 + int(CPF[5]) * 6 + int(CPF[6]) * 5 + int(CPF[7]) * 4 + int(CPF[8]) * 3 + int(CPF[9]) * 2 )) * 10 % 11

# Novamente, se o resultado for 10 ou 11, o dígito vira 0.
if DV2 >= 10:
    DV2 = 0

# Adiciona o DV2, completando o CPF.
CPF = CPF + str(DV2)
    
# Mostra o CPF final como um número inteiro.
print(int(CPF))