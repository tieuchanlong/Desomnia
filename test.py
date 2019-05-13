'''
Title: Boxes
Author: Wayne Seto
Date Created: 2019-04-11
'''

import pygame

pygame.init()  # Load the pygame module commands in the program

# Display variables
TITLE = "Boxes"  # Appears in the window title
FPS = 45  # Frames per second
WIDTH = 1457
HEIGHT = 800
SCREENDIM = (WIDTH, HEIGHT)

# Color Variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
GOLD = (212, 175, 55)
SILVER = (192, 192, 192)


# Classes

class MyClass:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.surface = pygame.Surface((0, 0), pygame.SRCALPHA, 32)
        self.red = 0
        self.green = 0
        self.blue = 0
        self.color = (self.red, self.green, self.blue)
        self.xDir = 1
        self.yDir = 1

    def getSurface(self):
        return self.surface

    def getPos(self):
        return self.pos

    def setColor(self, color=(0, 0, 0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        self.color = (self.red, self.green, self.blue)

    def setpos(self, x, y):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)

    def getX(self):
        return self.x

    def getWidth(self):
        return self.width

    def getY(self):
        return self.y

    def getHeight(self):
        return self.height


class text(MyClass):
    def __init__(self, content, font='Arial', fontSize=24):
        MyClass.__init__(self)
        self.fontFam = font
        self.fontSize = fontSize
        self.font = pygame.font.SysFont(self.fontFam, self.fontSize)
        self.content = content
        self.surface = self.font.render(self.content, 1, self.color)

    def setpos(self, x, y):
        MyClass.setpos(self, x, y)
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)

    def setColor(self, color=(0, 0, 0)):
        MyClass.setColor(self, color)
        self.surface = self.font.render(self.content, 1, self.color)

    def getText(self):
        return MyClass.getSurface(self)


class Player(MyClass):
    def __init__(self, x=0, y=0):
        MyClass.__init__(self, x, y)
        self.width = 150  # private data
        self.height = 20
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def setpos(self, x, y):
        MyClass.setpos(self, x, y)
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)

    def playermove(self, WIDTH, pressedKeys, spd=3):

        WIDTH = WIDTH

        if pressedKeys[pygame.K_a]:
            self.x -= spd
        if pressedKeys[pygame.K_d]:
            self.x += spd

        if self.x > WIDTH - self.surface.get_width():
            self.x = WIDTH - self.surface.get_width()
        if self.x < 0:
            self.x = 0

        self.pos = (self.x, self.y)

    def setColor(self, color=(0, 0, 0)):
        MyClass.setColor(self, color)
        self.surface.fill(self.color)

    def getPlayer(self):
        return MyClass.getSurface(self)


class Ball(MyClass):
    def __init__(self, x=0, y=0):
        MyClass.__init__(self, x, y)
        self.width = 25
        self.height = 20
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def setpos(self, x, y):
        MyClass.setpos(self, x, y)
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)

    def setColor(self, color=(0, 0, 0)):
        MyClass.setColor(self, color)
        self.surface.fill(self.color)

    def getBall(self):
        return MyClass.getSurface(self)

    def automove(self, WIDTH, HEIGHT, xspd=5, yspd=5):
        WIDTH = WIDTH
        HEIGHT = HEIGHT

        self.xspd = xspd
        self.yspd = yspd

        self.x += (self.xDir * self.xspd)
        self.y += (self.yDir * self.yspd)
        self.pos = (self.x, self.y)

        if self.x > WIDTH - self.surface.get_width():
            self.xDir = -1
        if self.x < 0:
            self.xDir = 1
        if self.y < 0:
            self.yDir = 1


class bricks(MyClass):
    def __init__(self, x=0, y=0):
        MyClass.__init__(self, x, y)
        self.width = 240
        self.height = 20
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def brickmoveleft(self, WIDTH, xspd=5):
        WIDTH = WIDTH
        self.xspd = xspd
        self.x += (self.xDir * self.xspd)
        self.pos = (self.x, self.y)
        if self.x > WIDTH / 2 - bricks.getbrickwall(self).get_width() - 30:
            self.xDir = -1
        if self.x < 0:
            self.xDir = 1

    def brickmoveright(self, WIDTH, xspd=5):
        WIDTH = WIDTH
        self.xspd = xspd
        self.x += (self.xDir * self.xspd)
        self.pos = (self.x, self.y)
        if self.x < WIDTH / 2 + bricks.getbrickwall(self).get_width() - 18:
            self.xDir = 1
        if self.x > WIDTH - self.width:
            self.xDir = -1

    def setpos(self, x, y):
        MyClass.setpos(self, x, y)
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)

    def setdirection(self, xDir):
        self.xDir = xDir

    def setdim(self, width, height):
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)

    def setColor(self, color=(0, 0, 0)):
        MyClass.setColor(self, color)
        self.surface.fill(self.color)

    def getbrickwall(self):
        return MyClass.getSurface(self)


