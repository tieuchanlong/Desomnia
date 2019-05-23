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
from myStats import *
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
global scenechange
section_area = 2
scenechange = -1

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
        if (startbackground_x > bg_pos[0][0]):
            section.move_x(startscrolling_x - Anna.x - Anna.width / 2)
            Anna.setPos(startscrolling_x - Anna.width / 2, Anna.y)
        else:
            startbackground_x = bg_pos[0][0]

    if (Anna.y + Anna.height / 2 > startscrolling_y):
        startbackground_y += Anna.y + Anna.height / 2 - startscrolling_y
        if (startbackground_y < bg_pos[len(bg) - 1][1] + bg[len(bg) - 1].get_height()):
            section.move_y(-(Anna.y + Anna.height / 2 - startscrolling_y))
            Anna.setPos(Anna.x, startscrolling_y - Anna.height / 2)
        else:
            startbackground_y = bg_pos[len(bg) - 1][1] + bg[len(bg) - 1].get_height()

    if (Anna.y + Anna.height / 2 < startscrolling_y):
        startbackground_y -= startscrolling_y - Anna.y - Anna.height / 2
        if (startbackground_y > bg_pos[0][1]):
            section.move_y(startscrolling_y - Anna.y - Anna.height / 2)
            Anna.setPos(Anna.x, startscrolling_y - Anna.height / 2)
        else:
            startbackground_y = bg_pos[0][1]

    Anna.player_climb(pressedKey, section.stairs)

    Anna.player_pickup(pressedKey, section.items)

    Anna.player_swim(pressedKey, section.waters)

    if (Anna.swim == False):
        Anna.playerMove(pressedKey,Anna.xspd)

    # moving enemies
    for i in range(len(section.moving_enemies)):
        section.moving_enemies[i].enemy_move(section.stable_grounds)

    for i in range(len(section.moving_enemies)):
        section.moving_enemies[i].enemy_follow(Anna)

    for i in range(len(section.stable_enemies)):
        section.stable_enemies[i].enemy_follow(Anna)

    for i in range(len(section.stable_enemies)):
        section.stable_enemies[i].enemy_attack(Anna)

    if (Anna.player_jump(pressedKey, section.stable_grounds, section.moving_grounds) == False):
        Anna.player_fall(Anna.yspd, section.stable_grounds, section.moving_grounds)

    Anna.player_skill(pressedKey, Anna_paint)
    Anna_brush.brush_move(Anna)
    Anna_brush.brush_hit(section.moving_enemies)

    for i in range(len(section.moving_npc)):
        section.moving_npc[i].npc_move(section.stable_grounds)

    for i in range(len(section.moving_grounds)):
        if (i < section.hor_ground):
            section.moving_grounds[i].ground_move(Anna, 1, 0)
        else:
            section.moving_grounds[i].ground_move(Anna, 0, 1)

    for i in range(len(section.traps)):
        section.traps[i].trap_attack(Anna)

    for i in range(len(section.moving_traps)):
        section.moving_traps[i].trap_move(Anna)

    ### --- Blit section --- ###
    for i in range(len(bg)):
        screen.blit(bg[i], bg_pos[i])

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

    for i in range(len(section.traps)):
        screen.blit(section.traps[i].getSurface(), section.traps[i].getPos())

    for i in range(len(section.moving_traps)):
        screen.blit(section.moving_traps[i].getSurface(), section.moving_traps[i].getPos())

    for i in range(len(section.moving_grounds)):
        screen.blit(section.moving_grounds[i].getSurface(), section.moving_grounds[i].getPos())

    for i in range(len(section.stable_enemies)):
        screen.blit(section.stable_enemies[i].getSurface(), section.stable_enemies[i].getPos())

    for i in range(len(section.moving_enemies)):
        screen.blit(section.moving_enemies[i].getSurface(), section.moving_enemies[i].getPos())

    for i in range(len(section.items)):
        screen.blit(section.items[i].getSurface(), section.items[i].getPos())

    for i in range(len(section.stairs)):
        screen.blit(section.stairs[i].getSurface(), section.stairs[i].getPos())

    for i in range(len(Anna.hp_bars)):
        screen.blit(Anna.hp_bars[i].getSurface(), Anna.hp_bars[i].getPos())

    screen.blit(Anna.getSurface(), Anna.getPos())
    screen.blit(Anna_brush.getSurface(), Anna_brush.getPos())
    screen.blit(Anna_paint.getSurface(), Anna_paint.getPos())

