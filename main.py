'''
    Title: Desomnia
    Author: Long Tieu, Wayne Seto, Ethan
    Date:
'''


import pygame
from myCharacter import *
from myBackground import *
from mySection import *
from myObject import *
pygame.init() # load the pygame module commands in the program

# Display variables
TITLE = 'Hello World' # Appear in the window title
FPS = 30 # Frames per second
WIDTH = 900
HEIGHT = 500
SCREENDIM = (WIDTH, HEIGHT)

# Color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)

# Create the window
screen = pygame.display.set_mode(SCREENDIM) # Create the main surface where all other assets are placed on top
pygame.display.set_caption(TITLE) # This updates the windows title
screen.fill(BLACK) # Fill the entire surface with the chosen color. Think of fill as erase.

clock = pygame.time.Clock()  # starts a clock object to measure time

global section_area
section_area = 6

def section_gameplay(section2):
    global startbackground_x
    global startbackground_y
    if (Anna.x + Anna.width / 2 > startscrolling_x):
        startbackground_x += Anna.x + Anna.width / 2 - startscrolling_x
        if (startbackground_x < bg_pos[len(bg) - 1][0] + bg[len(bg) - 1].get_width()):
            section2.move_x(-(Anna.x + Anna.width / 2 - startscrolling_x))
            Anna.setPos(startscrolling_x - Anna.width / 2, Anna.y)
        else:
            startbackground_x = bg_pos[len(bg) - 1][0] + bg[len(bg) - 1].get_width()

    if (Anna.x + Anna.width / 2 < startscrolling_x):
        startbackground_x -= startscrolling_x - Anna.x - Anna.width / 2
        if (startbackground_x > 0):
            section2.move_x(startscrolling_x - Anna.x - Anna.width / 2)
            Anna.setPos(startscrolling_x - Anna.width / 2, Anna.y)
        else:
            startbackground_x = 0

    if (Anna.y + Anna.height / 2 > startscrolling_y):
        startbackground_y += Anna.y + Anna.height / 2 - startscrolling_y
        if (startbackground_y < bg_pos[len(bg) - 1][1] + bg[len(bg) - 1].get_height()):
            section2.move_y(-(Anna.y + Anna.height / 2 - startscrolling_y))
            Anna.setPos(Anna.x, startscrolling_y - Anna.height / 2)
        else:
            startbackground_y = bg_pos[len(bg) - 1][1] + bg[len(bg) - 1].get_height()

    if (Anna.y + Anna.height / 2 < startscrolling_y):
        startbackground_y -= startscrolling_y - Anna.y - Anna.height / 2
        if (startbackground_y > 0):
            section2.move_y(startscrolling_y - Anna.y - Anna.height / 2)
            Anna.setPos(Anna.x, startscrolling_y - Anna.height / 2)
        else:
            startbackground_y = 0

    Anna.player_climb(pressedKey, section2.stairs)

    Anna.player_pickup(pressedKey, section2.items)

    Anna.player_swim(pressedKey, section2.waters)

    if (Anna.climb == False and Anna.swim == False):
        Anna.playerMove(pressedKey, Anna.xspd)

    # moving enemies
    for i in range(len(section2.moving_enemies)):
        section2.moving_enemies[i].enemy_move(section2.stable_grounds)

    if (Anna.player_jump(pressedKey, section2.stable_grounds) == False):
        Anna.player_fall(Anna.yspd, section2.stable_grounds)

    for i in range(len(section2.moving_npc)):
        section2.moving_npc[i].npc_move(section2.stable_grounds)

    for i in range(section2.hor_ground):
        section2.moving_grounds[i].ground_move(section2.stable_grounds, 1, 0)

    for i in range(section2.hor_ground, len(section2.moving_grounds)):
        section2.moving_grounds[i].ground_move(section2.stable_grounds, 0, 1)


    ### --- Blit section --- ###
    for i in range(len(bg)):
        screen.blit(bg[i], bg_pos[i])

    for i in range(len(section2.moving_enemies)):
        screen.blit(section2.moving_enemies[i].getSurface(), section2.moving_enemies[i].getPos())

    # moving npc
    for i in range(len(section2.npc)):
        screen.blit(section2.npc[i].getSurface(), section2.npc[i].getPos())

    for i in range(len(section2.moving_npc)):
        screen.blit(section2.moving_npc[i].getSurface(), section2.moving_npc[i].getPos())

    # water
    for i in range(len(section2.waters)):
        screen.blit(section2.waters[i].getSurface(), section2.waters[i].getPos())

    # grounds
    for i in range(len(section2.stable_grounds)):
        screen.blit(section2.stable_grounds[i].getSurface(), section2.stable_grounds[i].getPos())

    for i in range(len(section2.moving_grounds)):
        screen.blit(section2.moving_grounds[i].getSurface(), section2.moving_grounds[i].getPos())

    for i in range(len(section2.items)):
        screen.blit(section2.items[i].getSurface(), section2.items[i].getPos())

    for i in range(len(section2.stairs)):
        screen.blit(section2.stairs[i].getSurface(), section2.stairs[i].getPos())

    screen.blit(Anna.getSurface(), Anna.getPos())

