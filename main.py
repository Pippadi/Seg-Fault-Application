# Tha main application's program
# Currently working code

from tkinter import *
from tkinter.ttk import Combobox
import pandas as pd

# Spreadsheets
pp=pd.read_csv('population.csv')
dataset=pd.read_csv('dataset.csv')

# Variables
inftime=0
finftime=inftime+1
reptime=0

class Window:
  def __init__(program, win):
    # List of coordinates
    coordinates=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
    # Code to add widgets
    btn1=Button(win, text="Find", command=program.getcoordinates)
    btn1.place(x=150, y=250)
    btn2=Button(win, text="Time", command=program.avgtime)
    btn2.place(x=300, y=250)
    title=Label(win, text="Title", fg="black", font=("Arial", 16))
    title.place(x=200, y=35)
    # txtx=Entry(win, text="Enter the X-coordinate", bd=2)
    # txtx.place(x=150, y=100)
    # txty=Entry(win, text="Enter the Y-coordinate", bd=2)
    # txty.place(x=150, y=150)
    lblx=Label(win, text="X-Coordinate")
    lblx.place(x=20, y=100)
    lbly=Label(win, text="Y-Coordinate")
    lbly.place(x=20, y=150)
    ddx=Combobox(win, values=coordinates)
    ddx.place(x=150, y=100)
    ddy=Combobox(win, values=coordinates)
    ddy.place(x=150, y=150)
    # Bind to functions
    btn1.bind('<Button-1>', program.getcoordinates)
    btn2.bind('<Button-1>', program.avgtime)

  def avgtime(num1):
    print(dataset.head[2:3])
    # Get the average time
    

  def getcoordinates(program):
    # For debug only
    print(pp.head(5))
    value=
    print(value)
    
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
    

window=Tk()
programwin=Window(window)
window.title('Application')
window.geometry("500x500+10+10")
window.mainloop()
