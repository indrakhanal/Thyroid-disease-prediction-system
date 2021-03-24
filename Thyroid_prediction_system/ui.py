from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
from joblib import dump, load
import numpy as np
import tkinter as tk
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
from Thyroid_prediction_system.normal import Normal
from Thyroid_prediction_system.hypo import HypoThyroidism
from Thyroid_prediction_system.hyper import HyperThyroidism


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title('thyroid disease prediction system')
        self.minsize(850, 850)

        menubar = Menu(self)
        self.config(menu=menubar)
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='exit', command = self.quit)
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='About')

        tab_control = ttk.Notebook(self)
        self.tab1 = ttk.Frame(tab_control)
        tab_control.add(self.tab1, text='Home')

        self.tab3 = ttk.Frame(tab_control)
        tab_control.add(self.tab3, text='Diagnosis Report')
        tab_control.pack(expan=1, fill='both')

        Label(self, text='Machine Learning Tools for Thyroid Disease', bd=15, font=("monaco", 24, 'bold')).pack(side=TOP)
        self.tab_one()
        self.tab_three()

    def tab_one(self):
        label_frame = LabelFrame(self.tab1, text='Enter Known value to all fields', font=("monaco", 16, 'bold'))
        label_frame.grid(column=0, row=2)

        label = Label(label_frame, text='Enter Name:', font=("monaco", 16))
        label.grid(column=0, row=2, padx=12, pady=8)

        self.text_edit1 = Entry(label_frame, width=20)
        self.text_edit1.grid(column=1, row=2)

        label1 = Label(label_frame, text='Enter Age:', font=("monaco", 16))
        label1.grid(column=2, row=2, padx=12, pady=8)

        self.text_edit2 = Entry(label_frame, width=25)
        self.text_edit2.grid(column=3, row=2)

        label_frame1 = LabelFrame(self.tab1, text='Enter M for Male and F for female', font=("monaco", 15, 'bold'))
        label_frame1.grid(column=1, row=3, padx=8, pady=4)

        label2 = Label(label_frame1, text='Enter Sex:', font=("monaco", 16))
        label2.grid(column=0, row=0, padx=8, pady=4)

        self.text_edit3 = Entry(label_frame1, width=25)
        self.text_edit3.grid(column=1, row=0, padx=8, pady=4)

        label_frame2 = LabelFrame(self.tab1, text='Enter exact reported value', font=("monaco", 16, 'bold'))
        label_frame2.grid(column=0, row=5, padx=8, pady=4)

        label3 = Label(label_frame2, text='Enter TSH:', font=("monaco", 16))
        label3.grid(column=0, row=0, padx=8, pady=4)

        self.text_edit4 = Entry(label_frame2, width=25)
        self.text_edit4.grid(column=1, row=0)

        label4 = Label(label_frame2, text='Enter T4U:', font=("monaco", 16))
        label4.grid(column=2, row=0, padx=8, pady=4)

        self.text_edit5 = Entry(label_frame2, width=25)
        self.text_edit5.grid(column=3, row=0)

        label5 = Label(label_frame2, text='Enter FTI:', font=("monaco", 16))
        label5.grid(column=0, row=1, padx=8, pady=4)

        self.text_edit6 = Entry(label_frame2, width=25)
        self.text_edit6.grid(column=1, row=1)

        label6 = Label(label_frame2, text='Enter TT4:', font=("monaco", 16))
        label6.grid(column=2, row=1, padx=8, pady=4)

        self.text_edit7 = Entry(label_frame2, width=25)
        self.text_edit7.grid(column=3, row=1)

        label7 = Label(label_frame2, text='Enter T3:', font=("monaco", 16))
        label7.grid(column=0, row=2, padx=8, pady=4)

        self.text_edit8 = Entry(label_frame2, width=25)
        self.text_edit8.grid(column=1, row=2)

        label_frame3 = LabelFrame(self.tab1, text='Following are true or false enter (T) or (F)', font=("monaco", 14, 'bold'))
        label_frame3.grid(column=1, row=7)

        label8 = Label(label_frame3, text='On_thyroxine:', font=("monaco", 16))
        label8.grid(column=0, row=0, padx=8, pady=4)

        self.text_edit9 = Entry(label_frame3, width=10)
        self.text_edit9.grid(column=1, row=0)

        label12 = Label(label_frame3, text='Thyroid surgery:', font=("monaco", 16))
        label12.grid(column=0, row=2, padx=8, pady=4)

        self.text_edit13 = Entry(label_frame3, width=10)
        self.text_edit13.grid(column=1, row=2)

        self.label_frame4 = LabelFrame(self.tab1, text='result of diagnosis',
                                  font=("monaco", 21), bg='red', fg='blue')
        self.label_frame4.grid(column=0, row=8, padx=8, pady=4)

        label_frame5 = Label(self.tab1, text='', font=("monaco", 16, 'bold'), bg='black', fg='white')
        label_frame5.grid(column=0, row=10)

        button1 = ttk.Button(label_frame5, text='Predict', width=30, command=self.show_data)
        button1.grid(column=0, row=0)

        button2 = ttk.Button(label_frame5, text='Save Result', width=15, command=self.save_result)
        button2.grid(column=1, row=0)

        button3 = ttk.Button(label_frame5, text='Quit', width=15, command=self.window_close)
        button3.grid(column=2, row=0)

    def show_data(self):
        self.name = self.text_edit1.get()
        self.age = self.text_edit2.get()
        sex = self.text_edit3.get()
        self.tsh = self.text_edit4.get()
        self.t4u = self.text_edit5.get()
        self.fti = self.text_edit6.get()
        self.tt4 = self.text_edit7.get()
        self.t3 = self.text_edit8.get()
        on_thyroxine = self.text_edit9.get()
        surgery = self.text_edit13.get()
        if (len(self.name) and len(self.age) and len(self.tsh) and len(self.t4u) and len(sex) and len(self.fti) and len(self.tt4) and len(self.t3) and len(on_thyroxine) \
             and len(surgery)) != 0:
            try:
                if sex == 'M':
                    self.sex = 1
                elif sex == 'F':
                    self.sex = 0

                    # validation on_thyroxine
                if on_thyroxine == 'T':
                    self.thyroxine=1
                elif on_thyroxine == 'F':
                    self.thyroxine=0

                        # validation on surgery
                if surgery == 'T':
                    self.surgery = 1
                elif surgery == 'F':
                    self.surgery = 0

                self.ml_model()
            except:
                ms.showwarning('Warning!!','letters are case sensitive please recheck')
        else:
            ms.showerror('Error!!', 'you should fill all the field')

    def clear_all_text(self):
        self.display_data().delete("all")

    def window_close(self):
        self.quit()
        self.destroy()
        exit()

    def ml_model(self):
        self.age = float(float(self.age))/100
        input = np.array([[self.age, float(self.sex), self.thyroxine, self.surgery, float(self.tsh), float(self.t3), float(self.tt4),  float(self.t4u), float(self.fti)]])
        print(input)
        model = load('final_model.joblib')
        print(model, 'model')
        result = model.predict(input)
        if result == [1]:
            self.result = 'Normal'
        if result == [2]:
            self.result = 'Hypothyroidism'
        if result == [3]:
            self.result = 'Hyperthyroidism'

        label = Label(self.label_frame4, text=f'The diagnosis of {self.name}  is  {self.result}',font=("monaco", 16, 'bold'), bg='white')
        label.grid(column=0, row=0)

    def save_result(self):
        try:
            if len(self.result)>0:
                conn = sqlite3.connect('thyroid_info.db')
                c = conn.cursor()
                c.execute('INSERT INTO Patient (name, age, result, tsh, tT3, TT4, T4U,FTI ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                          (self.name, self.age*100, self.result, self.tsh, self.t3, self.tt4, self.t4u, self.fti))
                conn.commit()
                ms.showinfo('SUCCESS!!', 'Record added Successfully')
        except:
            ms.showerror('ERROR!!',' you first need to predict data')

    def display_data(self):
        con = sqlite3.connect('thyroid_info.db')
        con.cursor()
        all_data = con.execute("select * from Patient")
        return all_data

    def tab_three(self):
        new_label = LabelFrame(self.tab3, text=f"", font=("monaco", 16, 'bold'), bg='white')
        new_label.grid(column=0, row=0)

        label_frame = LabelFrame(self.tab3, text=f"PATIENT'S DIAGNOSIS RECORDS", font=("monaco", 16, 'bold'))
        label_frame.grid(column=0, row=1)

        tree = ttk.Treeview(label_frame, column=("name", "age ", "Result", "tsh", "t3", "tt4", "t4u", "fti"), show='headings')
        tree.column("#1", anchor=tk.W, minwidth=0, width=120)
        tree.heading("#1", text="Patient Name")
        tree.column("#2", anchor=tk.CENTER, minwidth=0, width=120)
        tree.heading("#2", text="Age")
        tree.column("#3", anchor=tk.W, minwidth=0, width=120)
        tree.heading("#3", text="Result")
        tree.column("#4", anchor=tk.CENTER, minwidth=0, width=120)
        tree.heading("#4", text="TSH")
        tree.column("#5", anchor=tk.CENTER, minwidth=0, width=120)
        tree.heading("#5", text="T3")
        tree.column("#6", anchor=tk.CENTER, minwidth=0, width=120)
        tree.heading("#6", text="TT4")
        tree.column("#7", anchor=tk.CENTER, minwidth=0, width=120)
        tree.heading("#7", text="T4U")
        tree.column("#8", anchor=tk.CENTER, minwidth=0, width=100)
        tree.heading("#8", text="FTI")

        tree.pack(side=LEFT, expand=True, fill=BOTH)

        data = self.display_data()
        list_item = []
        for row in data:
            tree.insert("", tk.END, values=row)
            list_item.append(row)
        list_count = len(list_item)

        label = Label(new_label, text=f'total {list_count} item Tested', bg='white')
        label.grid(row=0, column=1)

        new_list = []
        new_list1 = []
        new_list2 = []
        for item in list_item:
            num = (item[2]).count('Normal')
            new_list.append(num)
            hypo = (item[2]).count('Hypothyroidism')
            new_list1.append(hypo)
            hyper = (item[2]).count('Hyperthyroidism')
            new_list2.append(hyper)
        normal = (sum(new_list))
        hypo = sum(new_list1)
        hyper = sum(new_list2)

        # calling normal class here

        label1 = Label(new_label, text=f'Into which', bg='white')
        label1.grid(row=1, column=1)
        label2 = Button(new_label, text=f' {normal} item Tested Normal', command = Normal, bg='skyblue', font=("monaco", 12, 'bold'))
        label2.grid(row=2, column=1)
        label2 = Button(new_label, text=f' {hypo} item Tested Hypothyroidism', command=HypoThyroidism, bg='pink', font=("monaco", 12, 'bold'))
        label2.grid(row=3, column=1)
        label2 = Button(new_label, text=f'{hyper} item Tested Hyperthyroidism', command=HyperThyroidism, bg='orange', font=("monaco", 12, 'bold'))
        label2.grid(row=5, column=1)


win = Window()
win.mainloop()