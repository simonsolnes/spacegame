#!/usr/bin/env python3
from common import *

from ship import Ship
from fragment import Fragments
from atlas import Atlas
from screen import Screen

class Game():
    def __init__(self):
        pg.init()
        self.fps = 60
        self.clock = pg.time.Clock()
        self.ship = Ship()
        self.screen = Screen(self.ship, self.clock)
        self.atlas = Atlas()
        self.fragments = Fragments(Vector(0, 0), self.atlas.dim, int(abs(self.atlas.dim) / 10))

        self.all = [self.screen, self.fragments, self.ship, self.atlas]

    def update(self):
        for item in self.all:
            item.update(self.atlas)

    def draw(self):
        for item in self.all:
            item.draw(self.screen)

    def evenhandler(self):
        keys = pg.key.get_pressed()

        userquit = any([x.type == pg.QUIT for x in pg.event.get()])
        if keys[pg.K_q] or keys[pg.K_ESCAPE] or userquit:
            exit()
        
    def run(self):
        while True:
            self.evenhandler()
            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(self.fps)

if __name__ == '__main__':
    game = Game()
    game.run()
