# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 17:08:31 2018

@author: My PC
"""

import tkinter as tk

frame = tk.Tk()
#frame = tk.Frame(root)
#frame.pack()

w = tk.Label(frame,text="ATM").grid(row=0, column=1, columnspan=2,rowspan=1,pady=5,padx=5)


e = tk.Entry(frame)
e.grid( row = 1, rowspan = 1, columnspan = 4,padx = 10)
insert = tk.Button(frame,text="insert card").grid(row=3,column=1,columnspan=2,rowspan=1, ipadx=30)

#buttons
one = tk.Button(frame, width = 10, text = "1").grid(row = 6, column = 0)
two = tk.Button(frame, width = 10, text = "2").grid(row = 6, column = 1)
three = tk.Button(frame, width = 10, text = "3").grid(row = 6, column = 2)
enter_button = tk.Button(frame, width = 10,text = "ENTER").grid(row = 6, column = 3)

four = tk.Button(frame, width = 10, text = "4").grid(row = 7, column = 0)
five = tk.Button(frame, width = 10, text = "5").grid(row = 7, column = 1)
six = tk.Button(frame, width = 10, text = "6").grid(row = 7, column = 2)
clear_button = tk.Button(frame, width = 10, text = "CLEAR").grid(row = 7, column = 3)

seven = tk.Button(frame, width = 10, text = "7").grid(row = 8, column = 0)
eight = tk.Button(frame, width = 10, text = "8").grid(row = 8, column = 1)
nine = tk.Button(frame, width = 10, text = "9").grid(row = 8, column = 2)
cancel_button = tk.Button(frame, width = 10, text = "CANCEL").grid(row = 8, column = 3)



frame.title('ATM INTERFACE')
frame.mainloop()
