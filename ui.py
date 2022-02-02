from tkinter import *
import datetime
import time
import threading
import csv
import os
import random

random.seed(5188)

#Create csv writer outside, so it can be called by functions
out_file = open("results.csv","w")
out_file.write("")

writer = csv.writer(out_file,delimiter=",",lineterminator="\n")

fields = ["Bus Color", "Picked Color", "Time"]
writer.writerow(fields)


class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()
        self.baseColors = ['red', 'goldenrod4', 'green', 'yellow', 'blue', 'purple']
        self.modColors = ['red', 'goldenrod4', 'green', 'yellow', 'blue', 'purple']
        self.activeTest = ""
        self.round = 0
        self.start = 0
        self.end = 0

    def callback(self):
        self.root.quit()

    def buttonCallback(self, colorPressed, correctColor, colors):
        self.end = time.time()

        writer.writerow([correctColor, colorPressed, self.end - self.start])
        self.round += 1
        if(self.round >= 48): # 8 trials per color 
            os.remove(self.activeTest + "_results.csv")
            out_file.close()
            os.rename("results.csv", self.activeTest + "_results.csv")
            self.root.destroy()
        else:
            self.renderButtons(colors)
            

    def renderButtons(self, colors):    
        busButton = Button(self.root, bg = colors[self.round % 6], height = 3, width = 10)
        busButton.place(x = 230, y = 160)
        shuffled = list(colors)
        random.shuffle(shuffled)
        for i in range(len(colors)):
            button = Button(self.root, bg = shuffled[i], height = 3, width = 10, command = lambda i=i: self.buttonCallback(shuffled[i], colors[self.round % 6], colors))
            button.place(x = 10 + i * 90, y = 50)
        self.start = time.time()

    def activateBase(self):
        self.activeTest = 'base'
        self.renderButtons(self.baseColors)

    def activateMod(self):
        self.activeTest = 'mod'
        self.renderButtons(self.modColors)

    def run(self):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)


        self.root.title("Potsdam Transport Company Bus Shedule Manager")
        self.root.geometry('1000x600')

        directions = Label(self.root, font=('Helvetica 12 bold'), text="Operators: Press route icon associated with the bus that has arrived at the stop to record route delays, Arrivals will be broadcast \n over headsets or shown at the bottom right ")
        directions.grid(column=0, row=0)

        lbl = Label(self.root, font=('Helvetica 12 bold'), text="current bus at stop :")
        lbl.place(x=70, y=170)

        baseTrial = Button(self.root, text="Base Trial", height = 3, width = 10, command=lambda: self.activateBase())
        baseTrial.place(x = 230, y = 300)

        modTrial = Button(self.root, text="Mod Trial", height = 3, width = 10, command=lambda: self.activateMod())
        modTrial.place(x = 320, y = 300)

        self.root.mainloop()


app = App()