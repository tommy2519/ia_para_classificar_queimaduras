from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import modelo

file_path = None

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

    result_text = modelo.modelo_ia(file_path)
    result_label = Label(third_page, text=result_text)
    result_label.grid(column=0, row=1)
