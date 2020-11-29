from tkinter import *
from tkinter import ttk
app = Tk()
app.title("pythonUP currency converter")
app.geometry('960x720')

app['bg'] = '#0059b3'


# Currency Converter

# define rates based on EUR
eur = 1
gbp = 0.898889
ngn = 455.228
usd = 1.19636

# divide by the exchange rate


def convert(f_curr, s_curr, amt):
    f_curr = f_curr.lower()
    s_curr = s_curr.lower()

    base_val = eur
    if(s_curr != 'eur'):
        if(s_curr == 'ngn'):
            base_val = 1/ngn
        elif(s_curr == 'gbp'):
            base_val = 1/gbp
        elif(s_curr == 'usd'):
            base_val == 1/usd
        else:
            return 'conversion rate not available'
    if(f_curr == 'ngn'):
        return amt / ngn / base_val
    elif(f_curr == 'gbp'):
        return amt / gbp / base_val
    elif(f_curr == 'usd'):
        return amt / usd / base_val
    else:
        return 'conversion rate not available'


def handle_conv():
    global amt
    global f_curr
    global s_curr
    try:
        amt = float(inp.get())
        message.config(text="converting...")
        print(sec_var.get())
    except ValueError:
        message.config(text="Input has to be a number")
    f_curr = first_var.get()
    s_curr = sec_var.get()

    new_amt = convert(f_curr, s_curr, amt)
    message.config(text=f'Your new amount is {new_amt}{s_curr}')


# create converter frame
frame = Frame(app, width=560, height=300, padx=20, pady=20,
              highlightcolor="white", highlightthickness=1)

message = Label(
    frame, text='Input amount, select currencies and click convert')
message.grid(row=0, column=0, rowspan=2, columnspan=9, pady=20)

# create input
inp = Entry(frame, borderwidth=3)
inp_label = Label(frame, text="Amount")
inp.grid(row=3, column=0, columnspan=3)
inp_label.grid(row=2, column=0, columnspan=3)

curr_options = ["NGN", "USD", "GBP", 'EUR']

# first currency
first_var = StringVar()
first_option = ttk.Combobox(frame, textvariable=first_var, values=curr_options)
first_option_label = Label(frame, text="From")
first_option_label.grid(row=2, column=3, columnspan=3)

first_option.grid(row=3, column=3, columnspan=3)

sep = ttk.Separator(frame, orient=VERTICAL)

# second currency
sec_var = StringVar()
second_option = ttk.Combobox(frame,  textvariable=sec_var, values=curr_options)
second_option.current(3)
second_option.grid(row=3, column=6, columnspan=3)
second_option_label = Label(frame, text="To")
second_option_label.grid(row=2, column=6, columnspan=3)
frame.place(relx=.5, rely=.5, anchor='c')

sep.grid(row=4, rowspan=2, column=0, columnspan=9, sticky='ns', pady=20)
# convert button
conv_but = Button(frame, text='Convert', padx=100,
                  pady=15, command=handle_conv)
conv_but.grid(row=6, column=0, columnspan=9)


app.mainloop()
