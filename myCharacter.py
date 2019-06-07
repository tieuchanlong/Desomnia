from myParentclass import *
from myObject import *
from myDialogue import *
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
        self.idl_imagecounter = -1
        self.walk_imagecounter = -1
        self.swim_imagecounter = -1
        self.drawings = text(WIDTH - 30, 20, '0', 40, "Renogare", (255, 255, 255))
        self.drawing_UI = image('media/star.png', WIDTH - 100, 10, 50, 50)
        self.coins = text(WIDTH - 30, 100, '0', 40, "Renogare", (255, 255, 255))
        self.coin_UI = image('media/coin00.png', WIDTH - 100, 90, 50, 50)
        self.coin_UI.surface = pygame.transform.scale(self.coin_UI.surface, (40, 40))

    def playerMove(self, pressedKey, spd, conversation):
            if (self.bounce == False):
                if (pressedKey[pygame.K_a] and conversation.dialogueLEVEL == -1):
                    self.x -= spd
                    self.dir = -1
                    self.player_walk_anim()
                elif (pressedKey[pygame.K_d] and conversation.dialogueLEVEL == -1):
                    self.x += spd
                    self.dir = 1
                    self.player_walk_anim()
                else:
                    self.player_idle_anim()
            else:
                self.x += 10*self.dir
                self.bounce_count += 10

            if (self.jump + self.yspd >= 0 and self.bounce_count > 100):
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

    def player_jump(self, pressedKey, grounds, moving_grounds, conversation):
        if (self.jump == 0 and self.fall == False and self.swim == False and self.bounce == False and conversation.dialogueLEVEL == -1 and pressedKey[pygame.K_SPACE]):
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
                self.player_swim_anim()
                self.dir = 0
                self.dir1 = 0
                if (pressedKey[pygame.K_w]):
                    self.y -= self.yspd
                    self.dir1 = -1
                if (pressedKey[pygame.K_s]):
                    self.y += self.yspd
                    self.dir1 = 1
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


    def player_pickup(self, pressedKey, items):
        for i in range(len(items)):
            items[i].interact(pressedKey, self)

    def player_attack(self, pressedKey, section, conversation):
        self.end_attack = pygame.time.get_ticks()
        if (pygame.mouse.get_pressed()[0] == 1 and conversation.dialogueLEVEL == -1):
            if (self.normal_active == False):
                self.normal_active = True
                self.start_attack = pygame.time.get_ticks()
                self.attack_typ = (self.attack_typ + 1) % 3
                section.throw_stuffs.append(throw_stuff(self.attack_typ, self.dir))
                if (self.attack_typ < 2):
                    section.throw_stuffs[len(section.throw_stuffs)-1].setPos(self.x + self.width - section.throw_stuffs[len(section.throw_stuffs)-1].width, self.y)
                else:
                    section.throw_stuffs[len(section.throw_stuffs) - 1].setPos(self.x + self.width - section.throw_stuffs[len(section.throw_stuffs) - 1].width, self.y - 40)

        if (self.end_attack - self.start_attack >= 1000):
            self.normal_active = False

            if (self.end_attack - self.start_attack >= 2000):
                self.attack_typ = -1


    def player_skill(self, pressedKey, paint, conversation):
        if (pygame.mouse.get_pressed()[2] == 1 and conversation.dialogueLEVEL == -1 and paint.amount > 0):
            if (self.skill_active == False):
                self.attack = True
                paint.dec_bar(10) # can change value

            self.skill_active = True

    def dec_hp(self):
        if (self.hp > 0):
            self.hp_bars[self.hp - 1].surface = pygame.image.load('media/hp_broken.png').convert_alpha()
            self.hp -=1

    def player_idle_anim(self):
        self.idl_imagecounter += 1
        self.walk_imagecounter = -1
        self.jump_imagecounter = -1

        if self.idl_imagecounter >= 20:
            self.idl_imagecounter = 0

        self.surface = pygame.image.load('media/anna_idle_0' + str(int(self.idl_imagecounter / 10)) + '.png').convert_alpha()
        if (self.dir == 1):
            self.surface = pygame.transform.flip(self.surface, 0, 0)
        else:
            self.surface = pygame.transform.flip(self.surface, 1, 0)

    def player_walk_anim(self):
        self.walk_imagecounter += 1
        self.idl_imagecounter = -1
        self.jump_imagecounter = -1

        if self.walk_imagecounter >= 20:
            self.walk_imagecounter = 0

        self.surface = pygame.image.load('media/anna_walk_0' + str(int(self.walk_imagecounter / 5)) + '.png').convert_alpha()
        if (self.dir == 1):
            self.surface = pygame.transform.flip(self.surface, 0, 0)
        else:
            self.surface = pygame.transform.flip(self.surface, 1, 0)

    '''def player_jump_anim(self):
        self.jump_imagecounter += 1
        self.walk_imagecounter = -1
        self.idl_imagecounter = -1

        if self.jump_imagecounter >= 30:
            self.jump_imagecounter = 0

        self.surface = pygame.image.load('media/anna_jump_0' + str(int(self.jump_imagecounter / 10)) + '.png').convert_alpha()
        if (self.dir == 1):
            self.surface = pygame.transform.flip(self.surface, 0, 0)
        else:
            self.surface = pygame.transform.flip(self.surface, 1, 0)'''

    def player_att_anim(self):
        self.att_imagecounter += 1
        self.idl_imagecounter = -1

        if self.att_imagecounter >= 30:
            self.att_imagecounter = 0

        self.surface = pygame.image.load('media/anna_attack_0' + str(int(self.att_imagecounter / 10)) + '.png').convert_alpha()
        if (self.dir == 1):
            self.surface = pygame.transform.flip(self.surface, 1, 0)
        else:
            self.surface = pygame.transform.flip(self.surface, 0, 0)


    def player_swim_anim(self):
        self.swim_imagecounter += 1
        if self.swim_imagecounter >= 40:
            self.swim_imagecounter = 0

        self.surface = pygame.image.load('media/anna_swim_0' + str(int(self.swim_imagecounter / 10)) + '.png').convert_alpha()

        if (self.dir == 1):
            self.surface = pygame.transform.flip(self.surface, 0, 0)
        else:
            self.surface = pygame.transform.flip(self.surface, 1, 0)