def scene_change():
    global scenechange
    global block1
    global block2
    global block3
    global block4
    global block5

    if (scenechange == 0):
        block1 = scene_block(WIDTH, HEIGHT/5, -WIDTH, 0)
        block2 = scene_block(WIDTH + 200, HEIGHT / 5, -WIDTH-100, HEIGHT/5)
        block3 = scene_block(WIDTH + 400, HEIGHT / 5, -WIDTH - 200, 2*HEIGHT / 5)
        block4 = scene_block(WIDTH + 600, HEIGHT / 5, -WIDTH - 400, 3*HEIGHT / 5)
        block5 = scene_block(WIDTH + 800, HEIGHT / 5, -WIDTH - 600, 4 * HEIGHT / 5)
        scenechange = 1

    if (scenechange == 1):
        block1.move()
        block2.move()
        block3.move()
        block4.move()
        block5.move()
        if (block5.x > WIDTH):
            scenechange = -1

        screen.blit(block1.getSurface(), block1.getPos())
        screen.blit(block2.getSurface(), block2.getPos())
        screen.blit(block3.getSurface(), block3.getPos())
        screen.blit(block4.getSurface(), block4.getPos())
        screen.blit(block5.getSurface(), block5.getPos())

def section1_init():
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

    section1.moving_npc.append(moving_npc(30, 30, section1.stable_grounds[4].x + 300, section1.stable_grounds[4].y - 30))
    section1.moving_npc[0].set_rangex(section1.stable_grounds[4].x + 300, section1.stable_grounds[4].x + 600)
    section1.moving_npc[0].setColor((255, 0, 0))


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

    # Inititate the player
    global Anna
    Anna = player(35, 35, section1.stable_grounds[0].x + 200, section1.stable_grounds[0].y - 35)
    Anna.setColor((0, 0, 255))

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
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg_pos.append([0, -HEIGHT])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), -HEIGHT])
    bg_pos.append([0, bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), bg_pos[0][1] + bg[0].get_height()])
    startscrolling_x = WIDTH/2
    startscrolling_y = HEIGHT/2
    startbackground_x = 0
    startbackground_y = 0


def section1_gameplay():
    global  scenechange
    global section_area

    if (scenechange != 1):
        section_gameplay(section1)

    if (Anna.x >= WIDTH and scenechange == -1):
        section_area = 2
        scenechange = 0

