import tkinter as tk
import specSQLpac as TNR
import specTKpac as SBR
from PIL import ImageTk

con = TNR.Constance()
con.initimg()

class Cart():
    global cart
    global PyP
    global menu
    global manget
    global bute
    global itsself
    
    def __init__(self,PyP,menu,itsself):
        self.itsself = itsself
        self.cart = {}
        self.PyP = PyP
        self.menu = menu
    
    def add(self,refnum):
        q = refnum
        if q in list(self.cart.keys()):
            self.cart[q] += 1
        else:
            self.cart[q] = 1
        print(self.cart)
    
    def sub(self,refnum):
        q = refnum
        try:
            if self.cart[q] == 1:
                del self.cart[q]
            else:
                self.cart[q] -= 1
        except:
            pass
        
    def induce(self):
        self.manget = tk.Toplevel(self.itsself.tree)
        self.manget.config(bg = con.grey)
        q = tk.Label(self.manget,text = "CART",fg = con.purp,bg = con.grey,font = ("Comic Sans MS",18,"bold"))
        S = ""
        print(self.cart)
        for i in list(self.cart.keys()):
            for j in self.menu:
                if i == j[0]:
                    S += j[1] + "        " + str(j[2])+"*"+str(self.cart[i]) +"\n"
                else:
                    pass
        s = tk.Label(self.manget,text = S,fg = con.purp,bg = con.bgrey,font = ("Comic Sans MS",14,"italic"))
        self.bute = tk.Button(self.manget,text = "PLACE ORDER",command =  lambda:self.finnish(S),fg = con.purp,bg = con.bgrey,font = ("Comic Sans MS",18,"italic"))
        q.pack()
        s.pack()
        self.bute.pack()
        self.manget.mainloop()
        
    def finnish(self,S):
        W = SBR.Mes("Please Enter Your Address",True,self.itsself.tree)
        ad = W.start()
        Order = "An Order has been placed with contents:\n" + S
        IK = self.PyP.Rest_IK_get(self.itsself.name)
        self.PyP.send_Request(IK,Order,ad)
        SBR.yay("Order Placed")
        #self.itsself.destroy()
        #self.manget.destroy()
        
class Resta(tk.Toplevel):
    global menu
    global placeholder
    global cart
    global MList
    global Lbud
    global Rbud
    global Cbud

    def __init__(self,name = "wee",PyP = 0,tree = 0):
        self.tree = tree
        self.PyP=PyP
        self.name = name
        self.menu = self.PyP.fetch_Resto_men(self.PyP.IK_get(name,con.resto))
        self.placeholder = 0
        super().__init__(tree)
        self.cart = Cart(self.PyP,self.menu,self)
        self.title(name)
        self.config(background = con.grey)
        self.geometry("1300x450")
        self.resizable(False,False)

        self.MList = []
        self.creat_menu()
        self.plac_button()
        
        q = ImageTk.PhotoImage(con.Larrow)
        s = ImageTk.PhotoImage(con.Rarrow)
        t = ImageTk.PhotoImage(con.cartLO)
        self.Lbud = tk.Button(self,image = q,command = lambda : self.movL(),bg=con.bgrey,border = 0,height = 395)#,width = 62,height = 250
        self.Rbud = tk.Button(self,image = s,command = lambda : self.movR(),bg=con.bgrey,border = 0,height = 395)
        self.Cbud = tk.Button(self,image = t,command = lambda : self.cart.induce(),bg=con.bgrey,border = 0,height = 45,width = 1295)
        self.Cbud.image = s 
        self.Lbud.image = q
        self.Rbud.image = t
        self.Lbud.place(x = 0,y = 0)
        self.Cbud.place(x = 0,y = 400)
        self.Rbud.place(relx = 1,rely = 0.0,anchor = "ne")
        
        self.mainloop()

    def creat_menu(self):
        for i in self.MList:
            i.destroy()
            
        self.MList = []
        for i in range(self.placeholder,self.placeholder+12):
            try:
                self.MList.append(SBR.MBlock(self,self.menu[i][1],self.menu[i][2],self.menu[i][0],self.menu[i][3],self.cart))
            except:
                self.MList.append(SBR.MBlock(self,"","","",""))
    
    def plac_button(self):
        self.MList[0].place(x=50,y=0)
        self.MList[1].place(x=650,y=0)
        self.MList[2].place(x=50,y=100)
        self.MList[3].place(x=650,y=100)
        self.MList[4].place(x=50,y=200)
        self.MList[5].place(x=650,y=200)
        self.MList[6].place(x=50,y=300)
        self.MList[7].place(x=650,y=300)
          
    def movR(self):
        if self.placeholder < len(self.menu):
            self.placeholder += 8
            self.creat_menu()
            self.plac_button()
        else:
            pass
        
    def movL(self):
        if self.placeholder != 0:
            self.placeholder -= 8
            self.creat_menu()
            self.plac_button()
        else:
            pass  
                
