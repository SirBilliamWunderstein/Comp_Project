import specSQLpac as DIU
import specTKpac as SBR
import mysql.connector as dcp
import random as rd
import pickle as dex
import tkinter as tk
from PIL import Image,ImageTk;

global pYp
global PyP

con = DIU.Constance()

def Login():
    Q = SBR.Mes("Enter Username:")
    use = Q.start()
        
    R = SBR.Mes("Enter Password")
    pas = R.start()
    lak = ""
    port = dcp.connect(user = "root",host = "localhost",password = "mysql",auth_plugin='mysql_native_password')
    ship = port.cursor()
    try:
        ship.execute("CREATE USER '{}'@'localhost' IDENTIFIED WITH mysql_native_password BY '{}';".format(use,pas))
        for i in [con.lak,con.resto,con.eve,con.reqb,con.anon]:
            ship.execute("GRANT ALL ON {} TO '{}'@'localhost';".format(i,use))
        for i in range(16):
            lak += chr(rd.randint(ord("a"),ord("z")))
        ship.execute("use {}".format(con.lak,))
        ship.execute("insert into listak values('{}','{}')".format(lak,use))
        port.commit()
        pYp = DIU.PypedPyper(use,pas,lak)
        PyP = DIU.PyperedPype(use,pas);
    except:
        S = SBR.Mes("Enter LAK")
        lak = S.start()
        pYp = DIU.PypedPyper(use,pas,lak)
        PyP = DIU.PyperedPype(use,pas);
    
    port.close()
    
try:
    binfil = open("./bindump/LAK.dat","rb")
    L = dex.load(binfil)
    pYp = DIU.PypedPyper(L[0],L[2],L[1])
    PyP = DIU.PyperedPype(L[0],L[2]);
except FileNotFoundError:
    Login()

def Lister(li,db):
    Q = "____________________________OPTION_______________________________\n"
    for i in range(len(li)):
        Q += "\t" + str(i+1) + "\t\t" + li[i] + ":" + PyP.Nam_get(li[i],db) + "\n"
    Q += "\t\t\t\t\t\t\t\t\t\tChoose:"
    
    return Q

Mainop = """
____________________________OPTION_______________________________

    1        Show Restaurants
    2        Show Events
    3        Show Anonymous Location
    4        Open Create Menu
                                        Choose:  
"""

Createop = """
____________________________OPTION_______________________________

    1        Create Restaurant
    2        Create Events
    3        Create Anonymous Location
                                        Choose:
"""

Changeop = """
____________________________OPTION_______________________________
    
    1        Update Info
    2        Update Description
    3        View Info
    4        View Description
                                        Choose:
"""

def resto_men_up(IK):
    while True:
        Q = int(input("Enter Reference Number of Menu:"))
        sq = input("Name:")
        l = int(input("Price:"))
        my = input("Category:")
        try:
            pYp.Standard_column_updater(con.resto,IK,"Food",Q,"ID",sq)
            pYp.Standard_column_updater(con.resto,IK,"Price",Q,"ID",l)
            pYp.Standard_column_updater(con.resto,IK,"Category",Q,"ID",my)
        except:
            pYp.ship.execute("insert into {} values({},'{}',{},'{}')".format(IK,Q,sq,l,my))
            pYp.portbay.commit()
        
        if input("continue(y/n)?") == "n":
            break

def changeOp(IK,db):
    x = input(Changeop)
    if x == 1:
        if db == con.anon or con.eve:
            ss = input("Enter File Location of picture [png format]:")
            pYp.bin_file_updater(db,IK,ss)
        else:
            resto_men_up(IK)
    if x == 2:
        desc = input("Enter Description:")
        pYp.Standard_column_updater(db,con.dblis[db],"descr",IK,"IK",desc)
    if x == 3:
        if db == con.eve:
            q = tk.Tk()
            q.configure(width = 512,height = 512)
            check = PyP.Postriever(IK)
            if check == con.success:
                imag = ImageTk.PhotoImage(Image.open("./Pic/"+IK+".png"))
                ss = tk.Label(q,image = imag)
                ss.image = imag
                ss.pack()
                q.mainloop()
        elif db == con.anon:
            q = tk.Tk()
            q.configure(width =120,height = 120)
            imag = ImageTk.PhotoImage(Image.open("./Icon/"+IK+".png"))
            ss = tk.Label(q,image = imag)
            ss.image = imag
            ss.pack()
            q.mainloop()
        else:
            S = PyP.Restriever(IK)
            print("____________________MENU______________________")
            for i in S:
                print(i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+i[3]+"\n")          
    if x == 4:
        try:
            pYp.ship.fetchall()
        except:
            pass
        pYp.ship.execute("use {}".format(db,))
        pYp.ship.execute("select descr from {} where IK = '{}';".format(con.dblis[db],IK))
        q = pYp.fetchall()
        print(q[0])

def resto_men_crat():
    menu = {}
    while True:
        name = input("Food Name:")
        pric = int(input("price:"))
        cat = input("category(b,l,d,a):")
        
        menu[name] = [pric,cat]
        
        if input("continue(y/n)?") == "n":
            break
    return menu

def createOp():
    x = int(input(Createop))
    Title = input("Enter Title:")
    adr = input("Enter Adrress:")
    desc = input("Enter Description:")
    if x == 1:
        opclo = input("Enter Opening/closing time [format -> hhmm:hhmm]:")
        menu = resto_men_crat()
        pYp.resto_create(Title,menu,adr,opclo,desc)
    elif x == 2:
        cont = int(input("Enter contact number:"))
        picloc = input("Enter Poster File Location:")
        PyP.eve_Create(Title,adr,picloc,cont,desc)
        
    elif x == 3:
        cont = int(input("Enter contact number:"))
        picloc = input("Enter Icon File Location:")
        PyP.Anonym_Create(Title,picloc,adr,cont,desc)

while True:
    x = int(input(Mainop))
    if x == 1:
        Q = Lister(pYp.infodat[3],con.resto)
        s = int(input(Q))
        changeOp(pYp.infodat[3][s-1], con.resto)
        
    elif x == 2:
        Q = Lister(pYp.infodat[4],con.eve)
        s = int(input(Q))
        changeOp(pYp.infodat[4][s-1], con.eve)
        
    elif x == 3:
        Q = Lister(pYp.infodat[5],con.anon)
        s = int(input(Q))
        changeOp(pYp.infodat[5][s-1], con.anon)
        
    elif x == 4:
        createOp()
        




        