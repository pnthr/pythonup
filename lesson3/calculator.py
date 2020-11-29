# Calculator

# First we define arithmetic operation functions
# This function adds two numbers

from tkinter import *

# Graphical User Interface GUI


def add(x, y):
    return x + y

# This function subtracts two numbers


def subtract(x, y):
    return x - y

# This function multiplies two numbers


def multiply(x, y):
    return x * y

# This function divides two numbers


def divide(x, y):
    return x / y


def calculator(x, y, operation):
    if(operation == 'add' or operation == '+'):
        return add(x, y)
    elif(operation == 'subtract' or operation == '-'):
        return subtract(x, y)
    elif(operation == 'multiply' or operation == '*'):
        return multiply(x, y)
    elif(operation == 'divide' or operation == '/'):
        return divide(x, y)
    else:
        return "Check your input. x,y values must be integers and available operations are 'add', 'subtract', 'multiply' or 'divide'"


root = Tk()
root.title("pythonUP calculator")

scr = Entry(root, width=25, borderwidth=3)
scr.grid(row=0, column=0, rowspan=2, columnspan=4)


def handle_but(number):
    current = scr.get()
    scr.delete(0, END)
    scr.insert(0, current + str(number))


def handle_clear():
    scr.delete(0, END)


def handle_op(op):
    f_num = scr.get()
    global first_num
    global curr_op
    first_num = float(f_num)
    curr_op = op
    scr.delete(0, END)


def handle_eq():
    s_num = scr.get()
    global sec_num
    sec_num = float(s_num)
    res = calculator(first_num, sec_num, curr_op)
    scr.delete(0, END)
    scr.insert(0, str(res))


but1 = Button(root, text='1', padx=20, pady=15, command=lambda: handle_but(1))
but2 = Button(root, text='2', padx=20, pady=15, command=lambda: handle_but(2))
but3 = Button(root, text='3', padx=20, pady=15, command=lambda: handle_but(3))
but4 = Button(root, text='4', padx=20, pady=15, command=lambda: handle_but(4))
but5 = Button(root, text='5', padx=20, pady=15, command=lambda: handle_but(5))
but6 = Button(root, text='6', padx=20, pady=15, command=lambda: handle_but(6))
but7 = Button(root, text='7', padx=20, pady=15, command=lambda: handle_but(7))
but8 = Button(root, text='8', padx=20, pady=15, command=lambda: handle_but(8))
but9 = Button(root, text='9', padx=20, pady=15, command=lambda: handle_but(9))
but0 = Button(root, text='0', padx=20, pady=15, command=lambda: handle_but(0))
but_point = Button(root, text='.', padx=22, pady=15,
                   command=lambda: handle_but('.'))
but_add = Button(root, text='+', padx=20, pady=15,
                 command=lambda: handle_op('+'))
but_clear = Button(root, text='AC', padx=15, pady=15, command=handle_clear)
but_sub = Button(root, text='-', padx=20, pady=15,
                 command=lambda: handle_op('-'))
but_mul = Button(root, text='*', padx=20, pady=15,
                 command=lambda: handle_op('*'))
but_div = Button(root, text='/', padx=20, pady=15,
                 command=lambda: handle_op('/'))
but_eq = Button(root, text='=', padx=105, pady=15,
                command=handle_eq)


but7.grid(row=2, column=0)
but8.grid(row=2, column=1)
but9.grid(row=2, column=2)
but_add.grid(row=2, column=3)

but4.grid(row=3, column=0)
but5.grid(row=3, column=1)
but6.grid(row=3, column=2)
but_sub.grid(row=3, column=3)

but1.grid(row=4, column=0)
but2.grid(row=4, column=1)
but3.grid(row=4, column=2)
but_mul.grid(row=4, column=3)

but0.grid(row=5, column=0)
but_point.grid(row=5, column=1)
but_clear.grid(row=5, column=2)
but_div.grid(row=5, column=3)

but_eq.grid(row=6, column=0, columnspan=4)
root.mainloop()
