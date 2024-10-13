from tkinter import ttk
from tkinter import Tk
from tkinter import*
tk =Tk()
tk.geometry('200x200')
a = Spinbox(tk , from_ = 1, to = 31)
w = Spinbox(tk , from_ = 1901, to =2024 )
months=['January','February','March','April','May','June','August','September','October','November','December']
w.pack()
a.pack()
monthchoosen=ttk. Combobox(width=20, values= months)
monthchoosen.pack()
Label(tk,text="selected month is March").pack()
button=Button(tk,text='click',font=('times new roman',33),fg='dark blue',bg='light blue')
button.pack()
tk.mainloop()