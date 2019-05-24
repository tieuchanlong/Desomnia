from myParentclass import *
import pygame

class hp_bar(sprite): # the mid ground for climbing
    def __init__(self, width, height, x=0, y=0):  # add frames input
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def player_hit(self):
        # load hp bar broken animation
        return

class paint_bar(sprite):
    def __init__(self, width, height, x=0, y=0):  # add frames input
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.red = 255
        self.green = 255
        self.blue = 255
        self.color = (self.red, self.green, self.blue)
        self.surface.fill(self.color)


    def dec_bar(self, amount):
        if (self.height >= amount):
            print('Yes')
            self.height -= amount

        self.y = 80 - self.height
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim)
        self.surface.fill(self.color)

        self.pos = (self.x, self.y)