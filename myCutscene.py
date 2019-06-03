'''
    Title: Desomnia ( Tutorial Screen )
    Author: Long Tieu, Wayne Seto, Ethan
    Date:
'''

import pygame
pygame.init() # load the pygame module commands in the program

# Display variables
TITLE = 'DESOMNIA' # Appear in the window title
FPS = 30 # Frames per second
WIDTH = 900
HEIGHT = 500
SCREENDIM = (WIDTH, HEIGHT)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Color variables
cs = (64, 64, 64)
cs0 = (95.5, 95.5, 95.5)
cs1 = (127, 127, 127)
cs2 = (159, 159, 159)
cs3 = (191, 191, 191)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
kindred = (205,92,92)
kindblue = (132,112,255)
hostilered = (255, 0, 0)

###

# Create the window
screen = pygame.display.set_mode(SCREENDIM) # Create the main surface where all other assets are placed on top
pygame.display.set_caption(TITLE) # This updates the windows title
screen.fill(BLACK) # Fill the entire surface with the chosen color. Think of fill as erase.

clock = pygame.time.Clock()  # starts a clock object to measure time

### --- Codes starts here --- ###

class text():
    def __init__(self, x, y, content, fontsize, font="Arial", color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.red = 0
        self.green = 0
        self.blue = 0
        self.color = color
        self.content = content
        self.fontfam = font
        self.fontsize = fontsize
        self.font = pygame.font.SysFont(self.fontfam, self.fontsize)
        self.surface = self.font.render(self.content, 1, self.color)

    def textsetpos(self, x, y):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)

    def gettextpos(self):
        return self.pos

    def textsetColor(self, color):
        self.color = color
        self.surface = self.font.render(self.content, 1, self.color)

    def getText(self):
        return self.surface

### --- Codes starts here --- ###

def cutscene01():

    text01 = text(100, 70, '"In a Wonderland they lie, Dreaming as the days go by,', 28, "Renogare", BLACK)
    x = WIDTH / 2 - text01.getText().get_width() / 2
    y = HEIGHT / 2 - text01.getText().get_height() / 2 -200
    text01.textsetpos(x, y)
    start_ticks = pygame.time.get_ticks()

    if start_ticks/1000 > 1.1:
        text01.textsetColor(cs)
    if start_ticks/1000 > 1.25:
        text01.textsetColor(cs0)
    if start_ticks/1000 > 1.4:
        text01.textsetColor(cs1)
    if start_ticks/1000 > 1.55:
        text01.textsetColor(cs2)
    if start_ticks/1000 > 1.7:
        text01.textsetColor(cs3)
    if start_ticks/1000 > 1.85:
        text01.textsetColor(WHITE)

    if start_ticks / 1000 > 25.1:
        text01.textsetColor(cs3)
    if start_ticks / 1000 > 25.25:
        text01.textsetColor(cs2)
    if start_ticks / 1000 > 25.4:
        text01.textsetColor(cs1)
    if start_ticks / 1000 > 25.55:
        text01.textsetColor(cs0)
    if start_ticks / 1000 > 25.7:
        text01.textsetColor(cs)
    if start_ticks / 1000 > 25.85:
        text01.textsetColor(BLACK)

    screen.blit(text01.getText(), text01.gettextpos())


def cutscene02():

    text02 = text(100, 70, 'Dreaming as the summers die,', 28, "Renogare", BLACK)
    x = WIDTH / 2 - text02.getText().get_width() / 2
    y = HEIGHT / 2 - text02.getText().get_height() / 2 - 150
    text02.textsetpos(x, y)
    start_ticks = pygame.time.get_ticks()

    if start_ticks / 1000 > 5.1:
        text02.textsetColor(cs)
    if start_ticks / 1000 > 5.25:
        text02.textsetColor(cs0)
    if start_ticks / 1000 > 5.4:
        text02.textsetColor(cs1)
    if start_ticks / 1000 > 5.55:
        text02.textsetColor(cs2)
    if start_ticks / 1000 > 5.7:
        text02.textsetColor(cs3)
    if start_ticks / 1000 > 5.85:
        text02.textsetColor(WHITE)

    if start_ticks / 1000 > 25.1:
        text02.textsetColor(cs3)
    if start_ticks / 1000 > 25.25:
        text02.textsetColor(cs2)
    if start_ticks / 1000 > 25.4:
        text02.textsetColor(cs1)
    if start_ticks / 1000 > 25.55:
        text02.textsetColor(cs0)
    if start_ticks / 1000 > 25.7:
        text02.textsetColor(cs)
    if start_ticks / 1000 > 25.85:
        text02.textsetColor(BLACK)


    screen.blit(text02.getText(), text02.gettextpos())

