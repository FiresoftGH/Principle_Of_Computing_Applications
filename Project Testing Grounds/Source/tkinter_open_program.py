from tkinter import *
from tkinter import filedialog
import os

window = Tk()
window.title("Open Other Programs")
window.geometry("300x300")

def open_program():
    program_1 = filedialog.askopenfile()
    label_1.config(text = program_1)
    os.system(program_1)

button_1 = Button(window, text = "Open Program 1", command = open_program)
button_1.pack(pady = 20)

label_1 = Label(window, text = "")
label_1.pack(pady = 20)
window.mainloop()