def section1_init():
    # Inititate the player
    global Anna
    Anna = player(35, 35, WIDTH/2 - 35/2, 200)
    Anna.setColor((0, 0, 255))


    # Initiate the first section
    global section1
    section1 = section()
    section1.stable_grounds.append(ground(WIDTH, 100, 0, HEIGHT - 100))
    section1.stable_grounds.append(ground(150, 40, section1.stable_grounds[0].x + section1.stable_grounds[0].width + 200, 300))
    section1.stable_grounds.append(ground(WIDTH + 200, 100, section1.stable_grounds[1].x + section1.stable_grounds[1].width + 250, HEIGHT - 100))
    section1.stable_grounds.append(ground(WIDTH + 350, 150, section1.stable_grounds[1].x + section1.stable_grounds[1].width + 140, section1.stable_grounds[2].y + section1.stable_grounds[2].height))
    section1.stable_grounds.append(ground(2100, 1000, 0, section1.stable_grounds[3].y + section1.stable_grounds[3].height))
    section1.stable_grounds.append(ground(500, 260, section1.stable_grounds[2].x + section1.stable_grounds[2].width - 700, section1.stable_grounds[2].y - 260))
    section1.stable_grounds.append(ground(section1.stable_grounds[0].width + 100, section1.stable_grounds[2].height + section1.stable_grounds[3].height + section1.stable_grounds[4].height, section1.stable_grounds[2].x + section1.stable_grounds[2].width + 1000, section1.stable_grounds[3].y))
    section1.stable_grounds.append(ground(1000, 50, section1.stable_grounds[3].x + section1.stable_grounds[3].width, section1.stable_grounds[3].y))

    section1.moving_enemies.append(enemy(30, 30, 200, section1.stable_grounds[4].y - 30))
    section1.moving_enemies[0].setColor((255, 0, 0))


    section1.stairs.append(stair(40, section1.stable_grounds[5].height + 40, section1.stable_grounds[5].x + section1.stable_grounds[5].width/2, section1.stable_grounds[5].y - 40))

    section1.stairs[0].setColor((0, 255, 0))

    section1.items.append(interactive_object(20, 20, section1.stable_grounds[5].x + 50, section1.stable_grounds[5].y - 30))
    section1.items[0].setColor((255, 255, 0))

    section1.npc.append(npc(30, 30, section1.stable_grounds[6].x + 100, section1.stable_grounds[6].y - 30))
    section1.npc.append(npc(30, 30, section1.stable_grounds[6].x + 250, section1.stable_grounds[6].y - 30))
    section1.npc.append(npc(30, 30, section1.stable_grounds[6].x + 500, section1.stable_grounds[6].y - 30))
    section1.npc.append(npc(30, 30, section1.stable_grounds[6].x + 700, section1.stable_grounds[6].y - 30))

    section1.moving_npc.append(moving_npc(30, 30, section1.stable_grounds[6].x + 10, section1.stable_grounds[6].y - 30))
    section1.moving_npc[0].move_range = (section1.stable_grounds[6].x, section1.npc[2].x - 30)
    section1.moving_npc[0].setColor((255, 0, 0))


    # Initiate background image
    global bg
    global bg_pos
    global startscrolling_x
    global startscrolling_y
    global startbackground_x
    global startbackground_y
    bg = []
    bg_pos = []
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg_pos.append([0,0])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), 0])
    startscrolling_x = WIDTH/2
    startscrolling_y = HEIGHT/2
    startbackground_x = 0
    startbackground_y = 0


