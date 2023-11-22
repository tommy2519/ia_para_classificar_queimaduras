import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def abrir_arquivo():
    caminho_da_imagem = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.png *.jpeg")])
    if caminho_da_imagem:
        carregar_imagem(caminho_da_imagem)

def carregar_imagem(caminho_da_imagem):
    imagem_pil = Image.open(caminho_da_imagem)
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    canvas.create_image(0, 0, anchor="nw", image=imagem_tk)
    canvas.imagem_tk = imagem_tk  # Mantém uma referência à imagem para evitar a coleta de lixo

# Cria uma instância da janela
janela = tk.Tk()
janela.title("Exibir Imagem")
janela.geometry("800x600")




# Cria um botão para abrir o arquivo
botao = tk.Button(janela, text="Selecionar Imagem", command=abrir_arquivo)
botao.pack()

# Cria um Canvas para exibir a imagem
canvas = tk.Canvas(janela, width=750, height=400, bg="#7FDA89")
#canvas.pack(padx=40, pady=75)
canvas.pack()

carregar_imagem("/home/tommy/Documentos/ProjetoTcc/reconhecer_queimadura/cnn_reconhecimento_de_placas/imagem3.png")

# Utiliza o mesmo Canvas da primeira janela
canvas_segunda_janela = tk.Canvas(janela, width=750, height=400, bg="#7FDA89")
canvas_segunda_janela.pack()

# Cria a imagem e a adiciona ao Canvas
imagem_pil = Image.open("/home/tommy/Documentos/ProjetoTcc/reconhecer_queimadura/cnn_reconhecimento_de_placas/imagem3.png")
imagem_tk = ImageTk.PhotoImage(imagem_pil)
canvas_segunda_janela.imagem_tk = imagem_tk  # Mantém uma referência à imagem para evitar a coleta de lixo
canvas_segunda_janela.create_image(0, 0, anchor="nw", image=imagem_tk)

# Inicia o loop principal da GUI
janela.mainloop()
