from myParentclass import *

class save_point(interactive_object):
    def __init__(self, width, height, x=0, y=0, ar=0):
        interactive_object.__init__(self, width, height, x, y - 20)
        self.area = ar
        self.org_x = x
        self.org_y = y - 20
        self.imagecounter = -1

    def save_game(self, pressedKey, player, section):
        # save game
        if (abs(player.x - self.x) <= 100):
            if (pressedKey[pygame.K_e]):
                self.setColor((255, 255, 0))
                return 1, (section, self.org_x, self.org_y + self.height - player.height)

        return 0, (-10, 0, 0)

    def save_anim(self):
        self.imagecounter += 1

        if self.imagecounter >= 24:
            self.imagecounter = 0

        self.surface = pygame.image.load('media/fireplace-' + str(int(self.imagecounter / 4)) + '.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (60, 60))

class instruction_point(interactive_object):
    def __init__(self, width, height, x=0, y=0, ar=0):
        interactive_object.__init__(self, width, height, x, y)
        self.area = ar
        self.surface = pygame.image.load('media/board.png').convert_alpha()

    def interact(self, pressedKey, player):
        # Add some interaction
        if (abs(player.x - self.x) <= 100):
            if (pressedKey[pygame.K_e]):
                # Add instructions
                return

class control_panel(interactive_object):
    def __init__(self, width, height, x=0, y=0):
        interactive_object.__init__(self, width, height, x, y)
        self.active = False


    def interact(self, pressedKey, player):
        if (abs(player.x - self.x) <= 100):
            if (pressedKey[pygame.K_e]):
                self.setColor((255, 255, 0))
                self.active = True

class drawing_piece(interactive_object):
    def __init__(self, width, height, x=0, y=0):
        interactive_object.__init__(self, width, height, x, y)
        self.surface = pygame.image.load('media/star.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (30, 30))

    def interact(self, pressedKey, player):
        if (self.checkcollision(self, player)):
            self.setPos(-10000, -10000)
            self.collect = True
            print('Yes')


class gate(interactive_object):
    def __init__(self, width, height, x=0, y=0):
        interactive_object.__init__(self, width, height, x, y)
        self.active = False
        self.surface = pygame.image.load('media/door.png').convert_alpha()

    def enter_gate(self, pressedKey, player):
        # save game
        if (abs(player.x - self.x) <= 100):
            if (pressedKey[pygame.K_e]):
                self.setColor((255, 255, 0))
                self.active = True

class water_fountain(interactive_object):
    def __init__(self, width, height, x=0, y=0):
        interactive_object.__init__(self, width, height, x, y)
        self.active = False
        self.coin_check = False
        self.surface = pygame.image.load('media/water_fountain.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (width, height))

    def interact(self, pressedKey, player):
        return

    def put_coin(self, pressedKey, player, coins):
        # save game
        if (abs(player.x - self.x) <= 100 and coins >= 5):
            if (pressedKey[pygame.K_e]):
                # minus the amount of coins
                return 5

        return 0


class stair(interactive_object):
    def __init__(self, width, height, x=0, y=0):
        interactive_object.__init__(self, width, height, x, y)

class brush(sprite):
    def __init__(self, width, height, x=0, y=0, typ = 1):  # add frames input
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.xspd = 30
        self.dir = 0
        self.turn = 1
        self.round = 0
        self.typ = typ
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def brush_stay(self, player):
        if (player.attack == True):
            self.appear = False
        else:
            self.appear = True

        if (player.dir == -1):
            self.x = player.x - self.width - 10
        else:
            self.x = player.x + player.width + 10

        self.y = player.y + player.height - self.height - 10
        self.pos = (self.x, self.y)

    def brush_move(self, player):
        if (self.dir == 0):
            self.appear = False
            if (player.dir == -1):
                self.x = player.x - self.width - 50
            else:
                self.x = player.x + player.width + 50

        if (self.x <= player.x):
            dist = abs(player.x - self.x - self.width)
        else:
            dist = abs(player.x + player.width - self.x)

        if (player.attack == True):
            self.appear = True
            if (abs(self.xspd) == 30):
                self.turn = 1 - self.turn

                self.round += 1

            if (self.turn == 0):
                self.xspd -= 1
            else:
                self.xspd += 1

            if (self.x < player.x):
                self.dir = -1
            else:
                self.dir = 1

            self.x += self.dir * self.xspd

        if (dist < 30):
            self.dir = 0
            self.xspd = 30
            self.turn = 1
            player.skill_active = False
            player.attack = False

        self.y = player.y + 10
        self.pos = (self.x, self.y)

    def brush_hit(self, enemies):
        for i in range(len(enemies)):
            if (self.checkcollision(self, enemies[i]) and self.turn == 0):
                enemies[i].stun = True
                if (self.x < enemies[i].x):
                    enemies[i].dir = 1
                else:
                    enemies[i].dir = -1

class throw_stuff(sprite):
    def __init__(self, typ = 0, direction = 1):  # add frames input
        sprite.__init__(self, 0, 0)
        self.xspd = 10
        self.yspd = -15
        self.dir = direction
        self.turn = 1
        self.round = 0
        self.typ = typ
        if (self.typ < 2):
            self.width = 10
            self.height = 10
            self.yspd = 0
        else:
            self.width = 80
            self.height = 40

        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.imagecounter = -1


        self.red = 0
        self.green = 0
        self.blue = 0
        self.color = (self.red, self.green, self.blue)

    def stuff_move(self, enemies, boss, grounds, paint):
        self.stuff_anim()
        for i in range(len(grounds)):
            if (self.checkcollision(self, grounds[i]) and self.y <= grounds[i].y):
                self.xspd = 0
                self.yspd = 0
                self.dir = 0
                self.setPos(-10000, -10000)
                return

        for i in range(len(enemies)):
            if (self.checkcollision(self, enemies[i])):
                self.xspd = 0
                self.yspd = 0
                self.dir = 0
                self.setPos(-10000, -10000)
                enemies[i].hp -= 1
                enemies[i].bounce = True
                if (self.x + self.width <= enemies[i].x + enemies[i].width/2):
                    enemies[i].dir = -1
                else:
                    enemies[i].dir = 1

                paint.dec_bar(-5)

                return

        if (self.checkcollision(self, boss)):
            self.xspd = 0
            self.yspd = 0
            self.dir = 0
            self.setPos(-10000, -10000)
            boss.hp -= 1
            return

        self.x += self.xspd * self.dir
        if (self.typ == 2):
            self.y += self.yspd
            self.yspd += 1
            if (self.yspd >= 10):
                self.yspd = 10

        self.pos = (self.x, self.y)

    def stuff_anim(self):
        self.imagecounter += 1

        if self.imagecounter >= 8:
            self.imagecounter = 0

        if (self.typ < 2):
            self.surface = pygame.image.load('media/magic_orb0' + str(int(self.imagecounter/2)) + '.png').convert_alpha()
        else:
            self.surface = pygame.image.load('media/cat.png').convert_alpha()
            self.surface = pygame.transform.scale(self.surface, (80, 60))
        if (self.dir == 1):
            self.surface = pygame.transform.flip(self.surface, 1, 0)
        else:
            self.surface = pygame.transform.flip(self.surface, 0, 0)


class bullet(sprite):
    def __init__(self, width, height, x=0, y=0, dir=1):
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dir = dir
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.red = 0
        self.green = 0
        self.blue = 0
        self.color = (0, 0, 0)
        self.surface = pygame.image.load('media/fireball.png').convert_alpha()
        if (self.dir == -1):
            self.surface = pygame.transform.flip(self.surface, 1, 0)
        self.surface = pygame.transform.scale(self.surface, (width + 50, height + 50))
        self.xspd = 15
        self.yspd = 10

    def bullet_move(self, player): # follow player
        self.x = self.x + self.xspd*self.dir

        if (self.x > WIDTH or self.x < 0):
            self.x = -10000
            self.y = -10000
            self.dir = 0

        if (self.checkcollision(self, player)):
            #player take damage animation
            player.dir = self.dir
            self.dir = 0
            self.setPos(-3000, -3000)

            player.jump = -15

            if (player.jump == -15 and player.bounce == False):
                player.dec_hp()

            player.bounce = True

        self.pos = (self.x, self.y)

class rock(sprite):
    def __init__(self, width, height, boss):  # add frames input
        x = random.randrange(int(boss.move_range[0]) - 100, int(boss.move_range[1]) + 200)
        y = boss.y - random.randrange(HEIGHT - 1000, HEIGHT - 500)
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.yspd = 6
        self.dir1 = 1
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface = pygame.image.load('media/lava_rock.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.width, self.height))

    def move_x(self, dist):
        self.setPos(self.x + dist, self.y)

    def move_y(self, dist):
        self.setPos(self.x, self.y + dist)

    def rock_move(self, player):
        self.y += self.dir1 * self.yspd

        if (self.checkcollision(self, player)):
            player.dec_hp()
            self.yspd = 0
            self.setPos(-10000, -10000)

        self.setPos(self.x, self.y)