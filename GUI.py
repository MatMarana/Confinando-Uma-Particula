from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=4)
root.mainloop()