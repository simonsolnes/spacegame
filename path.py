from common import *

class PathFragment():
    def __init__(self, pos):
        self.pos = pos
        self.color = [150, 150, 150]
        self.age = pg.time.get_ticks()
        self.radius = 10

    def update(self, atlas):
        deltatime = pg.time.get_ticks() - self.age
        deltatime = deltatime if deltatime else 1

        col = self.color[0] - log(deltatime, 1.4)
        if col < 30:
            col = 30
        self.color = [col, col, col]

        self.radius = self.radius - (deltatime / 80)
        if self.radius < 1:
            self.radius = 1

    def draw(self, screen):
        relpos = screen.relpos(self.pos, Vector(10, 10))
        pg.gfxdraw.filled_circle(screen.display, *relpos.as_point, int(self.radius), self.color)
        pg.gfxdraw.aacircle(screen.display, *relpos.as_point, int(self.radius), self.color)


class Path():
    def __init__(self):
        self.fragments = []

    def add(self, pos):
        self.fragments.append(PathFragment(pos))

    def update(self, atlas):
        while len(self.fragments) > 8:
            self.fragments.pop(0)
        for fragment in self.fragments:
            fragment.update(atlas)


    def draw(self,screen):
        for i, fragment in enumerate(self.fragments):
            fragment.draw(screen)
        