def getSpriteCollision(sprite1, sprite2):
    x = max(sprite1.getX(), sprite2.getX())
    y = max(sprite1.getY(), sprite2.getY())
    x1 = min(sprite1.getX() + sprite1.getWidth(), sprite2.getX() + sprite2.getWidth())
    y1 = min(sprite1.getY() + sprite1.getHeight(), sprite2.getY() + sprite2.getHeight())
    if x < x1 and y < y1:
        sprite1.xDir = sprite1.xDir
        sprite1.yDir = -sprite1.yDir
        collide = 1
        return collide


# Create the Window
screen = pygame.display.set_mode(SCREENDIM)  # Creates the main surface where all other assets are placed on top
pygame.display.set_caption(TITLE)  # This updates the window title with TITLE
screen.fill(GREY)  # Fill the entire surface with the color . Think of fill as erase

clock = pygame.time.Clock()  # starts a clock object to measure time


### --- Codes starts here --- ###


def startscreen():
    global level, playercolor

    playercolor = (0, 0, 0)
    level = 0

    startscreen = text("WELCOME TO BRICK BREAKER")
    startscreen.setColor(WHITE)
    startscreen.setpos(WIDTH / 2 - startscreen.getText().get_width() / 2,
                       HEIGHT / 2 - startscreen.getText().get_width() / 2)

    selectcolor = text("PLEASE SELECT A COLOR FOR YOUR PLAYER")
    selectcolor.setColor(WHITE)
    selectcolor.setpos(WIDTH / 2 - selectcolor.getText().get_width() / 2, 300)

    playerchoice = text("1 --> BLUE | 2 --> RED | 3 --> GREEN")
    playerchoice.setColor(WHITE)
    playerchoice.setpos(WIDTH / 2 - playerchoice.getText().get_width() / 2, 350)

    if pressedKeys[pygame.K_1]:
        playercolor = BLUE
        level = 1
        return BLUE
    elif pressedKeys[pygame.K_2]:
        playercolor = RED
        level = 1
        return RED
    elif pressedKeys[pygame.K_3]:
        playercolor = GREEN
        level = 1
        print(playercolor)
        return GREEN

    screen.blit(startscreen.getText(), startscreen.getPos())
    screen.blit(selectcolor.getText(), selectcolor.getPos())
    screen.blit(playerchoice.getText(), playerchoice.getPos())

    return playercolor, level


