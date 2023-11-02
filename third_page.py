import tkinter as tk


# Função para abrir a terceira janela
def abrir_terceira_janela(janela_segunda,resultado_analise):
    janela_segunda.withdraw()  # Oculta a segunda janela
    terceira_janela = tk.Tk()
    # Define a cor de fundo da janela
    terceira_janela.configure(bg="#259073")
    terceira_janela.title("Terceira Janela")
    terceira_janela.geometry("1280x800")

    # ... código para a terceira janela ...

    # Exibir o resultado da análise
    caminho_label = tk.Label(terceira_janela, text=f"{resultado_analise}")
    caminho_label.pack()

    terceira_janela.mainloop()
