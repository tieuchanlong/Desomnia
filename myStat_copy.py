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
        self.surface = pygame.image.load('media/hp_full.png').convert_alpha()


#############
# dec_hp section

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


class player(sprite):
    def __init__(self, width, height, x=0, y=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)
        self.xspd = 10
        self.yspd = 10
        self.jump = 0
        self.dir = 1
        self.fall = False
        self.swim = False
        self.climb = False
        self.attack = False
        self.attack_typ = -1
        self.start_attack = 0
        self.end_attack = 0
        self.skill_active = False
        self.normal_active = False
        self.hp = 5
        self.hp_bars = []
        self.bounce = False
        self.bounce_count = 0

    def playerMove(self, pressedKey, spd):
        if (self.bounce == False):
            if (pressedKey[pygame.K_a]):
                self.x -= spd
                self.dir = -1
            if (pressedKey[pygame.K_d]):
                self.x += spd
                self.dir = 1
        else:
            self.x += 20*self.dir
            self.bounce_count += 20

        if (self.jump + self.yspd >= 0 and self.bounce_count > 200):
            self.bounce = False
            self.bounce_count = 0

        self.pos = (self.x, self.y)

    def player_fall(self, spd, grounds, moving_grounds):
        self.fall = True
        for i in range(len(grounds)):
            if self.checkcollision(self, grounds[i]) and self.y + self.height >= grounds[i].y and self.y < grounds[i].y:
                self.fall = False
                self.y = grounds[i].y - self.height
                self.pos = (self.x, self.y)
                break

        for i in range(len(moving_grounds)):
            if self.checkcollision(self, moving_grounds[i]) and self.y + self.height >= moving_grounds[i].y and self.y < moving_grounds[i].y:
                self.fall = False
                self.y = moving_grounds[i].y - self.height
                self.pos = (self.x, self.y)
                break

        if (self.fall == True and self.swim == False):
            self.y += spd + self.jump
            #self.jump += 0.5
            self.pos = (self.x, self.y)

    def player_jump(self, pressedKey, grounds, moving_grounds):
        if (self.jump == 0 and self.fall == False and self.swim == False and self.bounce == False and pressedKey[pygame.K_SPACE]):
            self.jump = -24
            return True

        if (self.jump + self.yspd >= 0):
            self.jump = 0
            return False


        self.y = self.jump + self.yspd + self.y
        self.pos = (self.x, self.y)
        self.jump += 0.5

        return True

    def player_swim(self, pressedKey, waters):
        if (self.bounce == False):
            self.swim = False
            for i in range(len(waters)):
                if (self.checkcollision(self, waters[i]) and self.y >= waters[i].y):
                    self.swim = True
                    self.fall = False
                    break

            if (self.swim == True):
                if (pressedKey[pygame.K_w]):
                    self.y -= self.yspd
                if (pressedKey[pygame.K_s]):
                    self.y += self.yspd
                if (pressedKey[pygame.K_a]):
                    self.x -= self.xspd
                    self.dir = -1
                if (pressedKey[pygame.K_d]):
                    self.x += self.xspd
                    self.dir = 1

                if self.x > waters[i].x + waters[i].width - self.width or self.x < 0:
                    self.x = min(self.x, waters[i].x + waters[i].width - self.width)
                    self.x = max(self.x, 0)

                if self.y > waters[i].y + waters[i].height - self.height - 20 or self.y < 0:
                    self.y = min(self.y, waters[i].y + waters[i].height - self.height - 20)
                    self.y = max(self.y, 0)

                if (pressedKey[pygame.K_SPACE]):
                    self.jump = -30
                    self.swim = False
        else:
            self.x += 20 * self.dir
            self.bounce_count += 20

        if (self.jump + self.yspd >= 0 and self.bounce_count > 100):
            self.bounce = False
            self.bounce_count = 0

        self.pos = (self.x, self.y)

    def player_climb(self, pressedKey, stairs):
        for i in range(len(stairs)):
            if (self.checkcollision(self, stairs[i])):
                # show the text indeicates climbing

                if (pressedKey[pygame.K_e]):
                    self.x = stairs[i].x + stairs[i].width/2 - self.width/2
                    self.pos = (self.x, self.y)
                    self.climb = True
                    # Load climb animation
                    break

        if (self.climb == True):
            if (pressedKey[pygame.K_e] and self.y + self.height > stairs[i].y + stairs[i].height):
                # load normal animation
                self.fall = True
                self.climb = False
                return

            if (pressedKey[pygame.K_w]):
                self.y -= self.yspd/2

            if (pressedKey[pygame.K_s]):
                self.y += self.yspd/2


            '''if self.y > stairs[i].y + stairs[i].height - self.height or self.y < stairs[i].y:
                self.y = min(self.y, stairs[i].y + stairs[i].height - self.height)
                self.y = max(self.y, stairs[i].y)'''

        self.pos = (self.x, self.y)

    def player_pickup(self, pressedKey, items):
        for i in range(len(items)):
            items[i].interact(pressedKey, self)


    def player_attack(self, pressedKey, section):
        self.end_attack = pygame.time.get_ticks()
        if (pressedKey[pygame.K_r]):
            if (self.normal_active == False):
                self.normal_active = True
                self.start_attack = pygame.time.get_ticks()
                self.attack_typ = (self.attack_typ + 1) % 3
                section.throw_stuffs.append(throw_stuff(self.attack_typ, self.dir))
                section.throw_stuffs[len(section.throw_stuffs)-1].setPos(self.x + self.width - section.throw_stuffs[len(section.throw_stuffs)-1].width, self.y + section.throw_stuffs[len(section.throw_stuffs)-1].height)

        if (self.end_attack - self.start_attack >= 1000):
            self.normal_active = False

            if (self.end_attack - self.start_attack >= 2000):
                self.attack_typ = -1


    def player_skill(self, pressedKey, paint):
        if (pressedKey[pygame.K_q] and paint.height > 0):
            if (self.skill_active == False):
                self.attack = True
                paint.dec_bar(10) # can change value

            self.skill_active = True

    def dec_hp(self):
        if (self.hp > 0):
            self.hp_bars[self.hp - 1].setColor((0, 0, 0))
            self.hp -=1
            self.surface = pygame.image.load('media/hp_broken.png').convert_alpha()

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

player = player(200, 200, 300, 300)

while running:
    for event in pygame.event.get(): # return all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked
            running = False

    pressedKeys = pygame.key.get_pressed()
    screen.fill(WHITE)

    player.dec_hp()
    screen.blit(player.getSurface(), (200, 100))


    clock.tick(FPS)# pause the game until FPS time is reached
    pygame.display.flip()


pygame.quit()