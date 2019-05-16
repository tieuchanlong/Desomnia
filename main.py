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

def section_gameplay(section):
    global startbackground_x
    global startbackground_y
    if (Anna.x + Anna.width / 2 > startscrolling_x):
        startbackground_x += Anna.x + Anna.width / 2 - startscrolling_x
        if (startbackground_x < bg_pos[len(bg) - 1][0] + bg[len(bg) - 1].get_width()):
            section.move_x(-(Anna.x + Anna.width / 2 - startscrolling_x))
            Anna.setPos(startscrolling_x - Anna.width / 2, Anna.y)
        else:
            startbackground_x = bg_pos[len(bg) - 1][0] + bg[len(bg) - 1].get_width()

    if (Anna.x + Anna.width / 2 < startscrolling_x):
        startbackground_x -= startscrolling_x - Anna.x - Anna.width / 2
        if (startbackground_x > 0):
            section.move_x(startscrolling_x - Anna.x - Anna.width / 2)
            Anna.setPos(startscrolling_x - Anna.width / 2, Anna.y)
        else:
            startbackground_x = 0

    if (Anna.y + Anna.height / 2 > startscrolling_y):
        startbackground_y += Anna.y + Anna.height / 2 - startscrolling_y
        if (startbackground_y < bg_pos[len(bg) - 1][1] + bg[len(bg) - 1].get_height()):
            section.move_y(-(Anna.y + Anna.height / 2 - startscrolling_y))
            Anna.setPos(Anna.x, startscrolling_y - Anna.height / 2)
        else:
            startbackground_y = bg_pos[len(bg) - 1][1] + bg[len(bg) - 1].get_height()

    if (Anna.y + Anna.height / 2 < startscrolling_y):
        startbackground_y -= startscrolling_y - Anna.y - Anna.height / 2
        if (startbackground_y > 0):
            section.move_y(startscrolling_y - Anna.y - Anna.height / 2)
            Anna.setPos(Anna.x, startscrolling_y - Anna.height / 2)
        else:
            startbackground_y = 0

    Anna.player_climb(pressedKey, section.stairs)

    Anna.player_pickup(pressedKey, section.items)

    Anna.player_swim(pressedKey, section.waters)

    if (Anna.climb == False and Anna.swim == False):
        Anna.playerMove(pressedKey, Anna.xspd)

    # moving enemies
    for i in range(len(section.moving_enemies)):
        section.moving_enemies[i].enemy_move(section.stable_grounds)

    if (Anna.player_jump(pressedKey, section.stable_grounds) == False):
        Anna.player_fall(Anna.yspd, section.stable_grounds)

    for i in range(len(section.moving_npc)):
        section.moving_npc[i].npc_move(section.stable_grounds)

    for i in range(section.hor_ground):
        section.moving_grounds[i].ground_move(section.stable_grounds, 1, 0)

    for i in range(section.hor_ground, len(section.moving_grounds)):
        section.moving_grounds[i].ground_move(section.stable_grounds, 0, 1)


    ### --- Blit section --- ###
    for i in range(len(bg)):
        screen.blit(bg[i], bg_pos[i])

    for i in range(len(section.moving_enemies)):
        screen.blit(section.moving_enemies[i].getSurface(), section.moving_enemies[i].getPos())

    # moving npc
    for i in range(len(section.npc)):
        screen.blit(section.npc[i].getSurface(), section.npc[i].getPos())

    for i in range(len(section.moving_npc)):
        screen.blit(section.moving_npc[i].getSurface(), section.moving_npc[i].getPos())

    # water
    for i in range(len(section.waters)):
        screen.blit(section.waters[i].getSurface(), section.waters[i].getPos())

    # grounds
    for i in range(len(section.stable_grounds)):
        screen.blit(section.stable_grounds[i].getSurface(), section.stable_grounds[i].getPos())

    for i in range(len(section.moving_grounds)):
        screen.blit(section.moving_grounds[i].getSurface(), section.moving_grounds[i].getPos())

    for i in range(len(section.items)):
        screen.blit(section.items[i].getSurface(), section.items[i].getPos())

    for i in range(len(section.stairs)):
        screen.blit(section.stairs[i].getSurface(), section.stairs[i].getPos())

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

    section1.moving_npc.append(moving_npc(30, 30, section1.stable_grounds[6].x + 10, section1.stable_grounds[6].y - 30, 0.1))
    section1.moving_npc[0].set_rangex(section1.stable_grounds[6].x, section1.npc[3].x - 30)
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
    section2.stable_grounds.append(ground(400, 150, section2.stable_grounds[5].x + 700, section2.stable_grounds[5].y - 150))
    section2.stable_grounds.append(ground(150, 50, section2.stable_grounds[11].x - 200, section2.stable_grounds[11].y - 100))
    section2.stable_grounds.append(ground(50, 50, section2.stable_grounds[12].x - 100, section2.stable_grounds[12].y - 100))
    section2.stable_grounds.append(ground(150, 50, section2.stable_grounds[11].x + 50, section2.stable_grounds[13].y - 100))
    section2.stable_grounds.append(ground(300, 150, section2.stable_grounds[11].x + section2.stable_grounds[11].width + 700, section2.stable_grounds[5].y - 150))
    section2.stable_grounds.append(ground(100, 50, section2.stable_grounds[15].x - 200, section2.stable_grounds[15].y - 100))
    section2.stable_grounds.append(ground(70, 50, section2.stable_grounds[16].x - 200, section2.stable_grounds[16].y - 100))

    # NPC
    section2.moving_npc.append(moving_npc(30, 30, section2.stable_grounds[0].x, section2.stable_grounds[0].y - 30))
    section2.moving_npc[0].set_rangex(section2.stable_grounds[0].x, section2.stable_grounds[1].x - 130)
    section2.moving_npc[0].setColor((255, 0, 0))

    section2.moving_npc.append(moving_npc(30, 30, section2.moving_npc[0].x + section2.moving_npc[0].width + 100, section2.stable_grounds[0].y - 30))
    section2.moving_npc[1].set_rangex(section2.moving_npc[1].x, section2.stable_grounds[1].x - 30)
    section2.moving_npc[1].setColor((255, 0, 0))


    # Enemies
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[5].x + 300, section2.stable_grounds[5].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[5].x + 500, section2.stable_grounds[5].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[11].x, section2.stable_grounds[11].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[11].x + section2.stable_grounds[11].width - 30, section2.stable_grounds[11].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[6].x, section2.stable_grounds[6].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[7].x, section2.stable_grounds[7].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[8].x, section2.stable_grounds[8].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[9].x, section2.stable_grounds[9].y - 30))

    section2.moving_enemies[1].dir = -1
    section2.moving_enemies[2].dir = -1

    for i in range(len(section2.moving_enemies)):
        section2.moving_enemies[i].setColor((255, 0, 0))


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

    # Special cases
    if (section2.moving_npc[0].x <= section2.stable_grounds[0].x):
        section2.moving_npc[1].dir = 1

    if (section2.moving_npc[0].dir != section2.moving_npc[1].dir):
        section2.moving_npc[0].dir = section2.moving_npc[1].dir


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

    # Enemies
    section3.moving_enemies.append(enemy(30, 30, section3.stable_grounds[11].x, section3.stable_grounds[11].y - 30))
    section3.moving_enemies.append(enemy(30, 30, section3.stable_grounds[11].x, section3.stable_grounds[11].y - 30))
    section3.moving_enemies.append(enemy(30, 30, section3.stable_grounds[13].x, section3.stable_grounds[13].y - 30))

    section3.moving_enemies[0].dir = -1

    for i in range(len(section3.moving_enemies)):
        section3.moving_enemies[i].setColor((255, 0, 0))

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

    section4.stable_grounds.append(ground(5*WIDTH + 1000, 1000, -WIDTH-500, HEIGHT - 100))
    section4.stable_grounds.append(ground(500, 300, 1000, section4.stable_grounds[0].y - 250))
    section4.stable_grounds.append(ground(200, 100, 0, section4.stable_grounds[0].y - 400))
    section4.stable_grounds.append(ground(500, 300, section4.stable_grounds[0].x + 500, section4.stable_grounds[0].y - 300))
    section4.stable_grounds.append(ground(100, 50, section4.stable_grounds[0].x - 200, section4.stable_grounds[0].y - 100))
    section4.stable_grounds.append(ground(100, 50, section4.stable_grounds[4].x - 200, section4.stable_grounds[4].y))
    section4.stable_grounds.append(ground(100, 50, section4.stable_grounds[4].x - 100, section4.stable_grounds[5].y - 150))
    section4.stable_grounds.append(ground(100, 50, section4.stable_grounds[6].x - 200, section4.stable_grounds[6].y - 150))
    section4.stable_grounds.append(ground(300, 100, section4.stable_grounds[0].x - 150, section4.stable_grounds[7].y - 250))
    section4.stable_grounds.append(ground(500, 1100, section4.stable_grounds[0].x, section4.stable_grounds[0].y - section4.stable_grounds[0].height - 1000))
    section4.stable_grounds.append(ground(200, 50, 2500, section4.stable_grounds[0].y - 150))
    section4.stable_grounds.append(ground(200, 50, section4.stable_grounds[10].x + section4.stable_grounds[10].width + 100, section4.stable_grounds[10].y - 150))
    section4.stable_grounds.append(ground(200, 50, section4.stable_grounds[11].x + section4.stable_grounds[11].width + 100, section4.stable_grounds[11].y - 150))

    section4.moving_grounds.append(moving_ground(100, 50, section4.stable_grounds[8].x + section4.stable_grounds[8].width + 50, section4.stable_grounds[8].y))
    section4.moving_grounds[0].set_rangex(section4.moving_grounds[0].x, section4.moving_grounds[0].x)
    section4.moving_grounds[0].set_rangey(section4.stable_grounds[0].y - 150, section4.moving_grounds[0].y)

    section4.moving_grounds.append(moving_ground(100, 50, section4.moving_grounds[0].x + section4.moving_grounds[0].width + 100, section4.stable_grounds[8].y))
    section4.moving_grounds[1].set_rangex(section4.moving_grounds[1].x, section4.moving_grounds[1].x)
    section4.moving_grounds[1].set_rangey(section4.stable_grounds[0].y - 150, section4.moving_grounds[1].y)

    section4.moving_grounds.append(moving_ground(100, 50, section4.moving_grounds[0].x + section4.moving_grounds[0].width + 100, section4.stable_grounds[8].y))
    section4.moving_grounds[2].set_rangex(section4.moving_grounds[1].x, section4.moving_grounds[1].x)
    section4.moving_grounds[2].set_rangey(section4.stable_grounds[12].y - 150, section4.stable_grounds[12].y - 500)

    section4.waters.append(water(WIDTH - section4.stable_grounds[8].width, 1000, section4.stable_grounds[8].x + section4.stable_grounds[8].width, section4.stable_grounds[8].y + 100))

    # Enemies
    section4.moving_enemies.append(enemy(30, 30, 700, section4.stable_grounds[0].y - 30))
    section4.moving_enemies.append(enemy(30, 30, 2000, section4.stable_grounds[0].y - 30))
    section4.moving_enemies.append(enemy(30, 30, section4.stable_grounds[1].x, section4.stable_grounds[1].y - 30))
    section4.moving_enemies.append(enemy(30, 30, section4.stable_grounds[0].x, section4.stable_grounds[0].y - 30))
    section4.moving_enemies.append(enemy(30, 30, section4.stable_grounds[0].x + 500, section4.stable_grounds[0].y - 30))
    section4.moving_enemies.append(enemy(30, 30, section4.stable_grounds[3].x, section4.stable_grounds[3].y - 30))

    section4.moving_enemies[0].dir = -1

    for i in range(len(section4.moving_enemies)):
        section4.moving_enemies[i].setColor((255, 0, 0))


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
        section_area = 8


