from common import *

class Compound():
    def __init__(self, angle):
        self.start = int(angle)
        self.end = self.start
        self.countr = 0
        self.color = (150, 150, 150)

        self.arcs = [] # rad, start, end
        self.f = lambda x, y: (x, y)

        self.killed = False

    def extend(self, angle):
        self.end = int(angle)
        self.countr += 1
        if self.countr == 1:
            if self.end > self.start:
                self.f = lambda x, y: (x, y)
            else:
                self.f = lambda x, y: (y, x)

    def update(self, atlas):
        if randint(0, int(abs(self.start - self.end) / 100)) == 0:
            num = randint(*self.f(self.start, self.end))
            self.arcs.append([randint(10, 40), num])


        if randint(0, 5) == 0:
            for i in self.arcs:
                if len(i) == 2:
                    i.append(randint(*self.f(i[1], self.end)))
        

    def draw(self, screen, pos):

        relpos = screen.relpos(pos, Vector(0, 0))


        #pg.gfxdraw.line(screen.display, *pos1.as_point, *pos2.as_point, [255, 255, 255])

        if not self.killed:
            for arc in self.arcs:
                rad = arc[0]
                a = arc[1]
                if len(arc) == 3:
                    b = arc[2]
                else:
                    b = self.end
                
                
                pg.gfxdraw.arc(screen.display, *relpos.as_point, rad, *self.f(a, b), self.color)
                
    def kill(self, ticks):
        self.killed = True
            

        
        
        

class Roteffect():
    def __init__(self):
        self.points = []
        self.last_tick = 0
        self.last_dir = 0
        self.compounds = []


    def add(self, angle, ticks, direction):
        if direction != self.last_dir or ticks != self.last_tick + 1:
            self.compounds.append(Compound(angle))
        else:
            self.compounds[-1].extend(angle)
        self.last_tick = ticks
        self.last_dir = direction
        

    def update(self, atlas):
        if atlas.ticks != self.last_tick:
            if self.compounds:
                self.compounds[-1].kill(atlas)
            
        

        for compound in self.compounds:
            compound.update(atlas)


    def draw(self, screen, pos):
        for compound in self.compounds:
            #compound.draw(screen, pos)
            pass
