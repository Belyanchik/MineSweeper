class Buttons:
    def __init__(self, x, y, content, plx, ply, flag = False, chk = False):
        self.x = x
        self.y = y
        self.content = content
        self.plx = plx
        self.ply = ply
        self.flag = flag
        self.chk = chk

    def setFlag(self): #будет использоваться для флагов, в данный момент, нигде не применяется
        if(self.flag == True):
            self.flag = False
        else:
            self.flag = True

    def setOpen(self): #меняет состояние закрытой клетки на открытую
        self.chk = True