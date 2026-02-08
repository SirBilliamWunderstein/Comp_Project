import tkinter as tk
import specSQLpac as SBR
import specTKpac as DIU
from PIL import ImageTk,Image

con = SBR.Constance()
con.initimg()

class infbox(tk.Canvas):
    global polyfera
    global yscr
    global TITLECARD
    global PackFr
    global opBud
    global descW
    global PyP
    
    def __init__(self,polyfera,PyP):
        self.polyfera = polyfera
        self.PyP = PyP
        super().__init__(self.polyfera,width = 300,height = 450,scrollregion=(0,0,300,1500),bg = con.grey)
        
        self.place(x=0,y=150)
        
        self.PackFr = tk.Frame(self,bg = con.grey)
        self.TITLECARD = tk.Label(self.PackFr,font = ("Comic Sans MS",18,"bold"),bg= con.bgrey,fg = con.purp,borderwidth = 0)
        qq = ImageTk.PhotoImage(con.SampBud)
        self.opBud = tk.Button(self.PackFr,image = qq,width = 300,height = 75,bg = con.bgrey)
        self.opBud.image = qq
        self.descW = tk.Label(self.PackFr,bg = con.grey,fg = con.purp,font = ("Comic Sans MS",14,"bold"))
        
        self.yscr = tk.Scrollbar(self,orient = "vertical",command=self.yview)
        self.config(yscrollcommand=self.yscr.set)
        
        self.focus_set()
        '''
        self.bind("<Button-5>",self.upscr)
        self.bind("<Button-4>",self.downscr)
        self.PackFr.bind("<Button-5>",self.upscr)
        self.PackFr.bind("<Button-4>",self.downscr)
        self.TITLECARD.bind("<Button-5>",self.upscr)
        self.TITLECARD.bind("<Button-4>",self.downscr)
        self.opBud.bind("<Button-5>",self.upscr)
        self.opBud.bind("<Button-4>",self.downscr)
        self.descW.bind("<Button-5>",self.upscr)
        self.descW.bind("<Button-4>",self.downscr)'''
        
        self.bind("<MouseWheel>",self.on_mousewheel)
        self.PackFr.bind("<MouseWheel>",self.on_mousewheel)
        self.TITLECARD.bind("<MouseWheel>",self.on_mousewheel)
        self.opBud.bind("<MouseWheel>",self.on_mousewheel)
        self.descW.bind("<MouseWheel>",self.on_mousewheel)

    
    def upscr(self,event):
        self.yview_scroll(1, "units")
    
    def on_mousewheel(self,event):
        if event.num == 5 or event.delta < 0:
            self.upscr(event)
        else:
            self.downscr(event)
    
    def TestInsertion(self,desc):
        q = len(desc)
        Q = ""
        for i in range(q):
            if (i+1)%30 == 0:
                Q = Q + desc[i].lower() + "\n"
            else:
                Q += desc[i].lower()
        self.descW.config(text = Q)
        
    def TleInsertion(self,title):
        q = len(title)
        Q = ""
        for i in range(q):
            if (i+1)%23 == 0:
                Q = Q + title[i].lower() + "\n"
            else:
                Q += title[i].lower()
        self.TITLECARD.config(text = Q)
        self.create_text((0,0),text = Q,anchor = "nw")
    
    def PacMan(self):
        self.TITLECARD.grid(row = 0,column = 0)
        self.descW.grid(row = 1,column = 0)
        self.opBud.grid(row = 2,column = 0)
        self.create_window((0, 0), window=self.PackFr, anchor="nw")
    
    def False_Maker(self,typ):
        desc = ""
        if typ == 1:
            desc += "It's Grass\nor is it?"
        elif typ == 2:
            desc += "It's water!\nMolecular formula: H2O\nHybridisation: sp3\nbond angle: 104.5"
        elif typ == 3:
            desc += "I live here!"
        elif typ == 4:
            desc += "Hey!\nIm Walking Here"
        elif typ == 5:
            desc += "TREE"
        
        self.TleInsertion("")
        self.TestInsertion(desc)
        #self.TleInsertion(" ")
        self.buttonman(4)
        self.PacMan()
        pass
    
    def Maker(self,IK):
        DB = self.PyP.db_Get(IK)
        desc = self.PyP.Nam_get(IK,DB,"descr")
        ra = self.PyP.Nam_get(IK,DB,"Title")
        self.TestInsertion(desc)
        self.TleInsertion(ra)
        self.buttonman(IK, DB)
        self.PacMan()
        
    def buttonman(self,IK,type = "0"):
        if type == "0" or type == con.anon:
            q = ImageTk.PhotoImage(con.SampBud)
            self.opBud.config(image = q,command = lambda : print())
            self.opBud.image = q
            pass
        elif type == con.resto:
            q = ImageTk.PhotoImage(con.RbudI)
            self.opBud.config(image = q,command = lambda : self.maker_Func(self.opBud.IK,1))
            self.opBud.image = q
            self.opBud.IK = IK
        elif type == con.eve:
            q = ImageTk.PhotoImage(con.EbudI)
            self.opBud.config(image = q,command = lambda : self.maker_Func(self.opBud.IK,2))
            self.opBud.IK = IK
            self.opBud.image = q
    
    def maker_Func(self,IK,type):
        if type == 1:
            q = self.PyP.Nam_get(IK,con.resto,"Title")
            print(q)
            DIU.Resta(q,self.PyP,self.polyfera)
        elif type == 2:
            q = tk.Toplevel(self.polyfera)
            q.configure(width = 512,height = 512)
            check = self.PyP.Postriever(IK)
            if check == con.success:
                imag = ImageTk.PhotoImage(Image.open("./Pic/"+IK+".png"))
                ss = tk.Label(q,image = imag)
                ss.image = imag
                #ss.place(x = 0,y = 0)
                ss.pack()
                q.mainloop()
    
    def downscr(self,event):
        self.yview_scroll(-1, "units")