def level1(playercolor):
    global level

    level = 1


    # brickbreaker TEXT
    brickbreakertext = text("BRICK BREAKER")
    brickbreakertext.setColor(WHITE)
    brickbreakertext.setpos(WIDTH / 2 - brickbreakertext.getText().get_width() / 2, 0)

    # player TILES
    player = Player(300, 550)
    player.setColor(playercolor)
    player.setpos(WIDTH / 2 - player.getPlayer().get_width() / 2, HEIGHT - 20)

    # ball
    ball = Ball(800, 400)
    ball.setColor(WHITE)
    ball.setpos(WIDTH / 2 - ball.getBall().get_width() / 2, HEIGHT - 40)

    # level1 brickwall
    movingbrickwall = []
    upperbrickwall = []
    midbrickwall = []
    lowerbrickwall = []

    # Appending level 1 bricks

    for i in range(4):
        movingbrickwall.append(bricks(100, 100))
        movingbrickwall[i].setdim(50, 20)
        movingbrickwall[i].setColor(GOLD)

    for i in range(20):
        upperbrickwall.append(bricks(100, 100))
        upperbrickwall[i].setdim(100, 20)
        upperbrickwall[i].setColor(SILVER)

    for i in range(10):
        midbrickwall.append(bricks(100, 100))
        midbrickwall[i].setColor(GOLD)

    for i in range(30):
        lowerbrickwall.append(bricks(100, 100))
        lowerbrickwall[i].setdim(100, 20)
        lowerbrickwall[i].setColor(SILVER)

    # Appending level 2 bricks

    ## LEVEL 1 BRICKS START HERE ##

    # LEVEL 1 - MOVINGBRICKWALL

    movingbrickwall[0].setpos(WIDTH / 2 - bricks.getbrickwall(movingbrickwall[0]).get_width() - 30, 70)
    movingbrickwall[1].setpos(WIDTH / 2 + bricks.getbrickwall(movingbrickwall[1]).get_width() - 18, 70)
    movingbrickwall[2].setpos(0, 430)
    movingbrickwall[3].setpos(WIDTH - movingbrickwall[3].width, 430)

    # LEVEL 1- UPPERBRICKWALL

    upperbrickwall[0].setpos(0, 150)
    for i in range(1, len(upperbrickwall)):
        distance = 120 / 9 + upperbrickwall[i].width
        upperbrickwall[i].x = upperbrickwall[i - 1].x + distance
        upperbrickwall[i].setpos(upperbrickwall[i].x, 150)

    # LEVEL 1- MIDBRICKWALL

    midbrickwall[0].setpos(32, 250)

    for i in range(1, len(midbrickwall)):
        distance = 48 + midbrickwall[i].width
        midbrickwall[i].x = midbrickwall[i - 1].x + distance
        midbrickwall[i].setpos(midbrickwall[i].x, 250)
    # LEVEL 1- LOWERBRICKWALL

    lowerbrickwall[0].setpos(0, 350)
    for i in range(1, len(lowerbrickwall)):
        distance = 120 / 9 + lowerbrickwall[i].width
        lowerbrickwall[i].x = lowerbrickwall[i - 1].x + distance
        lowerbrickwall[i].setpos(lowerbrickwall[i].x, 350)

    player.playermove(WIDTH, pressedKeys, 12)
    ball.automove(WIDTH, HEIGHT, 8, 8)

    getSpriteCollision(ball, player)
    for i in range(len(movingbrickwall)):
        if getSpriteCollision(ball, movingbrickwall[i]) == 1:
            movingbrickwall[i].setpos(0, -100)
    for i in range(len(upperbrickwall)):
        if getSpriteCollision(ball, upperbrickwall[i]) == 1:
            upperbrickwall[i].setpos(0, -100)
    for i in range(len(midbrickwall)):
        if getSpriteCollision(ball, midbrickwall[i]) == 1:
            midbrickwall[i].setpos(0, -100)
    for i in range(len(lowerbrickwall)):
        if getSpriteCollision(ball, lowerbrickwall[i]) == 1:
            lowerbrickwall[i].setpos(0, -100)

    screen.blit(brickbreakertext.getText(), brickbreakertext.getPos())
    screen.blit(player.getPlayer(), player.getPos())
    screen.blit(ball.getBall(), ball.getPos())

    movingbrickwall[0].brickmoveleft(WIDTH, 5)
    movingbrickwall[1].brickmoveright(WIDTH, 5)
    movingbrickwall[2].brickmoveleft(WIDTH, 5)
    movingbrickwall[3].brickmoveright(WIDTH, 5)
    for i in range(len(movingbrickwall)):
        screen.blit(movingbrickwall[i].getbrickwall(), movingbrickwall[i].getPos())
    for i in range(len(upperbrickwall)):
        screen.blit(upperbrickwall[i].getbrickwall(), upperbrickwall[i].getPos())
    for i in range(len(midbrickwall)):
        screen.blit(midbrickwall[i].getbrickwall(), midbrickwall[i].getPos())
    for i in range(len(lowerbrickwall)):
        screen.blit(lowerbrickwall[i].getbrickwall(), lowerbrickwall[i].getPos())


## LEVEL 1 BRICKS END HERE ##


## LEVEL 2 BRICKS START HERE ##

