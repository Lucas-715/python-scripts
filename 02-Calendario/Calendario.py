import calendar

print("- Visualizador de Calendário -")

while True:
    try:
        ano = int(input("Digite o Ano: "))
        mes = int(input("Digite o Mês (1-12): "))
        
        if 1 <= mes <= 12:
            # Design do Calendario
            print("\n" + "="*20)
            print(calendar.month(ano, mes))
            print("="*20)
            break
        else:
            print("Erro: O mês deve ser um número entre 1 e 12.")

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números para o ano e o mês.")