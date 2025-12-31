import tkinter as tk
import specSQLpac as TNR
import pickle as dex
import random as rd
from PIL import Image,ImageTk

con = TNR.Constance()
con.initimg()

class MakTil():
    global x
    global y
    global pos
    global polyfera
    global bdit
    global bitdat
    global imageL
    global PyP
    
    def __init__(self,fr,x,y,PyP,infobox):
        self.infobox = infobox
        self.x = x
        self.PyP = PyP
        self.y = y
        self.pos = str(x) + ";" + str(y)
        self.polyfera = fr
        self.bdit = {}
        self.imageL = {}
        
        binfil = open("./bindump/mapdat/"+self.pos + ".dat","rb")
        q = dex.load(binfil)
        print(q)
        sp = 0
        if q[0] == 1:
            self.bitdat = q[1]
            sp = 1
        elif q[0] == 0:
            self.bitdat = q[1:]
        binfil.close()
        
        self.twofive(sp)
    
    def twofive(self,sp = 0):
        if sp == 0:
            s = 1
            for i in self.bitdat:
                timag = ImageTk.PhotoImage(self.image_get(i,s))
                self.bdit[s] = localbutton(self.polyfera,i,timag,self.infobox)
                self.bdit[s].cdse = i
                self.bdit[s].image = timag
                s += 1
            print(self.bdit)
        self.plac_button()
    
    def plac_button(self):
        for i in list(self.bdit.keys()):
            self.bdit[i].place(x = ((i-1)%5)*120 - 1,y = ((i-1)//5)*120 - 1)

    def image_get(self,ip,s):
        if ip == 1:
            num = rd.randint(0,1)
            return con.grassL[num]
        elif ip == 2:
            return con.waterL
        elif ip == 3:
            return con.buildL
        elif ip == 4:
            return con.roadL
        elif ip == 5:
            return con.treeL
        else:
            lee = ""
            if PyP.db_Get(IK) == con.resto:
                lee = con.rIc
            elif PyP.db_Get(IK) == con.eve:
                lee = con.eIc
            elif PyP.db_Get(IK) == con.anon:
                lee = Image.open("./Icon/" + ip + ".png")
            return lee

class localbutton(tk.Button):
    def __init__(self,polyfera,coma,timag,infobox):
        self.i = coma
        self.infobox = infobox
        super().__init__(polyfera,command = self.clicke,image = timag,height= 120,width = 120,borderwidth = 0)
    
    def clicke(self):
        ip = self.i
        try:
            if ip == 1 or ip == 2 or ip == 3:
                self.infobox.false_Maker()
            else:
                self.infobox.Maker(ip)
        except:
            self.infobox.Maker(ip)



