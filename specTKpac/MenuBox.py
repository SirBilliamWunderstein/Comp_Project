import tkinter as tk
import specSQLpac as TNR
import specTKpac as SBR
import os

con = TNR.Constance()

class MenuBox(tk.Frame):
    global user
    global reg1
    global logout
    
    def __init__(self,tree,key_app,button_do,PyP = 0,infobox = 0):
        self.infobox = infobox
        self.key_app = key_app
        self.button_do = button_do
        self.tree = tree
        self.PyP = PyP
        super().__init__(self.tree,width = 300,height = 150,bg = con.grey)
        
        self.user = tk.Label(self,text = "Sir Billiam",fg = con.purp,bg = con.grey,font = ("Comic Sans MS",18,"bold"))#text = self.PyP.infodat[0])
        self.logout = tk.Button(self,text = "logout",fg = con.purp,bg = con.bgrey,font = ("Comic Sans MS",14,"bold"))
        self.reg1 = tk.Button(self,text = "reg1",command = self.regionreload,fg = con.purp,bg = con.bgrey,font = ("Comic Sans MS",14,"bold"))
        
        self.user.place(x = 10,y = 10)
        self.logout.place(x = 10,y = 100)
        self.reg1.place(x = 175,y = 100)
        
        self.place(x = 0,y = 0)
    
    def logout(self):
        os.remove("./bindump/ret.dat")
        system.exit(0)
    
    def regionreload(self):
        self.key_app.canvas.destroy()
        self.button_do = SBR.Buddon(self.tree, "./imsorrylilone.png",self.PyP,self.infobox)
        self.key_app = SBR.Keys(self.tree, selfbutton_do.canvas)
        
        