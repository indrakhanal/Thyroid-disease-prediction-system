from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3


class HypoThyroidism(Tk):
    def __init__(self):
        super(HypoThyroidism, self).__init__()
        self.title('Data Collection only for Hypothyroidism cases')
        self.minsize(400, 200)
        self.show_normal()

    def display_data(self):
        con = sqlite3.connect('thyroid_info.db')
        con.cursor()
        all_data = con.execute("select * from Patient where result='Hypothyroidism'")
        return all_data

    def show_normal(self):
        label_frame1 = LabelFrame(self, text=f"Result of patient With Hypothyroidism Result", font=("monaco", 16, 'bold'))
        label_frame1.grid(column=0, row=0)

        trees = ttk.Treeview(label_frame1, column=("Name", "Age ", "Result", "tsh", "t3", "tt4", "t4u", "fti"),
                            show='headings')
        trees.column("#1", anchor=tk.W, minwidth=0, width=100)
        trees.heading("#1", text="Patient Name")
        trees.column("#2", anchor=tk.CENTER, minwidth=0, width=40)
        trees.heading("#2", text="Age")
        trees.column("#3", anchor=tk.W, minwidth=0, width=100)
        trees.heading("#3", text="Result")
        trees.column("#4", anchor=tk.CENTER, minwidth=0, width=50)
        trees.heading("#4", text="TSH")
        trees.column("#5", anchor=tk.CENTER, minwidth=0, width=50)
        trees.heading("#5", text="T3")
        trees.column("#6", anchor=tk.CENTER, minwidth=0, width=50)
        trees.heading("#6", text="TT4")
        trees.column("#7", anchor=tk.CENTER, minwidth=0, width=50)
        trees.heading("#7", text="T4U")
        trees.column("#8", anchor=tk.CENTER, minwidth=0, width=50)
        trees.heading("#8", text="FTI")

        trees.pack(side=LEFT, expand=True, fill=BOTH)

        data = self.display_data()
        for item in data:
            trees.insert("", tk.END, values=item)
            # list_item.append(row)
