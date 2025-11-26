import tkinter as tk
import specSQLpac as TNR    

con = TNR.Constance()

class Mes():
    global inp
    global que
    global ent
    global sub
    global root
    
    def __init__(self,q):
        self.root = tk.Tk()
        self.root.config(bg = con.grey)
        self.inp = tk.StringVar()
        self.root.title("Input window")
        
        self.que = tk.Label(self.root,text = q,fg = con.purp,bg = con.grey,font = ("Comic Sans MS",14,"bold"))
        self.que.pack()
        
        self.ent = tk.Entry(self.root,textvariable=self.inp,fg = con.purp,bg = con.bgrey,font = ("Comic Sans MS",18,"bold"))
        self.ent.pack()
        
        self.sub = tk.Button(self.root,text= "submit",fg = con.purp,command = self.root.destroy,bg = con.bgrey,font = ("Comic Sans MS",14,"bold"))
        self.sub.pack()
    
    def start(self):
        self.root.mainloop()
        return self.inp.get()
    