import random
import pygame


WIDTH = 900
HEIGHT = 500

class sprite:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.dir = random.randrange(2)
        if (self.dir == 0):
            self.dir = -1
        self.dir1 = 1
        self.pos = (self.x, self.y)
        self.surface = pygame.Surface((0, 0), pygame.SRCALPHA, 32)
        self.red = 255
        self.green = 255
        self.blue = 255
        self.color = (self.red, self.green, self.blue)

    def getSurface(self):
        return self.surface

    def setPos(self, x, y):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)

    def getPos(self):
        return self.pos

    def setColor(self, color=(0, 0, 0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        self.color = (self.red, self.green, self.blue)
        self.surface.fill(self.color)

    def playerMove(self, pressedKey, spd):
        if (pressedKey[pygame.K_a]):
            self.x -= spd
        if (pressedKey[pygame.K_d]):
            self.x += spd

        if (self.x > WIDTH - self.width or self.x < 0):
            self.x = min(self.x, WIDTH - self.width)
            self.x = max(self.x, 0)

        self.pos = (self.x, self.y)

    def checkcollision(self, obj1, obj2):
        x = max(obj1.x, obj2.x)
        y = max(obj1.y, obj2.y)
        x1 = min(obj1.x + obj1.width, obj2.x + obj2.width)
        y1 = min(obj1.y + obj1.height, obj2.y + obj2.height)
        if (x <= x1 and y <= y1):
            return True
        else:
            return False

class interactive_object(sprite):
    def __init__(self, width, height, x=0, y=0):  # add frames input
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def interact(self):
        #Add some interaction
        self.setPos(-100, -100)