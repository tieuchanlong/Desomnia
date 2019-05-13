from myParentclass import *

WIDTH = 900
HEIGHT = 500

class plant(sprite):
    def __init__(self, width, height, x=0, y=0):  # add frames input
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)


    def move(self, spd=1, onX=1, onY=1):
        sprite.move(self, spd, onX, onY)

        if (self.x > WIDTH - self.width or self.x < 0):
            self.x = min(self.x, WIDTH - self.width)
            self.x = max(self.x, 0)
            self.dir = -self.dir

        if (self.y > HEIGHT - self.height or self.y < 0):
            self.y = min(self.y, HEIGHT - self.height)
            self.y = max(self.y, 0)
            self.dir1 = -self.dir1

        self.pos = (self.x, self.y)

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

    def set_rangex(self, l, r):
        self.move_rangex = (l, r)

    def set_rangey(self, l, r):
        self.move_rangey = (l, r)

    def ground_move(self, grounds, onX = 1, onY = 1):  # try to detect player
        if (onX == 1):
            self.x += self.xspd  * self.dir

            if (self.x < self.move_rangex[0]):
                self.dir = -self.dir

            if (self.x > self.move_rangex[1] - self.width):
                self.dir = -self.dir

            for i in range(len(grounds)):
                if (self.checkcollision(self, grounds[i]) and grounds[
                    i].y < self.y + self.height):  # when the enemy bump into high ground
                    self.dir = -self.dir

        if (onY == 1):
            self.y += self.yspd * self.dir1

            if (self.y < self.move_rangey[0]):
                self.dir = -self.dir

            if (self.x > self.move_rangey[1] - self.width):
                self.dir = -self.dir

            for i in range(len(grounds)):
                if (self.checkcollision(self, grounds[i]) and grounds[
                    i].y < self.y + self.height):  # when the enemy bump into high ground
                    self.dir = -self.dir

        self.pos = (self.x, self.y)


class water(sprite):
    def __init__(self, width, height, x=0, y=0):  # add frames input
        sprite.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.typ = random.randrange(3)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)