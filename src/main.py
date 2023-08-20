from tkinter import Tk, Button, Label, W, filedialog, messagebox
from tkinter.font import Font
import shutil

window = Tk()
path_to_save = ""

window.title("Missing Translation Save Manipulation Tool")
window.resizable(False, False)
window.configure(background = "#04819E")

cascadia_font = Font(family = "Cascadia Code", size = 18)

cur_path_lbl = Label(text = "Current path: ", font = cascadia_font)
cur_path_lbl.configure(background = "#04819E")
cur_path_lbl.grid(column = 0, row = 2, sticky = W, columnspan = 2)

def pick_path():
    global path_to_save, cur_path_lbl
    prev_path = path_to_save
    path_to_save = filedialog.askdirectory()
    if "MissingTranslation" not in path_to_save and path_to_save != "":
        messagebox.showerror(title = "Error!", message = "Invalid path!")
        path_to_save = prev_path
    else:
        cur_path_lbl.configure(text = f"Current path: {path_to_save}")
        cur_path_lbl.update()

def del_save():
    global path_to_save
    try:
        shutil.rmtree(path_to_save)
    except FileNotFoundError:
        messagebox.showerror(title = "Error!", message = "Empty/Invalid path!")
        return
    except PermissionError:
        messagebox.showerror(title = "Erorr!", message = "Please close the game before manipulating the save!")
        return
    
    messagebox.showinfo(title = "Success!", message = "Save deleted!")

title = Label(text = "Missing Translation SMT", font = ("Cascadia Code", 36))
title.configure(background = "#04819E")
title.grid(column = 0, row = 0, columnspan= 2)

pick_path_btn = Button(text = "Pick save path", font = cascadia_font, command = pick_path)
pick_path_btn.configure(background = "#04819E")
pick_path_btn.grid(column = 1, row = 1)

del_save_btn = Button(text = "Delete save", font = cascadia_font, command = del_save)
del_save_btn.configure(background = "#04819E")
del_save_btn.grid(column = 0, row = 1, sticky = W)

window.mainloop()