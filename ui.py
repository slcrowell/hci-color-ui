from tkinter import *
import datetime
import time
import csv
window = Tk()
i=0;

window.title("Potsdam Transport Company Bus Shedule Manager")
window.geometry('1000x600')
lbl = Label(window, font=('Helvetica 12 bold'), text="Operators: Press route icon associated with the bus that has arrived at the stop to record route delays, Arrivals will be broadcast \n over headsets or shown at the bottom right ")
lbl.grid(column=0, row=0)

#Create csv writer outside, so it can be called by functions
out_file = open("results.csv","w")
out_file.write("")

writer = csv.writer(out_file,delimiter=",",lineterminator="\n")

fields = ["Bus Color", "Picked Color", "Time"]
writer.writerow(fields)


# Create a function with one paramter, i.e., of
# the text you want to show when button is clicked
def which_button(button_press):
    # Printing the text when a button is clicked
    print(button_press)

def stoptimer1():
    end = time.time()
    print("red button pressed")
    gap = end - start;
    
    writer.writerow([color,"red",gap])

    a="reaction time is"
    print(f"{a}  {gap}")

def stoptimer2():
    end = time.time()
    print("brown button pressed")
    gap = end - start;

    writer.writerow([color,"brown",gap])

    a="reaction time is"
    print(f"{a}  {gap}")

def stoptimer3():
    end = time.time()
    print("green button pressed")
    gap = end - start;

    writer.writerow([color,"green",gap])

    a="reaction time is"
    print(f"{a}  {gap}")

def stoptimer4():
    end = time.time()
    print("yellow button pressed")
    gap = end - start;

    writer.writerow([color,"yellow",gap])

    a="reaction time is"
    print(f"{a}  {gap}")

def stoptimer5():
    end = time.time()
    print("blue button pressed")
    gap = end - start;

    writer.writerow([color,"blue",gap])

    a="reaction time is"
    print(f"{a}  {gap}")

def stoptimer6():
    end = time.time()
    print("purple button pressed")
    gap = end - start;

    writer.writerow([color,"purple",gap])

    a="reaction time is"
    print(f"{a}  {gap}")


# Creating and displaying of button b1
b1 = Button(window, bg = 'red',height = 3, width = 10,
            command = stoptimer1)
b1.place(x=10, y=55)

# Creating and displaying of button b2
b2 = Button(window, bg = 'goldenrod4',height = 3, width = 10,
            command = stoptimer2)
b2.place(x=100, y=55)

# Creating and displaying of button b3
b3 = Button(window, bg = 'green',height = 3, width = 10,
            command = stoptimer3)
b3.place(x=190, y=55)

# Creating and displaying of button b4
b4 = Button(window, bg = 'yellow',height = 3, width = 10,
            command = stoptimer4)
b4.place(x=280, y=55)


# Creating and displaying of button b5
b5 = Button(window, bg = 'blue',height = 3, width = 10,
            command = stoptimer5)
b5.place(x=370, y=55)


# Creating and displaying of button b6
b6 = Button(window, bg = 'purple',height = 3, width = 10,
            command = stoptimer6)
b6.place(x=460, y=55)



lbl = Label(window, font=('Helvetica 12 bold'), text="current bus at stop :")
lbl.place(x=70, y=170)

#display the current bus color upon click
print("summery of user feedback")
def fun1():
     global i
     i=0;
def fun2():
    global i
    i=i+1;
mylist = ["red", "green", "blue","purple","goldenrod4","yellow"]
def update_color():
    #Making color global will allow the writer to use it from the button function
    global color,start

    color = mylist[i]
    print(color + "  color bus arrived")
    b10 = Button(window, bg = color ,height = 3, width = 10)
    b10.place(x=230, y=160)
    start = time.time()
    fun2();
    if i==6:
        fun1();
button = Button(window,width=20,font=('Helvetica 12 bold'), text="click here for the next bus", command=update_color)
button.place(x=50, y=300)


window.mainloop()