def section2_init():
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
    '''section2.stable_grounds.append(ground(300, 150, section2.stable_grounds[11].x + section2.stable_grounds[11].width + 700, section2.stable_grounds[5].y - 150))
    section2.stable_grounds.append(ground(100, 50, section2.stable_grounds[15].x - 200, section2.stable_grounds[15].y - 100))
    section2.stable_grounds.append(ground(70, 50, section2.stable_grounds[16].x - 200, section2.stable_grounds[16].y - 100))'''

    # Inititate the player
    global Anna
    Anna = player(35, 35, section2.stable_grounds[0].x, section2.stable_grounds[0].y - 35)
    Anna.setColor((0, 0, 255))
    Anna.hp_bars.append(hp_bar(20, 20, 100, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 150, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 200, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 250, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 300, 50))

    global Anna_brush
    Anna_brush = brush(120, 10, Anna.x + Anna.width, Anna.y)

    global Anna_paint
    Anna_paint = paint_bar(60, 60, 20, 20)

    # NPC
    section2.moving_npc.append(moving_npc(30, 30, section2.stable_grounds[0].x, section2.stable_grounds[0].y - 30))
    section2.moving_npc[0].set_rangex(section2.stable_grounds[0].x, section2.stable_grounds[1].x - 130)
    section2.moving_npc[0].setColor((255, 0, 0))

    section2.moving_npc.append(moving_npc(30, 30, section2.moving_npc[0].x + section2.moving_npc[0].width + 100, section2.stable_grounds[0].y - 30))
    section2.moving_npc[1].set_rangex(section2.moving_npc[1].x, section2.stable_grounds[1].x - 30)
    section2.moving_npc[1].setColor((255, 0, 0))


    section2.hor_ground = 1

    section2.moving_grounds.append(moving_ground(150, 50, section2.stable_grounds[0].x, section2.moving_npc[0].y - 50))
    section2.moving_grounds[0].set_rangex(section2.moving_npc[0].x, section2.stable_grounds[1].x)
    section2.moving_grounds[0].xspd = 1
    section2.moving_grounds[0].set_rangey(section2.moving_grounds[0].y, section2.moving_grounds[0].y)


    # Enemies
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[5].x + 300, section2.stable_grounds[5].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[5].x + 1000, section2.stable_grounds[5].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[11].x, section2.stable_grounds[11].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[5].x + 1600, section2.stable_grounds[5].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[6].x, section2.stable_grounds[6].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[7].x, section2.stable_grounds[7].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[8].x, section2.stable_grounds[8].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[9].x, section2.stable_grounds[9].y - 30))

    section2.moving_enemies[1].dir = -1
    section2.moving_enemies[2].dir = -1

    section2.items.append(interactive_object(20, 20, section2.stable_grounds[14].x + 50, section2.stable_grounds[14].y - 30))
    section2.items[0].setColor((255, 255, 0))

    section2.waters.append(water(7 * WIDTH, 2000, section2.stable_grounds[0].x, section2.stable_grounds[0].y + 100))
    section2.waters[0].setColor((113, 226, 230))

    '''for i in range(20):
        section2.moving_enemies.append(swimming_enemy(30, 50, section2.waters[0].x + random.randrange(7 * WIDTH)), 10*i)'''

    for i in range(len(section2.moving_enemies)):
        section2.moving_enemies[i].setColor((255, 0, 0))


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
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg_pos.append([section2.stable_grounds[0].x, -HEIGHT])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), -HEIGHT])
    bg_pos.append([section2.stable_grounds[0].x, bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), bg_pos[0][1] + bg[0].get_height()])
    startscrolling_x = WIDTH/2
    startscrolling_y = HEIGHT/2
    startbackground_x = 0
    startbackground_y = 0


def section2_gameplay():
    global scenechange
    global section_area


    if (scenechange != 1):
        section_gameplay(section2)

    # Special cases
    if (section2.moving_npc[0].x <= section2.stable_grounds[0].x):
        section2.moving_npc[1].dir = 1

    if (section2.moving_npc[0].dir != section2.moving_npc[1].dir):
        section2.moving_npc[0].dir = section2.moving_npc[1].dir
        section2.moving_grounds[0].dir = -1

    if (Anna.x >= WIDTH and scenechange == -1):
        section_area = 4
        scenechange = 0

