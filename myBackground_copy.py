'''
    Title: Desomnia ( Start Screen )
    Author: Long Tieu, Wayne Seto, Ethan
    Date:
'''

import pygame
from myParentclass import *
pygame.init() # load the pygame module commands in the program

# Display variables
TITLE = 'DESOMNIA' # Appear in the window title
FPS = 30 # Frames per second
WIDTH = 900
HEIGHT = 500
SCREENDIM = (WIDTH, HEIGHT)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
kindred = (205,92,92)
kindblue = (132,112,255)
hostilered = (255, 0, 0)

###

# Create the window
screen = pygame.display.set_mode(SCREENDIM) # Create the main surface where all other assets are placed on top
pygame.display.set_caption(TITLE) # This updates the windows title
screen.fill(BLACK) # Fill the entire surface with the chosen color. Think of fill as erase.

clock = pygame.time.Clock()  # starts a clock object to measure time

class scene_block(sprite):
    def __init__(self, width, height, x=0, y=0):  # add frames input
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.dir = 1
        self.xspd = 30
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.red = 0
        self.green = 0
        self.blue = 0
        self.color = (self.red, self.green, self.blue)
        self.surface.fill(self.color)


    def move(self):
        self.x += self.xspd*self.dir
        self.pos = (self.x, self.y)

        '''if (self.x > WIDTH - self.width):
            del self'''

class image(sprite):
    def __init__(self, fileName, x=0, y=0, width=0, height=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.surface = pygame.image.load(fileName).convert_alpha()


class ground(sprite): # the mid ground for climbing
    def __init__(self, width, height, x=0, y=0):  # add frames input
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.setColor((0, 0, 0))
        self.surface = pygame.image.load('media/grassground.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (width, height))
        self.groundimage = []

        '''i = self.x
        while (i < self.x + self.width):
            self.images.append(image('media/grassground.png', i, self.y, 20, 10))
            if (self.x - self.width - i < 20):
                self.images.append(image('media/grassground.png', self.x - self.width - 10, self.y, 20, 10))'''

class bush(sprite):
    def __init__(self, width, height, x=0, y=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(2)
        bush1 = pygame.image.load('media/bush00.png').convert_alpha()
        bush2 = pygame.image.load('media/bush01.png').convert_alpha()
        self.bush = []
        self.bush.append(bush1)
        self.bush.append(bush2)

    def randpickbush(self):
        randpick = random.randrange(self.bush)
        print(randpick)

    def flipbush(self, arrpos):
        bush_default_pos = self.bush[arrpos]
        self.surface = pygame.transform.flip(bush_default_pos, True, False)

class rocks(sprite):
    def __init__(self, width, height, x=0, y=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(2)
        rock1 = pygame.image.load('media/mush01.png').convert_alpha()
        rock2 = pygame.image.load('media/rock00.png').convert_alpha()
        self.rocks = []
        self.rocks.append(rock1)
        self.rocks.append(rock2)

    def fliprocks(self, arrpos):
        rocks_default_pos = self.rocks[arrpos]
        self.surface = pygame.transform.flip(rocks_default_pos, True, False)


class mushroom(sprite):
    def __init__(self, width, height, x=0, y=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(2)
        self.surface = pygame.image.load('media/mush00.png').convert_alpha()

    def flipmush(self):
        mush_default_pos = self.surface
        self.surface = pygame.transform.flip(mush_default_pos, True, False)


class bat(sprite):
    def __init__(self, width, height, x=0, y=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(2)
        bat1 = pygame.image.load('media/bat00.png').convert_alpha()
        bat2 = pygame.image.load('media/bat01.png').convert_alpha()
        self.bats = []
        self.bats.append(bat1)
        self.bats.append(bat2)

    def flipbats(self, arrpos):
        bats_default_pos = self.bats[arrpos]
        self.surface = pygame.transform.flip(bats_default_pos, True, False)

class woodlog(sprite):
    def __init__(self, width, height, x=0, y=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.surface = pygame.image.load('media/woodlog.png').convert_alpha()

running = True

bush = bush(200, 200, 300, 300)

while running:
    for event in pygame.event.get(): # return all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked
            running = False

    endtime = pygame.time.get_ticks()

    pressedKeys = pygame.key.get_pressed()
    screen.fill(WHITE)

    screen.blit(bush.getSurface(), (bush.x, 200))
    bush.randpickbush()



    clock.tick(FPS) # pause the game until FPS time is reached
    pygame.display.flip()


pygame.quit()