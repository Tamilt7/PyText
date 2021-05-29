
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, messagebox


# Global variables

filename = "Unnamed"
fd = None


window = Tk()
window.title(filename + " - PyText")
window.resizable(0, 0)
textbox = ScrolledText(window, width=150, height=40)


# File menu


def cmdNew():
    global fd
    x = messagebox.askyesnocancel("Warning!!", "Do you want to save the current file?")
    if x:
        cmdSave()
    elif x is False:
        pass
    else:
        return

    fd = None
    textbox.delete(1.0, END)


def cmdOpen():
    global fd
    x = messagebox.askyesnocancel("Warning!!", "Do you want to save the current file?")
    if x:
        cmdSave()
    elif x is None:
        return
    fd = filedialog.askopenfile(parent=window, mode="r")
    text = fd.read()
    textbox.delete(0.0, END)
    textbox.insert(0.0, text)


def cmdSave():
    global fd
    text = textbox.get(0.0, END)
    if fd is None:
        files = [("All files", "*.*"), ("Text files", ".txt"), ("Python files", ".py")]
        fd = filedialog.asksaveasfile(parent=window, mode="w", defaultextension=".txt", filetypes=files)
        if fd:
            print(fd)
        else:
            return
    # else:
    #     fd.mode = "w"

    try:
        fd.write(text)
        print(fd)
    except:
        messagebox.showerror(title="Error", message="Problem writing file!!")
        type(fd)


def cmdSaveas():
    global fd
    text = textbox.get(0.0, END)

    files = [("All files", "*.*"), ("Text files", ".txt"), ("Python files", ".py")]
    fd = filedialog.asksaveasfile(parent=window, mode="w", defaultextension=".txt", filetypes=files)
    if fd:
        print(fd)
    else:
        return

    try:
        fd.write(text)
    except:
        messagebox.showerror(title="Error", message="Problem writing file!!")


def cmdExit():
    x = messagebox.askyesnocancel("Warning!!", "Do you want to save the current file?")
    if x:
        cmdSave()
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

