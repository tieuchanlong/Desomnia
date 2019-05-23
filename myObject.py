from myParentclass import *

class save_point(interactive_object):
    def __init__(self, width, height, x=0, y=0):
        interactive_object.__init__(self, width, height, x, y)

    def interact(self, player):
        # save game
        return

class drawing_piece(interactive_object):
    def __init__(self, width, height, x=0, y=0):
        interactive_object.__init__(self, width, height, x, y)

    def interact(self, player):
        # save game
        return

class gate(interactive_object):
    def __init__(self, width, height, x=0, y=0):
        interactive_object.__init__(self, width, height, x, y)

    def interact(self, player):
        # get to next level
        return

class stair(interactive_object):
    def __init__(self, width, height, x=0, y=0):
        interactive_object.__init__(self, width, height, x, y)

class brush(sprite):
    def __init__(self, width, height, x=0, y=0):  # add frames input
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.xspd = 30
        self.dir = 0
        self.turn = 1
        self.round = 0
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def brush_move(self, player):
        if (self.dir == 0):
            if (player.dir == -1):
                self.x = player.x - self.width - 50
            else:
                self.x = player.x + player.width + 50

        if (self.x <= player.x):
            dist = abs(player.x - self.x - self.width)
        else:
            dist = abs(player.x + player.width - self.x)


        if (player.attack == True):
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
                enemies[i].bounce = True
                if (self.x < enemies[i].x):
                    enemies[i].dir = 1
                else:
                    enemies[i].dir = -1


