# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 17:08:31 2018

@author: My PC
"""

import tkinter as tk

frame = tk.Tk()
frame.geometry('360x360')
#frame = tk.Frame(root)
#frame.pack()

w = tk.Label(frame,text="ATM",font = ("Arial Bold", 40), fg = "blue").grid(row=0, column=1, columnspan=2,rowspan=1,pady=5,padx=5)


e = tk.Entry(frame)
e.grid( row = 1, rowspan = 1, columnspan = 4,padx = 10)
insert = tk.Button(frame,text="insert card").grid(row=3,column=1,columnspan=2,rowspan=1, ipadx=30)

#buttons
one = tk.Button(frame, width = 10, text = "1", font = ("Arial Bold", 10)).grid(row = 6, column = 0, padx = 5, pady = 5)
two = tk.Button(frame, width = 10, text = "2", font = ("Arial Bold", 10)).grid(row = 6, column = 1, padx = 5, pady = 5)
three = tk.Button(frame, width = 10, text = "3", font = ("Arial Bold", 10)).grid(row = 6, column = 2, padx = 5, pady = 5)
enter_button = tk.Button(frame, width = 10,text = "ENTER", fg = 'green', font = ("Arial Bold", 10)).grid(row = 6, column = 3, padx = 5, pady = 5)

four = tk.Button(frame, width = 10, text = "4", font = ("Arial Bold", 10)).grid(row = 7, column = 0, padx = 5, pady = 5)
five = tk.Button(frame, width = 10, text = "5", font = ("Arial Bold", 10)).grid(row = 7, column = 1, padx = 5, pady = 5)
six = tk.Button(frame, width = 10, text = "6", font = ("Arial Bold", 10)).grid(row = 7, column = 2, padx = 5, pady = 5)
clear_button = tk.Button(frame, width = 10, text = "CLEAR", fg = 'orange', font = ("Arial Bold", 10)).grid(row = 7, column = 3, padx = 5, pady = 5)

seven = tk.Button(frame, width = 10, text = "7", font = ("Arial Bold", 10)).grid(row = 8, column = 0, padx = 5, pady = 5)
eight = tk.Button(frame, width = 10, text = "8", font = ("Arial Bold", 10)).grid(row = 8, column = 1, padx = 5, pady = 5)
nine = tk.Button(frame, width = 10, text = "9", font = ("Arial Bold", 10)).grid(row = 8, column = 2, padx = 5, pady = 5)
empty_button = tk.Button(frame, width = 10, text = "", state = "disabled").grid(row = 8, column = 3, padx = 5, pady = 5)

minus = tk.Button(frame, width = 10, text = "-", font = ("Arial Bold", 10)).grid(row = 9, column = 0, padx = 5, pady = 5)
zero = tk.Button(frame, width = 10, text = "0", font = ("Arial Bold", 10)).grid(row = 9, column = 1, padx = 5, pady = 5)
plus = tk.Button(frame, width = 10, text = "+", font = ("Arial Bold", 10)).grid(row = 9, column = 2, padx = 5, pady = 5)
cancel_button = tk.Button(frame, width = 10, text = "CANCEL", fg = "red", font = ("Arial Bold", 10)).grid(row = 9, column = 3, padx = 5, pady = 5)



frame.title('ATM INTERFACE')
frame.mainloop()