def section1_gameplay():
    section_gameplay(section1)

    if (Anna.x >= WIDTH):
        section_area = 2

def section2_init():
    # Inititate the player
    global Anna
    Anna = player(35, 35, 0, 200)
    Anna.setColor((0, 0, 255))


    # Initiate the first section
    global section2
    section2 = section()
    section2.stable_grounds.append(ground(WIDTH, 500, 0, HEIGHT - 100))
    section2.stable_grounds.append(ground(400, 300, section2.stable_grounds[0].x + section2.stable_grounds[0].width - 500, section2.stable_grounds[0].y - 300))
    section2.stable_grounds.append(ground(200, 50, section2.stable_grounds[0].x + section2.stable_grounds[0].width + 200, section2.stable_grounds[1].y + 50))
    section2.stable_grounds.append(ground(200, 50, section2.stable_grounds[2].x + section2.stable_grounds[2].width + 200, section2.stable_grounds[2].y))
    section2.stable_grounds.append(ground(200, 50, section2.stable_grounds[3].x + section2.stable_grounds[3].width + 200, section2.stable_grounds[3].y))
    section2.stable_grounds.append(ground(2 * WIDTH, 500, section2.stable_grounds[4].x + section2.stable_grounds[4].width + 200, HEIGHT - 100))
    section2.stable_grounds.append(ground(section2.stable_grounds[5].width, 100, section2.stable_grounds[5].x, section2.stable_grounds[5].y + section2.stable_grounds[5].height + 150))
    section2.stable_grounds.append(ground(section2.stable_grounds[5].width, 100, section2.stable_grounds[5].x, section2.stable_grounds[6].y + section2.stable_grounds[6].height + 150))
    section2.stable_grounds.append(ground(500, 60, section2.stable_grounds[5].x + section2.stable_grounds[5].width + 200, section2.stable_grounds[5].y - 250))
    section2.stable_grounds.append(ground(500, 60, section2.stable_grounds[5].x + section2.stable_grounds[5].width + 200, section2.stable_grounds[8].y - 250))
    section2.stable_grounds.append(ground(400, 2*WIDTH, section2.stable_grounds[9].x + 100, section2.stable_grounds[9].y - 100))
    section2.stable_grounds.append(ground(300, 150, section2.stable_grounds[5].x + 500, section2.stable_grounds[5].y - 150))
    section2.stable_grounds.append(ground(150, 50, section2.stable_grounds[11].x - 200, section2.stable_grounds[11].y - 100))
    section2.stable_grounds.append(ground(50, 50, section2.stable_grounds[12].x - 100, section2.stable_grounds[12].y - 100))
    section2.stable_grounds.append(ground(150, 50, section2.stable_grounds[11].x + 50, section2.stable_grounds[13].y - 100))
    section2.stable_grounds.append(ground(300, 150, section2.stable_grounds[11].x + section2.stable_grounds[11].width + 700, section2.stable_grounds[5].y - 150))
    section2.stable_grounds.append(ground(100, 50, section2.stable_grounds[15].x - 200, section2.stable_grounds[15].y - 100))
    section2.stable_grounds.append(ground(70, 50, section2.stable_grounds[16].x - 200, section2.stable_grounds[16].y - 100))


    section2.waters.append(water(7 * WIDTH, 2000, section2.stable_grounds[0].x, section2.stable_grounds[0].y + 100))
    section2.waters[0].setColor((113, 226, 230))

    # Initiate background image
    global bg
    global bg_pos
    global startscrolling_x
    global startscrolling_y
    global startbackground_x
    global startbackground_y
    bg = []
    bg_pos = []
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg_pos.append([0,0])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), 0])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), 0])
    startscrolling_x = WIDTH/2
    startscrolling_y = HEIGHT/2
    startbackground_x = 0
    startbackground_y = 0