class enemy(sprite):
    def __init__(self, width, height, x=0, y=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface = pygame.image.load('media/enemy_idle_00.png').convert_alpha()
        self.xspd = 5
        self.yspd = 10
        self.hp = 5
        self.hit_dist = 0  # hit dist is the distance flew after being hit
        self.rad_vision = 100  # the range of vision for enemy
        self.attack = False
        self.stun = False
        self.move_range = (self.x - 200, self.x + 200)
        self.bounce = False
        self.att_imagecounter = -1
        self.idl_imagecounter = -1
        self.die_imagecounter = -1


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

    def enemy_move(self, grounds): # try to detect player
        self.enemy_idle_anim()
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
                    self.dir = -1

                check = False
                for i in range(len(grounds)):
                    if (self.checkcollision(self, grounds[i])):
                        check = True
                        break

                if (check == False):
                    self.dir = -1

            else:
                if (self.x <= self.move_range[1]):
                    self.dir = -1
                else:
                    self.dir = 1

                check = False
                for i in range(len(grounds)):
                    if (self.checkcollision(self, grounds[i])):
                        check = True
                        break

                if (check == False):
                    self.dir = 1


            self.x += self.xspd/2 *self.dir
            self.pos = (self.x, self.y)

            self.enemy_attack(player, grounds)

    def enemy_attack(self, player, grounds):
        # do some attack movements
        self.enemy_att_anim()

        if (self.checkcollision(self, player)):
            player.jump = -15

            if (player.jump == -15 and player.bounce == False):
                player.dec_hp()

            player.bounce = True

            if (player.x > self.x):
                player.dir = 1
            else:
                player.dir = -1

    def enemy_die(self):
        if (self.hp == 0):
            self.enemy_die_anim()
            if (self.die_imagecounter >= 40):
                self.setPos(-10000, -10000)

    def enemy_idle_anim(self):
        self.idl_imagecounter += 1
        self.att_imagecounter = -1

        if self.idl_imagecounter >= 20:
            self.idl_imagecounter = 0

        self.surface = pygame.image.load('media/enemy_idle_0' + str(int(self.idl_imagecounter / 10)) + '.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (40, 40))

        if (self.dir == 1):
            self.surface = pygame.transform.flip(self.surface, 1, 0)
        else:
            self.surface = pygame.transform.flip(self.surface, 0, 0)

    def enemy_att_anim(self):
        self.att_imagecounter += 1
        self.idl_imagecounter = -1

        if self.att_imagecounter >= 30:
            self.att_imagecounter = 0

        self.surface = pygame.image.load('media/enemy_att_0' + str(int(self.att_imagecounter / 10)) + '.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (40, 40))

        if (self.dir == 1):
            self.surface = pygame.transform.flip(self.surface, 1, 0)
        else:
            self.surface = pygame.transform.flip(self.surface, 0, 0)

    def enemy_die_anim(self):
        self.die_imagecounter += 1

        if self.att_imagecounter >= 40:
            self.die_imagecounter = 0
            self.surface = pygame.image.load('media/enemy_die_00.png').convert_alpha()
            self.surface = pygame.transform.scale(self.surface, (40, 40))
        else:
            self.surface = pygame.image.load('media/enemy_die_0' + str(int(self.die_imagecounter / 10)) + '.png').convert_alpha()
            self.surface = pygame.transform.scale(self.surface, (40, 40))


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
        self.xspd = 10
        self.hp = 30
        self.move_range = (self.x, self.x + WIDTH)
        self.surface.fill(self.color)
        self.rocks = []
        self.att_imagecounter = -1
        self.angry_imagecounter = -1
        self.die_imagecounter = -1

    def move_x(self, dist):
        self.setPos(self.x + dist, self.y)
        self.move_range = (self.move_range[0] + dist, self.move_range[1] + dist)

    def move_y(self, dist):
        self.setPos(self.x, self.y + dist)

    def boss_attack(self, player):
        if (self.hp > 0):
            self.end_attack = pygame.time.get_ticks()

            for i in range(len(self.rocks)):
                self.rocks[i].rock_move(player)

            if (self.end_attack - self.start_attack >= 10000):
                if (self.attack_typ == 0):
                    for i in range(20):
                        self.rocks.append(rock(50, 50, self))
                        while True:
                            check = False
                            for j in range(len(self.rocks)-1):
                                if (self.rocks[j].checkcollision(self.rocks[j], self.rocks[len(self.rocks)-1])):
                                    check = True

                            if (check == False):
                                break

                            if (check == True):
                                check = False
                                self.rocks[len(self.rocks)-1].setPos(random.randrange(int(self.move_range[0]), int(self.move_range[1]) + 100), self.y - random.randrange(HEIGHT, HEIGHT + 200))

                self.attack_typ = (self.attack_typ + 1) % 2
                self.start_attack = pygame.time.get_ticks()

            if (self.attack_typ == 0):
                self.boss_att_anim()
                self.x += self.dir * self.xspd

                if (self.x < self.move_range[0]):
                    self.dir = 1
                    self.x = self.move_range[0]

                if (self.x > self.move_range[1]):
                    self.dir = -1
                    self.x = self.move_range[1]

            if (self.attack_typ == 1):
                # load some animation
                self.boss_angry_ani()

                self.x = self.x

            if (self.checkcollision(self, player)):
                player.jump = -15

                if (player.jump == -15 and player.bounce == False):
                    player.dec_hp()

                player.bounce = True

                if (player.x > self.x):
                    player.dir = 1
                else:
                    player.dir = -1

            self.pos = (self.x, self.y)

    def boss_die(self):
        if (self.hp <= 0):
            # Load death animation
            self.boss_die_ani()

    def boss_att_anim(self):
        self.att_imagecounter += 1
        self.angry_imagecounter = -1
        self.die_imagecounter = -1

        if self.att_imagecounter >= 70:
            self.att_imagecounter = 0

        self.surface = pygame.image.load('media/boss_attack0' + str(int(self.att_imagecounter / 10)) + '.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.width, self.height))

        if (self.dir == 1):
            self.surface = pygame.transform.flip(self.surface, True, False)
        else:
            self.surface = pygame.transform.flip(self.surface, False, False)


    def boss_angry_ani(self):
        self.att_imagecounter = -1
        self.angry_imagecounter += 1
        self.die_imagecounter = -1

        if self.angry_imagecounter >= 24:
            self.angry_imagecounter= 0

        self.surface = pygame.image.load('media/boss_angry0' + str(int(self.angry_imagecounter / 4)) + '.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.width, self.height))

    def boss_die_ani(self):
        self.att_imagecounter = -1
        self.angry_imagecounter = -1
        self.die_imagecounter += 1

        if self.die_imagecounter >= 60:
            self.die_imagecounter = 0
            self.surface = pygame.image.load('media/boss_die0' + str(int(self.die_imagecounter / 10)) + '.png').convert_alpha()
            self.surface = pygame.transform.scale(self.surface, (self.width, self.height))
            self.setPos(-10000, -10000)


        self.surface = pygame.image.load('media/boss_die0' + str(int(self.die_imagecounter / 10)) + '.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.width, self.height))
        self.surface = pygame.transform.flip(self.surface, True, False)


class npc(sprite):
    def __init__(self, width, height, x=0, y=0):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface = pygame.image.load('media/npc_idle_00.png').convert_alpha()
        self.xspd = 5
        self.yspd = 10
        self.talk = False
        self.rad_vision = 20 # the range of vision for enemy
        self.imagecounter = -1

    def npc_talk(self, pressedKey, player):
        if (abs(player.x - self.x) <= 150):
            if (pressedKey[pygame.K_e]):
                self.talk = True

    def npc_idle(self):
        self.imagecounter += 1
        if self.imagecounter >= 30:
            self.imagecounter = 0

        self.surface = pygame.image.load('media/npc_idle_0' + str(int(self.imagecounter/10)) + '.png').convert_alpha()
        if (self.dir == 1):
            self.surface = pygame.transform.flip(self.surface, 1, 0)
        else:
            self.surface = pygame.transform.flip(self.surface, 0, 0)

class moving_npc(npc):
    def __init__(self, width, height, x=0, y=0, spd=1):
        npc.__init__(self, width, height, x, y)
        self.xspd = spd
        self.move_range = (self.x - 200, self.x + 200)

    def npc_move(self, grounds): # try to detect player
        self.x += self.xspd * self.dir

        if (self.x < self.move_range[0]):
            self.dir = 1

        if (self.x > self.move_range[1] - self.width):
            self.dir = -1

        self.npc_idle()

        self.pos = (self.x , self.y)

    def set_rangex(self, l, r):
        self.move_range = (l, r)

