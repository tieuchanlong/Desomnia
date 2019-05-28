from myParentclass import *
from myObject import *
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
        self.hp = 5
        self.hit_dist = 0 # hit dist is the distance flew after being hit
        self.rad_vision = 100 # the range of vision for enemy
        self.attack = False
        self.stun = False
        self.move_range = (self.x - 200, self.x + 200)
        self.bounce = False


    def set_rangex(self, l, r):
        self.move_range = (l, r)

    def enemy_move(self, grounds): # try to detect player
        if (self.stun == False and self.bounce == False):
            self.x += self.xspd/2 * self.dir

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
                    cnt+=1

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

        self.pos = (self.x , self.y)

    def enemy_follow(self, player, grounds):
        if (abs(self.x - player.x) <= self.rad_vision and abs(self.y - player.y) <= self.rad_vision and self.move_range[0] <= self.x <= self.move_range[1]): # can change default range
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


            self.x += self.xspd/2 *self.dir
            #self.move_range = (self.move_range[0] + self.xspd*self.dir, self.move_range[1] + self.xspd*self.dir)
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


class jumping_enemy(enemy):
    def __init__(self, width, height, x=0, y=0):
        enemy.__init__(self, width, height, x, y)
        self.start_attack = 0
        self.end_attack = 0
        self.move_range = (self.x - 400, self.x + 400)
        self.rad_vision = 200

    def enemy_follow(self, player, grounds):
        if (self.stun == False and self.bounce == False):
            if (abs(self.x - player.x) <= self.rad_vision and self.move_range[0] <= player.x <= self.move_range[1] and abs(self.y - player.y) <= self.rad_vision and self.move_range[0] <= self.x <= self.move_range[1]):  # can change default range
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
                self.pos = (self.x, self.y)

                self.enemy_attack(player, grounds)

            if (self.attack == False):
                self.width = 60
                self.dim = (self.width, self.height)
                self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
                self.setColor((255, 0, 0))
        else:
            self.width = 60
            self.dim = (self.width, self.height)
            self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
            self.setColor((255, 0, 0))
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

    def enemy_attack(self, player, grounds):
        self.width = 100
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.setColor((255, 0, 0))
        # do some attack animations

        if (self.checkcollision(self, player)):
            player.hp -= 1
            player.jump = -15
            player.bounce = True

            if (player.x > self.x):
                player.dir = 1
            else:
                player.dir = -1

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
        self.rad_vision = 300
        self.hp = 5
        self.start_shoot = 0
        self.end_shoot = 0
        self.attack = False
        self.stun = False
        self.hit = 0


    def enemy_follow(self, player, section):
        if (self.stun == False):
            self.end_shoot = pygame.time.get_ticks()
            if (abs(self.x - player.x) <= self.rad_vision and abs(self.y - player.y) <= self.rad_vision and self.attack == False): # can change default range
                self.attack = True
                self.start_shoot = pygame.time.get_ticks()
            elif (abs(self.x - player.x) > self.rad_vision or abs(self.y - player.y) > self.rad_vision):
                self.attack = False

            if (self.attack == True):
                if (self.x > player.x):
                    self.dir = -1
                    # load turn back animation
                else:
                    self.dir = 1
                    # load turn back animation

                if (self.end_shoot - self.start_shoot >= 2000):
                    # load shoot animation
                    self.start_shoot = pygame.time.get_ticks()
                    section.bullets.append(bullet(10, 10, self.x + self.width/2, self.y, self.dir))
        else:
            self.hit += 5
            if (self.hit > 600):
                self.hit = 0
                self.stun = False

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
        self.hp = 100

    def boss_attack(self, player):
        self.end_attack = pygame.time.get_ticks()

        if (self.end_attack - self.start_attack >= 10000):
            self.attack_typ = (self.attack_typ + 1) % 3

        if (self.attack_typ == 0):
            self.x += self.dir * self.xspd

            if (self.x < 0):
                self.dir = 1
                self.x = 0

            if (self.x > WIDTH - self.width):
                self.dir = -1
                self.x = WIDTH - self.width
                WIDTH - self.width

        if (self.attack_typ == 1):
            # load some animation
            self.x = self.x

        if (self.attack_typ == 2):
            # load some animation
            self.x = self.x

        self.pos = (self.x, self.y)


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
        self.surface.fill(self.color)
        self.xspd = 5
        self.yspd = 10
        self.talk = False
        self.rad_vision = 20 # the range of vision for enemy

    def npc_talk(self, pressedKey, player):
        if (abs(player.x - self.x) <= 150):
            if (pressedKey[pygame.K_e]):
                self.talk = True

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