def level2():
    global level

    level = 2

    # brickbreaker TEXT
    brickbreakertext = text("BRICK BREAKER")
    brickbreakertext.setColor(WHITE)
    brickbreakertext.setpos(WIDTH / 2 - brickbreakertext.getText().get_width() / 2, 0)

    # player TILES
    player = Player(300, 550)
    player.setColor(WHITE)
    player.setpos(WIDTH / 2 - player.getPlayer().get_width() / 2, HEIGHT - 20)

    # ball
    ball = Ball(800, 500)
    ball.setColor(BLUE)
    ball.setpos(WIDTH / 2 - ball.getBall().get_width() / 2, HEIGHT - 40)

    # level2 brickwall
    lv2upperbrickwall = []
    lv2midbrickwall = []
    lv2lowerbrickwall = []
    lv2hiddenbrickwall = []

    for i in range(25):
        lv2upperbrickwall.append(bricks(100, 100))
        lv2upperbrickwall[i].setdim(100, 30)
        lv2upperbrickwall[i].setColor(WHITE)

    for i in range(25):
        lv2midbrickwall.append(bricks(100, 100))
        lv2midbrickwall[i].setdim(100, 30)
        lv2midbrickwall[i].setColor(WHITE)

    for i in range(25):
        lv2lowerbrickwall.append(bricks(100, 100))
        lv2lowerbrickwall[i].setdim(100, 30)
        lv2lowerbrickwall[i].setColor(WHITE)

    for i in range(100):
        lv2hiddenbrickwall.append(bricks(100, 100))
        lv2hiddenbrickwall[i].setdim(50, 15)
        lv2hiddenbrickwall[i].setColor(WHITE)

    # LEVEL 2- UPPERBRICKWALL

    lv2upperbrickwall[0].setpos(0, 50)
    for i in range(1, len(lv2upperbrickwall)):
        distance = 120 / 9 + lv2upperbrickwall[i].width
        lv2upperbrickwall[i].x = lv2upperbrickwall[i - 1].x + distance
        lv2upperbrickwall[i].setpos(lv2upperbrickwall[i].x, 50)

    lv2upperbrickwall[13].setpos(lv2upperbrickwall[0].width + lv2upperbrickwall[0].x - lv2upperbrickwall[13].width / 2,
                                 100)

    for i in range(14, len(lv2upperbrickwall)):
        distance = lv2upperbrickwall[1].x - lv2upperbrickwall[0].x - lv2upperbrickwall[0].width
        lv2upperbrickwall[i].x = lv2upperbrickwall[i - 1].x + lv2upperbrickwall[i - 1].width + distance
        lv2upperbrickwall[i].setpos(lv2upperbrickwall[i].x, 100)

    # LEVEL 2 - MIDBRICKWALL

    lv2midbrickwall[0].setpos(0, 150)
    for i in range(1, len(lv2midbrickwall)):
        distance = 120 / 9 + lv2midbrickwall[i].width
        lv2midbrickwall[i].x = lv2midbrickwall[i - 1].x + distance
        lv2midbrickwall[i].setpos(lv2midbrickwall[i].x, 150)

    lv2midbrickwall[13].setpos(lv2midbrickwall[0].width + lv2midbrickwall[0].x - lv2midbrickwall[13].width / 2, 200)
    for i in range(14, len(lv2midbrickwall)):
        distance = lv2midbrickwall[1].x - lv2midbrickwall[0].x - lv2midbrickwall[0].width
        lv2midbrickwall[i].x = lv2midbrickwall[i - 1].x + lv2midbrickwall[i - 1].width + distance
        lv2midbrickwall[i].setpos(lv2midbrickwall[i].x, 200)

    # LEVEL 2 - LOWERBRICKWALL

    lv2lowerbrickwall[0].setpos(0, 250)
    for i in range(1, len(lv2lowerbrickwall)):
        distance = 120 / 9 + lv2lowerbrickwall[i].width
        lv2lowerbrickwall[i].x = lv2lowerbrickwall[i - 1].x + distance
        lv2lowerbrickwall[i].setpos(lv2lowerbrickwall[i].x, 250)

    lv2lowerbrickwall[13].setpos(lv2lowerbrickwall[0].width + lv2lowerbrickwall[0].x - lv2lowerbrickwall[13].width / 2,
                                 300)
    for i in range(14, len(lv2lowerbrickwall)):
        distance = lv2lowerbrickwall[1].x - lv2lowerbrickwall[0].x - lv2lowerbrickwall[0].width
        lv2lowerbrickwall[i].x = lv2lowerbrickwall[i - 1].x + lv2lowerbrickwall[i - 1].width + distance
        lv2lowerbrickwall[i].setpos(lv2lowerbrickwall[i].x, 300)

    # LEVEL 2 - HIDDENBRICKWALL

    lv2hiddenbrickwall[0].setpos(lv2upperbrickwall[0].width / 4, lv2hiddenbrickwall[0].height / 4 + 150)
    for i in range(1, len(lv2hiddenbrickwall)):
        distance = lv2hiddenbrickwall[i].width + lv2upperbrickwall[0].width / 2 + 120 / 9
        lv2hiddenbrickwall[i].x = lv2hiddenbrickwall[i - 1].x + distance
        lv2hiddenbrickwall[i].setpos(lv2hiddenbrickwall[i].x, lv2hiddenbrickwall[0].height / 4 + 150)

    lv2hiddenbrickwall[13].setpos(lv2midbrickwall[0].width / 4, lv2hiddenbrickwall[0].height / 4 + 250)
    for i in range(14, len(lv2hiddenbrickwall)):
        distance = lv2hiddenbrickwall[i].width + lv2midbrickwall[0].width / 2 + 120 / 9
        lv2hiddenbrickwall[i].x = lv2hiddenbrickwall[i - 1].x + distance
        lv2hiddenbrickwall[i].setpos(lv2hiddenbrickwall[i].x, lv2hiddenbrickwall[0].height / 4 + 250)

    lv2hiddenbrickwall[26].setpos(lv2lowerbrickwall[0].width / 4, lv2hiddenbrickwall[0].height / 4 + 350)
    for i in range(27, len(lv2hiddenbrickwall)):
        distance = lv2hiddenbrickwall[i].width + lv2lowerbrickwall[0].width / 2 + 120 / 9
        lv2hiddenbrickwall[i].x = lv2hiddenbrickwall[i - 1].x + distance
        lv2hiddenbrickwall[i].setpos(lv2hiddenbrickwall[i].x, lv2hiddenbrickwall[0].height / 4 + 350)

    player.playermove(WIDTH, pressedKeys, 12)
    ball.automove(WIDTH, HEIGHT, 8, 8)

    for i in range(len(lv2hiddenbrickwall)):
        if getSpriteCollision(ball, lv2hiddenbrickwall[i]) == 1:
            lv2hiddenbrickwall[i].setpos(0, -100)
    for i in range(len(lv2upperbrickwall)):
        if getSpriteCollision(ball, lv2upperbrickwall[i]) == 1:
            lv2upperbrickwall[i].setpos(0, -100)
    for i in range(len(lv2midbrickwall)):
        if getSpriteCollision(ball, lv2midbrickwall[i]) == 1:
            lv2midbrickwall[i].setpos(0, -100)
    for i in range(len(lv2lowerbrickwall)):
        if getSpriteCollision(ball, lv2lowerbrickwall[i]) == 1:
            lv2lowerbrickwall[i].setpos(0, -100)

    screen.blit(brickbreakertext.getText(), brickbreakertext.getPos())
    screen.blit(player.getPlayer(), player.getPos())
    screen.blit(ball.getBall(), ball.getPos())

    for i in range(len(lv2upperbrickwall)):
        screen.blit(lv2upperbrickwall[i].getbrickwall(), lv2upperbrickwall[i].getPos())
    for i in range(len(lv2midbrickwall)):
        screen.blit(lv2midbrickwall[i].getbrickwall(), lv2midbrickwall[i].getPos())
    for i in range(len(lv2lowerbrickwall)):
        screen.blit(lv2lowerbrickwall[i].getbrickwall(), lv2lowerbrickwall[i].getPos())
    for i in range(len(lv2hiddenbrickwall)):
        screen.blit(lv2hiddenbrickwall[i].getbrickwall(), lv2hiddenbrickwall[i].getPos())