def section3_init():
    # Initiate the first section
    global section3
    section3 = section()
    section3.stable_grounds.append(ground(1000, 2*WIDTH, 0, 700))
    section3.stable_grounds.append(ground(800, 2 * WIDTH, section3.stable_grounds[0].x + section3.stable_grounds[0].width + 1300, section3.stable_grounds[0].y - 700))
    section3.stable_grounds.append(ground(60, 150, section3.stable_grounds[1].x - 60, section3.stable_grounds[0].y - 100))
    section3.stable_grounds.append(ground(60, 150, section3.stable_grounds[1].x - 60, section3.stable_grounds[2].y - 400))
    section3.stable_grounds.append(ground(500, 200, section3.stable_grounds[1].x + section3.stable_grounds[1].width + 300, section3.stable_grounds[1].y - 150))
    section3.stable_grounds.append(ground(2000, 300, section3.stable_grounds[4].x, section3.stable_grounds[4].y + section3.stable_grounds[4].height))
    section3.stable_grounds.append(ground(100, 50, section3.stable_grounds[4].x + section3.stable_grounds[4].width + 150, section3.stable_grounds[5].y - 50))
    section3.stable_grounds.append(ground(100, 50, section3.stable_grounds[6].x + section3.stable_grounds[6].width + 300, section3.stable_grounds[5].y - 50))
    section3.stable_grounds.append(ground(400, 50, section3.stable_grounds[7].x + section3.stable_grounds[7].width + 300, section3.stable_grounds[5].y - 50))
    section3.stable_grounds.append(ground(100, 50, section3.stable_grounds[6].x + section3.stable_grounds[6].width + 150, section3.stable_grounds[4].y - 400))
    section3.stable_grounds.append(ground(100, 50, section3.stable_grounds[7].x + section3.stable_grounds[7].width + 150, section3.stable_grounds[4].y - 400))
    section3.stable_grounds.append(ground(2000, 400, section3.stable_grounds[1].x + section3.stable_grounds[1].width, section3.stable_grounds[1].y + 500))
    section3.stable_grounds.append(ground(500, 50, section3.stable_grounds[11].x + section3.stable_grounds[11].width, section3.stable_grounds[11].y + 200))
    section3.stable_grounds.append(ground(300, 400, section3.stable_grounds[12].x + section3.stable_grounds[12].width, section3.stable_grounds[11].y))


    section3.moving_grounds.append(moving_ground(100, 50, section3.stable_grounds[0].x + section3.stable_grounds[0].width + 200, section3.stable_grounds[0].y - 160))
    section3.moving_grounds[0].set_rangex(section3.stable_grounds[0].x + section3.stable_grounds[0].width, section3.stable_grounds[1].x)
    section3.moving_grounds[0].set_rangey(section3.moving_grounds[0].y, section3.moving_grounds[0].y)

    section3.moving_grounds.append(moving_ground(200, 50, section3.stable_grounds[0].x + section3.stable_grounds[0].width + 200, section3.stable_grounds[0].y - 320))
    section3.moving_grounds[1].set_rangex(section3.stable_grounds[0].x + section3.stable_grounds[0].width - 100, section3.stable_grounds[1].x)
    section3.moving_grounds[1].set_rangey(section3.moving_grounds[1].y, section3.moving_grounds[1].y)


    section3.moving_grounds.append(moving_ground(200, 50, section3.stable_grounds[0].x - 400, section3.stable_grounds[0].y - 480))
    section3.moving_grounds[2].set_rangex(section3.stable_grounds[0].x + section3.stable_grounds[0].width - 200, section3.stable_grounds[1].x)
    section3.moving_grounds[2].set_rangey(section3.moving_grounds[2].y, section3.moving_grounds[2].y)

    section3.moving_grounds.append(moving_ground(200, 50, section3.stable_grounds[0].x - 400, section3.stable_grounds[0].y - 640))
    section3.moving_grounds[3].set_rangex(section3.stable_grounds[0].x + section3.stable_grounds[0].width - 300, section3.stable_grounds[1].x)
    section3.moving_grounds[3].set_rangey(section3.moving_grounds[3].y, section3.moving_grounds[3].y)


    # Enemies
    section3.moving_enemies.append(enemy(30, 30, section3.stable_grounds[11].x, section3.stable_grounds[11].y - 30))
    section3.moving_enemies.append(enemy(30, 30, section3.stable_grounds[11].x + 700, section3.stable_grounds[11].y - 30))
    section3.moving_enemies.append(enemy(30, 30, section3.stable_grounds[13].x, section3.stable_grounds[13].y - 30))

    section3.moving_enemies[0].dir = -1

    for i in range(len(section3.moving_enemies)):
        section3.moving_enemies[i].setColor((255, 0, 0))

    # Inititate the player
    global Anna
    Anna = player(35, 35, section3.stable_grounds[0].x, section3.stable_grounds[0].y - 35)
    Anna.setColor((0, 0, 255))

    # Items
    section3.items.append(interactive_object(20, 20, section3.stable_grounds[1].x + 100, section3.stable_grounds[1].y - 30))
    section3.items[0].setColor((255, 255, 0))

    section3.items.append(interactive_object(20, 20, section3.stable_grounds[10].x + 50, section3.stable_grounds[10].y - 30))
    section3.items[1].setColor((255, 255, 0))

    section3.hor_ground = 4

    # trap
    section3.traps.append(trap(section3.stable_grounds[2].width, section3.stable_grounds[1].height, section3.stable_grounds[1].x - section3.stable_grounds[2].width, section3.stable_grounds[1].y))


    for i in range(len(section3.traps)):
        section3.traps[i].setColor(BLACK)

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
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg_pos.append([section3.stable_grounds[0].x, -HEIGHT])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), -HEIGHT])
    bg_pos.append([section3.stable_grounds[0].x, bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), bg_pos[0][1] + bg[0].get_height()])
    startscrolling_x = WIDTH/2
    startscrolling_y = HEIGHT/2
    startbackground_x = 0 #
    startbackground_y = 0


def section3_gameplay():
    global scenechange
    global section_area
    section_gameplay(section3)

    if (Anna.x >= WIDTH and scenechange == -1):
        section_area = 6
        scenechange = 0


