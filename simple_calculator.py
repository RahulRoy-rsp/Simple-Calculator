from tkinter import *
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = Tk()
window.title("Simple Calculator ___RSP___")
window.geometry('340x400+300+100')
window.resizable(width=False, height=False)
window.configure(bg='#538FFB #5B54FA')

entry_field = Entry(window, relief=SUNKEN, borderwidth=3, width=50)
entry_field.place(x=20, y=30)


def click(x):
    entry_field.insert(END, x)


def clear():
    entry_field.delete(0, END)


def delete():
    # entry_field.delete(END)
    # entry_field.delete(entry_field.index("end") - 1)
    insert = entry_field.index("insert")
    entry_field.delete(insert - 1)


def calc():
    try:
        y = str(eval(entry_field.get()))
        entry_field.delete(0, END)
        entry_field.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Not a proper Equation")


_1 = Button(window, text='1', padx=15, pady=5, width=3, font=('Helvetica', 10, 'bold'),
            bg='#EDC126', command=lambda: click(1))
_1.place(x=20, y=80)

_2 = Button(window, text='2', padx=15, pady=5, width=3, font=('Helvetica', 10, 'bold'),
            bg='#EDC126', command=lambda: click(2))
_2.place(x=100, y=80)

_3 = Button(window, text='3', padx=15, pady=5, width=3, font=('Helvetica', 10, 'bold'),
            bg='#EDC126', command=lambda: click(3))
_3.place(x=180, y=80)

_4 = Button(window, text='4', padx=15, pady=5, width=3, font=('Helvetica', 10, 'bold'),
            bg='#EDC126', command=lambda: click(4))
_4.place(x=260, y=80)

_5 = Button(window, text='5', padx=15, pady=5, width=3, font=('Helvetica', 10, 'bold'),
            bg='#EDC126', command=lambda: click(5))
_5.place(x=20, y=140)

_6 = Button(window, text='6', padx=15, pady=5, width=3, font=('Helvetica', 10, 'bold'),
            bg='#EDC126', command=lambda: click(6))
_6.place(x=100, y=140)

_7 = Button(window, text='7', padx=15, pady=5, width=3, font=('Helvetica', 10, 'bold'),
            bg='#EDC126', command=lambda: click(7))
_7.place(x=180, y=140)

_8 = Button(window, text='8', padx=15, pady=5, width=3, font=('Helvetica', 10, 'bold'),
            bg='#EDC126', command=lambda: click(8))
_8.place(x=260, y=140)

_9 = Button(window, text='9', padx=15, pady=5, width=3, font=('Helvetica', 10, 'bold'),
            bg='#EDC126', command=lambda: click(9))
_9.place(x=20, y=200)

_0 = Button(window, text='0', padx=15, pady=5, width=3, font=('Helvetica', 10, 'bold'),
            bg='#EDC126', command=lambda: click(0))
_0.place(x=100, y=200)

_backspace = Button(window, text='<--', padx=15, pady=5, width=3, bg='#EDC126',
                    font=('Helvetica', 10, 'bold'), command=delete)
_backspace.place(x=180, y=200)

clear_button = Button(window, text='Clear', padx=15, pady=5, width=3, bg='#EDC126',
                      font=('Helvetica', 10, 'bold'), command=clear)
clear_button.place(x=260, y=200)

add_button = Button(window, text='+', padx=15, pady=5, width=3, bg='#EDC126',
                    font=('Helvetica', 10, 'bold'), command=lambda: click('+'))
add_button.place(x=20, y=260)

subtract_button = Button(window, text='-', padx=15, pady=5, width=3, bg='#EDC126',
                         font=('Helvetica', 10, 'bold'), command=lambda: click('-'))
subtract_button.place(x=100, y=260)

multiply_button = Button(window, text='*', padx=15, pady=5, width=3, bg='#EDC126',
                         font=('Helvetica', 10, 'bold'), command=lambda: click('*'))
multiply_button.place(x=180, y=260)

divide_button = Button(window, text='/', padx=15, pady=5, width=3, bg='#EDC126',
                       font=('Helvetica', 10, 'bold'), command=lambda: click('/'))
divide_button.place(x=260, y=260)

opening_bracket = Button(window, text='(', padx=15, pady=5, width=3, bg='#EDC126',
                         font=('Helvetica', 10, 'bold'), command=lambda: click('('))
opening_bracket.place(x=20, y=320)

closing_bracket = Button(window, text=")", padx=15, pady=5, width=3, bg='#EDC126',
                         font=('Helvetica', 10, 'bold'), command=lambda: click(')'))
closing_bracket.place(x=100, y=320)

calculate_button = Button(window, text='Calculate', padx=15, pady=5, width=12, bg='#EDC126',
                          font=('Helvetica', 10, 'bold'), command=calc)
calculate_button.place(x=180, y=320)

window.mainloop()
