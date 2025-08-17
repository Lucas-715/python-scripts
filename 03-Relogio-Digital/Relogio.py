from tkinter import *
from time import strftime

# Função para atualizar o relógio
def atalizar_relogio():
    horario_atual = strftime('%H:%M:%S %p')
    rotulo_relogio.config(text=horario_atual)
    rotulo_relogio.after(1000, atalizar_relogio)

# Criação da janela principal
janela = Tk()
janela.title("Relógio Digital Simples")

# Criação do rótulo para exibir o horário
rotulo_relogio = Label(
    janela, 
    font=('calibri', 40, 'bold'), 
    background="black",
    foreground='white'
    )

# Posiciona o rótulo no centro da janela
rotulo_relogio.pack(anchor='center')

# Iniciar a atualização do relógio
atalizar_relogio()

# Iniciar o loop da interface gráfica
janela.mainloop()
