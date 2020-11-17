# Tha main application's program
# Currently working code

from tkinter import *

class Window:
  def __init__(program, win):
    # List of coordinates
    xc=("1", "2", "3")
    # Code to add widgets
    btn1=Button(window, text="Button 1")
    btn1.place(x=150, y=250)
    btn2=Button(window, text="Button 2")
    btn2.place(x=300, y=250)
    title=Label(window, text="Title", fg="black", font=("Arial", 16))
    title.place(x=200, y=35)
    #txtx=Entry(window, text="Enter the X-coordinate", bd=2)
    #txtx.place(x=150, y=100)
    txty=Entry(window, text="Enter the Y-coordinate", bd=2)
    txty.place(x=150, y=150)
    lblx=Label(window, text="X-Coordinate")
    lblx.place(x=20, y=100)
    lbly=Label(window, text="Y-Coordinate")
    lbly.place(x=20, y=150)
    lb=Listbox(window, height=2)
    for ncoordinates in xc:
      lb.insert(END, ncoordinates)
    lb.place(x=150, y=95)
    
  # def avgtime():
    # Get the average time

  # def getcoordinates():
    # 
  
  # def filterd():
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

