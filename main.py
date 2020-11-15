# Tha main application's program

from tkinter import *
window=Tk()

def _init_:
  # Code to add widgets
  btn1=Button(window, text="Button 1", fg="blue")
  btn1.place(x=150, y=250)
  btn2=Button(window, text="Button 2", fg="green")
  btn2.place(x=300, y=250)
  title=Label(window, text="Label Widget", fg="black", font=("Arial", 16))
  title.place(x=175, y=95)
  txtfield=Entry(window, text="Entry widget", bd=2)
  txtfield.place(x=190, y=150)

window.title('Sample Window')
window.geometry("500x400+10+20")
window.mainloop()