def section5_init():
    # Inititate the player
    global Anna
    Anna = player(35, 35, 0, 200)
    Anna.setColor((0, 0, 255))


    # Initiate the first section
    global section5
    section5 = section()

    section5.stable_grounds.append(ground(1000, 500, -500, HEIGHT - 100))
    section5.stable_grounds.append(ground(100, 50, section5.stable_grounds[0].x + section5.stable_grounds[0].width + 150, section5.stable_grounds[0].y))
    section5.stable_grounds.append(ground(100, 50, section5.stable_grounds[1].x + section5.stable_grounds[1].width + 150, section5.stable_grounds[1].y - 150))
    section5.stable_grounds.append(ground(400, 100, section5.stable_grounds[2].x + section5.stable_grounds[2].width + 150, section5.stable_grounds[2].y))
    section5.stable_grounds.append(ground(250, 60, section5.stable_grounds[3].x + section5.stable_grounds[3].width - 250,section5.stable_grounds[3].y - 60))
    section5.stable_grounds.append(ground(100, 50, section5.stable_grounds[4].x  - 250, section5.stable_grounds[4].y - 150))
    section5.stable_grounds.append(ground(100, 50, section5.stable_grounds[5].x - 250, section5.stable_grounds[5].y - 200))
    section5.stable_grounds.append(ground(400, section5.stable_grounds[0].height, section5.stable_grounds[0].x - 800, section5.stable_grounds[0].y))

    # Enemies
    section5.moving_enemies.append(enemy(30, 30, section5.stable_grounds[7].x, section5.stable_grounds[7].y - 30))
    section5.moving_enemies.append(enemy(30, 30, section5.stable_grounds[7].x + section5.stable_grounds[7].width - 30, section5.stable_grounds[7].y - 30))

    section5.moving_enemies[0].dir = -1

    for i in range(len(section5.moving_enemies)):
        section5.moving_enemies[i].setColor((255, 0, 0))

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


