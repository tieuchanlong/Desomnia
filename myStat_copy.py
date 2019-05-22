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