# A sample program that performs basic mathematical operations

from tkinter import *

class Window:
    #  initializing function
    def __init__(program, win):
        program.title=Label(win, text="Sample Calculator", fg="blue", font=("Arial", 15))
        program.title.place(x=110, y=70)
        program.lbl1=Label(win, text="First Number")
        program.lbl2=Label(win, text="Second Number")
        program.t1=Entry(bd=2)
        program.t2=Entry(bd=2)
        program.rtxt=Entry(bd=2)
        program.addbtn=Button(win, text="+")
        program.subbtn=Button(win, text="-")
        program.multibtn=Button(win, text="*")
        program.dividebtn=Button(win, text="/")
        # Specify locations
        program.lbl1.place(x=80, y=130)
        program.lbl2.place(x=80, y=170)
        program.t1.place(x=250, y=130)
        program.t2.place(x=250, y=170)
        program.rtxt.place(x=125, y=290)
        program.addbtn.place(x=50, y=400)
        program.subbtn.place(x=100, y=400)
        program.multibtn.place(x=150, y=400)
        program.dividebtn.place(x=200, y=400)
    def add(program):
        result=0
    def subtract(program):
        result=1
    def multiply(program):
        result=5
    def divide(program):
        result=4

window=Tk()
mywin=Window(window)
window.title('Calculator Program')
window.geometry("400x400+10+10")
window.mainloop()
