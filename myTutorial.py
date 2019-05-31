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

lowopasheet = []
lowopasheet.append("media/dialoguebox01.png")
lowopasheetload = (pygame.image.load(lowopasheet[0]).convert_alpha())

dialoguebox = []
dialoguebox.append("media/dialoguebox01.png")
dialogueboxload = (pygame.image.load(dialoguebox[0]).convert_alpha())

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

def tutorialmove():
    tit01 = text(100, 70, "MOVEMENT TUTORIAL", 50, "Renogare", WHITE)
    x = WIDTH / 2 - tit01.getText().get_width() / 2
    y = HEIGHT / 2 - tit01.getText().get_height() / 2 - 200
    tit01.textsetpos(x, y)

    tut01 = text(100, 70, "Press [ D ] to move LEFT", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut01.getText().get_width() / 2
    y = HEIGHT / 2 - tut01.getText().get_height() / 2 - 150
    tut01.textsetpos(x, y)

    tut02 = text(100, 70, "Press [ A ] to move RIGHT", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut02.getText().get_width() / 2
    y = HEIGHT / 2 - tut02.getText().get_height() / 2 - 100
    tut02.textsetpos(x, y)

    tut03 = text(100, 70, "Press [ W ] to move FORWARD", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut03.getText().get_width() / 2
    y = HEIGHT / 2 - tut03.getText().get_height() / 2 - 50
    tut03.textsetpos(x, y)

    tut04 = text(100, 70, "Press [ S ] to move BACKWARD", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut04.getText().get_width() / 2
    y = HEIGHT / 2 - tut04.getText().get_height() / 2 + 0
    tut04.textsetpos(x, y)

    tut05 = text(100, 70, "Press [ SPACE ] to JUMP", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut05.getText().get_width() / 2
    y = HEIGHT / 2 - tut05.getText().get_height() / 2 + 50
    tut05.textsetpos(x, y)

    exit01 = text(100, 70, "Press [ ESC ] to EXIT INTERACTION PAGE", 35, "Renogare", WHITE)
    x = WIDTH / 2 - exit01.getText().get_width() / 2
    y = HEIGHT / 2 - exit01.getText().get_height() / 2 + 200
    exit01.textsetpos(x, y)

    screen.blit(tit01.getText(), tit01.gettextpos())
    screen.blit(tut01.getText(), tut01.gettextpos())
    screen.blit(tut02.getText(), tut02.gettextpos())
    screen.blit(tut03.getText(), tut03.gettextpos())
    screen.blit(tut04.getText(), tut04.gettextpos())
    screen.blit(tut05.getText(), tut05.gettextpos())
    screen.blit(exit01.getText(), exit01.gettextpos())

def tutorialatt():

    tit2 = text(100, 70, "ATTACK TUTORIAL", 50, "Renogare", WHITE)
    x = WIDTH / 2 - tit2.getText().get_width() / 2
    y = HEIGHT / 2 - tit2.getText().get_height() / 2 - 200
    tit2.textsetpos(x, y)

    tut06 = text(100, 70, "Press [ MOUSE LEFT-CLICK ] to ATTACK", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut06.getText().get_width() / 2
    y = HEIGHT / 2 - tut06.getText().get_height() / 2 - 100
    tut06.textsetpos(x, y)

    tut07 = text(100, 70, "The first click always shoot in a respectable distance ", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut07.getText().get_width() / 2
    y = HEIGHT / 2 - tut07.getText().get_height() / 2 - 50
    tut07.textsetpos(x, y)

    tut08 = text(100, 70, "The second click allows it to shoot even further", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut08.getText().get_width() / 2
    y = HEIGHT / 2 - tut08.getText().get_height() / 2
    tut08.textsetpos(x, y)

    tut09 = text(100, 70, "The third click aka combo can lob [something] ", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut09.getText().get_width() / 2
    y = HEIGHT / 2 - tut09.getText().get_height() / 2 + 50
    tut09.textsetpos(x, y)

    exit02 = text(100, 70, "Press [ ESC ] to EXIT INTERACTION PAGE", 35, "Renogare", WHITE)
    x = WIDTH / 2 - exit02.getText().get_width() / 2
    y = HEIGHT / 2 - exit02.getText().get_height() / 2 + 200
    exit02.textsetpos(x, y)

    screen.blit(tit2.getText(), tit2.gettextpos())
    screen.blit(tut06.getText(), tut06.gettextpos())
    screen.blit(tut07.getText(), tut07.gettextpos())
    screen.blit(tut08.getText(), tut08.gettextpos())
    screen.blit(tut09.getText(), tut09.gettextpos())
    screen.blit(exit02.getText(), exit02.gettextpos())

def tutorialspeatt():

    tit3 = text(100, 70, "SPECIAL ATTACK TUTORIAL", 50, "Renogare", WHITE)
    x = WIDTH / 2 - tit3.getText().get_width() / 2
    y = HEIGHT / 2 - tit3.getText().get_height() / 2 - 200
    tit3.textsetpos(x, y)

    tut10 = text(100, 70, "Press [ MOUSE RIGHT-CLICK ] to initial special attack", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut10.getText().get_width() / 2
    y = HEIGHT / 2 - tut10.getText().get_height() / 2 - 100
    tut10.textsetpos(x, y)

    tut11 = text(100, 70, "It is considered as the ultimate ", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut11.getText().get_width() / 2
    y = HEIGHT / 2 - tut11.getText().get_height() / 2 - 50
    tut11.textsetpos(x, y)

    tut12 = text(100, 70, "It will use up all the paintnergy", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut12.getText().get_width() / 2
    y = HEIGHT / 2 - tut12.getText().get_height() / 2
    tut12.textsetpos(x, y)

    tut13 = text(100, 70, "The third click aka combo can lob [something] ", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut13.getText().get_width() / 2
    y = HEIGHT / 2 - tut13.getText().get_height() / 2 + 50
    tut13.textsetpos(x, y)

    exit01 = text(100, 70, "Press [ ESC ] to EXIT INTERACTION PAGE", 35, "Renogare", WHITE)
    x = WIDTH / 2 - exit01.getText().get_width() / 2
    y = HEIGHT / 2 - exit01.getText().get_height() / 2 + 200
    exit01.textsetpos(x, y)

    screen.blit(tit3.getText(), tit3.gettextpos())
    screen.blit(tut10.getText(), tut10.gettextpos())
    screen.blit(tut11.getText(), tut11.gettextpos())
    screen.blit(tut12.getText(), tut12.gettextpos())
    screen.blit(tut13.getText(), tut13.gettextpos())
    screen.blit(exit01.getText(), exit01.gettextpos())

def tutorialtech():

    tit4 = text(100, 70, "TECHNICAL TUTORIAL", 50, "Renogare", WHITE)
    x = WIDTH / 2 - tit4.getText().get_width() / 2
    y = HEIGHT / 2 - tit4.getText().get_height() / 2 - 200
    tit4.textsetpos(x, y)

    tut14 = text(100, 70, "Press [ TAB ] to PAUSE", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut14.getText().get_width() / 2
    y = HEIGHT / 2 - tut14.getText().get_height() / 2 - 100
    tut14.textsetpos(x, y)

    tut15 = text(100, 70, "It is recommended to take a break", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut15.getText().get_width() / 2
    y = HEIGHT / 2 - tut15.getText().get_height() / 2 - 50
    tut15.textsetpos(x, y)

    tut16 = text(100, 70, "after two - one hours of playing", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut16.getText().get_width() / 2
    y = HEIGHT / 2 - tut16.getText().get_height() / 2
    tut16.textsetpos(x, y)

    tut17 = text(100, 70, "The third click aka combo can lob [something] ", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut17.getText().get_width() / 2
    y = HEIGHT / 2 - tut17.getText().get_height() / 2 + 50
    tut17.textsetpos(x, y)

    exit01 = text(100, 70, "Press [ ESC ] to EXIT INTERACTION PAGE", 35, "Renogare", WHITE)
    x = WIDTH / 2 - exit01.getText().get_width() / 2
    y = HEIGHT / 2 - exit01.getText().get_height() / 2 + 200
    exit01.textsetpos(x, y)

    screen.blit(tit4.getText(), tit4.gettextpos())
    screen.blit(tut14.getText(), tut14.gettextpos())
    screen.blit(tut15.getText(), tut15.gettextpos())
    screen.blit(tut16.getText(), tut16.gettextpos())
    screen.blit(tut17.getText(), tut17.gettextpos())
    screen.blit(exit01.getText(), exit01.gettextpos())

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

    endtime = pygame.time.get_ticks()

    print(tutoriallevel)

    if tutoriallevel == 0:
        if pressedKeys[pygame.K_e] and endtime - starttime > 1000:
            starttime = pygame.time.get_ticks()
            tutoriallevel = 1 # switch different tutorial

    if tutoriallevel == 1:
        tutorialmove()
        if pressedKeys[pygame.K_ESCAPE] and endtime - starttime > 1000:
            starttime = pygame.time.get_ticks()
            tutoriallevel = 0

    if tutoriallevel == 2:
        tutorialatt()
        if pressedKeys[pygame.K_ESCAPE] and endtime - starttime > 1000:
            starttime = pygame.time.get_ticks()
            tutoriallevel = 0

    if tutoriallevel == 3:
        tutorialspeatt()
        if pressedKeys[pygame.K_ESCAPE] and endtime - starttime > 1000:
            starttime = pygame.time.get_ticks()
            tutoriallevel = 0

    if tutoriallevel == 4:
        tutorialtech()
        if pressedKeys[pygame.K_ESCAPE] and endtime - starttime > 1000:
            starttime = pygame.time.get_ticks()
            tutoriallevel = 0


    clock.tick(FPS) # pause the game until FPS time is reached
    pygame.display.flip()


pygame.quit()