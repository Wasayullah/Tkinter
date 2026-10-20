from tkinter import *
window = Tk()

window.title("Labels in Tkinter")
label = Label(window,
              text="Hello World",
              font=("Arial",40,"bold"),
              fg="green",bg="black"
              relief=RAISED
              
              )
label.pack()
# label.place(x=100,y=100)

window.mainloop()
