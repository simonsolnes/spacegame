from common import *

class Screen():
    def __init__(self, ship, clock):
        self.dim = Vector(900, 700)
        self.display = pg.display.set_mode(self.dim.as_point)
        self.ship = ship
        self.pos = Vector(self.ship.pos.x - self.dim.x / 2, self.ship.pos.y - self.dim.y / 2)
        self.clock = clock
    @property
    def center(self):
        return self.dim / 2

    def update(self, atlas):
        self.pos += (Vector(self.ship.pos.x - self.dim.x / 2, self.ship.pos.y - self.dim.y / 2) - self.pos) / 8

    def draw(self, screen):
        pg.display.set_caption('Space - ' + str(int(self.clock.get_fps())))
        self.display.fill((30, 30, 30))

    def relpos(self, pos, dim):
        relpos = Vector(int(pos.x - self.pos.x), int(pos.y - self.pos.y))
    
#https://stackoverflow.com/questions/25068538/intersection-and-difference-of-two-rectangles/25068722#25068722
        
        points = [
            Vector(relpos.x,            relpos.y),
            Vector(relpos.x + dim.x,    relpos.y),
            Vector(relpos.x,            relpos.y + dim.y),
            Vector(relpos.x + dim.x,    relpos.y + dim.y)
        ]

        w = self.dim.x
        h = self.dim.y

        #if any([p.x > 0 and p.x < w and p.y > 0 and p.y < h for p in points]):
        return relpos
        #else:
            #raise OutOfBounds
