import random
import tkinter as tk

from tkinter import ttk
# shuffling of digits
list = []
for i in range(0, 10):
    list.append(i)

random.shuffle(list)

# window name
key = tk.Tk()

key.title("Shuffling numbers")
# size of keypad
key.geometry('600x400')

# adding background color
key.configure(bg='lightslategrey')
exp = " "

# declaring varaibles
name_var = tk.StringVar()
pin_Var = tk.StringVar()

# creating a label for name using widget label
name_label = tk.Label(key, text="USERNAME", font=('calibre', 10, 'bold'))

# creating a entry for input
login_entry = tk.Entry(key, textvariable=name_var, font=('calibre', 10, 'normal'))

# placing the labels in the entry box
name_label.grid(row=0, column=0)
login_entry.grid(row=0, column=1)

exp = ""

# displaying data
def press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)

# clear button
def clear():
    global exp
    exp = ""
    equation.set(exp)

# action button
def action():
    user = login_entry.get()
    passw = Dis_entry.get()
    # print(f"The id and pin you entered is{user}{passw}")
    login(user, passw)

# methos for checking login
def login(user, passw):
    if (user == "ravindra" and passw == "4387"):
        log_in = True
    else:
        log_in = False

    try:
        if log_in == True:
            print("logged in successfullly", user)
        elif log_in == False:
            print("Invalid user or password")

    except:
        db.rollback()
        print("error occured")

# entry box
equation = tk.StringVar()
Dis_entry = ttk.Entry(key, state='readonly', textvariable=equation, show="*")
Dis_entry.grid(rowspan=1, columnspan=100, ipadx=999, ipady=20)

# bottons
a = ttk.Button(key, text=list[0], width=6, command=lambda: press(list[0]))
a.grid(row=2, column=0, ipadx=6, ipady=10)

b = ttk.Button(key, text=list[1], width=6, command=lambda: press(list[1]))
b.grid(row=2, column=1, ipadx=6, ipady=10)

c = ttk.Button(key, text=list[2], width=6, command=lambda: press(list[2]))
c.grid(row=2, column=2, ipadx=6, ipady=10)

d = ttk.Button(key, text=list[3], width=6, command=lambda: press(list[3]))
d.grid(row=3, column=0, ipadx=6, ipady=10)

e = ttk.Button(key, text=list[4], width=6, command=lambda: press(list[4]))
e.grid(row=3, column=1, ipadx=6, ipady=10)

f = ttk.Button(key, text=list[5], width=6, command=lambda: press(list[5]))
f.grid(row=3, column=2, ipadx=6, ipady=10)

g = ttk.Button(key, text=list[6], width=6, command=lambda: press(list[6]))
g.grid(row=4, column=0, ipadx=6, ipady=10)

h = ttk.Button(key, text=list[7], width=6, command=lambda: press(list[7]))
h.grid(row=4, column=1, ipadx=6, ipady=10)

i = ttk.Button(key, text=list[8], width=6, command=lambda: press(list[8]))
i.grid(row=4, column=2, ipadx=6, ipady=10)

clear = ttk.Button(key, text='clear', width=6, command=clear)
clear.grid(row=5, column=0, ipadx=6, ipady=10)

k = ttk.Button(key, text=list[9], width=6, command=lambda: press(list[9]))
k.grid(row=5, column=1, ipadx=6, ipady=10)

enter = ttk.Button(key, text='Enter', width=6, command=action)
enter.grid(row=5, column=2, ipadx=6, ipady=10)

key.mainloop()