def section4_init():
    # Initiate the first section
    global section4
    section4 = section()

    section4.stable_grounds.append(ground(6*WIDTH + 1000, 1000, -WIDTH-500, HEIGHT - 100))
    section4.stable_grounds.append(ground(500, 300, 1000, section4.stable_grounds[0].y - 250))
    section4.stable_grounds.append(ground(500, 100, 0, section4.stable_grounds[0].y - 450))
    section4.stable_grounds.append(ground(500, 100, section4.stable_grounds[2].x - 800, section4.stable_grounds[0].y - 300))
    section4.stable_grounds.append(ground(100, 50, section4.stable_grounds[0].x - 200, section4.stable_grounds[0].y - 100))
    section4.stable_grounds.append(ground(100, 50, section4.stable_grounds[4].x - 200, section4.stable_grounds[4].y))
    section4.stable_grounds.append(ground(100, 50, section4.stable_grounds[4].x - 100, section4.stable_grounds[5].y - 150))
    section4.stable_grounds.append(ground(100, 50, section4.stable_grounds[6].x - 200, section4.stable_grounds[6].y - 150))
    section4.stable_grounds.append(ground(400, 100, section4.stable_grounds[0].x - 250, section4.stable_grounds[7].y - 150))
    section4.stable_grounds.append(ground(500, 1100, section4.stable_grounds[0].x, section4.stable_grounds[0].y + section4.stable_grounds[0].height + 1000))
    section4.stable_grounds.append(ground(200, 50, 2500, section4.stable_grounds[0].y - 150))
    section4.stable_grounds.append(ground(200, 50, section4.stable_grounds[10].x + section4.stable_grounds[10].width + 100, section4.stable_grounds[10].y - 150))
    section4.stable_grounds.append(ground(200, 50, section4.stable_grounds[11].x + section4.stable_grounds[11].width + 100, section4.stable_grounds[11].y - 150))

    section4.moving_grounds.append(moving_ground(100, 50, section4.stable_grounds[8].x + section4.stable_grounds[8].width + 200, section4.stable_grounds[8].y))
    section4.moving_grounds[0].set_rangex(section4.moving_grounds[0].x, section4.moving_grounds[0].x)
    section4.moving_grounds[0].set_rangey(section4.stable_grounds[0].y - 150, section4.stable_grounds[8].y)

    section4.moving_grounds.append(moving_ground(100, 50, section4.stable_grounds[3].x - 300, section4.stable_grounds[3].y))
    section4.moving_grounds[1].set_rangex(section4.moving_grounds[1].x, section4.moving_grounds[1].x)
    section4.moving_grounds[1].set_rangey(section4.stable_grounds[0].y - 150, section4.stable_grounds[3].y)

    section4.moving_grounds.append(moving_ground(100, 50, section4.stable_grounds[12].x + section4.stable_grounds[12].width + 300, section4.stable_grounds[8].y))
    section4.moving_grounds[2].set_rangex(section4.moving_grounds[2].x, section4.moving_grounds[2].x)
    section4.moving_grounds[2].set_rangey(section4.stable_grounds[12].y - 150, section4.stable_grounds[12].y - 500)

    section4.waters.append(water(WIDTH - section4.stable_grounds[8].width, 1000, section4.stable_grounds[8].x + section4.stable_grounds[8].width, section4.stable_grounds[9].y + 100))

    # Inititate the player
    global Anna
    Anna = player(35, 35, section4.stable_grounds[2].x + 50, section4.stable_grounds[2].y - 35)
    Anna.setColor((0, 0, 255))

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


    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[2].x + section4.stable_grounds[2].width + 600, section4.stable_grounds[0].y - 40))
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[2].x + section4.stable_grounds[2].width + 1200, section4.stable_grounds[0].y - 40))
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[2].x + section4.stable_grounds[2].width + 1800, section4.stable_grounds[0].y - 40))
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[2].x + section4.stable_grounds[2].width + 2400, section4.stable_grounds[0].y - 40))
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[2].x + section4.stable_grounds[2].width + 3000,section4.stable_grounds[0].y - 40))
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[0].x + 500,section4.stable_grounds[0].y - 40))
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[0].x + 1200,section4.stable_grounds[0].y - 40))
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.moving_grounds[0].x + section4.moving_grounds[0].width/2 - 15, section4.stable_grounds[0].y - 40))
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[3].x + 200, section4.stable_grounds[3].y - 40))
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[2].x + section4.stable_grounds[2].width + 3600, section4.stable_grounds[0].y - 40))
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[2].x + section4.stable_grounds[2].width + 4200,section4.stable_grounds[0].y - 40))

    for i in range(len(section4.stable_enemies)):
        section4.stable_enemies[i].setColor((255, 0, 0))


    # Items
    section4.items.append(interactive_object(20, 20, section4.stable_grounds[3].x + 200, section4.stable_grounds[3].y - 30))
    section4.items[0].setColor((255, 255, 0))

    section4.items.append(interactive_object(20, 20, section4.stable_grounds[8].x + 100, section4.stable_grounds[8].y - 30))
    section4.items[1].setColor((255, 255, 0))

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
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg_pos.append([section4.stable_grounds[7].x - 100, -HEIGHT])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), -HEIGHT])
    bg_pos.append([section4.stable_grounds[7].x - 100, bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), bg_pos[0][1] + bg[0].get_height()])
    startscrolling_x = WIDTH/2
    startscrolling_y = HEIGHT/2
    startbackground_x = 0
    startbackground_y = 0


