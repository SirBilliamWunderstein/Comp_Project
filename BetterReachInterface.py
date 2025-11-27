import specTKpac as SBR
import specSQLpac as DIU
import tkinter as tk
from PIL import Image,ImageTk
import mysql.connector as dcp

global PyP

def Login():
    Q = SBR.Mes("Please enter your username:")
    x = Q.start()

    R = SBR.Mes("Please Enter your password:")
    y = R.start()
    
    port = dcp.connect(user = "root",host = "localhost",password = "mysql",auth_plugin='mysql_native_password')
    ship = port.cursor()
    ship.execute("CREATE USER '{}'@'localhost' IDENTIFIED WITH mysql_native_password BY '{}';".format(x,y))
    port.commit()
    port.close()
    #CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';
    
    PyP = DIU.PyperedPype(x,y)

con = DIU.Constance()

try:
    binfil = open("./bindump/ret.dat","rb")
    Q = pickle.load(binfil)
    PyP = DIU.PyperedPype(Q[0],Q[1])
    binfil.close()
except:
    Login()
#PyP = DIU.PyperedPype("","")
PyP= 0

tree = tk.Tk()
tree.title("BetterReach")
tree.configure(width = 900,height = 600)

infbx = SBR.infbox(tree,PyP)

mapImag = "./imsorrylilone.png"

button_do = SBR.Buddon(tree, mapImag,PyP,infbx)
key_app = SBR.Keys(tree, button_do.canvas)



tree.mainloop()