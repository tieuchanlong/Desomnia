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
        self.surface = pygame.image.load('media/hp_full.png').convert_alpha()


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
        self.amount = 50
        self.surface = pygame.image.load('media/paintbar_05.png').convert_alpha()

    def dec_bar(self, amount):
        print('Player ' + str(self.amount))
        if (self.amount > 0 and self.amount < 50):
            self.amount -= amount

        if (self.amount == 50 and amount > 0):
            self.amount -= amount

        if (self.amount == 0 and amount > 0):
            self.amount -= amount


    def check_amount(self):
        if (self.amount == 0):
            self.surface = pygame.image.load('media/paintbar_00.png').convert_alpha()

        if (self.amount == 10):
            self.surface = pygame.image.load('media/paintbar_01.png').convert_alpha()

        if (self.amount == 20):
            self.surface = pygame.image.load('media/paintbar_02.png').convert_alpha()

        if (self.amount == 30):
            self.surface = pygame.image.load('media/paintbar_03.png').convert_alpha()

        if (self.amount == 40):
            self.surface = pygame.image.load('media/paintbar_04.png').convert_alpha()

        if (self.amount == 50):
            self.surface = pygame.image.load('media/paintbar_05.png').convert_alpha()
