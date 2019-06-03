'''
    Title: Desomnia ( Tutorial Screen )
    Author: Long Tieu, Wayne Seto, Ethan
    Date:
'''

from myParentclass import *
import pygame

pygame.init()  # load the pygame module commands in the program

# Display variables
TITLE = 'DESOMNIA'  # Appear in the window title
FPS = 30  # Frames per second
WIDTH = 900
HEIGHT = 500
SCREENDIM = (WIDTH, HEIGHT)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

# Color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
kindred = (205, 92, 92)
kindblue = (132, 112, 255)
hostilered = (255, 0, 0)


class enemy(sprite):
    def __init__(self, filename, width, height, x=0, y=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface = pygame.image.load(filename).convert_alpha()
        self.xspd = 5
        self.yspd = 10
        self.hp = 5
        self.hit_dist = 0  # hit dist is the distance flew after being hit
        self.rad_vision = 100  # the range of vision for enemy
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

    def enemy_move(self, grounds):  # try to detect player
        if (self.stun == False and self.bounce == False):
            self.x += self.xspd / 2 * self.dir

            if (self.x < self.move_range[0]):
                if (self.attack == False):
                    self.dir = 1
                else:
                    self.dir = 0

            if (self.x > self.move_range[1] and self.attack == False):
                if (self.attack == False):
                    self.dir = -1
                else:
                    self.dir = 0

            cnt = 0
            for i in range(len(grounds)):
                if self.checkcollision(self, grounds[i]) == False:
                    cnt += 1

            if (cnt == len(grounds)):
                self.dir = -self.dir
        else:
            self.hit_dist += self.xspd
            if (self.hit_dist < 100):
                self.x -= self.dir * self.xspd
            elif (self.hit_dist >= 100):
                self.bounce = False

                if (self.stun == False):
                    self.hit_dist = 0
                else:
                    if (self.hit_dist > 600):
                        self.stun = False
                        self.hit_dist = 0

        self.pos = (self.x, self.y)

    def enemy_follow(self, player, grounds):
        if (abs(self.x - player.x) <= self.rad_vision and abs(self.y - player.y) <= self.rad_vision and self.move_range[
            0] <= self.x <= self.move_range[1]):  # can change default range
            self.attack = True
        else:
            self.attack = False

        if (self.bounce == True):
            self.attack = False

        if (self.attack == True):
            self.enemy_attack(player, grounds)
            if (self.x < player.x):
                # load turn back animation
                if (self.x >= self.move_range[0]):
                    self.dir = 1
                else:
                    self.dir = 0
            else:
                if (self.x <= self.move_range[1]):
                    self.dir = -1
                else:
                    self.dir = 0

            self.x += self.xspd / 2 * self.dir
            # self.move_range = (self.move_range[0] + self.xspd*self.dir, self.move_range[1] + self.xspd*self.dir)
            self.pos = (self.x, self.y)

            self.enemy_attack(player, grounds)

    def enemy_attack(self, player, grounds):
        # do some attack movements

        if (self.checkcollision(self, player)):
            player.jump = -15

            if (player.jump == -15 and player.bounce == False):
                player.dec_hp()

            player.bounce = True

            if (player.x > self.x):
                player.dir = 1
            else:
                player.dir = -1

    def enemy_idle(self):
        self.imagecounter += 1
        if self.imagecounter >= 20:
            self.imagecounter = 0

        self.surface = pygame.image.load(
            'media/enemy_idle_0' + str(int(self.imagecounter / 10)) + '.png').convert_alpha()

    def enemy_att(self):
        self.imagecounter += 1
        if self.imagecounter >= 30:
            self.imagecounter = 0

        self.surface = pygame.image.load(
            'media/enemy_att_0' + str(int(self.imagecounter / 10)) + '.png').convert_alpha()

    def enemy_die(self):
        self.imagecounter += 1
        if self.imagecounter >= 40:
            self.imagecounter = 0

        self.surface = pygame.image.load(
            'media/enemy_die_0' + str(int(self.imagecounter / 10)) + '.png').convert_alpha()


running = True

enemy1 = enemy(200, 200, 300, 300)
enemy2 = enemy(200, 200, 400, 100)
enemy1.setScale(200, 200)

while running:
    for event in pygame.event.get():  # return all inputs and triggers into an array
        if event.type == pygame.QUIT:  # If the red X was clicked
            running = False

    pressedKeys = pygame.key.get_pressed()
    screen.fill(WHITE)

    # enemy1.setColor(BLACK)

    print(enemy1.hp)

    enemy2.enemy_idle()

    if pressedKeys[pygame.K_e]:  # test the dying animation
        enemy1.hp -= 1

    if enemy1.hp <= 0:
        enemy1.enemy_die()
        screen.blit(enemy1.getSurface(), (200, 100))

    else:
        enemy1.enemy_att()
        screen.blit(enemy1.getSurface(), (200, 100))

    screen.blit(enemy2.getSurface(), (400, 100))

    clock.tick(FPS)  # pause the game until FPS time is reached
    pygame.display.flip()

pygame.quit()