def cutscene03():

    text03 = text(100, 70, 'Ever drifting down the stream, Lingering in the golden gleam, ', 28, "Renogare", BLACK)
    x = WIDTH / 2 - text03.getText().get_width() / 2
    y = HEIGHT / 2 - text03.getText().get_height() / 2 - 100
    text03.textsetpos(x, y)
    start_ticks = pygame.time.get_ticks()

    if start_ticks / 1000 > 9.1:
        text03.textsetColor(cs)
    if start_ticks / 1000 > 9.25:
        text03.textsetColor(cs0)
    if start_ticks / 1000 > 9.4:
        text03.textsetColor(cs1)
    if start_ticks / 1000 > 9.55:
        text03.textsetColor(cs2)
    if start_ticks / 1000 > 9.7:
        text03.textsetColor(cs3)
    if start_ticks / 1000 > 9.85:
        text03.textsetColor(WHITE)

    if start_ticks / 1000 > 25.1:
        text03.textsetColor(cs3)
    if start_ticks / 1000 > 25.25:
        text03.textsetColor(cs2)
    if start_ticks / 1000 > 25.4:
        text03.textsetColor(cs1)
    if start_ticks / 1000 > 25.55:
        text03.textsetColor(cs0)
    if start_ticks / 1000 > 25.7:
        text03.textsetColor(cs)
    if start_ticks / 1000 > 25.85:
        text03.textsetColor(BLACK)

    screen.blit(text03.getText(), text03.gettextpos())

def cutscene04():

    text04 = text(100, 70, 'Life, what is it but a dream?"', 28, "Renogare", BLACK)
    x = WIDTH / 2 - text04.getText().get_width() / 2
    y = HEIGHT / 2 - text04.getText().get_height() / 2 - 50
    text04.textsetpos(x, y)

    start_ticks = pygame.time.get_ticks()

    if start_ticks / 1000 > 14.1:
        text04.textsetColor(cs)
    if start_ticks / 1000 > 14.25:
        text04.textsetColor(cs0)
    if start_ticks / 1000 > 14.4:
        text04.textsetColor(cs1)
    if start_ticks / 1000 > 14.55:
        text04.textsetColor(cs2)
    if start_ticks / 1000 > 14.7:
        text04.textsetColor(cs3)
    if start_ticks / 1000 > 14.85:
        text04.textsetColor(WHITE)

    if start_ticks / 1000 > 25.1:
        text04.textsetColor(cs3)
    if start_ticks / 1000 > 25.25:
        text04.textsetColor(cs2)
    if start_ticks / 1000 > 25.4:
        text04.textsetColor(cs1)
    if start_ticks / 1000 > 25.55:
        text04.textsetColor(cs0)
    if start_ticks / 1000 > 25.7:
        text04.textsetColor(cs)
    if start_ticks / 1000 > 25.85:
        text04.textsetColor(BLACK)

    screen.blit(text04.getText(), text04.gettextpos())

def cutscene05():

    text05 = text(100, 70, '-Lewis Carroll, Through the Looking Glass', 26, "Renogare", BLACK)
    x = WIDTH / 2 - text05.getText().get_width() / 2
    y = HEIGHT / 2 - text05.getText().get_height() / 2 + 175
    text05.textsetpos(x, y)

    start_ticks = pygame.time.get_ticks()

    if start_ticks / 1000 > 19.1:
        text05.textsetColor(cs)
    if start_ticks / 1000 > 19.25:
        text05.textsetColor(cs0)
    if start_ticks / 1000 > 19.4:
        text05.textsetColor(cs1)
    if start_ticks / 1000 > 19.55:
        text05.textsetColor(cs2)
    if start_ticks / 1000 > 19.7:
        text05.textsetColor(cs3)
    if start_ticks / 1000 > 19.85:
        text05.textsetColor(WHITE)

    if start_ticks / 1000 > 25.1:
        text05.textsetColor(cs3)
    if start_ticks / 1000 > 25.25:
        text05.textsetColor(cs2)
    if start_ticks / 1000 > 25.4:
        text05.textsetColor(cs1)
    if start_ticks / 1000 > 25.55:
        text05.textsetColor(cs0)
    if start_ticks / 1000 > 25.7:
        text05.textsetColor(cs)
    if start_ticks / 1000 > 25.85:
        text05.textsetColor(BLACK)

    screen.blit(text05.getText(), text05.gettextpos())

#Lewis Carroll, Through the Looking Glass


running = True

tutoriallevel = 0
starttime = 0
endtime = 0

while running:
    for event in pygame.event.get(): # return all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked
            running = False

    pressedKeys = pygame.key.get_pressed()
    screen.fill(BLACK)


    cutscene01()
    cutscene02()
    cutscene03()
    cutscene04()
    cutscene05()




    clock.tick(FPS) # pause the game until FPS time is reached
    pygame.display.flip()


pygame.quit()