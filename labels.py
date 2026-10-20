from tkinter import *
window = Tk()
window.geometry("400x200")
label = Label(window,text="Hello World",font=("Arial",40,"bold"),fg="green",bg="black")
label.pack()
# label.place(x=100,y=100)

window.mainloop()
