import specTKpac as SBR
import specSQLpac as DIU
import tkinter as tk
import pickle
from PIL import Image,ImageTk
import mysql.connector as dcp

global PyP
global button_do
global key_app

def Login():
    Q = SBR.Mes("Please enter your username:")
    x = Q.start()
    global PyP

    R = SBR.Mes("Please Enter your password:")
    y = R.start()
    
    binfil = open("./bindump/ret.dat","wb")
    pickle.dump([x,y],binfil)
    binfil.close()
    
    port = dcp.connect(user = "root",host = "localhost",password = "mysql",auth_plugin='mysql_native_password')
    ship = port.cursor()
    try:
        ship.execute("CREATE USER '{}'@'localhost' IDENTIFIED WITH mysql_native_password BY '{}';".format(x,y))
    except:
        PyP = DIU.PyperedPype(x,y)
        return 0
    LL = [con.resto,con.eve,con.reqb,con.anon]
    for i in LL:
        ship.execute("use {}".format(i,))
        ship.execute("GRANT ALL ON {}.* TO '{}'@'localhost';".format(i,x))
        ship.execute("flush privileges;")
        port.commit()
    port.commit()
    port.close()
    #CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';
    PyP = DIU.PyperedPype(x,y)

global con
con = DIU.Constance()

try:
    binfil = open("./bindump/ret.dat","rb")
    Q = pickle.load(binfil)
    PyP = DIU.PyperedPype(Q[0],Q[1])
    binfil.close()
except FileNotFoundError:
    Login()

#PyP= 0

tree = tk.Tk()
tree.title("BetterReach")
tree.configure(width = 900,height = 600)
tree.resizable(False, False)

infbx = SBR.infbox(tree,PyP)

mapImag = "./GUI/THEMAP.png"

button_do = SBR.Buddon(tree, mapImag,PyP,infbx)
key_app = SBR.Keys(tree, button_do.canvas)

MenuBox = SBR.MenuBox(tree,key_app,button_do,PyP,infbx)

tree.mainloop()
