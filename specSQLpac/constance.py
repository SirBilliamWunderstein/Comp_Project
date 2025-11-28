from PIL import Image

class Constance():
    global incorrect_userpass
    global lakmismatch
    global lak
    global anon
    global eve
    global resto
    global reqb
    global success
    global failed
    global tkplus
    global tkminus
    global grey
    global purp
    global bgrey
    global GrassL
    global waterL
    global buildL
    global rIc
    global eIc
    global RbudI
    global EbudI
    global Larrow
    global Rarrow
    global cartLO
    global mapdat
    

    def __init__(self):
        self.incorrect_userpass = "Avienfvi49gdniana1"
        self.lakmismatch = "uivhewndiki2nvuji4"
        self.lak = "LooselyAuthenticatedkeyDB"
        self.anon = "AnonymousDB"
        self.eve = "EventDB"
        self.resto = "RestaurantDB"
        self.reqb = "DeliverRequestDB"
        self.mapdat = "MapFileDatabase"
        self.success = "waids"
        self.failed = "sdiaw"
        self.grey = "#343434"
        self.purp = "#6a1aa6"
        self.bgrey = "#262626"
        self.grassL = {}
        self.waterL = {}
        self.buildL = {}

    def initimg(self):
        self.tkplus = Image.open("./GUI/Plus.png")
        self.tkminus = Image.open("./GUI/Minus.png")
        self.grassL[0] = Image.open("./GUI/grass.jpeg")
        self.grassL[1] = Image.open("./GUI/grass2.png")
        self.waterL[0] = Image.open("./GUI/Minus.png")
        self.waterL[1] = Image.open("./GUI/Minus.png")
        self.waterL[2] = Image.open("./GUI/Minus.png")
        self.waterL[3] = Image.open("./GUI/Minus.png")
        self.waterL[4] = Image.open("./GUI/Minus.png")
        self.waterL[5] = Image.open("./GUI/Minus.png")
        self.buildL = Image.open("./GUI/building.jpg")
        self.imageL = Image.open("./GUI/Minus.png")
        self.Larrow = Image.open("./GUI/Larrow.png")
        self.Rarrow = Image.open("./GUI/Rarrow.png")
        self.cartLO = Image.open("./GUI/CartLO.png")
        self.rIc = Image.open("./GUI/Minus.png")
        self.eIc = Image.open("./GUI/Minus.png")
        self.RbudI = Image.open("./GUI/Minus.png")
        self.EbudI = Image.open("./GUI/Minus.png")
        #self.ANONbudI = Image.open("./GUI/Minus.png")
        
        
        
        
