from common import *
from path import Path
from roteffect import Roteffect

class Ship():
    def __init__(self):
        self.pos = Vector(100, 100)
        self.color = [200, 200, 200]
        self.vel = Vector(0, 0)
        self.angle = 0

        self.path = Path()
        self.roteffect = Roteffect()

        self.points = [
            Vector(40, 0),
            Vector(0, -10),
            Vector(0, 10)
        ]

    def rotate(self, deg):
        self.points = [x.rotate(deg) for x in self.points]
        self.angle = (self.angle + deg)

    def thrust(self):
        self.vel += deg_to_vec(self.angle) / 1.4

    def back(self):
        self.vel -= deg_to_vec(self.angle) / 1.4

    def update(self, atlas):
        keys = pg.key.get_pressed()

        if keys[pg.K_f]:
            self.thrust()
        if keys[pg.K_s]:
            self.back()

        rot = 10 if abs(self.vel) == 0 else 60 * ( 1 / abs(self.vel))
        if rot > 10:
            rot = 10
        
        if keys[pg.K_r]:
            self.roteffect.add(self.angle, atlas.ticks, 'l')
            self.rotate(- rot)
        if keys[pg.K_t]:
            self.roteffect.add(self.angle, atlas.ticks, 'r')
            self.rotate(rot)

        self.vel -= self.vel / 30
        self.pos += self.vel
        if self.pos.x < 0:
            self.pos.x = 0
            self.vel.x = 0
        elif self.pos.x > atlas.dim.x:
            self.pos.x = atlas.dim.x
            self.vel.x = 0

        if self.pos.y < 0:
            self.pos.y = 0
            self.vel.y = 0
        elif self.pos.y > atlas.dim.x:
            self.pos.y = atlas.dim.y
            self.vel.y = 0

        direction = deg_to_vec(self.angle).normalized()
        self.path.add(self.pos.copy())
        self.path.update(atlas)

        self.roteffect.update(atlas)

    def draw(self, screen):
        self.path.draw(screen)
        relpos = screen.relpos(self.pos, Vector(20, 20))
        pointlist = [(relpos + x).as_point for x in self.points]
        pg.gfxdraw.polygon(screen.display, pointlist, self.color)
        pg.draw.polygon(screen.display, self.color, pointlist)

        direction = deg_to_vec(self.angle).normalized()

        circpos = (relpos).as_point

        pg.gfxdraw.filled_circle(screen.display, *circpos, 10, self.color)
        pg.gfxdraw.aacircle(screen.display, *circpos, 10, self.color)

        self.roteffect.draw(screen, self.pos)
