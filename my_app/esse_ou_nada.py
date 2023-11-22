from tkinter import *
import tkinter as tk
from tkinter import filedialog
import tkinter
from PIL import Image, ImageTk
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tkinterdnd2 import DND_FILES, TkinterDnD
from modelo import modelo_ia, classificacao

file_path = None


# Função para arrastar imagem ao campo e atribuir a variável global o caminho do arquivo
def arrastar_arquivo(event, parent_window):
    global file_path

    try:

        file_path = event.data
        if file_path:
            selected_image = Image.open(file_path)
            selected_image = selected_image.resize((720, 480), resample=Image.LANCZOS)
            abrir_segunda_janela(parent_window, selected_image)
    
    except Exception as e:

        abrir_error_janela(first_Page)

# Função a ser chamada quando o botão "análise" for clicado
def selecionar_arquivo(parent_window):
    global file_path

    try:

        file_path = filedialog.askopenfilename(initialdir="/", title="Selecione um arquivo")
        if file_path:
            selected_image = Image.open(file_path)
            selected_image = selected_image.resize((720, 480), resample=Image.LANCZOS)
            abrir_segunda_janela(parent_window, selected_image)

    except Exception as e:
        abrir_error_janela(first_Page)



################################### SECOUND PAGE #############################################
def abrir_segunda_janela(parent_window, image):
    second_page = Toplevel(parent_window)
    # Define a cor de fundo da janela
    second_page.configure(bg="#259073")
    second_page.title("Trata Lesões - Imagem")
    second_page.geometry("1280x800")

    # Maximiza a janela
    second_page.attributes('-zoomed', True)
    
    try:

        tk_image = ImageTk.PhotoImage(image)
        
        label = Label(second_page, image=tk_image)
        label.image = tk_image
        label.pack()

        imageText = Label(second_page, text=f"Imagem em análise...", justify="left", bg="#259073", fg="white", font='25')
        imageText.pack()

        # Chama a função para analisar a imagem
        modelo_ia(file_path)
        
        
        second_page.after(5000, lambda: close_second_and_open_third(second_page))
        #second_page.after(5, lambda: close_second_and_open_third(second_page))

    except Exception as e:

        abrir_error_janela(second_page)