def section5_gameplay():
    section_gameplay(section5)

    if (Anna.x >= WIDTH):
        section_area = 10

def section6_init():
    # Inititate the player
    global Anna
    Anna = player(35, 35, 0, 200)
    Anna.setColor((0, 0, 255))


    # Initiate the first section
    global section6
    section6 = section()

    section6.stable_grounds.append(ground(2*WIDTH, 950, -WIDTH-600, HEIGHT - 200))
    section6.stable_grounds.append(ground(200, 950, section6.stable_grounds[0].x + section6.stable_grounds[0].width + 400, HEIGHT - 200))
    section6.stable_grounds.append(ground(200, 950, section6.stable_grounds[1].x + section6.stable_grounds[1].width + 400, HEIGHT - 200))
    section6.stable_grounds.append(ground(200, 950, section6.stable_grounds[2].x + section6.stable_grounds[2].width + 400, HEIGHT - 200))
    section6.stable_grounds.append(ground(200, 950, section6.stable_grounds[3].x + section6.stable_grounds[3].width + 400, HEIGHT - 200))
    section6.stable_grounds.append(ground(300, 70, section6.stable_grounds[0].x + 500, section6.stable_grounds[0].y - 70))
    section6.stable_grounds.append(ground(300, 70, section6.stable_grounds[5].x + section6.stable_grounds[5].width + 500, section6.stable_grounds[0].y - 70))
    section6.stable_grounds.append(ground(200, 100, section6.stable_grounds[0].x - 200, section6.stable_grounds[0].y + 100))
    section6.stable_grounds.append(ground(100, 50, section6.stable_grounds[7].x - 400, section6.stable_grounds[7].y + section6.stable_grounds[7].height + 100))
    section6.stable_grounds.append(ground(80, 50, section6.stable_grounds[0].x - 80, section6.stable_grounds[8].y + section6.stable_grounds[8].height + 100))
    section6.stable_grounds.append(ground(100, 50, section6.stable_grounds[9].x - 80, section6.stable_grounds[9].y + section6.stable_grounds[9].height + 200))
    section6.stable_grounds.append(ground(WIDTH + 400, 1000, section6.stable_grounds[10].x - WIDTH - 500, section6.stable_grounds[9].y - section6.stable_grounds[9].height - 100))
    section6.stable_grounds.append(ground(WIDTH + 600, 500, section6.stable_grounds[0].x, section6.stable_grounds[0].y - section6.stable_grounds[0].height - 200))


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


