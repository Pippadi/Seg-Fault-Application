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
        program.lbl1.place(x=, y=)
        program.lbl2.place(x=, y=)
        program.t1.place(x=, y=)
        program.t2.place(x=, y=)
        program.rtxt.place(x=, y=)
        
    def add():
        result=
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
