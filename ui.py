from tkinter import *
import datetime
import time
import threading

class App(threading.Thread):

    def __init__(self, baseButtons, modButtons):
        threading.Thread.__init__(self)
        self.start()
        self.baseButtons = baseButtons
        self.modButtons = modButtons
        self.index = 0;

    def callback(self):
        self.root.quit()

    def buttonCallback(self, info, i, isBase):
        if(info[0]["color"] == info[i]["color"]):
            self.index += 1
            if(self.index >= len(self.baseButtons)):
                self.root.destroy()
            else:
                self.renderButtons(self.baseButtons[self.index] if isBase else self.modButtons[self.index], isBase)
            

    def renderButtons(self, toRender, isBase):    
        busButton = Button(self.root, bg = toRender[0]["color"], height = 3, width = 10)
        busButton.place(x = toRender[0]["x"], y = toRender[0]["y"])

        for i in range(1, len(toRender)):
            button = Button(self.root, bg = toRender[i]["color"], height = 3, width = 10, command = lambda i=i: self.buttonCallback(toRender, i, isBase))
            button.place(x = toRender[i]["x"], y = toRender[i]["y"])

    def run(self):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)


        self.root.title("Potsdam Transport Company Bus Shedule Manager")
        self.root.geometry('1000x600')

        directions = Label(self.root, font=('Helvetica 12 bold'), text="Operators: Press route icon associated with the bus that has arrived at the stop to record route delays, Arrivals will be broadcast \n over headsets or shown at the bottom right ")
        directions.grid(column=0, row=0)

        lbl = Label(self.root, font=('Helvetica 12 bold'), text="current bus at stop :")
        lbl.place(x=70, y=170)

        baseTrial = Button(self.root, text="Base Trial", height = 3, width = 10, command=lambda: self.renderButtons(self.baseButtons[self.index], True))
        baseTrial.place(x = 230, y = 300)

        modTrial = Button(self.root, text="Mod Trial", height = 3, width = 10, command=lambda: self.renderButtons(self.modButtons[self.index], False))
        modTrial.place(x = 320, y = 300)

        self.root.mainloop()

buttons = [
    [{
        "color": 'red',
        "x": 230,
        "y": 160   
    },
    {
        "color": 'red',
        "x": 10,
        "y": 55   
    },
    {
        "color": 'goldenrod4',
        "x": 100,
        "y": 55   
    },
    {
        "color": 'green',
        "x": 190,
        "y": 55   
    },
    {
        "color": 'yellow',
        "x": 280,
        "y": 55   
    },
    {
        "color": 'blue',
        "x": 370,
        "y": 55   
    },
    {
        "color": 'purple',
        "x": 460,
        "y": 55   
    }],
    [{
        "color": 'goldenrod4',
        "x": 230,
        "y": 160   
    },
    {
        "color": 'red',
        "x": 10,
        "y": 55   
    },
    {
        "color": 'goldenrod4',
        "x": 100,
        "y": 55   
    },
    {
        "color": 'green',
        "x": 190,
        "y": 55   
    },
    {
        "color": 'yellow',
        "x": 280,
        "y": 55   
    },
    {
        "color": 'blue',
        "x": 370,
        "y": 55   
    },
    {
        "color": 'purple',
        "x": 460,
        "y": 55   
    }],
    [{
        "color": 'green',
        "x": 230,
        "y": 160   
    },
    {
        "color": 'red',
        "x": 10,
        "y": 55   
    },
    {
        "color": 'goldenrod4',
        "x": 100,
        "y": 55   
    },
    {
        "color": 'green',
        "x": 190,
        "y": 55   
    },
    {
        "color": 'yellow',
        "x": 280,
        "y": 55   
    },
    {
        "color": 'blue',
        "x": 370,
        "y": 55   
    },
    {
        "color": 'purple',
        "x": 460,
        "y": 55   
    }],
    [{
        "color": 'yellow',
        "x": 230,
        "y": 160   
    },
    {
        "color": 'red',
        "x": 10,
        "y": 55   
    },
    {
        "color": 'goldenrod4',
        "x": 100,
        "y": 55   
    },
    {
        "color": 'green',
        "x": 190,
        "y": 55   
    },
    {
        "color": 'yellow',
        "x": 280,
        "y": 55   
    },
    {
        "color": 'blue',
        "x": 370,
        "y": 55   
    },
    {
        "color": 'purple',
        "x": 460,
        "y": 55   
    }],
    [{
        "color": 'blue',
        "x": 230,
        "y": 160   
    },
    {
        "color": 'red',
        "x": 10,
        "y": 55   
    },
    {
        "color": 'goldenrod4',
        "x": 100,
        "y": 55   
    },
    {
        "color": 'green',
        "x": 190,
        "y": 55   
    },
    {
        "color": 'yellow',
        "x": 280,
        "y": 55   
    },
    {
        "color": 'blue',
        "x": 370,
        "y": 55   
    },
    {
        "color": 'purple',
        "x": 460,
        "y": 55   
    }],
    [{
        "color": 'purple',
        "x": 230,
        "y": 160   
    },
    {
        "color": 'red',
        "x": 10,
        "y": 55   
    },
    {
        "color": 'goldenrod4',
        "x": 100,
        "y": 55   
    },
    {
        "color": 'green',
        "x": 190,
        "y": 55   
    },
    {
        "color": 'yellow',
        "x": 280,
        "y": 55   
    },
    {
        "color": 'blue',
        "x": 370,
        "y": 55   
    },
    {
        "color": 'purple',
        "x": 460,
        "y": 55   
    }],
]

app = App(buttons, buttons)
