from common import *

class Atlas():
    def __init__(self):
        self.dim = Vector(2000, 2000)
        self.color = (180, 180, 180)
        self.ticks = 0

    def update(self, atlas):
        self.ticks += 1

    def draw(self, screen):

        hordim = Vector(screen.dim.x * 2 + self.dim.x, screen.dim.y)

        top = Vector(0 - screen.dim.x, 0 - screen.dim.y)
        reltop = screen.relpos(top, hordim)
        pg.draw.rect(screen.display, self.color, reltop.as_point + hordim.as_point)

        bot = Vector(0 - screen.dim.x, self.dim.y)
        relbot = screen.relpos(bot, hordim)
        pg.draw.rect(screen.display, self.color, relbot.as_point + hordim.as_point)

        verdim = Vector(screen.dim.x, self.dim.x)

        lef = Vector(-screen.dim.x, 0)
        rellef = screen.relpos(lef, verdim)
        pg.draw.rect(screen.display, self.color, rellef.as_point + verdim.as_point)

        rig = Vector(self.dim.x, 0)
        relrig = screen.relpos(rig, verdim)
        pg.draw.rect(screen.display, self.color, relrig.as_point + verdim.as_point)
