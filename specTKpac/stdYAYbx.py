import tkinter as tk
import specSQLpac as TNR    

con = TNR.Constance()

class yay():
    global que
    global ent
    global sub
    global root
    
    def __init__(self,q):
        self.root = tk.Tk()
        self.root.config(bg = con.grey)
        self.root.title("YAY")
        
        self.que = tk.Label(self.root,text = q,fg = con.purp,bg = con.grey,font = ("Comic Sans MS",14,"bold"))
        self.que.pack()
        
        self.sub = tk.Button(self.root,text= "OK",fg = con.purp,command = self.root.destroy,bg = con.bgrey,font = ("Comic Sans MS",14,"bold"))
        self.sub.pack()
        
        self.root.mainloop()