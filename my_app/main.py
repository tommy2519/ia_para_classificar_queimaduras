import tkinter as tk
from first_page import abrir_primeira_janela
from secound_page import abrir_segunda_janela
from third_page import abrir_terceira_janela

if __name__ == "__main__":
    root = tk.Tk()
    app = abrir_primeira_janela(root)
    root.mainloop()
