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
    
    def __init__(self,root,posx,posy,imag,infbox,PyP):
        self.tree = root
        self.xx = posx
        self.yy = posy
        self.infobox = infbox
        self.PyP = PyP
        super().__init__(self.tree,image = imag,highlightthickness = 0,borderwidth = 0,command = self.Box_Loader)
        self.image = imag
    
    def Box_Loader(self):
        self.tree.place_forget()
        self.fr = tk.Frame(self.tree,width = 600,height = 600)
        self.fr.place(y = 0,x = 0)
        self.til = SBR.MakTil(self.fr,self.xx,self.yy,self.PyP,self.infobox)
        
        
        
