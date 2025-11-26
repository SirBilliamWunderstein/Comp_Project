import specTKpac as SBR
import specSQLpac as DIU
import tkinter as tk
from PIL import Image,ImageTk

global PyP

con = DIU.Constance()
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