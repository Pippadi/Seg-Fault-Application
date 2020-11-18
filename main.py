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
    program.btnfind=Button(win, text="Find", command=program.getcoordinates)
    program.btnfind.place(x=150, y=250)
    program.btntime=Button(win, text="Calculate Time", command=program.specifictime)
    program.btntime.place(x=200, y=250)
    program.title=Label(win, text="Dataset Application", fg="black", font=("Arial", 16))
    program.title.place(x=250, y=29)
    # program.txtx=Entry(win, text="Enter the X-coordinate", bd=2)
    # program.txtx.place(x=150, y=100)
    # program.txty=Entry(win, text="Enter the Y-coordinate", bd=2)
    # program.txty.place(x=150, y=150)
    program.lblstats=Label(win, text="Statistics", font=("Arial", 14))
    program.lblstats.place(x=470, y=53)
    program.lbltime=Label(win, text="Average Time: ")
    program.lbltime.place(x=350, y=95)
    program.lbltime=Label(win, text="Total Population: ")
    program.lbltime.place(x=350, y=140)
    # program.lblavg=Label(win, text="Value")
    # program.lblavg.place(x=490, y=95)
    program.lblx=Label(win, text="X-Coordinate")
    program.lblx.place(x=20, y=95)
    program.lbly=Label(win, text="Y-Coordinate")
    program.lbly.place(x=20, y=140)
    program.ddx=Combobox(win, values=program.coordinates)
    program.ddx.place(x=150, y=95)
    program.ddy=Combobox(win, values=program.coordinates)
    program.ddy.place(x=150, y=140)

    # Execute the functions to calculate statistics
    program.avgtime()
    program.getpp()
    
    # Bind to functions
    program.btnfind.bind('<Button-1>', program.getcoordinates)
    program.btntime.bind('<Button-1>', program.avgtime)

  def avgtime(program):
    # print(dataset.head[2:3])
    # Get the average time
    
    # For Debug only
    # ycoordinate=int(program.ddy.get())
    
    rown=0
    tmr=int(dataset.iloc[rown,1])
    tmi=int(dataset.iloc[rown,0])+1
    # print("\nThe total time taken is: ")
    # print(tmr-tmi)

    ftmr=tmr+int(dataset.iloc[rown,1])
    rown=rown+1
    ftmi=tmi+int(dataset.iloc[rown,0])
    
    for i in range(462879):
      ftmr=ftmr+int(dataset.iloc[rown,1])
      rown=rown+1
      ftmi=ftmi+int(dataset.iloc[rown,0])

    totaltime=ftmr-ftmi
    # print(totaltime)
    avgtime=totaltime / 462880
    print("\nThe average time is: ")
    print(int(avgtime))

    program.lblavg=Label(text=str(int(avgtime))+" days")
    program.lblavg.place(x=490, y=95)

  def getpp(program):
    rown=0
    ppn=0
    
    for i in range(400):
      ppn=ppn+int(pp.iloc[rown,2])
      rown=rown+1

    print("The total population is: "+str(ppn)+" people")
    program.lblppn=Label(text=str(ppn)+" people")
    program.lblppn.place(x=490, y=140)

  def specifictime(program):
    xcoordinate=int(program.ddx.get())
    ycoordinate=int(program.ddy.get())
    rown=dataset.iloc[xcoordinate, ycoordinate]
    tmr=int(dataset.iloc[rown,1])
    tmi=int(dataset.iloc[rown,0])+1
    # print("\nThe total time taken is: ")
    # print(tmr-tmi)

    ftmr=tmr+int(dataset.iloc[rown,1])
    rown=rown+1
    ftmi=tmi+int(dataset.iloc[rown,0])
    
    totaltime=ftmr-ftmi
    # print(totaltime)
    avgtime=totaltime / 462880
    print("\nThe average time is: ")
    print(int(avgtime))

  def getcoordinates(program):
    # For debug only
    # print(pp.head(5))
    value=program.ddx.get()
    print("\n")
    print(value)
    
    
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
window.geometry("700x600+10+10")
window.mainloop()