def section4_gameplay():
    global  scenechange
    global section_area

    section_gameplay(section4)

    if (Anna.x >= WIDTH and scenechange == -1):
        section_area = 8
        scenechange = 0


def section5_init():
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
    section5.stable_grounds.append(ground(400, section5.stable_grounds[0].height, section5.stable_grounds[0].x - 1200, section5.stable_grounds[0].y))

    # Inititate the player
    global Anna
    Anna = player(35, 35, section5.stable_grounds[1].x + 100, section5.stable_grounds[1].y - 35)
    Anna.setColor((0, 0, 255))

    # Enemies
    section5.moving_enemies.append(enemy(30, 30, section5.stable_grounds[7].x, section5.stable_grounds[7].y - 30))
    section5.moving_enemies.append(enemy(30, 30, section5.stable_grounds[7].x + section5.stable_grounds[7].width - 30, section5.stable_grounds[7].y - 30))

    section5.moving_enemies[0].dir = -1

    for i in range(len(section5.moving_enemies)):
        section5.moving_enemies[i].setColor((255, 0, 0))

    section5.stable_enemies.append(shooting_enemy(30, 40, section5.stable_grounds[4].x + section5.stable_grounds[4].width - 15, section5.stable_grounds[4].y - 40))

    for i in range(len(section5.stable_enemies)):
        section5.stable_enemies[i].setColor((255, 0, 0))

    # Items
    section5.items.append(interactive_object(20, 20, section5.stable_grounds[6].x + 50, section5.stable_grounds[6].y - 30))
    section5.items[0].setColor((255, 255, 0))

    section5.items.append(interactive_object(20, 20, section5.stable_grounds[7].x + 50, section5.stable_grounds[7].y - 30))
    section5.items[1].setColor((255, 255, 0))

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
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg_pos.append([section5.stable_grounds[7].x, -HEIGHT])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), -HEIGHT])
    bg_pos.append([section5.stable_grounds[7].x, bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), bg_pos[0][1] + bg[0].get_height()])
    startscrolling_x = WIDTH/2
    startscrolling_y = HEIGHT/2
    startbackground_x = 0
    startbackground_y = 0


def section5_gameplay():
    global scenechange
    global section_area
    section_gameplay(section5)

    if (Anna.x >= WIDTH and scenechange == -1):
        section_area = 10
        scenechange = 0

