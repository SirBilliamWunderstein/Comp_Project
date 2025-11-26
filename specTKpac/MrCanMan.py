import tkinter as tk
from PIL import Image, ImageTk
from copy import deepcopy

class Buddon:
    global BDit
    global root
    global imag
    
    def __init__(self, root, imag):
        self.root = root
        self.imag = imag
        self.buddon_maker()

    def buddon_maker(self):
        img = Image.open(self.imag)
        button_size = 64
        buttons_per_row = img.width // button_size
        buttons_per_col = img.height // button_size
        tiles = []
        
        for i in range(buttons_per_col):
            for j in range(buttons_per_row):
                box = (j * button_size, i * button_size, (j + 1) * button_size, (i + 1) * button_size)
                tile = img.crop(box)
                tiles.append(ImageTk.PhotoImage(tile))

        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black", scrollregion=(0, 0, 3200, 1800))
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        frame = tk.Frame(self.canvas, width=3200, height=3200, bg="black")
        self.canvas.create_window((0, 0), window=frame, anchor="nw")

        self.hbar = tk.Scrollbar(frame, orient="horizontal", command=self.canvas.xview)
        self.vbar = tk.Scrollbar(frame, orient="vertical", command=self.canvas.yview)
        self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.hbar.place(relx=0, rely=1.0, anchor="sw", relwidth=1)
        self.vbar.place(relx=1.0, rely=0, anchor="ne", relheight=1)

        index = 0
        self.BDit = {}
        for i in range(buttons_per_col):
            for j in range(buttons_per_row):
                btn = tk.Button(frame, image=tiles[index], borderwidth=2,command =  lambda : print(deepcopy(i)), highlightthickness=0)
                self.BDit[str(i+1)+";"+ str(j+1)] = btn
                btn.image = tiles[index]
                btn.place(x=j * button_size, y=i * button_size, width=button_size, height=button_size)
                index += 1
        #print(self.BDit)


class Keys:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        #self.root.title("Sagar")

        canvas.focus_set()
        canvas.bind("<Left>", lambda event: canvas.xview_scroll(-1, "units"))
        canvas.bind("<Right>", lambda event: canvas.xview_scroll(1, "units"))
        canvas.bind("<Up>", lambda event: canvas.yview_scroll(-1, "units"))
        canvas.bind("<Down>", lambda event: canvas.yview_scroll(1, "units"))

"""class Left_Right_And_Centre:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.root.title("Sagar is like so gay")

        self.button_frame = tk.Frame(self.root, bg="#dddddd", bd=1, relief="raised")
        self.button_frame.place(relx=0.02, rely=0.9, anchor="sw")

        tk.Button(self.button_frame, text="↑", command=self.UP,
                  width=4, fg="blue", activebackground="blue",
                  activeforeground="white").grid(row=0, column=1)

        tk.Button(self.button_frame, text="←", command=self.Left,
                  width=4, fg="green", activebackground="green",
                  activeforeground="white").grid(row=1, column=0)

        tk.Button(self.button_frame, text="→", command=self.Right,
                  width=4, fg="red", activebackground="red",
                  activeforeground="white").grid(row=1, column=2)

        tk.Button(self.button_frame, text="↓", command=self.Down,
                  width=4, fg="orange", activebackground="orange",
                  activeforeground="white").grid(row=2, column=1)

        self.root.bind("<Configure>", self.follow_user)

    def follow_user(self, event):
        self.button_frame.lift()

    def Left(self):
        self.canvas.xview_scroll(-1, "units")

    def Right(self):
        self.canvas.xview_scroll(1, "units")

    def UP(self):
        self.canvas.yview_scroll(-1, "units")

    def Down(self):
        self.canvas.yview_scroll(1, "units")"""

imag = "../tesmap.png"


root = tk.Tk()
root.title("Sagar")
root.geometry("1200x700")

buddon_app = Buddon(root, imag)
key_app = Keys(root, buddon_app.canvas)
#control_app = Left_Right_And_Centre(root, buddon_app.canvas)

root.mainloop()

