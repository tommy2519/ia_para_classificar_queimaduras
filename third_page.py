import tkinter as tk
from modelo import classificacao


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
    # caminho_label = tk.Label(terceira_janela, text=f"{resultado_analise}")
    # caminho_label.pack()

    # Crie um Canvas para posicionar os Labels
    canvas = tk.Canvas(terceira_janela, bg="#259073")
    canvas.pack(fill="both", expand=True)

    # Texto classificação
    classificacao_queimadura = tk.Label(terceira_janela, text=f"I - GRAU DA QUEIMADURA (CLASSIFICAÇÃO):\n{classificacao[0]}", justify="left", bg="#259073", fg="white")
    classificacao_queimadura_id = canvas.create_window(20, 20, anchor="nw", window=classificacao_queimadura)

    # Texto características
    caracteristicas_queimadura = tk.Label(terceira_janela, text=f"II - CARACTERÍSTICAS ({classificacao[4]}):\n{classificacao[1]}", justify="left", bg="#259073", fg="white")
    caracteristicas_queimadura_id = canvas.create_window(20, 80, anchor="nw", window=caracteristicas_queimadura)

    # Texto Tipos de causa
    causas_queimadura = tk.Label(terceira_janela, text=f"III - TIPOS DE CAUSA:\n{classificacao[2]}", justify="left", bg="#259073", fg="white")
    causas_queimadura_id = canvas.create_window(20, 260, anchor="nw", window=causas_queimadura)

    # Texto cuidados
    cuidados_queimadura = tk.Label(terceira_janela, text=f"IV - CUIDADOS:\n{classificacao[3]}", justify="left", bg="#259073", fg="white")
    cuidados_queimadura_id = canvas.create_window(20, 390, anchor="nw", window=cuidados_queimadura)

    # Texto de porcentagem
    porcentagem_queimadura = tk.Label(terceira_janela, text=f"V - PORCENTAGEM COMO CALCULAR (REGRA DOS NOVE)", justify="left", bg="#259073", fg="white")
    porcentagem_queimadura_id = canvas.create_window(20, 540, anchor="nw", window=porcentagem_queimadura)



    terceira_janela.mainloop()
