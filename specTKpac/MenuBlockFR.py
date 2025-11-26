import tkinter as tk
from tkinter import font
import specSQLpac as TNR
from PIL import ImageTk

con = TNR.Constance()
con.initimg()

class MBlock(tk.Frame):
    global nam
    global pric
    global refno
    global cat
    global win
    global Frame
    global namL
    global pricL
    global catL
    global adb
    global subb
    global plus
    global cart

    def __init__(self,window,name,price,refnumber,category,cart = 0):
        self.nam = name
        self.pric = price
        self.refno = refnumber
        self.cat = category + " "
        self.wind = window
        self.cart = cart

        super().__init__(self.wind,bg=con.grey,width=600,height = 100,relief=tk.RIDGE,borderwidth=2)

        self.plus = ImageTk.PhotoImage(con.tkplus)
        self.minus = ImageTk.PhotoImage(con.tkminus)
        self.namL = tk.Label(self,text=self.nam,fg = con.purp,bg=con.bgrey,font = ("Comic Sans MS",18,"bold"),borderwidth=2,relief = "sunken")
        self.pricL = tk.Label(self,text=str(self.pric) + "₹",fg = con.purp,bg=con.bgrey,font = ("Comic Sans MS",18,"bold"),borderwidth=2,relief = "sunken")
        self.catL = tk.Label(self,text=str(self.cat),fg = con.purp,bg=con.bgrey,font = ("Comic Sans MS",14,"bold"),borderwidth=2,relief = "sunken")
        self.adb = tk.Button(self,image = self.plus,command = lambda : self.place_cart(),border = 1,bg=con.bgrey,relief = tk.RAISED)
        self.subb = tk.Button(self,image = self.minus,command = lambda : self.rem_cart(),border = 1,bg=con.bgrey,relief = tk.RAISED)

        self.subb.place(relx = 0.9,rely = 0.75,anchor = tk.CENTER)
        self.adb.place(relx = 0.6,rely = 0.75,anchor = tk.CENTER)
        self.namL.place(relx=0.02,rely = 0.02)
        self.pricL.place(relx = 0.02,rely = 0.53)
        self.catL.place(relx = 0.9,rely = 0.02)

    def place_cart(self):
        self.cart.add(self.refno)
        print("add")

    def rem_cart(self):
        self.cart.sub(self.refno)
        print("sub")