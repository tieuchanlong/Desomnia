from myParentclass import *

WIDTH = 900
HEIGHT = 500

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

class ground(sprite): # the mid ground for climbing
    def __init__(self, width, height, x=0, y=0):  # add frames input
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

class moving_ground(ground):
    def __init__(self, width, height, x=0, y=0):  # add frames input
        ground.__init__(self, width, height, x, y)
        self.move_rangex = (0, 0)
        self.move_rangey = (0, 0)
        self.xspd = 10
        self.yspd = 10
        self.dir = 1
        self.dir1 = -1

    def set_rangex(self, l, r):
        self.move_rangex = (l, r)

    def set_rangey(self, l, r):
        self.move_rangey = (l, r)

    def ground_move(self, player, onX = 1, onY = 1):  # try to detect player
        if (onX == 1):
            if (self.dir == -1):
                self.xspd = 10
            else:
                self.xspd = 25

            self.x += self.xspd  * self.dir

            if (self.checkcollision(self, player)):
                player.x += self.xspd * self.dir

            if (self.x < self.move_rangex[0]):
                self.x = self.move_rangex[0]
                self.dir = -self.dir

            if (self.x > self.move_rangex[1] - self.width):
                self.x = self.move_rangex[1] - self.width
                self.dir = -self.dir


        if (onY == 1):
            self.y += self.yspd * self.dir1

            if (self.checkcollision(self, player)):
                player.y += self.yspd * self.dir1

            if (self.y < self.move_rangey[0]):
                self.y = self.move_rangey[0]
                self.dir1 = -self.dir1

            if (self.x > self.move_rangey[1] - self.height):
                self.y = self.move_rangey[1] - self.height
                self.dir1 = -self.dir1


        self.pos = (self.x, self.y)


class trap(sprite):
    def __init__(self, width, height, x=0, y=0):  # add frames input
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def trap_attack(self, player):
        if (self.checkcollision(self, player)):
            player.hp -=1
            # do player loses health
            player.jump = -15
            player.bounce = True

            if (player.x > self.x):
                player.dir = 1
            else:
                player.dir = -1

            self.pos = (self.x, self.y)

class moving_trap(trap):
    def __init__(self, width, height, x=0, y=0):  # add frames input
        trap.__init__(self, width, height, x, y)
        self.move_range = (0, 0)
        self.yspd = 10

    def set_rangey(self, l, r):
        self.move_range = (l, r)

    def trap_move(self, player): # try to detect player
        self.y += self.yspd * self.dir1

        if (self.y < self.move_range[0]):
            self.dir1 = 1

        if (self.y > self.move_range[1]):
            self.dir1 = -1

        if (self.checkcollision(self, player)):
            player.hp -= 1
            player.jump = -15
            player.bounce = True

            if (player.x > self.x):
                player.dir = 1
            else:
                player.dir = -1

        self.pos = (self.x , self.y)

class water(sprite):
    def __init__(self, width, height, x=0, y=0):  # add frames input
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)