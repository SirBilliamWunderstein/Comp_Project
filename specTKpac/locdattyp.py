# grid -> letter letter
# pixel -> A to P

class location():
    global reg
    global grid
    global pix
    def __init__(self,region,grid,pixel):
        self.reg = region
        self.grid = grid
        self.pix = pixel

    def get(self):
        Q = self.reg + ":" + self.grid + ":" + self.pix
        return Q
    
    def GUI_get(self):
        Q = [self.reg,self.grid,self.pix]
        return Q

    # the below three be raplaced with proper graphics return types

    def region(self):
        return self.region
    
    def grid(self):
        return self.grid
    
    def pixel(self):
        return self.pixel