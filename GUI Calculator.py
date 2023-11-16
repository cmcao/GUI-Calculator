#**************************************************************************************************
# Python GUI Calculator
#**************************************************************************************************
#import everything from tkinter
from tkinter import *

# a press function with 1 argurment
def button_press(num):
    global equation_text #declare a global variable

    #this will add to equation text and convert str(num) to int/float
    equation_text = equation_text + str(num)

    #set new value and apper in the equation label
    equation_label.set(equation_text)

# a equals function
def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError: 
        equation_label.set("Syntax Error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Can't divide by 0")
        equation_text = ""

# a clear function
def clear():
    global equation_text
    equation_label.set("") #set empty string
    equation_text = "" #set it empty

window = Tk() # declare an object Tk()
window.title("GUI Calculator Program") # program name title appear in the GUI
window.geometry("500x500") #size of the calculator 

equation_text ="" #create empty string

equation_label = StringVar() # create an object that can be linked to both the Label and Entry widgets

# create a label with Calculator size
label = Label(window, textvariable=equation_label, font = ('consolas', 20), bg='green', width = 24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

#==================================Start Create all GUI from 0 - 9, +, -, *, /, = , clear =================
#Create GUI for button #1
button1 = Button(frame, text =1, height =4, width=9, font =35, command =lambda: button_press(1) )
button1.grid(row=0, column=0)

#Create GUI for button #2
button2 = Button(frame, text =2, height =4, width=9, font =35, command =lambda: button_press(2) )
button2.grid(row=0, column=1)

#Create GUI for button #3
button3 = Button(frame, text =3, height =4, width=9, font =35, command =lambda: button_press(3) )
button3.grid(row=0, column=2)

#Create GUI for button #4
button4 = Button(frame, text =4, height =4, width=9, font =35, command =lambda: button_press(4) )
button4.grid(row=1, column=0)

#Create GUI for button #5
button5 = Button(frame, text =5, height =4, width=9, font =35, command =lambda: button_press(5) )
button5.grid(row=1, column=1)

#Create GUI for button #6
button6 = Button(frame, text =6, height =4, width=9, font =35, command =lambda: button_press(6) )
button6.grid(row=1, column=2)

#Create GUI for button #7
button7 = Button(frame, text =7, height =4, width=9, font =35, command =lambda: button_press(7) )
button7.grid(row=2, column=0)

#Create GUI for button #8
button8 = Button(frame, text =8, height =4, width=9, font =35, command =lambda: button_press(8) )
button8.grid(row=2, column=1)

#Create GUI for button #9
button9 = Button(frame, text =9, height =4, width=9, font =35, command =lambda: button_press(9) )
button9.grid(row=2, column=2)

#Create GUI for button #0
button0 = Button(frame, text =0, height =4, width=9, font =35, command =lambda: button_press(0) )
button0.grid(row=3, column=0)

#Create GUI for button plus
plus = Button(frame, text ='+', height =4, width=9, font =35, command =lambda: button_press('+') )
plus.grid(row=0, column=3)

#Create GUI for button subtract
subtract = Button(frame, text ='-', height =4, width=9, font =35, command =lambda: button_press('-') )
subtract.grid(row=1, column=3)

#Create GUI for button multiply
multiple = Button(frame, text ='*', height =4, width=9, font =35, command =lambda: button_press('*') )
multiple.grid(row=2, column=3)

#Create GUI for button divide
divide = Button(frame, text ='/', height =4, width=9, font =35, command =lambda: button_press('/') )
divide.grid(row=3, column=3)

#Create GUI for button divide
divide = Button(frame, text ='/', height =4, width=9, font =35, command =lambda: button_press('/') )
divide.grid(row=3, column=3)

#Create GUI for button equal and using equal function
equal = Button(frame, text ='=', height =4, width=9, font =35, command =equals )
equal.grid(row=3, column=2)

#Create GUI for button decimal
decimal = Button(frame, text ='.', height =4, width=9, font =35, command =lambda: button_press('.') )
decimal.grid(row=3, column=1)

#Create GUI for button clear and using clear function 
clear = Button(window, text ='clear', height =4, width=39, font =35, command =clear )
clear.pack()

#==================================End of Create all GUI ==============================================
#execute the window calculator
window.mainloop() 