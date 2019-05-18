'''
    Title: Desomnia ( Start Screen )
    Author: Long Tieu, Wayne Seto, Ethan
    Date:
'''

import pygame
pygame.init() # load the pygame module commands in the program

# Display variables
TITLE = 'Hello World' # Appear in the window title
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

# Create the window
screen = pygame.display.set_mode(SCREENDIM) # Create the main surface where all other assets are placed on top
pygame.display.set_caption(TITLE) # This updates the windows title
screen.fill(BLACK) # Fill the entire surface with the chosen color. Think of fill as erase.

clock = pygame.time.Clock()  # starts a clock object to measure time

### --- Codes starts here --- ###

dialoguebox = []
dialoguebox.append("media/dialogueSquare.png")
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

randomCreature = text(100, 20, "Random Creature: ", 20, "Arial", kindred)
anna = text(100, 20, "Anna: ", 30, "Arial", kindblue)

def dialogue0():
    rcdialogue1 = text(310, 20, "Lady! Help is needed over here!", 30, "Arial", WHITE)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(randomCreature.getText(), randomCreature.gettextpos())
    screen.blit(rcdialogue1.getText(), rcdialogue1.gettextpos())

def dialogue1():
    andialogue1 = text(170, 20, "You can talk !?", 30, "Arial", WHITE)
    andialogue1.textsetpos(170, 20)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(anna.getText(), anna.gettextpos())
    screen.blit(andialogue1.getText(), andialogue1.gettextpos())

def dialogue2():
    randomCreature.textsetpos(100, 20)
    randomCreature.textsetColor(kindred)
    rcdialogue2 = text(100, 100, "Creatures that can talk are not hostile as you think it is.", 30, "Arial")
    rcdialogue2.textsetpos(310, 20)
    rcdialogue2.textsetColor(WHITE)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(randomCreature.getText(), randomCreature.gettextpos())
    screen.blit(rcdialogue2.getText(), rcdialogue2.gettextpos())

running = True

dialogueLEVEL = 0
starttime = 0
endtime = 0

while running:
    for event in pygame.event.get(): # return all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked
            running = False

    endtime = pygame.time.get_ticks()

    pressedKeys = pygame.key.get_pressed()
    screen.fill(BLACK)

    print(dialogueLEVEL)

    if dialogueLEVEL == 0:
        dialogue0()
        if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
           starttime = pygame.time.get_ticks()
           dialogueLEVEL = 1
    if dialogueLEVEL == 1:
        dialogue1()
        if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
           starttime = pygame.time.get_ticks()
           dialogueLEVEL = 2
    if dialogueLEVEL == 2:
        dialogue2()


    clock.tick(FPS) # pause the game until FPS time is reached
    pygame.display.flip()


pygame.quit()