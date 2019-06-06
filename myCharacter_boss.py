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

class enemy(sprite):
    def __init__(self, filename, width, height, x=0, y=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        # self.surface = pygame.image.load(filename).convert_alpha()
        self.xspd = 5
        self.yspd = 10
        self.hp = 5
        self.hit_dist = 0 # hit dist is the distance flew after being hit
        self.rad_vision = 100 # the range of vision for enemy
        self.attack = False
        self.stun = False
        self.move_range = (self.x - 200, self.x + 200)
        self.bounce = False
        self.imagecounter = -1


    def setScale(self, width, height):
        if (width > self.width):
            self.x -= (width - self.width)
        else:
            self.x += (self.width - width)

        if (height > self.height):
            self.y -= (height - self.height)
        else:
            self.y += (self.height - height)

        self.pos = (self.x, self.y)
        self.width = width
        self.height = height
        self.surface = pygame.transform.scale(self.getSurface(), (width, height))

    def set_rangex(self, l, r):
        self.move_range = (l, r)

class boss(enemy):
    def __init__(self, width, height, x=0, y=0):
        enemy.__init__(self, width, height, x, y)
        self.jump = 0
        self.rad_vision = WIDTH
        self.attack_typ = 0
        self.start_attack = 0
        self.end_attack = 0
        self.dir = 1
        self.xspd = 20
        self.hp = 50
        self.move_range = (self.x, self.x + WIDTH - 100)
        self.surface.fill(self.color)
        self.rocks = []

    def move_x(self, dist):
        self.setPos(self.x + dist, self.y)
        self.move_range = (self.move_range[0] + dist, self.move_range[1] + dist)

    def move_y(self, dist):
        self.setPos(self.x, self.y + dist)

    def boss_attack(self, player):
        self.end_attack = pygame.time.get_ticks()

        for i in range(len(self.rocks)):
            self.rocks[i].rock_move(player)

        if (self.end_attack - self.start_attack >= 10000):
            if (self.attack_typ == 0):
                for i in range(10):
                    self.rocks.append(rock(50, 50, self))

            self.attack_typ = (self.attack_typ + 1) % 2
            self.start_attack = pygame.time.get_ticks()

        if (self.attack_typ == 0):
            # dash animation boss_attack
            self.x += self.dir * self.xspd

            if (self.x < self.move_range[0]):
                self.dir = 1
                self.x = self.move_range[0]

            if (self.x > self.move_range[1]):
                self.dir = -1
                self.x = self.move_range[1]

        if (self.attack_typ == 1):
            # angry
            print(self.rocks[0].y)

            self.x = self.x

        self.pos = (self.x, self.y)


    def boss_att_anim(self):
        self.imagecounter += 1
        if self.imagecounter >= 70:
            self.imagecounter = 0

        self.surface = pygame.image.load('media/boss_attack0' + str(int(self.imagecounter / 10)) + '.png').convert_alpha()

        if self.dir == 1 and self.hp > 0:
            self.imagecounter += 1
            if self.imagecounter >= 70:
                self.imagecounter = 0

        boss_default_pos = pygame.image.load('media/boss_attack0' + str(int(self.imagecounter / 10)) + '.png').convert_alpha()
        self.surface = pygame.transform.flip(boss_default_pos, True, False)

    def boss_die(self, flower):
        if (self.hp == 0):
            # die
            flower.setPos(self.x + 100, self.y + self.height - flower.height)

    def boss_angry_ani(self):
        self.imagecounter += 1
        if self.imagecounter >= 24:
            self.imagecounter = 0

        self.surface = pygame.image.load('media/boss_angry0' + str(int(self.imagecounter / 4)) + '.png').convert_alpha()

        if self.dir == 1 and self.hp > 0:
            self.imagecounter += 1
            if self.imagecounter >= 24:
                self.imagecounter = 0

        bossANGRY_default_pos = pygame.image.load('media/boss_angry0' + str(int(self.imagecounter / 4)) + '.png').convert_alpha()
        self.surface = pygame.transform.flip(bossANGRY_default_pos, True, False)

    def boss_die_ani(self):
        if self.hp <= 0:
            self.imagecounter += 1
            if self.imagecounter >= 60:
                self.imagecounter = 0
                self.surface = pygame.image.load('media/boss_die0' + str(int(self.imagecounter / 10)) + '.png').convert_alpha()

        if self.hp <= 0 and self.dir == 1:
            self.imagecounter += 1
            if self.imagecounter >= 60:
                self.imagecounter = 0

            bossdie_default_pos = pygame.image.load('media/boss_die0' + str(int(self.imagecounter / 10)) + '.png').convert_alpha()
            self.surface = pygame.transform.flip(bossdie_default_pos, True, False)

running = True

boss = boss(300, 200, 300, 300)



while running:
    for event in pygame.event.get(): # return all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked
            running = False

    pressedKeys = pygame.key.get_pressed()
    screen.fill(WHITE)

    screen.blit(boss.getSurface(), (200, 100))
    #boss.boss_att_anim()
    #boss.boss_angry_ani()
    boss.hp = -1
    boss.boss_die_ani()



    clock.tick(FPS)# pause the game until FPS time is reached
    pygame.display.flip()


pygame.quit()