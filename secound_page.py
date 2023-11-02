import tkinter as tk
from modelo import modelo_ia
# Importação da função para abrir a terceira página
from third_page import abrir_terceira_janela

# Função para abrir a segunda janela
def abrir_segunda_janela(caminho_da_imagem):
    segunda_janela = tk.Tk()
    # Define a cor de fundo da janela
    segunda_janela.configure(bg="#259073")
    segunda_janela.title("Segunda Janela")
    segunda_janela.geometry("1280x800")

    # Exibir o valor de caminho_da_imagem na segunda janela
    caminho_label = tk.Label(segunda_janela, text=f"Valor de caminho_da_imagem: {caminho_da_imagem}")
    caminho_label.pack()

    
    # Atribuindo o valor da análise a variável
    resultado_analise = modelo_ia(caminho_da_imagem)


    # Exibir o resultado da análise
    caminho_label = tk.Label(segunda_janela, text=f"{resultado_analise}")
    caminho_label.pack()
    print(resultado_analise)

    # Aplica delay de 5s, Abre a terceira janela e enviar a variável resultado_analise
    segunda_janela.after(5000, lambda: abrir_terceira_janela(segunda_janela, resultado_analise))

    segunda_janela.mainloop()


