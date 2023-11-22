import tkinter as tk
from tkinter import filedialog, Canvas, PhotoImage
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk

def arrastar_arquivo(event, abrir_segunda_janela):
    # Obtém o caminho do arquivo a partir do evento de arrastar e soltar
    caminho_da_imagem = event.data
    if caminho_da_imagem:
        # Chama a função para abrir a segunda janela com o caminho da imagem
        abrir_segunda_janela(caminho_da_imagem)

def selecionar_arquivo(abrir_segunda_janela, canvas):
    # Abre a caixa de diálogo para selecionar um arquivo
    caminho_da_imagem = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.png *.jpeg")])
    if caminho_da_imagem:
        # Chama a função para abrir a segunda janela com o caminho da imagem
        abrir_segunda_janela(caminho_da_imagem, canvas)

def voltar_janela(terceira_janela, abrir_primeira_janela):
    # Fecha a terceira janela e abre a primeira
    terceira_janela.destroy()
    abrir_primeira_janela()

def abrir_primeira_janela():
    # Configurações iniciais da primeira janela
    janela = TkinterDnD.Tk()
    janela.configure(bg="#259073")
    janela.title("Home Page")
    janela.geometry("1280x800")

    # Configuração do canvas para arrastar e soltar
    canvas = tk.Canvas(janela, width=750, height=400, bg="#7FDA89")
    canvas.pack(padx=40, pady=75)

    # Ícone para indicar área de arrastar
    icone = PhotoImage(file="icon/upload-de-arquivo.png")
    icone_redimensionado = icone.subsample(icone.width() // 100, icone.height() // 100)
    canvas.create_image(20, 20, anchor="nw", image=icone_redimensionado)

    # Configuração do comportamento de arrastar e soltar no canvas
    canvas.drop_target_register(DND_FILES)
    canvas.dnd_bind('<<Drop>>', lambda event: arrastar_arquivo(event, abrir_segunda_janela))

    # Texto indicativo no canvas
    texto = "Arraste uma imagem aqui."
    texto_id = canvas.create_text(150, 150, text=texto, font=("Arial", 25), fill="white")

    # Centraliza o texto no canvas
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight()
    x_center = canvas_width / 2
    y_center = canvas_height / 2
    canvas.coords(texto_id, x_center, y_center)

    # Botão para selecionar um arquivo
    botao = tk.Button(janela, text="Buscar Imagem.", command=lambda: selecionar_arquivo(abrir_segunda_janela, canvas), bg="#7FDA89", fg="#FFFFFF")
    botao.pack()

    # Inicia o loop da primeira janela
    janela.mainloop()

def abrir_segunda_janela(caminho_da_imagem, canvas):
    # Configurações iniciais da segunda janela
    segunda_janela = tk.Tk()
    segunda_janela.configure(bg="#259073")
    segunda_janela.title("Segunda Janela")
    segunda_janela.geometry("1280x800")

    # Canvas para a segunda janela
    canvas_segunda = tk.Canvas(segunda_janela, width=750, height=400, bg="#7FDA89")
    canvas_segunda.pack()

    # Label indicando que a imagem está em análise
    caminho_label = tk.Label(segunda_janela, text=f"Imagem em análise...", justify="left", bg="#259073", fg="white", font='25')
    caminho_label.pack()

    # Abre a imagem no canvas da segunda janela
    imagem_pil = Image.open(caminho_da_imagem)
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    canvas_segunda.imagem_tk = imagem_tk
    canvas_segunda.create_image(0, 0, anchor="nw", image=imagem_tk)

    # Aguarda 5 segundos antes de abrir a terceira janela
    segunda_janela.after(5000, lambda: abrir_terceira_janela(segunda_janela))

    # Inicia o loop da segunda janela
    segunda_janela.mainloop()

def abrir_terceira_janela(segunda_janela):
    # Esconde a segunda janela
    segunda_janela.withdraw()

    # Configurações iniciais da terceira janela
    terceira_janela = tk.Tk()
    terceira_janela.title("Terceira Janela")
    terceira_janela.geometry("1280x800")

    # Canvas para a terceira janela
    canvas_terceira = tk.Canvas(terceira_janela, bg="#259073")
    canvas_terceira.pack(fill="both", expand=True)

    # Abre uma imagem fixa na terceira janela (ajuste conforme necessário)
    imagem_pil = Image.open("/home/tommy/Documentos/ProjetoTcc/reconhecer_queimadura/cnn_reconhecimento_de_placas/imagem3.png")
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    canvas_terceira.imagem_tk = imagem_tk
    canvas_terceira.create_image(0, 0, anchor="nw", image=imagem_tk)

    # Botão para voltar à primeira janela
    botao = tk.Button(terceira_janela, text="VOLTAR", command=lambda: voltar_janela(terceira_janela, abrir_primeira_janela), bg="#7FDA89", fg="#FFFFFF")
    botao.pack()

    # ... (Outros elementos)

    # Inicia o loop da terceira janela
    terceira_janela.mainloop()

# Inicia a primeira janela
abrir_primeira_janela()
