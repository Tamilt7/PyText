
from tkinter import *
from tkinter.scrolledtext import ScrolledText

window = Tk()
window.title("PyText")
window.resizable(0, 0)

textbox = ScrolledText(window, width=150, height=40)
textbox.pack()

window.configure(bg="blue")
window.mainloop()
