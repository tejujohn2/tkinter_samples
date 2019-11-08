from tkinter import *
root = Tk()
def doNothing():
    print("ok ok, I wont")

menu = Menu(root)
root.config(menu = menu)
subMenu = Menu(menu)
subMenu = Menu(menu, tearoff=0)
menu.add_cascade(label = "File", menu=subMenu)
subMenu.add_command(label="New Project", command=doNothing)
subMenu.add_command(label="New..", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
editMenu = Menu(menu, tearoff=0)
menu.add_cascade(label = "Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()