from tkinter import *
root = Tk()
root.geometry('500x300+500+200')
##main Menu
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

##The tool bar
toolbar = Frame(root, bg="blue")
insertButton = Button(toolbar, text="Insert a Image", command=doNothing)
insertButton.pack(side=LEFT, padx=2, pady=2)
printButton =Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)


## The Status Bar

status = Label(root, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
root.mainloop()

