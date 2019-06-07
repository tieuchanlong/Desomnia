'''
    Title: Desomnia ( Start Screen )
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

    def setText(self, text):
        self.content = text
        self.surface = self.font.render(self.content, 1, self.color)

    def gettextpos(self):
        return self.pos

    def textsetColor(self, color):
        self.color = color
        self.surface = self.font.render(self.content, 1, self.color)

    def getText(self):
        return self.surface


### --- Codes starts here --- ###


minions = text(90, 30, "Hostile Creature: ", 30, "Renogare", hostilered)

def dialogue0():
    rcdialogue1 = text(100, 70, "Lady! Help is needed over here!", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - rcdialogue1.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - rcdialogue1.getText().get_height() / 2
    rcdialogue1.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(rcdialogue1.getText(), rcdialogue1.gettextpos())

def dialogue1():
    andialogue1 = text(410, 70, "You can talk !?", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - andialogue1.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - andialogue1.getText().get_height() / 2
    andialogue1.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(andialogue1.getText(), andialogue1.gettextpos())

def dialogue2():
    rcdialogue2 = text(320, 60, "Creatures that can talk are not hostile", 30, "Renogare" , WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - rcdialogue2.getText().get_width() / 2
    y = dialogueboxload.get_height() / 2 - rcdialogue2.getText().get_height() / 2
    rcdialogue2.textsetpos(x, y)

    rcdialogue2a = text(420, 85, "as you think it is.", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - rcdialogue2a.getText().get_width() / 2
    y = 23 + dialogueboxload.get_height() / 2 - rcdialogue2a.getText().get_height() / 2
    rcdialogue2a.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(rcdialogue2.getText(), rcdialogue2.gettextpos())
    screen.blit(rcdialogue2a.getText(), rcdialogue2a.gettextpos())

def dialogue3():
    andialogue2 = text(320, 70, "So why are you different than others?", 30, "Renogare" , WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - andialogue2.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - andialogue2.getText().get_height() / 2
    andialogue2.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(andialogue2.getText(), andialogue2.gettextpos())

def dialogue4():
    rcdialogue3 = text(360, 60, "I will explain later if you bring", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - rcdialogue3.getText().get_width() / 2
    y = dialogueboxload.get_height() / 2 - rcdialogue3.getText().get_height() / 2
    rcdialogue3.textsetpos(x, y)

    rcdialogue3a = text(420, 85, "me the fruit basket.", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - rcdialogue3a.getText().get_width() / 2
    y = 23 + dialogueboxload.get_height() / 2 - rcdialogue3a.getText().get_height() / 2
    rcdialogue3a.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(rcdialogue3.getText(), rcdialogue3.gettextpos())
    screen.blit(rcdialogue3a.getText(), rcdialogue3a.gettextpos())

### after returning ###

def dialogue5():
    rcdialogue4 = text(350, 30, "Thank lord! You are a savior!", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - rcdialogue4.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - rcdialogue4.getText().get_height() / 2
    rcdialogue4.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(rcdialogue4.getText(), rcdialogue4.gettextpos())

def dialogue6():
    andialogue3 = text(400, 30, "Who exactly are you?", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - andialogue3.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - andialogue3.getText().get_height() / 2
    andialogue3.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(andialogue3.getText(), andialogue3.gettextpos())

def dialogue7():
    rcdialogue5 = text(350, 30, "The truth is I don't even know...", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - rcdialogue5.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - rcdialogue5.getText().get_height() / 2
    rcdialogue5.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(rcdialogue5.getText(), rcdialogue5.gettextpos())

def dialogue8():
    andialogue4 = text(400, 30, "Strange...because you seems familiar to me...", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - andialogue4.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - andialogue4.getText().get_height() / 2
    andialogue4.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(andialogue4.getText(), andialogue4.gettextpos())

def dialogue9():
    rcdialogue6 = text(350, 30, "You need a key to open the gate of desomnia.", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - rcdialogue6.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - rcdialogue6.getText().get_height() / 2
    rcdialogue6.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(rcdialogue6.getText(), rcdialogue6.gettextpos())

def dialogue10():
    nodi1 = text(350, 30, "(The creature handed you the key)", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - nodi1.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - nodi1.getText().get_height() / 2
    nodi1.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(nodi1.getText(), nodi1.gettextpos())

### Done Section ###

def dialogue11():
    andialogue5 = text(400, 30, "What's happening over there!", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - andialogue5.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - andialogue5.getText().get_height() / 2
    andialogue5.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(andialogue5.getText(), andialogue5.gettextpos())

def dialogue12():
    unk1 = text(350, 30, "(A loud screeching sound)", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - unk1.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - unk1.getText().get_height() / 2
    unk1.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(unk1.getText(), unk1.gettextpos())

def dialogue13():
    andialogue6 = text(400, 30, "The poor soul is getting attacked!", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - andialogue6.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - andialogue6.getText().get_height() / 2
    andialogue6.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(andialogue6.getText(), andialogue6.gettextpos())

def dialogue14():
    andialogue7 = text(400, 30, "I need to help him!", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - andialogue7.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - andialogue7.getText().get_height() / 2
    andialogue7.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(andialogue7.getText(), andialogue7.gettextpos())

### After the fight

def dialogue15():
    andialogue8 = text(400, 30, "Are you fine?", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - andialogue8.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - andialogue8.getText().get_height() / 2
    andialogue8.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(andialogue8.getText(), andialogue8.gettextpos())

def dialogue16():
    unk2 = text(350, 30, "(A painful hum)", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - unk2.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - unk2.getText().get_height() / 2
    unk2.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(unk2.getText(), unk2.gettextpos())

def dialogue17():
    andialogue9 = text(400, 30, "What should I do...", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - andialogue9.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - andialogue9.getText().get_height() / 2
    andialogue9.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(andialogue9.getText(), andialogue9.gettextpos())

def dialogue18():
    nodi2 = text(350, 30, "(The creature picked up a flower)", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - nodi2.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - nodi2.getText().get_height() / 2
    nodi2.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(nodi2.getText(), nodi2.gettextpos())

def dialogue19():
    andialogue10 = text(400, 30, "That's right! The flower of Luffia", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - andialogue10.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - andialogue10.getText().get_height() / 2
    andialogue10.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(andialogue10.getText(), andialogue10.gettextpos())

def dialogue20():
    andialogue11 = text(400, 30, "Hold on, I will be back with those flowers", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - andialogue11.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - andialogue11.getText().get_height() / 2
    andialogue11.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(andialogue11.getText(), andialogue11.gettextpos())

def dialogue21():
    unk3 = text(350, 30, "(A cheerful hum)", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - unk3.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - unk3.getText().get_height() / 2
    unk3.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(unk3.getText(), unk3.gettextpos())

def dialogue22():
    nodi3 = text(350, 30, "(The creature handed you a piece of drawing)", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - nodi3.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - nodi3.getText().get_height() / 2
    nodi3.textsetpos(x, y)

    screen.blit(dialogueboxload, (50, 10))
    screen.blit(nodi3.getText(), nodi3.gettextpos())

def dialogue23():
    nodi3 = text(350, 30, "Creature: Umu...", 30, "Renogare", WHITE)
    x = 50 + dialogueboxload.get_width() / 2 - nodi3.getText().get_width() / 2
    y = 10 + dialogueboxload.get_height() / 2 - nodi3.getText().get_height() / 2
    nodi3.textsetpos(x, y)


    screen.blit(dialogueboxload, (50, 10))
    screen.blit(nodi3.getText(), nodi3.gettextpos())

def pause_screen():
    global pauselevel

    ps1 = text(100, 100, "Resume", 35, "Renogare", WHITE)
    x = WIDTH / 2 - ps1.getText().get_width() / 2
    y =  HEIGHT / 2 - ps1.getText().get_height() / 2 - 50
    ps1.textsetpos(x, y)

    ps2 = text(100, 100, "Key Binds", 35, "Renogare", WHITE)
    x = WIDTH / 2 - ps2.getText().get_width() / 2
    y =  HEIGHT / 2 - ps2.getText().get_height() / 2 + 20
    ps2.textsetpos(x, y)

    ps3 = text(100, 100, "Exit", 35, "Renogare", WHITE)
    x = WIDTH / 2 - ps3.getText().get_width() / 2
    y = HEIGHT / 2 - ps3.getText().get_height() / 2 + 90
    ps3.textsetpos(x, y)

    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:
            mx, my = pygame.mouse.get_pos()
            if mx > ps1.x and mx < ps1.x + ps1.getText().get_width() and my > ps1.y and my < ps1.y + ps1.getText().get_height(): # resume
                pauselevel = 0
                return pauselevel
            elif mx > ps2.x and mx < ps2.x + ps2.getText().get_width() and my > ps2.y and my < ps2.y + ps2.getText().get_height():
                pauselevel = 2 # key binds screen
                return pauselevel
            elif mx > ps3.x and mx < ps3.x + ps3.getText().get_width() and my > ps3.y and my < ps3.y + ps3.getText().get_height():
                pauselevel = 3 # exit
                return pauselevel

    screen.blit(ps1.getText(), ps1.gettextpos())
    screen.blit(ps2.getText(), ps2.gettextpos())
    screen.blit(ps3.getText(), ps3.gettextpos())

def keybinds_screen():
    global pauselevel

    kb1 = text(100, 100, "| W | ------> MOVE FORWARD", 25, "Renogare", WHITE)
    x = WIDTH / 2 - kb1.getText().get_width() / 2
    y = HEIGHT / 2 - kb1.getText().get_height() / 2 - 200
    kb1.textsetpos(x, y)

    kb2 = text(100, 100, "| A | ------> MOVE LEFT", 25, "Renogare", WHITE)
    x = WIDTH / 2 - kb2.getText().get_width() / 2
    y = HEIGHT / 2 - kb2.getText().get_height() / 2 - 150
    kb2.textsetpos(x, y)

    kb3 = text(100, 100, "| S | ------> MOVE BACKWARD", 25, "Renogare", WHITE)
    x = WIDTH / 2 - kb3.getText().get_width() / 2
    y = HEIGHT / 2 - kb3.getText().get_height() / 2 - 100
    kb3.textsetpos(x, y)

    kb4 = text(100, 100, "| D | ------> MOVE RIGHT", 25, "Renogare", WHITE)
    x = WIDTH / 2 - kb4.getText().get_width() / 2
    y = HEIGHT / 2 - kb4.getText().get_height() / 2 - 50
    kb4.textsetpos(x, y)

    kb5 = text(100, 100, "| SPACE | ------> JUMP", 25, "Renogare", WHITE)
    x = WIDTH / 2 - kb5.getText().get_width() / 2
    y = HEIGHT / 2 - kb5.getText().get_height() / 2
    kb5.textsetpos(x, y)

    kb6 = text(100, 100, "| MOUSE LEFT-MOVE | ------> ATTACK" , 25, "Renogare", WHITE)
    x = WIDTH / 2 - kb6.getText().get_width() / 2
    y = HEIGHT / 2 - kb6.getText().get_height() / 2 + 50
    kb6.textsetpos(x, y)

    kb7 = text(100, 100, "| MOUSE RIGHT-MOVE | ------> SPECIAL ATTACK", 25, "Renogare", WHITE)
    x = WIDTH / 2 - kb7.getText().get_width() / 2
    y = HEIGHT / 2 - kb7.getText().get_height() / 2 + 100
    kb7.textsetpos(x, y)

    returnscreen = text(100, 100, "CLICK HERE TO RETURN TO PAUSE SCREEN", 25, "Renogare", WHITE)
    x = WIDTH / 2 - returnscreen.getText().get_width() / 2
    y = HEIGHT / 2 - returnscreen.getText().get_height() / 2 + 200
    returnscreen.textsetpos(x, y)

    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:
        mx, my = pygame.mouse.get_pos()
        if mx > returnscreen.x and mx < returnscreen.x + returnscreen.getText().get_width() and my > returnscreen.y and my < returnscreen.y + returnscreen.getText().get_height():  # resume
            pauselevel = 1
            return pauselevel

    screen.blit(kb1.getText(), kb1.gettextpos())
    screen.blit(kb2.getText(), kb2.gettextpos())
    screen.blit(kb3.getText(), kb3.gettextpos())
    screen.blit(kb4.getText(), kb4.gettextpos())
    screen.blit(kb5.getText(), kb5.gettextpos())
    screen.blit(kb6.getText(), kb6.gettextpos())
    screen.blit(kb7.getText(), kb7.gettextpos())
    screen.blit(returnscreen.getText(), returnscreen.gettextpos())

running = True

dialogueLEVEL = 0
pauselevel = 0
starttime = 0
endtime = 0

while running:
    for event in pygame.event.get(): # return all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked
            running = False

    endtime = pygame.time.get_ticks()

    pressedKeys = pygame.key.get_pressed()
    screen.fill(BLACK)

    if pressedKeys[pygame.K_TAB]:
        pauselevel = 1
    if pauselevel == 1:
        pause_screen()
    if pauselevel == 2:
        keybinds_screen()
    if pauselevel == 3:
        exit()

    if pauselevel == 0:
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
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 3
        if dialogueLEVEL == 3:
            dialogue3()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 4
        if dialogueLEVEL == 4:
            dialogue4()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 5
        ###### after returning #####
        if dialogueLEVEL == 5:
            dialogue5()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 6
        if dialogueLEVEL == 6:
            dialogue6()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 7
        if dialogueLEVEL == 7:
            dialogue7()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 8
        if dialogueLEVEL == 8:
            dialogue8()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 9
        #### done section ###
        if dialogueLEVEL == 9:
            dialogue9()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 10
        if dialogueLEVEL == 10:
            dialogue10()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 11
        if dialogueLEVEL == 11:
            dialogue11()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 12
        if dialogueLEVEL == 12:
            dialogue12()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 13
        if dialogueLEVEL == 13:
            dialogue13()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 14
        if dialogueLEVEL == 14:
            dialogue14()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 15
        if dialogueLEVEL == 15:
            dialogue15()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 16
        if dialogueLEVEL == 16:
            dialogue16()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 17
        if dialogueLEVEL == 17:
            dialogue17()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 18
        if dialogueLEVEL == 18:
            dialogue18()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 19
        if dialogueLEVEL == 19:
            dialogue19()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 20
        if dialogueLEVEL == 20:
            dialogue20()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 21
        if dialogueLEVEL == 21:
            dialogue21()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 22
        if dialogueLEVEL == 22:
            dialogue22()
            if pressedKeys[pygame.K_1] and endtime - starttime > 1000:
               starttime = pygame.time.get_ticks()
               dialogueLEVEL = 23



    clock.tick(FPS) # pause the game until FPS time is reached
    pygame.display.flip()


pygame.quit()