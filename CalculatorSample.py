# A sample program that performs basic mathematical operations

from tkinter import *

class Window:
    #  initializing function
    def __init__(program, win):
        program.title=Label(win, text="Sample Calculator", fg="blue", font=("Arial", 15))
        program.title.place(x=110, y=70)
        program.lbl1=Label(win, text="First Number")
        program.lbl1=Label(win, text="Second Number")
        program.t1=Entry(bd=2)
        program.t2=Entry(bd=2)
        program.rtxt=Entry(bd=2)
        program.addbtn=Button(win, text="+")
        program.subbtn=Button(win, text="-")
        program.multibtn=Button(win, text="*")
        program.dividebtn=Button(win, text="/")
    def add():
        result=0
    def subtract():
        result=1
    def multiply():
        result=5
    def divide():
        result=4
        

window=Tk()
mywin=Window(window)
window.title('Calculator Program')
window.geometry("400x400+10+10")
window.mainloop()
