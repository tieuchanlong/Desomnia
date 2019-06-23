import random
import pygame


WIDTH = 900
HEIGHT = 500

class sprite:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.dim = (0, 0)
        self.dir = random.randrange(2)
        self.dir = 1
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
        self.collect = False
        self.check = False
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface = pygame.image.load('media/coin00.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (20, 20))
        self.coin_check = True
        self.note_appear = False
        self.imagecounter = 0
        self.note = image('media/collect.png', self.x - 20, self.y - 50, 80, 50)

    def interact(self, pressedKey, player):
        #Add some interaction
        if (abs(player.x - self.x) <= 100):
            self.note_appear = True
            #screen.blit(self.note.surface, self.note.getPos())
            if (pressedKey[pygame.K_e]):
                if (pygame.mixer.Channel(6).get_busy() == False):
                    pygame.mixer.Channel(6).play(pygame.mixer.Sound('media/collect.wav'), 0)
                    pygame.mixer.Channel(6).set_volume(0.05)

                self.setPos(-10000, -10000)
                self.collect = True
        else:
            self.note_appear = False

    def move_x(self, dist):
        self.setPos(self.x + dist, self.y)
        self.note.setPos(self.note.x + dist, self.note.y)

    def move_y(self, dist):
        self.setPos(self.x, self.y + dist)
        self.note.setPos(self.note.x, self.note.y + dist)

    def coin_anim(self):
        self.imagecounter += 1

        if self.imagecounter >= 12:
            self.imagecounter = 0

        self.surface = pygame.image.load('media/coin0' + str(int(self.imagecounter / 3)) + '.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (20, 20))

class image(sprite):
    def __init__(self, fileName, x=0, y=0, width=0, height=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.appear = False
        self.dim = (self.width, self.height)
        self.surface = pygame.image.load(fileName).convert_alpha()

