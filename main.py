
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, messagebox
# import clipboard


# Global variables

filename = "Unnamed"
unnamed_flag = True

window = Tk()
window.title(filename + " - PyText")
# window.resizable(0, 0)
textbox = ScrolledText(window, width=150, height=40)


# File menu


def cmdNew():

    global filename, unnamed_flag

    x = messagebox.askyesnocancel("Warning!!",
                                  "Do you want to save the current file?")
    if x:
        cmdSave()
    elif x is False:
        pass
    else:
        return

    textbox.delete(1.0, END)

    filename, unnamed_flag = "Unnamed", True
    window.title(filename + " - PyText")


def cmdOpen():

    global filename, unnamed_flag

    x = messagebox.askyesnocancel("Warning!!",
                                  "Do you want to save the current file?")
    if x:
        cmdSave()
    elif x is None:
        return

    fd = filedialog.askopenfile(parent=window, mode="r")
    if fd:
        pass
    else:
        return

    textbox.delete(0.0, END)
    text = fd.read()
    textbox.insert(0.0, text)

    filename, unnamed_flag = fd.name, False
    window.title(filename + " - PyText")


def cmdSave():

    global unnamed_flag, filename

    text = textbox.get(0.0, END)
    if unnamed_flag:
        files = [("All files", "*.*"),
                 ("Text files", ".txt"),
                 ("Python files", ".py")]
        fd = filedialog.asksaveasfile(parent=window,
                                      mode="w",
                                      defaultextension=".txt",
                                      filetypes=files)
        if fd:
            print(fd)
        else:
            return
    else:
        fd = open(filename, "w")
    # else:
    #     fd.mode = "w"

    try:
        fd.write(text)
        print(fd)
    except:
        messagebox.showerror(title="Error",
                             message="Problem writing file!!")
        type(fd)
    finally:
        fd.close()

    unnamed_flag, filename = False, fd.name
    window.title(filename + " - PyText")


def cmdSaveas():

    global unnamed_flag, filename

    text = textbox.get(0.0, END)

    files = [("All files", "*.*"),
             ("Text files", ".txt"),
             ("Python files", ".py")]

    fd = filedialog.asksaveasfile(parent=window,
                                  mode="w",
                                  defaultextension=".txt",
                                  filetypes=files)
    if fd:
        print(fd)
    else:
        return

    try:
        fd.write(text)
    except:
        messagebox.showerror(title="Error", message="Problem writing file!!")

    unnamed_flag, filename = False, fd.name
    window.title(filename + " - PyText")


def cmdExit():
    x = messagebox.askyesnocancel("Warning!!",
                                  "Do you want to save the current file?")
    if x:
        cmdSave()

    window.destroy()


def cmdNew1(event):

    cmdNew()


def cmdOpen1(event):

    cmdOpen()


def cmdSave1(event):

    cmdSave()


def cmdSaveas1(event):

    cmdSaveas()


def cmdPaste():
    pass


def cmdPaste1():
    pass


menuBar = Menu(window)
menuBar2 = Menu(window)
window.configure(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=False)
editMenu = Menu(menuBar, tearoff=False)
helpMenu = Menu(menuBar, tearoff=False)

menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Edit", menu=editMenu)
menuBar.add_cascade(label="Help", menu=helpMenu)

fileMenu.add_command(label="New                      (Ctr+N)",
                     command=cmdNew)
fileMenu.add_command(label="Open                    (Ctr+N)",
                     command=cmdOpen)
fileMenu.add_command(label="Save                      (Ctr+S)",
                     command=cmdSave)
fileMenu.add_command(label="SaveAs       (Ctr+Shift+S)",
                     command=cmdSaveas)
fileMenu.add_command(label="Exit",
                     command=cmdExit)

editMenu.add_command(label="Cut                      (Ctr+X)",
                     command=cmdNew1)
editMenu.add_command(label="Copy                    (Ctr+C)",
                     command=cmdNew1)
editMenu.add_command(label="Paste                      (Ctr+V)",
                     command=cmdNew1)


textbox.pack()
window.bind("<Control_L><n>", cmdNew1)
window.bind("<Control_L><o>", cmdOpen1)
window.bind("<Control_L><s>", cmdSave1)
window.bind("<Control_L><Shift_L><s>", cmdSaveas1)
window.bind("<Control_L><Shift_L><v>", cmdPaste1)

window.mainloop()
