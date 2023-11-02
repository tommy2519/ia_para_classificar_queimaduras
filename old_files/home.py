from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import FirstPage

file_path = None

firstPage = Tk()
firstPage.title("Trata Lesões")
firstPage.geometry("1280x800")

imageText = Label(firstPage, text="Arraste sua Imagem Aqui")
imageText.grid(column=0, row=0)

searchFileButton = Button(firstPage, text="Buscar Arquivo", background="#7FDA89", command=lambda: FirstPage.searchFile(firstPage))
searchFileButton.grid(column=0, row=1)

firstPage.mainloop()
