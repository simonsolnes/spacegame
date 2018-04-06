from common import *

class Fragment():
    def __init__(self, pos):
        self.pos = pos

        x = uniform(-0.2, 0.2)
        y = uniform(-0.2, 0.2)
        self.vel = Vector(x, y)

        self.color = [x + 40 for x in [60, 60, 60]]

    def update(self, atlas):
        self.pos += self.vel

    def draw(self, screen):
        try:
            relpos = screen.relpos(Vector(self.pos.x + 20, self.pos.y +20), Vector(0, 0))
        except OutOfBounds:
            pass
        else:
            pg.gfxdraw.aacircle(screen.display, *relpos.as_point, 5, self.color)

class Fragments():
    def __init__(self, minval, maxval, num):
        self.fragments = []
        for i in range(num):
            x = uniform(minval.x, maxval.x)
            y = uniform(minval.y, maxval.y)
            self.fragments.append(Fragment(Vector(x, y)))

    def update(self, atlas):
        for fragment in self.fragments:
            fragment.update(atlas)

    def draw(self, screen):
        for fragment in self.fragments:
            fragment.draw(screen)