def section6_init():
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

    # Inititate the player
    global Anna
    Anna = player(35, 35, section6.stable_grounds[4].x + 200, section6.stable_grounds[4].y - 35)
    Anna.setColor((0, 0, 255))

    # Enemies
    section6.moving_enemies.append(jumping_enemy(60, 60, section6.stable_grounds[0].x, section6.stable_grounds[0].y - 60))
    section6.moving_enemies.append(jumping_enemy(60, 60, section6.stable_grounds[6].x - 60, section6.stable_grounds[0].y - 60))
    section6.moving_enemies.append(jumping_enemy(60, 60, section6.stable_grounds[6].x + section6.stable_grounds[6].width, section6.stable_grounds[0].y - 60))

    section6.moving_enemies[1].dir = -1

    for i in range(len(section6.moving_enemies)):
        section6.moving_enemies[i].setColor((255, 0, 0))

    section6.moving_traps.append(moving_trap(300, 2000, section6.stable_grounds[3].x + section6.stable_grounds[3].width + 40, section6.stable_grounds[0].y + 200))
    section6.moving_traps[0].set_rangey(section6.stable_grounds[0].y - 300, section6.stable_grounds[0].y + 200)
    section6.moving_traps[0].setColor(BLACK)

    section6.moving_traps.append(moving_trap(300, 2000, section6.stable_grounds[2].x + section6.stable_grounds[2].width + 40, section6.stable_grounds[0].y + 200))
    section6.moving_traps[1].set_rangey(section6.stable_grounds[0].y - 300, section6.stable_grounds[0].y + 200)
    section6.moving_traps[1].setColor(BLACK)

    section6.moving_traps.append(moving_trap(300, 2000, section6.stable_grounds[1].x + section6.stable_grounds[1].width + 40, section6.stable_grounds[0].y + 200))
    section6.moving_traps[2].set_rangey(section6.stable_grounds[0].y - 300, section6.stable_grounds[0].y + 200)
    section6.moving_traps[2].setColor(BLACK)

    section6.moving_traps.append(moving_trap(300, 2000, section6.stable_grounds[0].x + section6.stable_grounds[0].width + 40, section6.stable_grounds[0].y + 200))
    section6.moving_traps[3].set_rangey(section6.stable_grounds[0].y - 300, section6.stable_grounds[0].y + 200)
    section6.moving_traps[3].setColor(BLACK)

    # Items
    section6.items.append(interactive_object(20, 20, section6.stable_grounds[2].x - 100, section6.stable_grounds[6].y - 150))
    section6.items[0].setColor((255, 255, 0))

    section6.items.append(interactive_object(20, 20, section6.stable_grounds[12].x + 1000, section6.stable_grounds[12].y - 30))
    section6.items[1].setColor((255, 255, 0))

    section6.items.append(interactive_object(20, 20, section6.stable_grounds[11].x + 50, section6.stable_grounds[11].y - 30))
    section6.items[2].setColor((255, 255, 0))

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
    bg.append(pygame.image.load('media/mountains.png').convert())
    bg_pos.append([section6.stable_grounds[11].x, -HEIGHT])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), -HEIGHT])
    bg_pos.append([section6.stable_grounds[11].x, bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), bg_pos[0][1] + bg[0].get_height()])
    startscrolling_x = WIDTH/2
    startscrolling_y = HEIGHT/2
    startbackground_x = 0
    startbackground_y = 0


def section6_gameplay():
    global  scenechange
    global section_area

    section_gameplay(section6)

    if (Anna.x >= WIDTH and scenechange == -1):
        section_area = 12
        scenechange = 0


def section7_init():
    # Initiate the first section
    global section7
    section7 = section()

    section7.waters.append(water(WIDTH, 2*HEIGHT, 0, 0))

    # Inititate the player
    global Anna
    Anna = player(35, 35, section7.waters[0].x + 200, section7.waters[0].y)
    Anna.setColor((0, 0, 255))


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
    global  scenechange
    global section_area
    section_gameplay(section7)

    if (Anna.x >= WIDTH and scenechange == -1):
        section_area = 14
        scenechange = 0



def section8_init():
    # Initiate the first section
    global section8
    section8 = section()

    section8.stable_grounds.append(ground(WIDTH, 2*HEIGHT, 0, 0))

    # Inititate the player
    global Anna
    Anna = player(35, 35, section8.stable_grounds[0].x + section8.stable_grounds[0].width - 100, section8.stable_grounds[0].y - 35)
    Anna.setColor((0, 0, 255))

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
    global  scenechange
    global section_area
    section_gameplay(section8)

    if (Anna.x >= WIDTH and scenechange == -1):
        section_area = 16
        scenechange = 0


# --- CODE STARTS HERE --- #
running = True

while running:
    for event in pygame.event.get():  # Returns all input and triggers into an array
        if (event.type == pygame.QUIT): # If the red X was clicked
            running = False


    pressedKey = pygame.key.get_pressed()
    #print(section_area)

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

    scene_change()

    pygame.display.update()
    clock.tick(FPS) # This will pause the game until the FPS time is reached


pygame.quit()