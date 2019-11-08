from tkinter import *
import tkinter.messagebox
root = Tk()
tkinter.messagebox.showinfo("Window Title", "Monkeys cn live up to 300 years")
answer = tkinter.messagebox.askquestion('Question1', 'Do you like silly faces?')
if answer == 'yes':
    print('nice')



root.mainloop()