from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import SecondPage

file_path = None

def searchFile(parent_window):
    global file_path
    file_path = filedialog.askopenfilename(initialdir="/", title="Selecione um arquivo")
    if file_path:
        selected_image = Image.open(file_path)
        selected_image = selected_image.resize((720, 480), resample=Image.LANCZOS)
        SecondPage.display_image(parent_window, selected_image)
