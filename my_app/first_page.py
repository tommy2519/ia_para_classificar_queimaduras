import tkinter as tk
from tkinter import filedialog, Canvas, PhotoImage
#from secound_page import abrir_segunda_janela
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk


# Variável global para armazenar o valor do arquivo da imagem
caminho_da_imagem = ""

# Função para arrastar imagem ao campo e atribuir a variável global o caminho do arquivo
def arrastar_arquivo(event):
    global caminho_da_imagem
    caminho_da_imagem = event.data
    if caminho_da_imagem:
        from secound_page import abrir_segunda_janela
        abrir_segunda_janela(caminho_da_imagem)


# Função a ser chamada quando o botão "análise" for clicado
def selecionar_arquivo(parent_window):
    global caminho_da_imagem  # Usando a variável global
    caminho_da_imagem = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.png *.jpeg")])
    if caminho_da_imagem:
        print("#"*40)
        print("na primeira página- ", caminho_da_imagem)
        print("#"*40)
    #    rotulo.config(text=f"Imagem selecionada: {caminho_da_imagem}")
        # Abrir a terceira janela ao finalizar a função
    #    abrir_segunda_janela(caminho_da_imagem)
        selected_image = Image.open(caminho_da_imagem)
        selected_image = selected_image.resize((720, 480), resample=Image.LANCZOS)
        from secound_page import abrir_segunda_janela
        abrir_segunda_janela(parent_window,caminho_da_imagem, selected_image)

def abrir_primeira_janela(Canvas):
    
    # Cria uma instância da janela
    janela = TkinterDnD.Tk()

    # Define a cor de fundo da janela
    janela.configure(bg="#259073")

    # Título da janela
    janela.title("Home Page")

    # Define as dimensões da janela
    janela.geometry("1280x800")

    # Cria um Canvas como área de soltura
    canvas = tk.Canvas(janela, width=750, height=400, bg="#7FDA89")
    canvas.pack(padx=40, pady=75)

    # Carregue uma imagem (ícone)
    icone = PhotoImage(file="icon/upload-de-arquivo.png")
    # Redimensione o ícone para o tamanho desejado
    icone_redimensionado = icone.subsample(icone.width() // 100, icone.height() // 100)

    # Adicione o ícone ao Canvas no canto superior esquerdo (coordenadas 0, 0)
    canvas.create_image(20, 20, anchor="nw", image=icone_redimensionado)

    # Registra o Canvas para aceitar arquivos arrastados
    canvas.drop_target_register(DND_FILES)
    canvas.dnd_bind('<<Drop>>', arrastar_arquivo)

    # Adicione um texto dentro do Canvas
    texto = "Arraste uma imagem aqui."
    texto_id = canvas.create_text(150, 150, text=texto, font=("Arial", 25), fill="white")

    # Obtenha as dimensões do Canvas
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight()

    # Calcule a posição central do Canvas
    x_center = canvas_width / 2
    y_center = canvas_height / 2

    # Atualize a posição do texto para o centro
    canvas.coords(texto_id, x_center, y_center)

    # Botão de Fazer Análise
    botao = tk.Button(janela, text="Buscar Imagem.", command=lambda: selecionar_arquivo(janela), bg="#7FDA89", fg="#FFFFFF")
    botao.pack()

    # Realizar o evento da ação do botão "análise"
    #rotulo.bind("<Button-1>", mostrar_mensagem)



    # Inicia o loop principal da GUI
    janela.mainloop()


abrir_primeira_janela(Canvas)
