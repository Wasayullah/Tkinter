from tkinter import *
window = Tk()
photo = PhotoImage(file="logo.png")
window.title("Labels in Tkinter")
label = Label(window,
              text="Hello World",
              font=("Arial",40,"bold"),
              fg="green",bg="black",
              relief=SUNKEN,
              bd=10,
              padx=12,
              pady=12,
              image=photo
              )
label.pack()
# label.place(x=100,y=100)

window.mainloop()
