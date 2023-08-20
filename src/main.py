from tkinter import Tk, Button, Label, W, filedialog, messagebox
from tkinter.font import Font
from os import getenv
from shutil import rmtree
from subprocess import call
from time import sleep
import webbrowser


window = Tk()

path_to_save = getenv("APPDATA") + "\..\Local\MissingTranslation"

window.title("Missing Translation Save Manipulation Tool")
window.resizable(False, False)
window.configure(background = "#04819E")

cascadia_font = Font(family = "Cascadia Code", size = 18)

cur_path_lbl = Label(text = f"Current path: {path_to_save}", font = cascadia_font)
cur_path_lbl.configure(background = "#04819E")
cur_path_lbl.grid(column = 0, row = 2, sticky = W, columnspan = 2)

def del_save():
    global path_to_save
    call(["taskkill","/F","/IM","nw.exe"])

    sleep(.5)

    try:
        rmtree(path_to_save)
    except FileNotFoundError:
        messagebox.showerror(title = "Error!", message = "Save doesn't exist!")
        return
    
    messagebox.showinfo(title = "Success!", message = "Save deleted!")
    webbrowser.open("steam://rungameid/395520")

title = Label(text = "Missing Translation SMT", font = ("Cascadia Code", 36))
title.configure(background = "#04819E")
title.grid(column = 0, row = 0, columnspan= 2)

del_save_btn = Button(text = "Delete save", font = cascadia_font, command = del_save)
del_save_btn.configure(background = "#04819E")
del_save_btn.grid(column = 0, row = 1, sticky = W)

window.mainloop()