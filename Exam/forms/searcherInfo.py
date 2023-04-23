
import funcs
from tkinter import *
import tkinter as tk
from tkinter import ttk
from forms.review import review
from forms.viewReview import viewReview

class searcher(tk.Tk):
    def __init__(self,info ):
        super().__init__()
        frame = ttk.Frame(self)
        self.info=info
        self.title(f"Информация по {info[1]} ")
        self.geometry('400x800')
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=1)


        sql=f"SELECT * FROM Products where FMID = '{info[0]}' "
        data = funcs.getTables(sql)
        data2 = funcs.getTables("select fmid,avg(rate) as rating from Reviews group by fmid ;")
        data2["FMID"] = data2["FMID"].astype(int)
        df = data.merge(data2, on="FMID", how='left')
        rows = df.values
        headings = list(df.columns)

        i=0
        for head in headings:

            ttk.Label(frame,text=head).grid(row=i,column=0,sticky=W)
            i+=1

        j=0
        for row in rows[0]:
            print(row)
            ttk.Label(frame,text=row).grid(row=j,column=1,sticky=W)
            j+=1

        ttk.Button(frame, text="Просмотреть отзывы", command=self.viewReview).grid(row=i, column=0)
        ttk.Button(frame, text="Оставить отзыв", command=self.addRewiew).grid(row=j+1, column=0)
        frame.pack()

    def addRewiew(self):
        rev = review(self.info[0])
        self.destroy()
        pass

    def viewReview(self):
        vrev = viewReview(self.info[0])
        self.destroy()
        pass