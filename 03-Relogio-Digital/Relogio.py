from tkinter import *
from time import strftime
from datetime import date

# Função para mostrar a data
def atualizar_data():
    data_atual = date.today().strftime("%d/%m/%Y")
    rotulo_data.config(text=data_atual)

# Função para atualizar o relógio
def atualizar_relogio():
    horario_atual = strftime('%H:%M:%S %p')
    rotulo_hora.config(text=horario_atual)
    rotulo_hora.after(1000, atualizar_relogio)  # atualiza a cada 1 segundo

# Função para mudar a cor dos rótulos
def mudar_cor():
    # Alterna entre duas cores
    if rotulo_data.cget("background") == "black":
        rotulo_data.config(background="blue", foreground="yellow")
        rotulo_hora.config(background="blue", foreground="yellow")
    else:
        rotulo_data.config(background="black", foreground="white")
        rotulo_hora.config(background="black", foreground="white")

# Criação da janela principal
janela = Tk()
janela.title("Relógio Digital Simples")

# Rótulo para exibir a data
rotulo_data = Label(
    janela,
    font=('calibri', 30, 'bold'),
    background="black",
    foreground='white'
)
rotulo_data.pack(anchor='center')

# Rótulo para exibir o horário
rotulo_hora = Label(
    janela,
    font=('calibri', 40, 'bold'),
    background="black",
    foreground='white'
)
rotulo_hora.pack(anchor='center')

# Cria um botão que muda a cor
botao = Button(janela, text="Mudar Cor", command=mudar_cor)
botao.pack(pady=10)

# Iniciar a atualização
atualizar_data()
atualizar_relogio()

# Iniciar o loop da interface gráfica
janela.mainloop()
