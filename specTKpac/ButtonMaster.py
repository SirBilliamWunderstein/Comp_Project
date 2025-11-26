import tkinter as tk
import specTKpac as SBR

class buiton(tk.Button):
    global tree
    global infbx
    global xx
    global yy
    global Pyp
    global fr
    global til
    global menbx
    
    def __init__(self,root,posx,posy,imag,infbox = 0,PyP=0,menbox = 0):
        self.tree = root
        self.xx = posx
        self.yy = posy
        self.menbx = menbox
        self.PyP = PyP
        super().__init__(self.tree,image = imag,highlightthickness = 0,borderwidth = 0,command = self.Box_Loader)
        self.image = imag
    
    def Box_Loader(self):
        self.fr = tk.Frame(self.tree,width = 700,height = 700)
        self.root.place_forget()
        self.fr.place(y = 0,x = 300)
        self.til = SBR.TilLoader(self.fr,self.xx,self.yy,self.PyP)
        self.menbx.bbud.config(command = self.Lox_Boader)
        self.til.twofive()
    
    def Lox_Boader(self):
        self.root.place(x = 300,y= 0)
        self.fr.destroy()
        self.menbx.bbud.config(command = null)
    
    def hoverboard(self):
        pass