def endscreen():
    endscreen = text("YOU HAVE COMPLETED THE GAME!")
    endscreen.setColor(WHITE)
    endscreen.setpos(WIDTH / 2 - startscreen.getText().get_width() / 2,
                     HEIGHT / 2 - startscreen.getText().get_width() / 2)

    playagain = text("PLAY AGAIN?")
    playagain.setColor(WHITE)
    playagain.setpos(WIDTH / 2 - playagain.getText().get_width() / 2, 300)

    endchoice = text("Y --> YES | N --> NO")
    endchoice.setColor(WHITE)
    endchoice.setpos(WIDTH / 2 - endchoice.getText().get_width() / 2, 350)

    if pressedKeys[pygame.K_y]:
        running = True
    elif pressedKeys[pygame.K_n]:
        running = False

    screen.blit(endscreen.getText(), endscreen.getPos())
    screen.blit(playagain.getText(), playagain.getPos())
    screen.blit(endchoice.getText(), endchoice.getPos())


#### CODES START HERE ###

global level
level = 0

running = True

while running:

    for event in pygame.event.get():  # return all inputs and triggers into an array
        if event.type == pygame.QUIT:  # If the red X was clicked
            running = False

    pressedKeys = pygame.key.get_pressed()
    screen.fill(GREY)

    if level == 0:
        playercolor = startscreen()

    if level == 1:
        level1(playercolor)

    '''if level == 2:
        level2()
        
    if level == 3:
        endscreen()'''

    # LEVEL 1

    # LEVEL 2

    clock.tick(FPS)  # pause the game until FPS time is reached
    pygame.display.flip()

pygame.quit()
'''

'''
