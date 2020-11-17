# Tha main application's program
# Currently working code

from tkinter import *
from tkinter.ttk import Combobox
import pandas as pd

num1 = 1
data=pd.read_csv('population.csv')

class Window:
  def __init__(program, win):
    # List of coordinates
    program.xc=("1", "2", "3")
    # Code to add widgets
    btn1=Button(win, text="Button 1", command=program.getx)
    btn1.place(x=150, y=250)
    btn2=Button(win, text="Button 2")
    btn2.place(x=300, y=250)
    title=Label(win, text="Title", fg="black", font=("Arial", 16))
    title.place(x=200, y=35)
    # program.txtx=Entry(win, text="Enter the X-coordinate", bd=2)
    # program.txtx.place(x=150, y=100)
    txty=Entry(win, text="Enter the Y-coordinate", bd=2)
    txty.place(x=150, y=150)
    lblx=Label(win, text="X-Coordinate")
    lblx.place(x=20, y=100)
    lbly=Label(win, text="Y-Coordinate")
    lbly.place(x=20, y=150)
    ddx=Combobox(win, values=program.xc)
    ddx.place(x=150, y=100)
    lbx=Listbox(win, height=2)
    for ncoordinates in program.xc:
     lbx.insert(END, ncoordinates)
    lbx.place(x=150, y=200)
    # Bind to functions
    btn1.bind('<Button-1>', program.getx)
  #def avgtime():
    # Get the average time
    
  #def getcoordinates(xc, yc):
    # 
    
  #def filterd():
    # 
    
  #def filterr():
    # 
    
  #def filterbp():
    # 
    
  #def filterage(above60):
    #
    
    #if (above60==True):
    
    #else:
  
  def getx(program, value):
    # For debug only
    print(data.head(5))
    

window=Tk()
programwin=Window(window)
window.title('Application')
window.geometry("500x500+10+10")
window.mainloop()
