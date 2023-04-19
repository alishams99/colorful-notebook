from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Shams Notebook")
t=Text(window,bg="white")
t.pack()
window.geometry("300x300")


#colors
def red_c():
    t.config(bg="red")

def white_c():
    t.config(bg="white")

def green_c():
    t.config(bg="green")

def yellow_c():
    t.config(bg="yellow")

def blue_c():
    t.config(bg="blue")


#Save in txt file
def save():
    f = open("Shams_notebook.txt","w")
    f.write(t.get(1.0,END))
    messagebox.showinfo("Save","Your text saved!")

def e1():
    answer = messagebox.askquestion("Exit","Are you sure to exit?") 
    if answer == "yes":
        exit()
menubar = Menu(window)


#main menu

#colors
filemenu= Menu(menubar,tearoff=0)
filemenu.add_command(label="Red",command=red_c)
filemenu.add_command(label="Blue",command=blue_c)
filemenu.add_command(label="Yellow",command=yellow_c)
filemenu.add_command(label="White",command=white_c)
filemenu.add_command(label="Green",command=green_c)
menubar.add_cascade(label="Color Box",menu=filemenu)

#other button
menubar.add_command(label="Save",command=save)
menubar.add_command(label="Exit",command=e1)

window.config(menu=menubar)
window.mainloop()