def section2_gameplay():
    section_gameplay(section2)

    if (Anna.x >= WIDTH):
        section_area = 4

def section3_init():
    # Inititate the player
    global Anna
    Anna = player(35, 35, 0, 200)
    Anna.setColor((0, 0, 255))


    # Initiate the first section
    global section3
    section3 = section()
    section3.stable_grounds.append(ground(1000, 2*WIDTH, 0, 700))
    section3.stable_grounds.append(ground(800, 2 * WIDTH, section3.stable_grounds[0].x + section3.stable_grounds[0].width + 1300, section3.stable_grounds[0].y - 700))
    section3.stable_grounds.append(ground(60, 150, section3.stable_grounds[1].x - 60, section3.stable_grounds[0].y - 100))
    section3.stable_grounds.append(ground(60, 150, section3.stable_grounds[1].x - 60, section3.stable_grounds[1].y))
    section3.stable_grounds.append(ground(500, 500, section3.stable_grounds[1].x - 60, section3.stable_grounds[1].y))
    section3.stable_grounds.append(ground(1000, 300, section3.stable_grounds[4].x + section3.stable_grounds[4].width, section3.stable_grounds[4].y + 200))
    section3.stable_grounds.append(ground(100, 50, section3.stable_grounds[4].x + section3.stable_grounds[4].width + 150, section3.stable_grounds[5].y - 50))
    section3.stable_grounds.append(ground(100, 50, section3.stable_grounds[6].x + section3.stable_grounds[6].width + 400, section3.stable_grounds[5].y - 50))
    section3.stable_grounds.append(ground(400, 50, section3.stable_grounds[7].x + section3.stable_grounds[7].width + 400, section3.stable_grounds[5].y - 50))
    section3.stable_grounds.append(ground(100, 50, section3.stable_grounds[6].x + section3.stable_grounds[6].width + 150, section3.stable_grounds[4].y - 200))
    section3.stable_grounds.append(ground(100, 50, section3.stable_grounds[7].x + section3.stable_grounds[7].width + 150, section3.stable_grounds[4].y - 200))
    section3.stable_grounds.append(ground(2000, 50, section3.stable_grounds[1].x + section3.stable_grounds[1].width, section3.stable_grounds[1].y + 100))
    section3.stable_grounds.append(ground(500, 50, section3.stable_grounds[11].x + section3.stable_grounds[11].width, section3.stable_grounds[11].y + 200))
    section3.stable_grounds.append(ground(300, 50, section3.stable_grounds[12].x + section3.stable_grounds[12].width,section3.stable_grounds[11].y))

    section3.moving_grounds.append(moving_ground(200, 50, section3.stable_grounds[0].x + section3.stable_grounds[0].width + 200, section3.stable_grounds[0].y))
    section3.moving_grounds[0].set_rangex(section3.stable_grounds[0].x + section3.stable_grounds[0].width + 200, section3.stable_grounds[0].x + section3.stable_grounds[0].width + 1000)
    section3.moving_grounds[0].set_rangey(section3.moving_grounds[0].y, section3.moving_grounds[0].y)

    section3.moving_grounds.append(moving_ground(200, 50, section3.stable_grounds[0].x + section3.stable_grounds[0].width + 200, section3.stable_grounds[0].y - 500))
    section3.moving_grounds[1].set_rangex(section3.stable_grounds[0].x + section3.stable_grounds[0].width - 50,section3.stable_grounds[0].x + section3.stable_grounds[0].width + 1000)
    section3.moving_grounds[1].set_rangey(section3.moving_grounds[0].y, section3.moving_grounds[0].y)

    section3.moving_grounds.append(moving_ground(200, 50, section3.stable_grounds[0].x + section3.stable_grounds[0].width + 200, section3.stable_grounds[0].y - 250))
    section3.moving_grounds[2].set_rangex(section3.moving_grounds[2].x, section3.moving_grounds[2].x)
    section3.moving_grounds[2].set_rangey(section3.moving_grounds[0].y - 250, section3.moving_grounds[0].y - 800)

    section3.moving_grounds.append(moving_ground(100, 50, section3.stable_grounds[11].x + section3.stable_grounds[11].width + 50,section3.stable_grounds[11].y))
    section3.moving_grounds[3].set_rangex(section3.stable_grounds[11].x + section3.stable_grounds[11].width + 50, section3.stable_grounds[13].x - section3.moving_grounds[3].width - 50)
    section3.moving_grounds[3].set_rangey(section3.stable_grounds[11].y, section3.stable_grounds[11].y)

    section3.hor_ground = 2

    # Initiate background image
    global bg
    global bg_pos
    global startscrolling_x
    global startscrolling_y
    global startbackground_x
    global startbackground_y
    bg = []
    bg_pos = []
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg_pos.append([0,0])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), 0])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), 0])
    startscrolling_x = WIDTH/2
    startscrolling_y = HEIGHT/2
    startbackground_x = 0 #
    startbackground_y = 0