################################### THIRD PAGE #############################################
def abrir_terceira_janela(parent_window):
    # Cria a terceira janela
    third_page = Toplevel(parent_window)
    third_page.configure(bg="#259073")
    third_page.title("Trata Lesões - Terceira Página")
    third_page.geometry("1280x800")

    # Maximiza a janela
    third_page.attributes('-zoomed', True)

    # Cria uma barra de rolagem vertical
    scrollbar = Scrollbar(third_page)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Cria um canvas para conter os elementos
    canvas = Canvas(third_page, bg="#259073", yscrollcommand=scrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Configura a barra de rolagem para controlar o canvas
    scrollbar.config(command=canvas.yview)

    # Cria um frame dentro do canvas para os rótulos
    frame = Frame(canvas, bg="#259073")
    canvas.create_window(0, 0, anchor=NW, window=frame)

    # Exibe a imagem se o caminho do arquivo existir
    if file_path:
        selected_image = Image.open(file_path)
        selected_image = selected_image.resize((720, 480), resample=Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(selected_image)

        label = Label(frame, image=tk_image, bg="#259073")
        label.image = tk_image
        label.pack()
    
    # Texto classificação
    classificacao_queimadura = tk.Label(frame, text=f"I - GRAU DA QUEIMADURA (CLASSIFICAÇÃO):\n{classificacao[0]}", justify="left", bg="#259073", fg="white")
    classificacao_queimadura.pack(padx=20, pady=20)

    # Texto características
    caracteristicas_queimadura = tk.Label(frame, text=f"II - CARACTERÍSTICAS ({classificacao[4]}):\n{classificacao[1]}", justify="left", bg="#259073", fg="white")
    caracteristicas_queimadura.pack(padx=20, pady=20)

    # Texto Tipos de causa
    causas_queimadura = tk.Label(frame, text=f"III - TIPOS DE CAUSA:\n{classificacao[2]}", justify="left", bg="#259073", fg="white")
    causas_queimadura.pack(padx=20, pady=20)

    # Texto cuidados
    cuidados_queimadura = tk.Label(frame, text=f"IV - CUIDADOS:\n{classificacao[3]}", justify="left", bg="#259073", fg="white")
    cuidados_queimadura.pack(padx=20, pady=20)

    # Texto de porcentagem
    porcentagem_queimadura = tk.Label(frame, text=f"V - PORCENTAGEM COMO CALCULAR (REGRA DOS NOVE)", justify="left", bg="#259073", fg="white")
    porcentagem_queimadura.pack(padx=20, pady=20)


    # Carregar a imagem para o botão
    icone_botao = PhotoImage(file="icon/info.png")
    icone_botao = icone_botao.subsample(icone.width() // 100, icone.height() // 100)
    # Botão para abrir a quarta janela
    botao_quarta_janela = tkinter.Button(frame, image=icone_botao, command=lambda: abrir_quarta_janela(third_page), bg="#259073", bd=0, highlightthickness=0)
    botao_quarta_janela.image = icone_botao  # Salvar a referência para a imagem
    botao_quarta_janela.pack()

    # Atualiza os elementos no frame
    frame.update_idletasks()

    # Define a área do canvas que pode ser rolada
    canvas.config(scrollregion=canvas.bbox("all"))

# Função para fechar a segunda página e abrir a terceira
def close_second_and_open_third(second_page):
    second_page.destroy()
    abrir_terceira_janela(first_Page)




################################### FOURTH PAGE #############################################
def abrir_quarta_janela(parent_window):
    fourth_page = Toplevel(parent_window)
    fourth_page.configure(bg="#259073")
    fourth_page.title("Regra Dos Nove")
    fourth_page.geometry("1280x800")

    # Maximiza a janela
    fourth_page.attributes('-zoomed', True)

    # Cria uma barra de rolagem vertical
    scrollbar = Scrollbar(fourth_page)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Cria um canvas para conter os elementos
    canvas = Canvas(fourth_page, bg="#259073", yscrollcommand=scrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Configura a barra de rolagem para controlar o canvas
    scrollbar.config(command=canvas.yview)

    # Cria um frame dentro do canvas para os rótulos
    frame = Frame(canvas, bg="#259073")
    canvas.create_window(0, 0, anchor=NW, window=frame)

    # Texto da regra dos nove
    texto = """
    V - PORCENTAGEM COMO CALCULAR (REGRA DOS NOVE)
    \n\n    A porcentagem da queimadura se refere à extensão da área do corpo que foi afetada. A detecção \nda porcentagem da lesão tem o objetivo de determinar a gravidade, planejar o tratamento adequado \ne avaliar o risco de complicações. É uma medida útil para os profissionais de saúde entenderem o \ntamanho e a profundidade da queimadura.
    \n    A "Regra dos Nove" é uma técnica usada para estimar a porcentagem de superfície corporal \nqueimada em adultos. Ela divide o corpo em áreas que representam múltiplos de 9%, como \nobservado na figura 5. Para estimar a porcentagem da queimadura em um adulto usando a regra dos \nnove, deve-se avaliar a área queimada em cada uma dessas regiões e, em seguida, soma essas \nporcentagens para obter o total. Por exemplo, se a parte da frente do tronco e um braço foram \nqueimados, você somaria 18% (frente do tronco) com 9% (um braço) para obter 27% de superfície \ncorporal queimada.
    \n    Para crianças, a “regra da palma da mão” é mais precisa, já que a proporção de superfície corporal \nem relação ao tamanho da mão da criança é mais consistente. A palma da mão da criança, incluindo \nos dedos, representa aproximadamente 1% da superfície corporal total. Portanto, para estimar a \nporcentagem de queimadura em uma criança, deve-se usar a mão da criança como referência e \ncomparar a área queimada a ela. Por exemplo, se a área queimada é aproximadamente do tamanho \nda palma da mão da criança, isso representa cerca de 1% da superfície corporal.
    """
    label = Label(frame, text=texto, justify="left", bg="#259073", fg="white", padx=20, pady=20)
    label.pack()

    # Imagem da Regra dos nove
    image_path = "icon/regra_dos_nove.png"  # Caminho da imagem
    imagem = Image.open(image_path)  # Abre a imagem usando o PIL
    tk_image = ImageTk.PhotoImage(imagem)  # Converte a imagem para o formato do Tkinter

    label = Label(frame, image=tk_image)
    label.image = tk_image
    label.pack()

    # Atualiza os elementos no frame
    frame.update_idletasks()

    # Define a área do canvas que pode ser rolada
    canvas.config(scrollregion=canvas.bbox("all"))

    # Função para fechar a terceira página e abrir a quarta
    def close_third_and_open_fourth(third_page):
        third_page.destroy()
        abrir_quarta_janela(first_Page)


################################### ERROR PAGE #############################################
def abrir_error_janela(parent_window):

    error_page = Toplevel(parent_window)
    error_page.configure(bg="#259073")
    error_page.title("Página De Erro")
    error_page.geometry("1280x800")

    # Maximiza a janela
    error_page.attributes('-zoomed', True)


    # Função para fechar a segunda página e abrir a terceira
    def close_second_and_open_third(second_page):
        second_page.destroy()


################################### FIRST PAGE #############################################
# Cria uma instância da janela
first_Page = TkinterDnD.Tk()

# Define a cor de fundo da janela
first_Page.configure(bg="#259073")

# Título da janela
first_Page.title("Home Page")

# Define as dimensões da janela
first_Page.geometry("1280x800")

# Maximiza a janela
first_Page.attributes('-zoomed', True)

# Cria um Canvas como área de soltura
canvas = tkinter.Canvas(first_Page, width=750, height=400, bg="#7FDA89")
canvas.pack(padx=40, pady=75)

# Carregue uma imagem (ícone)
icone = PhotoImage(file="icon/upload-de-arquivo.png")
# Redimensione o ícone para o tamanho desejado
icone_redimensionado = icone.subsample(icone.width() // 100, icone.height() // 100)

# Adicione o ícone ao Canvas no canto superior esquerdo (coordenadas 0, 0)
canvas.create_image(20, 20, anchor="nw", image=icone_redimensionado)

# Registra o Canvas para aceitar arquivos arrastados
canvas.drop_target_register(DND_FILES)
canvas.dnd_bind('<<Drop>>', lambda event: arrastar_arquivo(event, first_Page))

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
botao = tkinter.Button(first_Page, text="Buscar Imagem.", command=lambda: selecionar_arquivo(first_Page), bg="#7FDA89", fg="#FFFFFF")
botao.pack()

# Inicia o loop principal da GUI
first_Page.mainloop()
