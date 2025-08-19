from tkinter import *
from time import strftime
from datetime import date

# --- Constantes de Cores ---
COR_TEMA_1_FUNDO = "black"
COR_TEMA_1_TEXTO = "white"
COR_TEMA_2_FUNDO = "#000080"  # Azul Marinho
COR_TEMA_2_TEXTO = "#FFFF00"  # Amarelo

# --- Funções ---
def atualizar_relogio():
    """Atualiza a hora a cada segundo."""
    horario_atual = strftime('%H:%M:%S %p')
    rotulo_hora.config(text=horario_atual)
    rotulo_hora.after(1000, atualizar_relogio)

def mudar_cor():
    """Alterna o tema de cores dos rótulos."""
    if rotulo_data.cget("background") == COR_TEMA_1_FUNDO:
        novo_fundo = COR_TEMA_2_FUNDO
        novo_texto = COR_TEMA_2_TEXTO
    else:
        novo_fundo = COR_TEMA_1_FUNDO
        novo_texto = COR_TEMA_1_TEXTO
    
    rotulo_data.config(background=novo_fundo, foreground=novo_texto)
    rotulo_hora.config(background=novo_fundo, foreground=novo_texto)

# --- Configuração da Janela Principal ---
janela = Tk()
janela.title("Relógio Digital")
janela.resizable(False, False)

# --- Widgets (Componentes da Tela) ---
data_atual = date.today().strftime("%d/%m/%Y")

rotulo_data = Label(
    janela,
    text=data_atual,
    font=('calibri', 30, 'bold'),
    background=COR_TEMA_1_FUNDO,
    foreground=COR_TEMA_1_TEXTO,
    pady=10
)
rotulo_data.pack(fill='both')

rotulo_hora = Label(
    janela,
    font=('calibri', 50, 'bold'),
    background=COR_TEMA_1_FUNDO,
    foreground=COR_TEMA_1_TEXTO,
    pady=20,
    padx=20
)
rotulo_hora.pack(fill='both')

botao_mudar_cor = Button(janela, text="Mudar Tema", command=mudar_cor)
botao_mudar_cor.pack(pady=10)

# --- Iniciar o Programa ---
atualizar_relogio()
janela.mainloop()