def section6_gameplay():
    section_gameplay(section6)

    if (Anna.x >= WIDTH):
        section_area = 12


def section7_init():
    # Inititate the player
    global Anna
    Anna = player(35, 35, 0, 200)
    Anna.setColor((0, 0, 255))


    # Initiate the first section
    global section7
    section7 = section()

    section7.waters.append(water(WIDTH, 2*HEIGHT, 0, 0))


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


def section7_gameplay():
    section_gameplay(section7)

    if (Anna.x >= WIDTH):
        section_area = 14



def section8_init():
    # Inititate the player
    global Anna
    Anna = player(35, 35, 0, 200)
    Anna.setColor((0, 0, 255))


    # Initiate the first section
    global section8
    section8 = section()

    section8.stable_grounds.append(ground(WIDTH, 2*HEIGHT, 0, 0))


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


def section8_gameplay():
    section_gameplay(section8)

    if (Anna.x >= WIDTH):
        section_area = 16


# --- CODE STARTS HERE --- #
running = True

while running:
    for event in pygame.event.get():  # Returns all input and triggers into an array
        if (event.type == pygame.QUIT): # If the red X was clicked
            running = False

    pressedKey = pygame.key.get_pressed()

    if (section_area == 0):
        section1_init()
        section_area = 1

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

    if (section_area == 8):
        section5_init()
        section_area = 9

    if (section_area == 9):
        section5_gameplay()

    if (section_area == 10):
        section6_init()
        section_area = 11

    if (section_area == 11):
        section6_gameplay()

    if (section_area == 12):
        section7_init()
        section_area = 13

    if (section_area == 13):
        section7_gameplay()

    pygame.display.update()
    clock.tick(FPS) # This will pause the game until the FPS time is reached


pygame.quit()