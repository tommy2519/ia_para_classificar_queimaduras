import tkinter as tk
from modelo import modelo_ia
from PIL import Image, ImageTk
from tensorflow.keras.preprocessing import image

# Importação da função para abrir a terceira página
#from third_page import abrir_terceira_janela

# Função para abrir a segunda janela
def abrir_segunda_janela(parent_window,caminho_da_imagem, selected_image):

    
    print("#"*40)
    print("na segunda página- ", caminho_da_imagem)
    print("#"*40)

    segunda_janela = tk.Toplevel(parent_window)
    segunda_janela.configure(bg="#259073")
    segunda_janela.title("Segunda Janela")
    segunda_janela.geometry("1280x800")

    # Utiliza o mesmo Canvas da primeira janela
    #canvas_segunda_janela = tk.Canvas(segunda_janela, width=750, height=400, bg="#7FDA89")
    #canvas_segunda_janela.pack()





    # Carregar a imagem usando o caminho fornecido
    imagem_pil = Image.open(selected_image)
    # Converter a imagem para o formato suportado pelo tkinter
    global tk_image  # Referência global para evitar a perda da imagem
    tk_image = ImageTk.PhotoImage(imagem_pil)
    
    label = tk.Label(segunda_janela, image=tk_image)
    label.image = tk_image
    label.grid(column=0, row=0)




    # Texto de aviso da análise sobre a imagem
    caminho_label = tk.Label(segunda_janela, text=f"Imagem em análise...", justify="left", bg="#259073", fg="white", font='25')
    caminho_label.pack()

    # Atribuindo o valor da análise a variável
    resultado_analise = modelo_ia(caminho_da_imagem)

    from third_page import abrir_terceira_janela
    # Aplica delay de 5s, Abre a terceira janela e enviar a variável resultado_analise
    segunda_janela.after(5000, lambda: abrir_terceira_janela(segunda_janela, resultado_analise))

    segunda_janela.mainloop()