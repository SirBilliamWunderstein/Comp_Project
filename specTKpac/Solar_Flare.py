import tkinter as tk
from Button_master import Buddon, Keys

class Menu:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="#444")
        self.frame.pack(fill="both", expand=True)
        self.label = tk.Label(self.frame, text="Menu", fg="white", bg="#444", font=("Arial", 16, "bold"))
        self.label.pack(padx=10, pady=10)

class InfoBox:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="#222")
        self.frame.pack(fill="both", expand=True)
        self.label = tk.Label(self.frame, text="Hover or click a button on the map.", fg="white", bg="#222", font=("Arial", 12))
        self.label.pack(padx=10, pady=10)
    def update_info(self, text):
        self.label.config(text=text)

class Map:
    def __init__(self, parent, image_path, info_callback):
        self.buddon = Buddon(parent, image_path)
        self.keys = Keys(parent, self.buddon.canvas)
        for i, btn in enumerate(self.buddon.buttons):
            btn.bind("<Enter>", lambda e, idx=i: info_callback(f"Button number: {idx + 1}, event: {idx + 71}"))
            btn.bind("<Button-1>", lambda e, idx=i: info_callback(f"Button number: {idx + 1}, event: {idx + 71}"))

class Main_Stuff_Root:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Buddon is like so gay")
        self.root.geometry("1200x700")
        self.root.configure(bg="#111")

        self.left_frame = tk.Frame(self.root, bg="#333")
        self.left_frame.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        self.menu_height = 0.6
        self.info_height = 0.4

        self.menu_frame = tk.Frame(self.left_frame, bg="#444")
        self.info_frame = tk.Frame(self.left_frame, bg="#222")

        self.menu_frame.place(relx=0, rely=0, relwidth=1, relheight=self.menu_height)
        self.info_frame.place(relx=0, rely=self.menu_height, relwidth=1, relheight=self.info_height)

        self.menu = Menu(self.menu_frame)
        self.info = InfoBox(self.info_frame)

        self.map_frame = tk.Frame(self.root, bg="black")
        self.map_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

        self.map = Map(self.map_frame, image_path, self.info.update_info)

        #self.root.bind("i", self.increase_info)
        #self.root.bind("I", self.increase_info)
        #self.root.bind("m", self.increase_menu)
        #self.root.bind("M", self.increase_menu)

    def update_layout(self):
        self.menu_frame.place(relx=0, rely=0, relwidth=1, relheight=self.menu_height)
        self.info_frame.place(relx=0, rely=self.menu_height, relwidth=1, relheight=self.info_height)

    def increase_info(self, event=None):
        if self.info_height < 0.9:
            self.info_height += 0.05
            self.menu_height = 1 - self.info_height
            self.update_layout()

    def increase_menu(self, event=None):
        if self.menu_height < 0.9:
            self.menu_height += 0.05
            self.info_height = 1 - self.menu_height
            self.update_layout()

if __name__ == "__main__":
    image_path = "../tesmap.png"
    root = tk.Tk()
    app = Main_Stuff_Root(root, image_path)
    root.mainloop()
