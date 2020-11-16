# A sample program that performs basic mathematical operations

from tkinter import *

class Window:
    def __init__(program, win):
        program.title=Label(win, text="Sample Calculator", fg="blue")
        program.title.place(x=0, y=100)
        program.lbl1=Label(win, text="First Number")
        program.lbl1=Label(win, text="Second Number")
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
window.geometry("400x300+10+10")
window.mainloop()
