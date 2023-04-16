'''
States Project
2217
4/15/23
'''
import decimal
import tkinter as tk
from tkinter import *
import math
import time

root = tk.Tk()

root.title("Future Value Calculator")

SWIDTH = root.winfo_screenwidth()
SHEIGHT = root.winfo_screenheight()

WWIDTH = SWIDTH//2 # Width 
WHEIGHT = SHEIGHT//2 # Height
#setting geometry for window
root.geometry('500x400')
 
root.eval('tk::PlaceWindow . center')

#Setting string vars for windows
inputA=tk.StringVar()
inputB=tk.StringVar()
inputC=tk.StringVar()
answer = tk.StringVar()
clicked = StringVar()
clicked.set( "Choose an option" )

class maths:
    #defines inputs and error
    def __init__(self):
        self.inputA = inputA.get()
        self.inputB = inputB.get()
        self.inputC = inputB.get()
        self.inputD = clicked.get()
        self.errored = False
        self.value = 0
        self.answer = answer.get()
    #tell if its 2 decimal
    def inputCalculateA(self):
        notDecimal = False
        self.inputA = inputA.get()
        input1 = self.inputA
        
        try:
            s = decimal.Decimal(input1)
            
        except:
            notDecimal = True
        
        if notDecimal == True:
            self.open_popup()
            self.errored == True
            
        else:
            if abs(s.as_tuple().exponent) > 2:
                self.open_popup()
                self.errored == True
                
            else:
                return(input1)
    #tells if its whole number
    def inputCalculateB(self):
        self.inputB = inputB.get()
        input1 = self.inputB
        notNum = False
        try:
            a = int(input1)
            
        except:
            notNum = True
        
        if notNum:
            self.open_popup()
            self.errored == True
        else:
            return(input1)
        
    #tells if it is a percentage
    def inputCalculateC(self):
        self.inputC = inputC.get()
        input1 = str(self.inputC)
        notNum = False
        
        try:
            input1 = int(self.inputC)
        except:
            notNum = True
        if notNum == False:
            input1 = int(self.inputC)
            if input1 > 100:
                self.open_popup()
                self.errored = True
                
            else:
                if input1 == 100:
                    return(1.0)
                elif input1 < 10:
                    a = '0.0' + str(input1)
                    print(a)
                    return(a)
                else:
                    a = '0.' + str(input1)
                    return(float(a))
        else:
            self.open_popup()
            self.errored = True
    #returns selection for dropbox
    def inputCalculateD(self):
        self.inputD = clicked.get()
        
        if self.inputD == 'Monthly':
            return(1)
        
        elif self.inputD == 'Yearly':
            return(2)
        
        else:
            return(0)
    #opens error popup
    def open_popup(self):
        top= tk.Tk()
        top.geometry("400x200")
        top.eval('tk::PlaceWindow . center')
        top.title("Error")
        tk.Label(top, text="Present Value :Must be numbers and have two digits\n Number Of Years must be whole number\nCompounding periods must be whole numbers").place(x=30,y=30)
    #clears sections
    def clear(self):
        inputA.set('')
        inputB.set('')
        inputC.set('')
        clicked.set('Choose an option')
    #calculates answer
    def calculate(self):
        self.errored = False
        iA = self.inputCalculateA()
        iB = self.inputCalculateB()
        iC = self.inputCalculateC()
        iD = self.inputCalculateD()
        if iA == None or iB == None or iC == None or iD == 0:
            self.open_popup()
            self.errored = True
        else:
            if iD == 1:
                N = 12
            else:
                N = 1
            PV = float(iA)
            R = float(iC)
            T =int(iB)
            print(iA, iB, iC, iD, PV, R, T, N)
            a = PV
            b = 1 + (R/N)
            c = N*T
            d = math.pow(b, c)
            answ = a * d
            answ = round(answ, 2)
            self.value = answ
            print(str(self.value))
            answer.set(self.value)
            
        

#Tkinter menu
def menu():
    options = ["Monthly","Yearly"]
    mathA = maths()
    while True:
        time.sleep(0.01)
        tk.Label(root, text="Present Value Dollars").grid(row=0)
        tk.Label(root, text="Number of years").grid(row=1)
        tk.Label(root, text="Intrest Rate").grid(row=2)
        tk.Label(root, text=("Calculated Future Value is : ")).grid(row=6)
        
        e1 = tk.Entry(root, textvariable = inputA)
        e2 = tk.Entry(root, textvariable = inputB)
        e3 = tk.Entry(root, textvariable = inputC)
        e4 = tk.Entry(root, textvariable = answer)
        
        drop = OptionMenu( root , clicked , *options )
        drop.grid(row=2, column=2)


        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=6, column=1)
        
        tk.Button(root, text='Calculate',command = mathA.calculate).grid(row=3, column=1, sticky=tk.W, pady=4)
        tk.Button(root, text='Clear',command = mathA.clear).grid(row=4, column=1, sticky=tk.W, pady=4)
        tk.Button(root, text='Exit',command = exit).grid(row=5, column=1, sticky=tk.W, pady=4)
        

        root.mainloop()

menu()