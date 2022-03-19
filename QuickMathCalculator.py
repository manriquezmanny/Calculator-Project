from tkinter import *
#creates Root Window
root = Tk()

#sets window size
root.geometry("475x300")


#creates user input field
input = Entry(root, width = 50, borderwidth = 5)
input.grid(row=0, column=0, columnspan=4)

#Creates Brand Label
brand = Label(root, text="Quick Math", font="cartoon 15 bold").grid(row=0, column=4, columnspan=2)

#functions that inputs number into field as string
def button_click(number):
    current_num = input.get()
    input.delete(0, END)
    input.insert(0, str(current_num) + str(number))

#function that clears the input field
def clear():
    input.delete(0, END)

#functions that get input and tell the equals function what operator was selected.
def multiply():
    global last_num
    last_num = input.get()
    input.delete(0, END)
    global operator
    operator = "multiply"

def divide():
    global last_num
    last_num = input.get()
    input.delete(0, END)
    global operator
    operator = "divide"

def add():
    global last_num
    last_num = input.get()
    input.delete(0, END)
    global operator
    operator = "add"

def subtract():
    global last_num
    last_num = input.get()
    input.delete(0, END)
    global operator
    operator = "subtract"

#function that gives solution depended on what operator was selected, and raises error if more than one operator was clicked; per solution.
def equals():
    if operator == "multiply":
        new_num = input.get()
        input.delete(0, END)
        try:
            product = float(last_num) * float(new_num)
            input.insert(0, str(product))
        except ValueError:
            input.insert(0, "Error: please click only one operator per equation!")

    elif operator == "divide":
        new_num = input.get()
        input.delete(0, END)
        try:
            quotient = float(last_num) / float(new_num)
            input.insert(0, str(quotient))
        except ValueError:
            input.insert(0, "Error: please click only one operator per equation!")

    elif operator == "add":
        new_num = input.get()
        input.delete(0, END)
        try:
            sum = float(last_num) + float(new_num)
            input.insert(0, str(sum))
        except ValueError:
            input.insert(0, "Error: please click only one operator per equation!")

    elif operator == "subtract":
        new_num = input.get()
        input.delete(0, END)
        try:
            difference = float(last_num) - float(new_num)
            input.insert(0, str(difference))
        except ValueError:
            input.insert(0, "Error: please click only one operator per equation!")
    else:
        input.delete(0, END)
        input.insert("Error, try again") 

#creates and positions functional buttons in the application.
button_7 = Button(root, text = "7", font="cartoon 10 bold", command=lambda: button_click(7)).grid(row=1, column=0, ipadx = 28, ipady = 20)
button_8 = Button(root, text = "8", font="cartoon 10 bold", command=lambda: button_click(8)).grid(row=1, column=1, ipadx = 28, ipady = 20)
button_9 = Button(root, text = "9", font="cartoon 10 bold", command=lambda: button_click(9)).grid(row=1, column=2, ipadx = 28, ipady = 20)

button_4 = Button(root, text = "4", font="cartoon 10 bold", command=lambda: button_click(4)).grid(row=2, column=0, ipadx = 28, ipady = 20)
button_5 = Button(root, text = "5", font="cartoon 10 bold", command=lambda: button_click(5)).grid(row=2, column=1, ipadx = 28, ipady = 20)
button_6 = Button(root, text = "6", font="cartoon 10 bold", command=lambda: button_click(6)).grid(row=2, column=2, ipadx = 28, ipady = 20)

button_1 = Button(root, text = "1", font="cartoon 10 bold", command=lambda: button_click(1)).grid(row=3, column=0, ipadx = 28, ipady = 20)
button_2 = Button(root, text = "2", font="cartoon 10 bold", command=lambda: button_click(2)).grid(row=3, column=1, ipadx = 28, ipady = 20)
button_3 = Button(root, text = "3", font="cartoon 10 bold", command=lambda: button_click(3)).grid(row=3, column=2, ipadx = 28, ipady = 20)

button_0 = Button(root, text = "0", font="cartoon 10 bold", command=lambda: button_click(0)).grid(row= 4, column=1, ipadx = 28, ipady = 20)

button_add = Button(root, text = "+", font="cartoon 10 bold", command=add).grid(row=2, column=3, ipadx= 30, ipady = 20)
button_subtract = Button(root, text = "-", font="cartoon 15", command=subtract).grid(row=1, column=3, ipadx=28, ipady=14)
button_multiply = Button(root, text = "x", font="cartoon 10 bold", command=multiply).grid(row=1, column =4, ipadx= 31, ipady=20)
button_divide = Button (root, text = "÷", font="cartoon 10 bold", command=divide).grid(row= 1, column=5, ipadx=30, ipady=20)

button_point = Button(root, text = ".", font="cartoon 10 bold", command=lambda: button_click(".")).grid(row=3, column=3, ipadx= 32, ipady= 20)
button_equals = Button(root, text = "=", bg = "#701f28", fg ="white", font="cartoon 10 bold", command=equals).grid(row=2, column=5, ipadx= 30, ipady=54, rowspan=2)
button_clear = Button(root, text="Clear", bg="silver", font="cartoon 10 bold", command=clear).grid(row=2, column=4, ipadx= 18, ipady=54, rowspan=2)

#I might use these lists to Create dynamicaly resizable buttons that fit the resizable window.
row_1_buttons = [button_7, button_8, button_9, button_subtract, button_multiply, button_divide]
row_2_buttons = [button_4, button_5, button_6, button_add, button_equals, button_clear]
row_3_buttons = [button_1, button_2, button_3, button_point]

#Creates the app's main loop
root.mainloop()