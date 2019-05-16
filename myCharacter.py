from myParentclass import *
import pygame

WIDTH = 900
HEIGHT = 500

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
        self.fall = False
        self.swim = False
        self.climb = False

    def playerMove(self, pressedKey, spd):
        if (pressedKey[pygame.K_a]):
            self.x -= spd
        if (pressedKey[pygame.K_d]):
            self.x += spd

        if (self.x < 0):
            self.x = max(self.x, 0)

        self.pos = (self.x, self.y)

    def player_fall(self, spd, grounds):
        self.fall = True
        for i in range(len(grounds)):
            if self.checkcollision(self, grounds[i]) and self.y + self.height >= grounds[i].y and self.y < grounds[i].y:
                self.fall = False
                self.y = grounds[i].y - self.height
                self.pos = (self.x, self.y)
                break

        if (self.fall == True and self.swim == False):
            self.y += spd + self.jump
            #self.jump += 0.5
            self.pos = (self.x, self.y)

    def player_jump(self, pressedKey, grounds):
        if (self.jump == 0 and self.fall == False and self.swim == False and pressedKey[pygame.K_SPACE]):
            self.jump = -24
            return True

        if (self.jump + self.yspd >= 0):
            self.jump = 0
            return False


        self.y = self.jump + self.yspd + self.y
        self.pos = (self.x, self.y)
        self.jump += 0.5

        for i in range(len(grounds)):
            if self.checkcollision(self, grounds[i]) and self.jump >= -10:
                #print('Yes')
                self.y = grounds[i].y - self.height
                self.jump = 0
                self.fall = True
                self.pos = (self.x, self.y)
                return False

        return True

    def player_swim(self, pressedKey, waters):
        self.swim = False
        for i in range(len(waters)):
            if (self.checkcollision(self, waters[i]) and self.y >= waters[i].y):
                self.swim = True
                break

        if (self.swim == True):
            if (pressedKey[pygame.K_w]):
                self.y -= self.yspd
            if (pressedKey[pygame.K_s]):
                self.y += self.yspd
            if (pressedKey[pygame.K_a]):
                self.x -= self.xspd
            if (pressedKey[pygame.K_d]):
                self.x += self.xspd

            if self.x > waters[i].x + waters[i].width - self.width or self.x < 0:
                self.x = min(self.x, waters[i].x + waters[i].width - self.width)
                self.x = max(self.x, 0)

            if self.y > waters[i].y + waters[i].height - self.height or self.y < 0:
                self.y = min(self.y, waters[i].y + waters[i].height - self.height)
                self.y = max(self.y, 0)

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
            if (self.checkcollision(self, items[i])):
                if (pressedKey[pygame.K_e]):
                    items[i].interact()


class companion(sprite):
    def __init__(self, width, height, x=0, y=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)
        self.xspd = 10
        self.yspd = 10

    def companion_move(self, spd=5): # follow player
        pos = pygame.mouse.get_pos(0)
        self.x = pos[0] - self.width/2

        if (self.x > WIDTH - self.width or self.x < 0):
            self.x = min(self.x, WIDTH - self.width)
            self.x = max(self.x, 0)

        self.pos = (self.x, self.y)

class enemy(sprite):
    def __init__(self, width, height, x=0, y=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)
        self.xspd = 5
        self.yspd = 10
        self.rad_vision = 20 # the range of vision for enemy
        self.attack = False
        self.move_range = (self.x - 200, self.x + 200)


    def enemy_move(self, grounds): # try to detect player
        self.x += self.xspd/2 * self.dir

        if (self.x < self.move_range[0]):
            self.dir = -self.dir

        if (self.x > self.move_range[1] - self.width):
            self.dir = -self.dir

        cnt = 0
        for i in range(len(grounds)):
            if self.checkcollision(self, grounds[i]) == False:
                cnt+=1

        if (cnt == len(grounds)):
            self.dir = -self.dir

        self.pos = (self.x , self.y)

    def enemy_follow(self, player):
        if (abs(self.x - player.x) <= self.rad_vision and abs(self.y - player.y) <= self.rad_vision): # can change default range
            self.attack = True
        else:
            self.attack = False

        if (self.attack == True):
            if (self.x < player.x):
                # load turn back animation
                self.x += self.xspd
                self.pos = (self.x, self.y)

    def enemy_attack(self, player):
        # do some attack movements
        return


class shooting_enemy(sprite):
    def __init__(self, width, height, x=0, y=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)
        self.xspd = 5
        self.rad_vision = 100
        self.bullets = []


    def enemy_follow(self, player):
        if (abs(self.x - player.x) <= self.rad_vision and abs(self.y - player.y) <= self.rad_vision): # can change default range
            self.attack = True
        else:
            self.attack = False

        if (self.attack == True):
            if (self.x < player.x):
                # load turn back animation
                return

    def enemy_attack(self, player):
        # do some attack movements
        return


class npc(sprite):
    def __init__(self, width, height, x=0, y=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)
        self.xspd = 5
        self.yspd = 10
        self.rad_vision = 20 # the range of vision for enemy

class moving_npc(npc):
    def __init__(self, width, height, x=0, y=0, spd=1):
        npc.__init__(self, width, height, x, y)
        self.xspd = spd
        self.move_range = (self.x - 200, self.x + 200)

    def npc_move(self, grounds): # try to detect player
        self.x += self.xspd * self.dir

        if (self.x < self.move_range[0]):
            self.dir = -self.dir

        if (self.x > self.move_range[1] - self.width):
            self.dir = -self.dir

        self.pos = (self.x , self.y)

    def set_rangex(self, l, r):
        self.move_range = (l, r)