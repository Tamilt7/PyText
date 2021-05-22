
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, messagebox

window = Tk()
window.title("PyText")
window.resizable(0, 0)

textbox = ScrolledText(window, width=150, height=40)


# File menu


def cmdNew():
    pass
    textbox.delete(1.0, END)


def cmdOpen():
    fd = filedialog.askopenfile(parent=window)
    text = fd.read()
    textbox.delete(1.0, END)
    textbox.insert(1.0, text)


def cmdSave():
    fd = filedialog.asksaveasfile(parent=window, mode="w", defaultextension=".txt")
    text = textbox.get(0.0, END)
    try:
        fd.write(text)
    except:
        messagebox.showerror(title="Error", message="Problem writing file!!")

def cmdSaveas():
    pass


def cmdExit():
    window.destroy()











menuBar = Menu(window)
window.configure(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=False)
editMenu = Menu(menuBar, tearoff=False)
helpMenu = Menu(menuBar, tearoff=False)

menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Edit", menu=editMenu)
menuBar.add_cascade(label="Help", menu=helpMenu)

fileMenu.add_command(label="New", command=cmdNew)
fileMenu.add_command(label="Open", command=cmdOpen)
fileMenu.add_command(label="Save", command=cmdSave)
fileMenu.add_command(label="SaveAs", command=cmdSaveas)
fileMenu.add_command(label="Exit", command=cmdExit)

textbox.pack()
window.mainloop()

