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
    program.coordinates=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
    # Code to add widgets
    program.btn1=Button(win, text="Find", command=program.getcoordinates)
    program.btn1.place(x=150, y=250)
    program.btn2=Button(win, text="Time", command=program.avgtime)
    program.btn2.place(x=300, y=250)
    program.title=Label(win, text="Title", fg="black", font=("Arial", 16))
    program.title.place(x=200, y=35)
    # program.txtx=Entry(win, text="Enter the X-coordinate", bd=2)
    # program.txtx.place(x=150, y=100)
    # program.txty=Entry(win, text="Enter the Y-coordinate", bd=2)
    # program.txty.place(x=150, y=150)
    program.lblx=Label(win, text="X-Coordinate")
    program.lblx.place(x=20, y=100)
    program.lbly=Label(win, text="Y-Coordinate")
    program.lbly.place(x=20, y=150)
    program.ddx=Combobox(win, values=program.coordinates)
    program.ddx.place(x=150, y=100)
    program.ddy=Combobox(win, values=program.coordinates)
    program.ddy.place(x=150, y=150)
    # Bind to functions
    program.btn1.bind('<Button-1>', program.getcoordinates)
    program.btn2.bind('<Button-1>', program.avgtime)

  def avgtime(program):
    # print(dataset.head[2:3])
    # Get the average time
    
    # For Debug only
    ycoordinate=int(program.ddy.get())
    rown=ycoordinate-1
    colmn=1
    tmr=int(dataset.iloc[rown,1])
    tmi=int(dataset.iloc[rown,0])+1
    print("\nThe total time taken is: ")
    print(tmr-tmi)

  def getcoordinates(program):
    # For debug only
    # print(pp.head(5))
    value=program.ddx.get()
    print("\n")
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