def section3_gameplay():
    section_gameplay(section3)

    if (Anna.x >= WIDTH):
        section_area = 6



def section4_init():
    # Inititate the player
    global Anna
    Anna = player(35, 35, 0, 200)
    Anna.setColor((0, 0, 255))


    # Initiate the first section
    global section4
    section4 = section()

    section4.stable_grounds.append(ground(4*WIDTH + 500, 1000, -WIDTH-500, HEIGHT - 100))
    section4.stable_grounds.append(ground(500, 300, 1000, section4.stable_grounds[0].y - 250))
    section4.stable_grounds.append(ground(200, 100, 0, section4.stable_grounds[0].y - 400))
    section4.stable_grounds.append(ground(500, 300, section4.stable_grounds[0].y - 300))
    section4.stable_grounds.append(ground(100, 50, section4.stable_grounds[0].x - 200, section4.stable_grounds[0].y - 100))
    section4.stable_grounds.append(ground(100, 50, section4.stable_grounds[4].x - 200, section4.stable_grounds[4].y))
    section4.stable_grounds.append(ground(100, 50, section4.stable_grounds[4].x - 100, section4.stable_grounds[5].y - 150))
    section4.stable_grounds.append(ground(100, 50, section4.stable_grounds[6].x - 200, section4.stable_grounds[6].y - 150))
    section4.stable_grounds.append(ground(300, 100, section4.stable_grounds[0].x - 100, section4.stable_grounds[7].y - 250))


    # Initiate background image
    global bg
    global bg_pos
    global startscrolling_x
    global startscrolling_y
    global startbackground_x
    global startbackground_y
    bg = []
    bg_pos = []
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg_pos.append([0,0])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), 0])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), 0])
    startscrolling_x = WIDTH/2
    startscrolling_y = HEIGHT/2
    startbackground_x = 0
    startbackground_y = 0


def section4_gameplay():
    section_gameplay(section4)

    if (Anna.x >= WIDTH):
        section_area = 6



# --- CODE STARTS HERE --- #
section1_init()
running = True

while running:
    for event in pygame.event.get():  # Returns all input and triggers into an array
        if (event.type == pygame.QUIT): # If the red X was clicked
            running = False

    pressedKey = pygame.key.get_pressed()

    if (section_area == 1):
        section1_gameplay()

    if (section_area == 2):
        section2_init()
        section_area = 3

    if (section_area == 3):
        section2_gameplay()

    if (section_area == 4):
        section3_init()
        section_area = 5

    if (section_area == 5):
        section3_gameplay()

    if (section_area == 6):
        section4_init()
        section_area = 7

    if (section_area == 7):
        section4_gameplay()

    pygame.display.update()
    clock.tick(FPS) # This will pause the game until the FPS time is reached


pygame.quit()