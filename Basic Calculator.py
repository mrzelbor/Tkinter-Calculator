from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("200x350")

equation = StringVar()

calculation = Label(root, textvariable=equation, font=("Arial", 20), bg="white", width=24, height=2, anchor="e")
calculation.grid(columnspan=4)

equa = ("")
def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)

def EqualPress():
    global equa
    total = str(eval(equa))
    equation.set(total)
    equa = ""

def Clean():
    global equa
    equa = ""
    equation.set("")

# Fourth Row
Clear = Button(root, text="C", command=Clean, font=("Arial", 14), height=2, width=3)
Clear.grid(row=4, column=0)
Button0 = Button(root, text="0", command=lambda:btnPress(0), font=("Arial", 14), height=2, width=3)
Button0.grid(row=4, column=1)
Equal = Button(root, text="=", command=EqualPress, font=("Arial", 14), height=2, width=3)
Equal.grid(row=4, column=2)
Subtraction = Button(root, text="-", command=lambda:btnPress("-"), font=("Arial", 14), height=2, width=3)
Subtraction.grid(row=4, column=3)

# Third Row
Button1 = Button(root, text="1", command=lambda:btnPress(1), font=("Arial", 14), height=2, width=3)
Button1.grid(row=3, column=0)
Button2 = Button(root, text="2", command=lambda:btnPress(2),font=("Arial", 14), height=2, width=3)
Button2.grid(row=3, column=1)
Button3 = Button(root, text="3", command=lambda:btnPress(3), font=("Arial", 14), height=2, width=3)
Button3.grid(row=3, column=2)
Addition = Button(root, text="+", command=lambda:btnPress("+"), font=("Arial", 14), height=2, width=3)
Addition.grid(row=3, column=3)

# Second Row
Button4 = Button(root, text="4", command=lambda:btnPress(4), font=("Arial", 14), height=2, width=3)
Button4.grid(row=2, column=0)
Button5 = Button(root, text="5", command=lambda:btnPress(5), font=("Arial", 14), height=2, width=3)
Button5.grid(row=2, column=1)
Button6 = Button(root, text="6", command=lambda:btnPress(6), font=("Arial", 14), height=2, width=3)
Button6.grid(row=2, column=2)
Multiply = Button(root, text="*", command=lambda:btnPress("*"), font=("Arial", 14), height=2, width=3)
Multiply.grid(row=2, column=3)

# First Row
Button7 = Button(root, text="7", command=lambda:btnPress(7), font=("Arial", 14), height=2, width=3)
Button7.grid(row=1, column=0)
Button8 = Button(root, text="8", command=lambda:btnPress(8), font=("Arial", 14), height=2, width=3)
Button8.grid(row=1, column=1)
Button9 = Button(root, text="9", command=lambda:btnPress(9), font=("Arial", 14), height=2, width=3)
Button9.grid(row=1, column=2)
Division = Button(root, text="/", command=lambda:btnPress("/"), font=("Arial", 14), height=2, width=3)
Division.grid(row=1, column=3)

# Make columns and rows expand to fit better
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)

root.mainloop()