'''
    Title: Desomnia ( Tutorial Screen )
    Author: Long Tieu, Wayne Seto, Ethan
    Date:
'''

from myParentclass import *
import pygame
pygame.init() # load the pygame module commands in the program

# Display variables
TITLE = 'DESOMNIA' # Appear in the window title
FPS = 30 # Frames per second
WIDTH = 900
HEIGHT = 500
SCREENDIM = (WIDTH, HEIGHT)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

# Color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
kindred = (205,92,92)
kindblue = (132,112,255)
hostilered = (255, 0, 0)

class npc(sprite):
    def __init__(self, width, height, x=0, y=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.red = 0
        self.green = 255
        self.blue = 0
        self.color = (self.red, self.green, self.blue)
        #self.surface.fill(self.color)
        self.xspd = 5
        self.yspd = 10
        self.talk = False
        self.rad_vision = 20 # the range of vision for enemy
        self.imagecounter = -1

    def setScale(self, width, height):
        '''if (width > self.width):
            self.x -= (width - self.width)
        else:
            self.x += (self.width - width)

        if (height > self.height):
            self.y -= (height - self.height)
        else:
            self.y += (self.height - height)

        self.pos = (self.x, self.y)'''
        self.width = width
        self.height = height
        self.surface = pygame.transform.scale(self.getSurface(), (width, height))

    def npc_talk(self, pressedKey, player):
        if (abs(player.x - self.x) <= 150):
            if (pressedKey[pygame.K_e]):
                self.talk = True

    def npc_idle(self):
        print(self.imagecounter)
        self.imagecounter += 1
        if self.imagecounter >= 30:
            self.imagecounter = 0

        self.surface = pygame.image.load('media/npc_idle_0' + str(int(self.imagecounter/10)) + '.png').convert_alpha()


running = True

npc00 = npc(200, 200, 300, 300)
npc00.setScale(200, 200)

while running:
    for event in pygame.event.get(): # return all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked
            running = False

    pressedKeys = pygame.key.get_pressed()
    screen.fill(WHITE)

    npc00.npc_idle()
    #npc00.setColor(BLACK)
    screen.blit(npc00.getSurface(), (200, 100))


    clock.tick(FPS)# pause the game until FPS time is reached
    pygame.display.flip()


pygame.quit()