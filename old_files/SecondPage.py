from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import ThirdPage
import FirstPage
import modelo

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

def close_second_and_open_third(second_page):
    second_page.destroy()
    ThirdPage.display_image_in_third_page(FirstPage.firstPage)
