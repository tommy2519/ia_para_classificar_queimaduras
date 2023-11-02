from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

file_path = None

def searchFile(parent_window):
    global file_path
    file_path = filedialog.askopenfilename(initialdir="/", title="Selecione um arquivo")
    if file_path:
        selected_image = Image.open(file_path)
        selected_image = selected_image.resize((720, 480), resample=Image.LANCZOS)
        display_image(parent_window, selected_image)

def modelo_ia():
    # Carregar o modelo treinado
    model = tf.keras.models.load_model('modelo_v3.h5')

    # Caminho para a imagem a ser testada
    test_image_path = file_path

    # Carregar e pré-processar a imagem
    img = image.load_img(test_image_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    # Fazer a previsão
    prediction = model.predict(img_array)

    # Mapear os índices das classes para os graus de queimadura
    class_labels = {0: 'Primeiro Grau', 1: 'Segundo Grau', 2: 'Terceiro Grau'}
    predicted_class = np.argmax(prediction)

    return f"A queimadura é classificada como: {class_labels[predicted_class]}"

def display_image(parent_window, image):
    second_page = Toplevel(parent_window)
    second_page.title("Trata Lesões - Imagem")
    second_page.geometry("1280x800")
    
    tk_image = ImageTk.PhotoImage(image)
    
    label = Label(second_page, image=tk_image)
    label.image = tk_image
    label.grid(column=0, row=0)

    imageText = Label(second_page, text="Imagem em análise...")
    imageText.grid(column=0, row=1)

    

    second_page.after(5000, lambda: close_second_and_open_third(second_page))

def display_image_in_third_page(parent_window):
    third_page = Toplevel(parent_window)
    third_page.title("Trata Lesões - Terceira Página")
    third_page.geometry("1280x800")

    if file_path:
        selected_image = Image.open(file_path)
        selected_image = selected_image.resize((720, 480), resample=Image.LANCZOS)

        tk_image = ImageTk.PhotoImage(selected_image)

        label = Label(third_page, image=tk_image)
        label.image = tk_image
        label.grid(column=0, row=0)

    result_text = modelo_ia()
    result_label = Label(third_page, text=result_text)
    result_label.grid(column=0, row=1)

def close_second_and_open_third(second_page):
    second_page.destroy()
    display_image_in_third_page(firstPage)

firstPage = Tk()
firstPage.title("Trata Lesões")
firstPage.geometry("1280x800")

imageText = Label(firstPage, text="Arraste sua Imagem Aqui.")
imageText.grid(column=0, row=0)

searchFileButton = Button(firstPage, text="Buscar Arquivo", background="#7FDA89", command=lambda: searchFile(firstPage))
searchFileButton.grid(column=0, row=1)

firstPage.mainloop()
