from tkinter import Tk, Button, Label
from tkinter.ttk import Combobox
import pandas

distribution = pandas.read_csv("Population.csv")
dataset = pandas.read_csv("Dataset.csv")
coordinates = tuple(str(i) for i in range(1, 21))

def avgtime(win):
    # Get the average time
    # For Debug only
    reportedTimeRow = 1
    infectedTimeRow = 0

    totalTime = 0
    for sampleNum in range(0, len(dataset) - 1):
        reportingTime = int(dataset.iloc[sampleNum, reportedTimeRow])
        infectionTime = int(dataset.iloc[sampleNum, infectedTimeRow])
        totalTime += reportingTime - infectionTime
    
    averageTime = totalTime / len(dataset)

    win.timeLabel = Label(text=str(averageTime) + " days")
    win.timeLabel.place(x=490, y=95)

window = Tk()

window.findBtn = Button(window, text="Find")
window.findBtn.place(x=150, y=250)
window.timeBtn = Button(window, text="Calculate Time")
window.timeBtn.place(x=200, y=250)

window.statsLbl=Label(window, text="Statistics", font=("Arial", 14))
window.statsLbl.place(x=470, y=53)
window.timeLabel=Label(window, text="Average Time: ")
window.timeLabel.place(x=350, y=95)
window.timeLabel=Label(window, text="Total Population: ")
window.timeLabel.place(x=350, y=140)
window.timeLabel=Label(window, text="Cases with \nRespiratory Issues: ")
window.timeLabel.place(x=350, y=185)

window.lblx=Label(window, text="X-Coordinate")
window.lblx.place(x=20, y=95)
window.lbly=Label(window, text="Y-Coordinate")
window.lbly.place(x=20, y=140)
window.ddx=Combobox(window, values=coordinates)
window.ddx.place(x=150, y=95)
window.ddy=Combobox(window, values=coordinates)
window.ddy.place(x=150, y=140)

window.timeBtn.bind("<Button-1>", avgtime)

window.title('Dataset Application')
window.geometry("700x600+10+10")
window.mainloop()