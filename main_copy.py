'''
    Title: Desomnia
    Author: Long Tieu, Wayne Seto, Ethan
    Date:

'''

from myCharacter import *
from myBackground import *
from mySection import *
from myObject import *
from myStats import *
from myCutscene import *
from myBackground_copy import *

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
global saving
global save_count
global endbackground1_x
global endbackground1_y
global endbackground2_x
global endbackground2_y
global endbackground3_x
global endbackground3_y
global endbackground4_x
global endbackground4_y
global endbackground5_x
global endbackground5_y
global endbackground6_x
global endbackground6_y
global start_x
global start_y
global end_x
global end_y
global flowers
global npc2_talk
global boss_trigger
global boss_fight
global big_boss
global cutscenelevel
global conversation

big_boss = boss(300, 200, 0, 0)
big_boss.setColor((255, 0, 0))

boss_trigger = trigger(50, HEIGHT, 0, 0)
boss_trigger.setColor((255, 255, 0))

flowers = []
npc2_talk = False
boss_fight = False

for i in range(3):
    flowers.append(interactive_object(20, 20, 0, 0))

section_area = 0
# bounderies need to be fixed in section area = 6
# if i die in section area 10, i teleported back to 8 level
# section 10 start is always on the edge, always die
# enemy in section 10, can kill anna in 2 hit
scenechange = 2
cutscenelevel = 0 # NORMAL LEVEL # 1 - INTRO # 2 - OUTRO
save_count = 0
saving = (6, 0, 0)

endbackground1_x = 0
endbackground1_y = 0
endbackground2_x = 0
endbackground2_y = 0
endbackground3_x = 0
endbackground3_y = 0
endbackground4_x = 0
endbackground4_y = 0
endbackground5_x = 0
endbackground5_y = 0
endbackground6_x = 0
endbackground6_y = 0

start_x = 0
start_y = 0
end_x = 0
end_y = 0

#### for testing to fix the error display surface quit ###
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

class instruction_point(interactive_object):
    def __init__(self, width, height, x=0, y=0, ar=0):
        interactive_object.__init__(self, width, height, x, y)
        self.area = ar
        self.surface = pygame.image.load('media/board.png').convert_alpha()

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

    def interact(self, pressedKey, player):
        # Add some interaction
        if (abs(player.x - self.x) <= 100):
            if (pressedKey[pygame.K_e]):
                # Add instructions
                return

def intro():
    global cutscenelevel
    global section_area
    cutscenelevel = 1
    section_area = 0
    return cutscenelevel


def section_gameplay(section):
    global startbackground_x
    global startbackground_y
    global saving
    global save_count
    global start_x
    global start_y
    global end_x
    global end_y
    global big_boss
    global boss_trigger
    global section_area
    global scenechange
    global Anna_paint
    global coins_collected
    global stars
    global coins_collect
    global flowers


    if (Anna.x + Anna.width / 2 > startscrolling_x):
        startbackground_x += Anna.x + Anna.width / 2 - startscrolling_x
        if (startbackground_x < end_x):
            section.move_x(-(Anna.x + Anna.width / 2 - startscrolling_x))
            big_boss.move_x(-(Anna.x + Anna.width / 2 - startscrolling_x))

            for i in range(len(stars)):
                stars[i].move_x(-(Anna.x + Anna.width / 2 - startscrolling_x))

            for i in range(len(flowers)):
                flowers[i].move_x(-(Anna.x + Anna.width / 2 - startscrolling_x))

            for i in range(len(big_boss.rocks)):
                big_boss.rocks[i].move_x(-(Anna.x + Anna.width / 2 - startscrolling_x))

            boss_trigger.move_x(-(Anna.x + Anna.width / 2 - startscrolling_x))

            Anna.setPos(startscrolling_x - Anna.width / 2, Anna.y)
        else:
            startbackground_x = end_x

    if (Anna.x + Anna.width / 2 < startscrolling_x):
        startbackground_x -= startscrolling_x - Anna.x - Anna.width / 2
        if (startbackground_x > start_x):
            section.move_x(startscrolling_x - Anna.x - Anna.width / 2)
            big_boss.move_x(startscrolling_x - Anna.x - Anna.width / 2)

            for i in range(len(stars)):
                stars[i].move_x(startscrolling_x - Anna.x - Anna.width / 2)

            for i in range(len(flowers)):
                flowers[i].move_x(startscrolling_x - Anna.x - Anna.width / 2)

            for i in range(len(big_boss.rocks)):
                big_boss.rocks[i].move_x(startscrolling_x - Anna.x - Anna.width / 2)

            boss_trigger.move_x(startscrolling_x - Anna.x - Anna.width / 2)

            Anna.setPos(startscrolling_x - Anna.width / 2, Anna.y)
        else:
            startbackground_x = start_x

    if (Anna.y + Anna.height / 2 > startscrolling_y):
        startbackground_y += Anna.y + Anna.height / 2 - startscrolling_y
        if (startbackground_y < end_y):
            section.move_y(-(Anna.y + Anna.height / 2 - startscrolling_y))
            big_boss.move_y(-(Anna.y + Anna.height / 2 - startscrolling_y))

            for i in range(len(stars)):
                stars[i].move_y(-(Anna.y + Anna.height / 2 - startscrolling_y))

            for i in range(len(flowers)):
                flowers[i].move_y(-(Anna.y + Anna.height / 2 - startscrolling_y))

            for i in range(len(big_boss.rocks)):
                big_boss.rocks[i].move_y(-(Anna.y + Anna.height / 2 - startscrolling_y))

            boss_trigger.move_y(-(Anna.y + Anna.height / 2 - startscrolling_y))

            Anna.setPos(Anna.x, startscrolling_y - Anna.height / 2)
        else:
            startbackground_y = end_y

    if (Anna.y + Anna.height / 2 < startscrolling_y):
        startbackground_y -= startscrolling_y - Anna.y - Anna.height / 2
        if (startbackground_y > start_y):
            section.move_y(startscrolling_y - Anna.y - Anna.height / 2)
            big_boss.move_y(startscrolling_y - Anna.y - Anna.height / 2)

            for i in range(len(stars)):
                stars[i].move_y(startscrolling_y - Anna.y - Anna.height / 2)

            for i in range(len(flowers)):
                flowers[i].move_y(startscrolling_y - Anna.y - Anna.height / 2)

            for i in range(len(big_boss.rocks)):
                big_boss.rocks[i].move_y(startscrolling_y - Anna.y - Anna.height / 2)

            boss_trigger.move_y(startscrolling_y - Anna.y - Anna.height / 2)

            Anna.setPos(Anna.x, startscrolling_y - Anna.height / 2)
        else:
            startbackground_y = start_y

    Anna.player_pickup(pressedKey, section.items)
    Anna.player_pickup(pressedKey, stars)

    if (conversation.dialogue_unlocked[12] == True):
        Anna.player_pickup(pressedKey, flowers)

    for i in range(len(section.items)):
        if (section.items[i].coin_check == True):
            section.items[i].coin_anim()

    star_count = 0
    for i in range(len(stars)):
        if (stars[i].collect == True):
            star_count += 1


    for i in range(len(section.items)):
        if (section.items[i].collect == True and section.items[i].check == False):
            coins_collect += 1
            section.items[i].check = True

    Anna.drawings.setText(str(star_count))
    Anna.coins.setText(str(coins_collect))

    Anna.player_swim(pressedKey, section.waters)

    ad, saving1 = section.saving_point.save_game(pressedKey, Anna, section_area-1)
    save_count += ad

    if (saving1[0] != -10):
        saving = saving1

    if (Anna.swim == False):
        Anna.playerMove(pressedKey,Anna.xspd, conversation)

    # moving enemies
    for i in range(len(section.moving_enemies)):
        section.moving_enemies[i].enemy_die()
        if (section.moving_enemies[i].hp > 0):
            section.moving_enemies[i].enemy_move(section.stable_grounds)

    for i in range(len(section.moving_enemies)):
        if (section.moving_enemies[i].hp > 0):
            section.moving_enemies[i].enemy_follow(Anna, section.stable_grounds)

    for i in range(len(section.stable_enemies)):
        if (section.stable_enemies[i].hp > 0):
            section.stable_enemies[i].enemy_follow(Anna, section)

    for i in range(len(section.bullets)):
        section.bullets[i].bullet_move(Anna)

    if (Anna.player_jump(pressedKey, section.stable_grounds, section.moving_grounds, conversation) == False):
        Anna.player_fall(Anna.yspd, section.stable_grounds, section.moving_grounds)

    if (Anna.swim == True):
        if (Anna.y + Anna.height > HEIGHT):
            Anna.setPos(Anna.x, HEIGHT - Anna.height)

    Anna.player_skill(pressedKey, Anna_paint, conversation)
    Anna.player_attack(pressedKey, section, conversation)
    Anna_brush.brush_move(Anna)
    Anna_brush.brush_hit(section.moving_enemies)
    Anna_brush.brush_hit(section.stable_enemies)
    Anna_brush1.brush_stay(Anna)

    Anna_paint.check_amount()

    for i in range(len(section.throw_stuffs)):
        section.throw_stuffs[i].stuff_move(section.moving_enemies, big_boss, section.stable_grounds, Anna_paint)

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

    for i in range(len(section.npc)):
        if (section.npc[i].talk):
            section.npc[i].npc_talk(pressedKey, Anna)

    if (Anna.y > HEIGHT):
        Anna.hp = 0


    section.saving_point.save_anim()

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
        for j in range(len(section.stable_grounds[i].images)):
            screen.blit(section.stable_grounds[i].images[j].getSurface(), section.stable_grounds[i].images[j].getPos())

    for i in range(len(section.backgrounds)):
        screen.blit(section.backgrounds[i].getSurface(), section.backgrounds[i].getPos())

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

    for i in range(len(section.gates)):
        screen.blit(section.gates[i].getSurface(), section.gates[i].getPos())

    for i in range(len(section.instruction_points)):
        screen.blit(section.instruction_points[i].getSurface(), section.instruction_points[i].getPos())

    for i in range(len(section.control_panels)):
        screen.blit(section.control_panels[i].getSurface(), section.control_panels[i].getPos())

    for i in range(len(section.bullets)):
        screen.blit(section.bullets[i].getSurface(), section.bullets[i].getPos())

    for i in range(len(Anna.hp_bars)):
        screen.blit(Anna.hp_bars[i].getSurface(), Anna.hp_bars[i].getPos())

    for i in range(len(section.throw_stuffs)):
        screen.blit(section.throw_stuffs[i].getSurface(), section.throw_stuffs[i].getPos())

    screen.blit(section.saving_point.getSurface(), section.saving_point.getPos())
    screen.blit(Anna.getSurface(), Anna.getPos())
    if (Anna_brush.appear == True):
        screen.blit(Anna_brush.getSurface(), Anna_brush.getPos())

    if (Anna_brush1.appear == True):
        screen.blit(Anna_brush1.getSurface(), Anna_brush1.getPos())

    screen.blit(Anna_paint.getSurface(), Anna_paint.getPos())
    screen.blit(Anna.drawings.getText(), Anna.drawings.gettextpos())
    screen.blit(Anna.drawing_UI.getSurface(), Anna.drawing_UI.getPos())
    screen.blit(Anna.coins.getText(), Anna.coins.gettextpos())
    screen.blit(Anna.coin_UI.getSurface(), Anna.coin_UI.getPos())

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
    global  endbackground1_x
    global  endbackground1_y

    section1 = section()
    section1.stable_grounds.append(ground(WIDTH, 100, 0, HEIGHT - 100))
    section1.stable_grounds.append(ground(150, 40, section1.stable_grounds[0].x + section1.stable_grounds[0].width + 200, 300))
    section1.stable_grounds.append(ground(WIDTH + 200, 100, section1.stable_grounds[1].x + section1.stable_grounds[1].width + 250, HEIGHT - 100))
    section1.stable_grounds.append(ground(WIDTH + 350, 150, section1.stable_grounds[1].x + section1.stable_grounds[1].width + 140, section1.stable_grounds[2].y + section1.stable_grounds[2].height))
    section1.stable_grounds.append(ground(2100, 600, 0, section1.stable_grounds[3].y + section1.stable_grounds[3].height))
    section1.stable_grounds.append(ground(500, 260, section1.stable_grounds[2].x + section1.stable_grounds[2].width - 700, section1.stable_grounds[2].y - 260))
    section1.stable_grounds.append(ground(section1.stable_grounds[0].width + 100, section1.stable_grounds[2].height + section1.stable_grounds[3].height + section1.stable_grounds[4].height, section1.stable_grounds[2].x + section1.stable_grounds[2].width + 1000, section1.stable_grounds[3].y))
    section1.stable_grounds.append(ground(1000, 100, section1.stable_grounds[3].x + section1.stable_grounds[3].width, section1.stable_grounds[3].y))
    section1.stable_grounds.append(ground(100, 50, section1.stable_grounds[2].x + section1.stable_grounds[2].width + 150, section1.stable_grounds[3].y - 200))

    endbackground1_x = section1.stable_grounds[6].x + 500
    endbackground1_y = section1.stable_grounds[6].y

    ### Background decoration
    section1.backgrounds.append(image('media/bush00.png', 100, 100, 300, 200))
    section1.backgrounds.append(image('media/bush00.png', 20, 20, 300, 400))
    print(section1.backgrounds[0])

    section1.moving_npc.append(moving_npc(30, 30, section1.stable_grounds[4].x + 300, section1.stable_grounds[4].y - 30))
    section1.moving_npc[0].set_rangex(section1.stable_grounds[4].x + 300, section1.stable_grounds[4].x + 600)

    section1.moving_npc.append(moving_npc(30, 30, section1.stable_grounds[4].x + 300, section1.stable_grounds[4].y - 30))
    section1.moving_npc[1].set_rangex(section1.stable_grounds[4].x + 1000, section1.stable_grounds[4].x + 1200)


    section1.items.append(interactive_object(20, 20, section1.stable_grounds[5].x + 50, section1.stable_grounds[5].y - 30))
    section1.items[0].setColor((255, 255, 0))

    section1.npc.append(npc(30, 30, section1.stable_grounds[6].x + 100, section1.stable_grounds[6].y - 30))
    section1.npc.append(npc(30, 30, section1.stable_grounds[6].x + 250, section1.stable_grounds[6].y - 30))
    section1.npc.append(npc(30, 30, section1.stable_grounds[6].x + 500, section1.stable_grounds[6].y - 30))
    section1.npc.append(npc(30, 30, section1.stable_grounds[6].x + 700, section1.stable_grounds[6].y - 30))

    section1.moving_npc.append(moving_npc(30, 30, section1.stable_grounds[6].x + 10, section1.stable_grounds[6].y - 30, 0.1))
    section1.moving_npc[2].set_rangex(section1.stable_grounds[6].x, section1.npc[3].x - 30)



    section1.instruction_points.append(instruction_point(50, 50, section1.stable_grounds[0].x + 200, section1.stable_grounds[0].y - 50))

    # Set up boundaries
    global start_x
    global start_y
    global end_x
    global end_y

    start_x = section1.stable_grounds[0].x
    start_y = -HEIGHT
    end_x = section1.stable_grounds[6].x
    end_y = section1.stable_grounds[4].y + section1.stable_grounds[4].height

    # Inititate the player
    global Anna
    global saving
    global save_count
    Anna = player(35, 35, section1.stable_grounds[0].x + 200, section1.stable_grounds[0].y - 35)
    if (save_count > 0):
        Anna.setPos(saving[1], saving[2])

    Anna.setColor((0, 0, 255))
    Anna.hp_bars.append(hp_bar(20, 20, 100, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 150, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 200, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 250, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 300, 50))

    global Anna_brush
    global Anna_brush1
    Anna_brush = brush(60, 10, Anna.x + Anna.width, Anna.y)
    Anna_brush1 = brush(10, 60, Anna.x + Anna.width, Anna.y, 0)

    global Anna_paint
    Anna_paint = paint_bar(60, 60, 20, 20)

    section1.saving_point = save_point(100, 20, section1.stable_grounds[6].x + 200, section1.stable_grounds[6].y - 20)

    # Initiate background image
    global bg
    global bg_pos
    global startscrolling_x
    global startscrolling_y
    global startbackground_x
    global startbackground_y
    bg = []
    bg_pos = []
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
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
    global saving
    global big_boss

    if (scenechange != 1):
        section_gameplay(section1)

    if (Anna.x < 0):
        Anna.setPos(0, Anna.y)

    if (Anna.x >= WIDTH and scenechange == -1):
        section_area = 2
        saving = (2, 0, HEIGHT - 100)
        scenechange = 0

def section2_init():
    # Initiate the first section
    global section2
    global endbackground2_x
    global endbackground2_y
    section2 = section()

    section2.stable_grounds.append(ground(WIDTH + 500, 500, 0, HEIGHT - 100))
    section2.stable_grounds.append(ground(400, 300, section2.stable_grounds[0].x + section2.stable_grounds[0].width - 700, section2.stable_grounds[0].y - 300))
    section2.stable_grounds.append(ground(200, 50, section2.stable_grounds[0].x + section2.stable_grounds[0].width + 200, section2.stable_grounds[1].y + 50))
    section2.stable_grounds.append(ground(200, 50, section2.stable_grounds[2].x + section2.stable_grounds[2].width + 200, section2.stable_grounds[2].y))
    section2.stable_grounds.append(ground(200, 50, section2.stable_grounds[3].x + section2.stable_grounds[3].width + 200, section2.stable_grounds[3].y))
    section2.stable_grounds.append(ground(2 * WIDTH, 500, section2.stable_grounds[4].x + section2.stable_grounds[4].width + 200, HEIGHT - 100))
    section2.stable_grounds.append(ground(section2.stable_grounds[5].width, 100, section2.stable_grounds[5].x, section2.stable_grounds[5].y + section2.stable_grounds[5].height + 150))
    section2.stable_grounds.append(ground(section2.stable_grounds[5].width, 100, section2.stable_grounds[5].x, section2.stable_grounds[6].y + section2.stable_grounds[6].height + 150))
    section2.stable_grounds.append(ground(500, 60, section2.stable_grounds[5].x + section2.stable_grounds[5].width + 200, section2.stable_grounds[5].y - 250))
    section2.stable_grounds.append(ground(500, 60, section2.stable_grounds[5].x + section2.stable_grounds[5].width + 200, section2.stable_grounds[8].y - 200))
    section2.stable_grounds.append(ground(400, 2*WIDTH, section2.stable_grounds[9].x + 100, section2.stable_grounds[9].y - 100))
    section2.stable_grounds.append(ground(400, 150, section2.stable_grounds[5].x + 700, section2.stable_grounds[5].y - 150))
    section2.stable_grounds.append(ground(150, 50, section2.stable_grounds[11].x - 200, section2.stable_grounds[11].y - 100))
    section2.stable_grounds.append(ground(50, 50, section2.stable_grounds[12].x - 100, section2.stable_grounds[12].y - 100))
    section2.stable_grounds.append(ground(150, 50, section2.stable_grounds[11].x + 50, section2.stable_grounds[13].y - 100))

    section2.waters.append(water(7 * WIDTH, 2000, section2.stable_grounds[0].x, section2.stable_grounds[0].y + 100))

    endbackground2_x = section2.waters[0].x + section2.waters[0].width - 900
    endbackground2_y = section2.waters[0].y

    section2.instruction_points.append(instruction_point(50, 50, section2.stable_grounds[1].x + 200, section2.stable_grounds[1].y - 50))

    # Traps
    section2.traps.append(trap(50, section2.waters[0].height, section2.stable_grounds[5].x - 50, section2.waters[0].y))

    section2.moving_traps.append(moving_trap(100, 2000, section2.stable_grounds[0].x + 200, section2.waters[0].y + 200))
    section2.moving_traps[0].set_rangey(section2.waters[0].y + 300, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(100, 2000, section2.moving_traps[0].x + section2.moving_traps[0].width + 300, section2.waters[0].y + 200))
    section2.moving_traps[1].set_rangey(section2.waters[0].y + 300, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(100, 2000, section2.moving_traps[1].x + section2.moving_traps[1].width + 300, section2.waters[0].y + 200))
    section2.moving_traps[2].set_rangey(section2.waters[0].y + 300, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(100, 2000, section2.moving_traps[2].x + section2.moving_traps[2].width + 300, section2.waters[0].y + 200))
    section2.moving_traps[3].set_rangey(section2.waters[0].y + 300, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(100, 2000, section2.moving_traps[3].x + section2.moving_traps[3].width + 300, section2.waters[0].y + 200))
    section2.moving_traps[4].set_rangey(section2.waters[0].y + 300, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(100, 2000, section2.moving_traps[4].x + section2.moving_traps[4].width + 300, section2.waters[0].y + 200))
    section2.moving_traps[5].set_rangey(section2.waters[0].y + 300, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(100, 2000, section2.moving_traps[5].x + section2.moving_traps[5].width + 300, section2.waters[0].y + 200))
    section2.moving_traps[6].set_rangey(section2.waters[0].y + 100, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(100, 2000, section2.moving_traps[6].x + section2.moving_traps[6].width + 300, section2.waters[0].y + 200))
    section2.moving_traps[7].set_rangey(section2.waters[0].y + 200, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(100, 2000, section2.moving_traps[7].x + section2.moving_traps[7].width + 300, section2.waters[0].y + 200))
    section2.moving_traps[8].set_rangey(section2.waters[0].y + 50, section2.stable_grounds[0].y + 1000)

    # Set up the boundaries
    global start_x
    global start_y
    global end_x
    global end_y

    start_x = section2.stable_grounds[0].x
    start_y = -HEIGHT
    end_x = section2.stable_grounds[10].x
    end_y = section2.stable_grounds[7].y

    # Inititate the player
    global Anna
    global saving
    global save_count
    Anna = player(35, 35, section2.stable_grounds[0].x, section2.stable_grounds[0].y - 35)
    if (save_count > 0):
        Anna.setPos(saving[1] - 50, saving[2])

    Anna.setColor((0, 0, 255))
    Anna.hp_bars.append(hp_bar(20, 20, 100, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 150, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 200, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 250, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 300, 50))

    global Anna_brush
    global Anna_brush1
    Anna_brush = brush(60, 10, Anna.x + Anna.width, Anna.y)
    Anna_brush1 = brush(10, 60, Anna.x + Anna.width, Anna.y, 0)

    global Anna_paint
    Anna_paint = paint_bar(60, 60, 20, 20)

    section2.saving_point = save_point(100, 20, section2.stable_grounds[1].x + 10, section2.stable_grounds[1].y - 20)

    # NPC
    section2.moving_npc.append(moving_npc(30, 30, section2.stable_grounds[0].x, section2.stable_grounds[0].y - 30))
    section2.moving_npc[0].set_rangex(section2.stable_grounds[0].x, section2.stable_grounds[1].x - 130)

    section2.moving_npc.append(moving_npc(30, 30, section2.moving_npc[0].x + section2.moving_npc[0].width + 100, section2.stable_grounds[0].y - 30))
    section2.moving_npc[1].set_rangex(section2.moving_npc[1].x, section2.stable_grounds[1].x - 30)


    section2.hor_ground = 1

    section2.moving_grounds.append(moving_ground(150, 50, section2.stable_grounds[0].x, section2.moving_npc[0].y - 50))
    section2.moving_grounds[0].set_rangex(section2.moving_npc[0].x, section2.stable_grounds[1].x)
    section2.moving_grounds[0].xspd = 1
    section2.moving_grounds[0].set_rangey(section2.moving_grounds[0].y, section2.moving_grounds[0].y)


    # Enemies
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[5].x + 300, section2.stable_grounds[5].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[5].x + 1000, section2.stable_grounds[5].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[11].x, section2.stable_grounds[11].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[5].x + 1400, section2.stable_grounds[5].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[6].x, section2.stable_grounds[6].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[7].x, section2.stable_grounds[7].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[8].x, section2.stable_grounds[8].y - 30))
    section2.moving_enemies.append(enemy(30, 30, section2.stable_grounds[9].x, section2.stable_grounds[9].y - 30))

    section2.moving_enemies[1].dir = -1
    section2.moving_enemies[2].dir = -1

    section2.items.append(interactive_object(20, 20, section2.stable_grounds[14].x + 50, section2.stable_grounds[14].y - 30))
    section2.items[0].setColor((255, 255, 0))


    for i in range(len(section2.moving_enemies)):
        section2.moving_enemies[i].setScale(60, 60)


    # Initiate background image
    global bg
    global bg_pos
    global startscrolling_x
    global startscrolling_y
    global startbackground_x
    global startbackground_y
    bg = []
    bg_pos = []
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
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
    global endbackground1_x
    global  endbackground1_y
    global saving
    global save_count
    global big_boss

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
        save_count += 1
        saving = (0, 0, 665)
        scenechange = 0

    if (Anna.x <= -Anna.width and scenechange == -1):
        section_area = 0
        save_count += 1
        saving = (0, 2200 + 2*WIDTH, HEIGHT - 50)
        scenechange = 0

    if (Anna.hp <= 0):
        section_area = 2
        scenechange = 0

def section3_init(): # Add 1 more trap
    # Initiate the first section
    global section3
    global start_move
    global move_count
    start_move = False
    move_count = 0

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
    section3.stable_grounds.append(ground(100, 50, section3.stable_grounds[1].x + section3.stable_grounds[1].width, section3.stable_grounds[11].y - 150))
    section3.stable_grounds.append(ground(100, 50, section3.stable_grounds[4].x - 100, section3.stable_grounds[14].y - 100))
    section3.stable_grounds.append(ground(100, 50, section3.stable_grounds[1].x + section3.stable_grounds[1].width, section3.stable_grounds[15].y - 150))
    section3.stable_grounds.append(ground(50, 2000, section3.stable_grounds[13].x + section3.stable_grounds[13].width, section3.stable_grounds[13].y - 500))

    section3.moving_grounds.append(moving_ground(100, 50, section3.stable_grounds[0].x + section3.stable_grounds[0].width + 200, section3.stable_grounds[0].y - 160))
    section3.moving_grounds[0].set_rangex(section3.stable_grounds[0].x + section3.stable_grounds[0].width, section3.stable_grounds[1].x + 100)
    section3.moving_grounds[0].set_rangey(section3.moving_grounds[0].y, section3.moving_grounds[0].y)

    section3.moving_grounds.append(moving_ground(200, 50, section3.stable_grounds[0].x + section3.stable_grounds[0].width + 200, section3.stable_grounds[0].y - 320))
    section3.moving_grounds[1].set_rangex(section3.stable_grounds[0].x + section3.stable_grounds[0].width - 100, section3.stable_grounds[1].x + 100)
    section3.moving_grounds[1].set_rangey(section3.moving_grounds[1].y, section3.moving_grounds[1].y)


    section3.moving_grounds.append(moving_ground(200, 50, section3.stable_grounds[0].x - 400, section3.stable_grounds[0].y - 480))
    section3.moving_grounds[2].set_rangex(section3.stable_grounds[0].x + section3.stable_grounds[0].width - 200, section3.stable_grounds[1].x + 100)
    section3.moving_grounds[2].set_rangey(section3.moving_grounds[2].y, section3.moving_grounds[2].y)

    section3.moving_grounds.append(moving_ground(200, 50, section3.stable_grounds[0].x - 400, section3.stable_grounds[0].y - 640))
    section3.moving_grounds[3].set_rangex(section3.stable_grounds[0].x + section3.stable_grounds[0].width - 300, section3.stable_grounds[1].x + 100)
    section3.moving_grounds[3].set_rangey(section3.moving_grounds[3].y, section3.moving_grounds[3].y)


    global endbackground3_x
    global endbackground3_y

    endbackground3_x = section3.stable_grounds[8].x
    endbackground3_x = section3.stable_grounds[11].y


    # Enemies
    section3.moving_enemies.append(enemy(30, 30, section3.stable_grounds[0].x + 600, section3.stable_grounds[0].y - 30))
    section3.moving_enemies.append(enemy(30, 30, section3.stable_grounds[11].x, section3.stable_grounds[11].y - 30))
    section3.moving_enemies.append(enemy(30, 30, section3.stable_grounds[11].x + 700, section3.stable_grounds[11].y - 30))
    section3.moving_enemies.append(enemy(30, 30, section3.stable_grounds[11].x + 1000, section3.stable_grounds[11].y - 30))
    section3.moving_enemies.append(enemy(30, 30, section3.stable_grounds[11].x + 1300, section3.stable_grounds[11].y - 30))
    section3.moving_enemies.append(enemy(30, 30, section3.stable_grounds[13].x, section3.stable_grounds[13].y - 30))

    section3.moving_enemies[0].dir = -1

    for i in range(len(section3.moving_enemies)):
        section3.moving_enemies[i].setColor((255, 0, 0))

    # Set up the boundaries
    global start_x
    global start_y
    global end_x
    global end_y

    start_x = section3.stable_grounds[0].x
    start_y = -HEIGHT
    end_x = section3.stable_grounds[13].x
    end_y = section3.stable_grounds[11].y

    # Inititate the player
    global Anna
    global saving
    global save_count
    Anna = player(35, 35, section3.stable_grounds[0].x, section3.stable_grounds[0].y - 35)
    if (save_count > 0):
        Anna.setPos(saving[1], saving[2])

    Anna.setColor((0, 0, 255))
    Anna.hp_bars.append(hp_bar(20, 20, 100, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 150, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 200, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 250, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 300, 50))

    global Anna_brush
    global Anna_brush1
    Anna_brush = brush(60, 10, Anna.x + Anna.width, Anna.y)
    Anna_brush1 = brush(10, 60, Anna.x + Anna.width, Anna.y, 0)

    global Anna_paint
    Anna_paint = paint_bar(60, 60, 20, 20)

    section3.saving_point = save_point(100, 20, section3.stable_grounds[1].x + 10, section3.stable_grounds[1].y - 20)

    # Items
    section3.items.append(interactive_object(20, 20, section3.stable_grounds[1].x + 100, section3.stable_grounds[1].y - 30))
    section3.items[0].setColor((255, 255, 0))

    section3.items.append(interactive_object(20, 20, section3.stable_grounds[10].x + 50, section3.stable_grounds[10].y - 30))
    section3.items[1].setColor((255, 255, 0))

    section3.items.append(interactive_object(50, 60, section3.stable_grounds[13].x + section3.stable_grounds[13].width - 50, section3.stable_grounds[13].y - 60))
    section3.items[2].setColor((255, 255, 0))

    section3.gates.append(gate(50, 60, section3.stable_grounds[8].x + 200, section3.stable_grounds[8].y - 60))

    section3.instruction_points.append(instruction_point(50, 50, section3.stable_grounds[1].x + 200, section3.stable_grounds[1].y - 50))


    section3.control_panels.append(control_panel(40, 40, section3.stable_grounds[4].x + section3.stable_grounds[13].width - 100, section3.stable_grounds[4].y - 40))

    section3.hor_ground = 4

    # trap
    section3.traps.append(trap(section3.stable_grounds[2].width, section3.stable_grounds[1].height, section3.stable_grounds[1].x - section3.stable_grounds[2].width, section3.stable_grounds[1].y))
    section3.traps.append(trap(section3.stable_grounds[6].x - section3.stable_grounds[4].x - section3.stable_grounds[4].width, section3.stable_grounds[6].height, section3.stable_grounds[4].x + section3.stable_grounds[4].width, section3.stable_grounds[6].y))
    section3.traps.append(trap(section3.stable_grounds[7].x - section3.stable_grounds[6].x - section3.stable_grounds[6].width, section3.stable_grounds[7].height, section3.stable_grounds[6].x + section3.stable_grounds[6].width, section3.stable_grounds[7].y))
    section3.traps.append(trap(section3.stable_grounds[8].x - section3.stable_grounds[7].x - section3.stable_grounds[7].width, section3.stable_grounds[8].height, section3.stable_grounds[7].x + section3.stable_grounds[7].width, section3.stable_grounds[8].y))
    section3.traps.append(trap(section3.stable_grounds[12].width, 100,section3.stable_grounds[12].x, section3.stable_grounds[12].y - 100))

    # Initiate background image
    global bg
    global bg_pos
    global startscrolling_x
    global startscrolling_y
    global startbackground_x
    global startbackground_y
    bg = []
    bg_pos = []
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
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
    global saving
    global endbackground2_x
    global endbackground2_y
    global save_count
    global start_move
    global move_count
    global big_boss

    section_gameplay(section3)
    section3.gates[0].enter_gate(pressedKey, Anna)

    if (section3.gates[0].active == True and scenechange == -1):
        section_area = 6
        saving = (6, 50, HEIGHT - 585)
        scenechange = 0

    if (Anna.x <= -Anna.width and scenechange == -1):
        save_count += 1
        section_area = 2
        saving = (2, endbackground2_x - Anna.width - 50, endbackground2_y - Anna.y)
        scenechange = 0

    if (Anna.x > WIDTH - Anna.width):
        Anna.setPos(WIDTH - Anna.width, Anna.y)


    if (section3.items[2].x <= -5000 and section3.items[2].y <= -5000):
        section3.control_panels[0].interact(pressedKey, Anna)
        if (section3.control_panels[0].active == True and move_count == 0):
            start_move = True

    if (start_move == True):
        section3.stable_grounds[6].setPos(section3.stable_grounds[6].x, section3.stable_grounds[6].y - 10)
        section3.stable_grounds[7].setPos(section3.stable_grounds[7].x, section3.stable_grounds[7].y - 10)
        move_count += 10

        if (move_count >= 300):
            start_move = False



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
    section4.stable_grounds.append(ground(500, 1100, section4.stable_grounds[0].x + section4.stable_grounds[0].width, section4.stable_grounds[0].y + 150))
    section4.stable_grounds.append(ground(200, 50, 2500, section4.stable_grounds[0].y - 150))
    section4.stable_grounds.append(ground(200, 50, section4.stable_grounds[10].x + section4.stable_grounds[10].width + 100, section4.stable_grounds[10].y - 150))
    section4.stable_grounds.append(ground(200, 50, section4.stable_grounds[11].x + section4.stable_grounds[11].width + 100, section4.stable_grounds[11].y - 150))
    section4.stable_grounds.append(ground(100, 50, section4.stable_grounds[8].x + section4.stable_grounds[8].width + 200, section4.stable_grounds[8].y + 100))
    section4.stable_grounds.append(ground(100, 50, section4.stable_grounds[3].x - 300, section4.stable_grounds[3].y))
    section4.stable_grounds.append(ground(100, 50, section4.stable_grounds[12].x + section4.stable_grounds[12].width + 300, section4.stable_grounds[12].y - 150))


    section4.waters.append(water(WIDTH - section4.stable_grounds[8].width, 1000, section4.stable_grounds[8].x + section4.stable_grounds[8].width, section4.stable_grounds[9].y + 100))
    # Set up the boundaries
    global start_x
    global start_y
    global end_x
    global end_y

    start_x = section4.stable_grounds[7].x
    start_y = -2*HEIGHT
    end_x = section4.stable_grounds[0].x + section4.stable_grounds[0].width
    end_y = section4.stable_grounds[0].y

    # Traps
    section4.traps.append(trap(section4.stable_grounds[0].x - section4.stable_grounds[7].x, 200, section4.stable_grounds[7].x, section4.stable_grounds[0].y + 100))

    # Inititate the player
    global Anna
    global saving
    global save_count
    Anna = player(35, 35, section4.stable_grounds[2].x + 50, section4.stable_grounds[2].y - 35)
    if (save_count > 0):
        Anna.setPos(saving[1], saving[2])

    Anna.setColor((0, 0, 255))
    Anna.hp_bars.append(hp_bar(20, 20, 100, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 150, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 200, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 250, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 300, 50))

    global Anna_brush
    global Anna_brush1
    Anna_brush = brush(60, 10, Anna.x + Anna.width, Anna.y)
    Anna_brush1 = brush(10, 60, Anna.x + Anna.width, Anna.y, 0)

    global Anna_paint
    Anna_paint = paint_bar(60, 60, 20, 20)

    section4.saving_point = save_point(100, 20, section4.stable_grounds[1].x + 10, section4.stable_grounds[1].y - 20)


    # Enemies
    section4.moving_enemies.append(enemy(30, 30, 700, section4.stable_grounds[0].y - 30))
    section4.moving_enemies.append(enemy(30, 30, 2000, section4.stable_grounds[0].y - 30))
    #section4.moving_enemies.append(enemy(30, 30, section4.stable_grounds[1].x, section4.stable_grounds[1].y - 30))
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
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[8].x + 100,section4.stable_grounds[8].y - 40))
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[0].x + 1200,section4.stable_grounds[0].y - 40))
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[14].x + section4.stable_grounds[14].width/2 - 15, section4.stable_grounds[0].y - 40))
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[3].x + 200, section4.stable_grounds[3].y - 40))
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[2].x + section4.stable_grounds[2].width + 3600, section4.stable_grounds[0].y - 40))
    section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[2].x + section4.stable_grounds[2].width + 4200,section4.stable_grounds[0].y - 40))

    for i in range(len(section4.stable_enemies)):
        section4.stable_enemies[i].setColor((255, 0, 0))


    # Npc
    section4.npc.append(npc(30, 30, section4.stable_grounds[9].x + section4.stable_grounds[9].width - 30, section4.stable_grounds[9].y - 30))
    section4.npc.append(npc(50, 50, section4.stable_grounds[1].x + 100, section4.stable_grounds[1].y - 50))
    section4.npc.append(npc(70, 70, section4.stable_grounds[0].x + section4.stable_grounds[0].width - 200, section4.stable_grounds[0].y - 70))

    # Items
    section4.items.append(drawing_piece(20, 20, section4.stable_grounds[12].x + 100, section4.stable_grounds[12].y - 40))

    section4.gates.append(gate(50, 60, section4.stable_grounds[2].x + 50, section4.stable_grounds[2].y - 60))

    section4.gates.append(gate(50, 60, section4.stable_grounds[15].x + 50, section4.stable_grounds[15].y - 60))

    section4.gates.append(gate(50, 60, section4.stable_grounds[3].x + 50, section4.stable_grounds[3].y - 60))

    # Initiate background image
    global bg
    global bg_pos
    global startscrolling_x
    global startscrolling_y
    global startbackground_x
    global startbackground_y
    bg = []
    bg_pos = []
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg_pos.append([section4.stable_grounds[0].x, -HEIGHT])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), -HEIGHT])

    bg_pos.append([section4.stable_grounds[0].x, bg_pos[0][1] + bg[0].get_height()])
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
    global save_count
    global saving
    global end_x
    global big_boss

    section4.gates[0].enter_gate(pressedKey, Anna)
    section4.gates[1].enter_gate(pressedKey, Anna)
    section4.gates[2].enter_gate(pressedKey, Anna)

    # Count flowers collected
    flowercount = 0
    for i in range(len(flowers)):
        if (flowers[i].collect == True):
            flowercount += 1

    if (flowercount == 0):
        section4.npc[2].npc_talk(pressedKey, Anna)
        # load some other dialogues
        #conversation1 = dialogue
    elif (flowercount < len(flowers)):
        section4.npc[2].npc_talk(pressedKey, Anna)
        # load some dialogues
    else:
        section4.npc[2].npc_talk(pressedKey, Anna)

    if (flowercount < len(flowers)):
        if (Anna.x >= end_x - 100):
            Anna.x = section4.stable_grounds[1].x + section4.stable_grounds[1].width + 100
            Anna.setPos(Anna.x, Anna.y)

    section_gameplay(section4)


    if (section4.gates[0].active == True and scenechange == -1):
        section_area = 4
        save_count += 1
        saving = (4, 4800, -40)
        scenechange = 0

    if (section4.gates[1].active == True and scenechange == -1):
        section_area = 8
        save_count += 1
        saving = (8, 700, HEIGHT - 200)
        scenechange = 0

    if (section4.gates[2].active == True and scenechange == -1):
        section_area = 10
        save_count += 1
        saving = (10, 2500, HEIGHT - 300)
        scenechange = 0

    if (Anna.x >= WIDTH and scenechange == -1):
        section_area = 14
        save_count += 1
        saving = (14, 0, 720)
        scenechange = 0


def section5_init():
    # Initiate the first section
    global section5
    global flowers

    section5 = section()

    section5.stable_grounds.append(ground(1000, 500, -500, HEIGHT - 100))
    section5.stable_grounds.append(ground(100, 50, section5.stable_grounds[0].x + section5.stable_grounds[0].width + 150, section5.stable_grounds[0].y))
    section5.stable_grounds.append(ground(100, 50, section5.stable_grounds[1].x + section5.stable_grounds[1].width + 150, section5.stable_grounds[1].y - 150))
    section5.stable_grounds.append(ground(400, 100, section5.stable_grounds[2].x + section5.stable_grounds[2].width + 150, section5.stable_grounds[2].y))
    section5.stable_grounds.append(ground(250, 60, section5.stable_grounds[3].x + section5.stable_grounds[3].width - 250,section5.stable_grounds[3].y - 60))
    section5.stable_grounds.append(ground(100, 50, section5.stable_grounds[4].x  - 250, section5.stable_grounds[4].y - 150))
    section5.stable_grounds.append(ground(100, 50, section5.stable_grounds[5].x - 250, section5.stable_grounds[5].y - 200))
    section5.stable_grounds.append(ground(400, section5.stable_grounds[0].height, section5.stable_grounds[0].x - 1200, section5.stable_grounds[0].y))

    # Set up the boundaries
    global start_x
    global start_y
    global end_x
    global end_y

    start_x = section5.stable_grounds[7].x
    start_y = -2 * HEIGHT
    end_x = section5.stable_grounds[4].x
    end_y = section5.stable_grounds[7].y

    # Inititate the player
    global Anna
    global saving
    global save_count
    Anna = player(35, 35, section5.stable_grounds[1].x + 100, section5.stable_grounds[1].y - 35)
    if (save_count > 0):
        Anna.setPos(saving[1], saving[2])

    Anna.setColor((0, 0, 255))
    Anna.hp_bars.append(hp_bar(20, 20, 100, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 150, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 200, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 250, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 300, 50))

    global Anna_brush
    global Anna_brush1
    Anna_brush = brush(60, 10, Anna.x + Anna.width, Anna.y)
    Anna_brush1 = brush(10, 60, Anna.x + Anna.width, Anna.y, 0)

    global Anna_paint
    Anna_paint = paint_bar(60, 60, 20, 20)


    # Enemies
    section5.moving_enemies.append(enemy(30, 30, section5.stable_grounds[7].x, section5.stable_grounds[7].y - 30))
    section5.moving_enemies.append(enemy(30, 30, section5.stable_grounds[7].x + section5.stable_grounds[7].width - 30, section5.stable_grounds[7].y - 30))

    section5.moving_enemies[0].dir = -1

    for i in range(len(section5.moving_enemies)):
        section5.moving_enemies[i].setColor((255, 0, 0))

    section5.stable_enemies.append(shooting_enemy(30, 40, section5.stable_grounds[4].x + section5.stable_grounds[4].width - 15, section5.stable_grounds[4].y - 40))

    for i in range(len(section5.stable_enemies)):
        section5.stable_enemies[i].setColor((255, 0, 0))

    section5.waters.append(water(section5.stable_grounds[0].x - section5.stable_grounds[7].x - section5.stable_grounds[7].width, 500, section5.stable_grounds[7].x + section5.stable_grounds[7].width, section5.stable_grounds[7].y + 200))

    # Items
    section5.items.append(drawing_piece(20, 20, section5.stable_grounds[6].x + 50, section5.stable_grounds[6].y - 40))
    section5.items.append(drawing_piece(20, 20, section5.stable_grounds[7].x + 50, section5.stable_grounds[7].y - 40))

    flowers[0].setPos(section5.stable_grounds[7].x + 50, section5.stable_grounds[7].y - 30)
    flowers[0].surface = pygame.image.load('media/flower.png').convert_alpha()

    flowers[1].setPos(section5.stable_grounds[5].x + 50, section5.stable_grounds[5].y - 30)
    flowers[1].surface = pygame.image.load('media/flower.png').convert_alpha()

    section5.gates.append(gate(40, 60, section5.stable_grounds[1].x + 50, section5.stable_grounds[1].y - 60))

    # Initiate background image
    global bg
    global bg_pos
    global startscrolling_x
    global startscrolling_y
    global startbackground_x
    global startbackground_y
    bg = []
    bg_pos = []
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg_pos.append([section5.stable_grounds[0].x, -HEIGHT])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), -HEIGHT])

    bg_pos.append([section5.stable_grounds[0].x, bg_pos[0][1] + bg[0].get_height()])
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
    global save_count
    global saving
    global flowers
    global big_boss

    if (npc2_talk == True):
        flowers[0].interact(pressedKey, Anna)
        flowers[1].interact(pressedKey, Anna)

    section_gameplay(section5)

    section5.gates[0].enter_gate(pressedKey, Anna)

    if (section5.gates[0].active == True and scenechange == -1):
        section_area = 6
        save_count += 1
        saving = (6, 3600, HEIGHT - 900)
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
    section6.stable_grounds.append(ground(WIDTH + 600, 500, section6.stable_grounds[0].x, section6.stable_grounds[0].y + section6.stable_grounds[0].height + 100))

    # Set up the boundaries
    global start_x
    global start_y
    global end_x
    global end_y

    start_x = section6.stable_grounds[11].x
    start_y = -2 * HEIGHT
    end_x = section6.stable_grounds[4].x
    end_y = section6.stable_grounds[11].y + section6.stable_grounds[11].height

    # Set up the boss
    global big_boss
    big_boss = boss(300, 200, section6.stable_grounds[11].x + 50, section6.stable_grounds[11].y - 200)
    big_boss.setColor((255, 0, 0))

    global boss_trigger
    boss_trigger = trigger(50, HEIGHT, section6.stable_grounds[11].x + WIDTH/2, section6.stable_grounds[11].y - HEIGHT)
    boss_trigger.setColor((255, 255, 0))

    # Inititate the player
    global Anna
    global saving
    global save_count
    Anna = player(35, 35, section6.stable_grounds[4].x + 200, section6.stable_grounds[4].y - 35)
    if (save_count > 0):
        Anna.setPos(saving[1], saving[2])

    Anna.setColor((0, 0, 255))
    Anna.hp_bars.append(hp_bar(20, 20, 100, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 150, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 200, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 250, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 300, 50))

    global Anna_brush
    global Anna_brush1
    Anna_brush = brush(60, 10, Anna.x + Anna.width, Anna.y)
    Anna_brush1 = brush(10, 60, Anna.x + Anna.width, Anna.y, 0)

    global Anna_paint
    Anna_paint = paint_bar(60, 60, 20, 20)

    section6.saving_point = save_point(100, 20, section6.stable_grounds[7].x + 10, section6.stable_grounds[7].y - 20)

    # Enemies
    section6.moving_enemies.append(jumping_enemy(60, 60, section6.stable_grounds[0].x, section6.stable_grounds[0].y - 60))
    section6.moving_enemies[0].set_rangex(section6.stable_grounds[0].x, section6.stable_grounds[5].x)
    section6.moving_enemies.append(jumping_enemy(60, 60, section6.stable_grounds[6].x - 60, section6.stable_grounds[0].y - 60))
    section6.moving_enemies[1].set_rangex(section6.stable_grounds[6].x - 60, section6.stable_grounds[6].x + 200)

    section6.moving_enemies[1].dir = -1

    for i in range(len(section6.moving_enemies)):
        section6.moving_enemies[i].setColor((255, 0, 0))


    section6.moving_traps.append(moving_trap(300, 2000, section6.stable_grounds[3].x + section6.stable_grounds[3].width + 40, section6.stable_grounds[0].y + 200))
    section6.moving_traps[0].set_rangey(section6.stable_grounds[0].y - 300, section6.stable_grounds[0].y + 200)

    section6.moving_traps.append(moving_trap(300, 2000, section6.stable_grounds[2].x + section6.stable_grounds[2].width + 40, section6.stable_grounds[0].y + 200))
    section6.moving_traps[1].set_rangey(section6.stable_grounds[0].y - 300, section6.stable_grounds[0].y + 200)

    section6.moving_traps.append(moving_trap(300, 2000, section6.stable_grounds[1].x + section6.stable_grounds[1].width + 40, section6.stable_grounds[0].y + 200))
    section6.moving_traps[2].set_rangey(section6.stable_grounds[0].y - 300, section6.stable_grounds[0].y + 200)

    section6.moving_traps.append(moving_trap(300, 2000, section6.stable_grounds[0].x + section6.stable_grounds[0].width + 40, section6.stable_grounds[0].y + 200))
    section6.moving_traps[3].set_rangey(section6.stable_grounds[0].y - 300, section6.stable_grounds[0].y + 200)

    section6.moving_traps.append(moving_trap(100, 400, section6.stable_grounds[12].x + 200, section6.stable_grounds[12].y + 400))
    section6.moving_traps[4].set_rangey(section6.stable_grounds[12].y - 250, section6.stable_grounds[12].y + 400)

    section6.moving_traps.append(moving_trap(100, 400, section6.moving_traps[4].x + section6.moving_traps[4].width + 200, section6.stable_grounds[12].y - 400))
    section6.moving_traps[5].set_rangey(section6.stable_grounds[12].y - 250, section6.stable_grounds[12].y + 400)

    section6.moving_traps.append(moving_trap(100, 400, section6.moving_traps[5].x + section6.moving_traps[5].width + 200, section6.stable_grounds[12].y + 400))
    section6.moving_traps[6].set_rangey(section6.stable_grounds[12].y - 250, section6.stable_grounds[12].y + 400)

    section6.moving_traps.append(moving_trap(100, 400, section6.moving_traps[6].x + section6.moving_traps[6].width + 200, section6.stable_grounds[12].y - 400))
    section6.moving_traps[7].set_rangey(section6.stable_grounds[12].y - 250, section6.stable_grounds[12].y + 400)

    # Items
    section6.items.append(drawing_piece(20, 20, section6.stable_grounds[2].x - 100, section6.stable_grounds[6].y - 150))
    section6.items[0].setColor((255, 255, 0))

    section6.items.append(interactive_object(20, 20, section6.stable_grounds[12].x + 1000, section6.stable_grounds[12].y - 30))
    section6.items[1].setColor((255, 255, 0))

    flowers[2].setPos(-10000, -10000)
    flowers[2].surface = pygame.image.load('media/flower.png').convert_alpha()

    section6.gates.append(gate(40, 60, section6.stable_grounds[4].x + 50, section6.stable_grounds[4].y - 60))

    # Initiate background image
    global bg
    global bg_pos
    global startscrolling_x
    global startscrolling_y
    global startbackground_x
    global startbackground_y
    bg = []
    bg_pos = []
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg_pos.append([section6.stable_grounds[0].x, -HEIGHT])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), -HEIGHT])

    bg_pos.append([section6.stable_grounds[0].x, bg_pos[0][1] + bg[0].get_height()])
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
    global section_boss
    global saving
    global save_count
    global npc2_talk
    global big_boss
    global end_x
    global boss_fight

    if (npc2_talk == True):
        flowers[2].interact(pressedKey, Anna)

    section_gameplay(section6)
    section6.gates[0].enter_gate(pressedKey, Anna)

    global boss_trigger

    if (boss_trigger.checkcollision(boss_trigger, Anna)):
        boss_fight = True


    big_boss.boss_attack(Anna)

    if (section6.gates[0].active == True and scenechange == -1):
        section_area = 6
        save_count += 1
        saving = (6, -WIDTH + 100, HEIGHT - 460)
        scenechange = 0

    if (Anna.x >= WIDTH and scenechange == -1):
        section_area = 12
        save_count += 1
        saving = (12, 200, 0)
        scenechange = 0

    screen.blit(flowers[2].getSurface(), flowers[2].getPos())
    screen.blit(big_boss.getSurface(), big_boss.getPos())
    screen.blit(boss_trigger.getSurface(), boss_trigger.getPos())

    for i in range(len(big_boss.rocks)):
        screen.blit(big_boss.rocks[i].getSurface(), big_boss.rocks[i].getPos())


def section7_init():
    # Initiate the first section
    global section7

    section7 = section()

    section7.waters.append(water(2*WIDTH, 2*HEIGHT, -WIDTH, 0))
    section7.waters.append(water(2 * WIDTH, 2 * HEIGHT, section7.waters[0].x + section7.waters[0].width, 0))

    section7.items.append(drawing_piece(20, 20, section7.waters[0].x + 100, section7.waters[0].y + 1000))

    # Traps
    section7.moving_traps.append(moving_trap(100, 2000, section7.waters[0].x + 200, section7.waters[0].y + 200))
    section7.moving_traps[0].set_rangey(section7.waters[0].y + 300, section7.waters[0].y + 500)

    section7.moving_traps.append(moving_trap(100, 2000, section7.moving_traps[0].x + section7.moving_traps[0].width + 300, section7.waters[0].y + 200))
    section7.moving_traps[1].set_rangey(section7.waters[0].y + 300, section7.waters[0].y + 500)

    section7.moving_traps.append(moving_trap(100, 2000, section7.moving_traps[1].x + section7.moving_traps[1].width + 300, section7.waters[0].y + 200))
    section7.moving_traps[2].set_rangey(section7.waters[0].y + 300, section7.waters[0].y + 500)

    section7.moving_traps.append(moving_trap(100, 2000, section7.moving_traps[2].x + section7.moving_traps[2].width + 300, section7.waters[0].y + 200))
    section7.moving_traps[3].set_rangey(section7.waters[0].y + 300, section7.waters[0].y + 500)

    section7.moving_traps.append(moving_trap(100, 2000, section7.moving_traps[3].x + section7.moving_traps[3].width + 300, section7.waters[0].y + 200))
    section7.moving_traps[4].set_rangey(section7.waters[0].y + 300, section7.waters[0].y + 500)

    section7.moving_traps.append(moving_trap(100, 2000, section7.moving_traps[4].x + section7.moving_traps[4].width + 300, section7.waters[0].y + 200))
    section7.moving_traps[5].set_rangey(section7.waters[0].y + 300, section7.waters[0].y + 500)

    section7.moving_traps.append(moving_trap(100, 2000, section7.moving_traps[5].x + section7.moving_traps[5].width + 300, section7.waters[0].y + 200))
    section7.moving_traps[6].set_rangey(section7.waters[0].y + 100, section7.waters[0].y + 500)

    section7.moving_traps.append(moving_trap(100, 2000, section7.moving_traps[6].x + section7.moving_traps[6].width + 300, section7.waters[0].y + 200))
    section7.moving_traps[7].set_rangey(section7.waters[0].y + 200, section7.waters[0].y + 500)

    section7.moving_traps.append(moving_trap(100, 2000, section7.moving_traps[7].x + section7.moving_traps[7].width + 300, section7.waters[0].y + 200))
    section7.moving_traps[8].set_rangey(section7.waters[0].y + 50, section7.waters[0].y + 500)

    # Set up the boundaries
    global start_x
    global start_y
    global end_x
    global end_y

    start_x = -WIDTH
    start_y = 0
    end_x = WIDTH
    end_y = HEIGHT

    # Inititate the player
    global Anna
    global saving
    global save_count
    Anna = player(35, 35, 0, section7.waters[0].y)
    if (save_count > 0):
        Anna.setPos(saving[1], saving[2])

    Anna.setColor((0, 0, 255))
    Anna.hp_bars.append(hp_bar(20, 20, 100, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 150, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 200, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 250, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 300, 50))

    global Anna_brush
    global Anna_brush1
    Anna_brush = brush(60, 10, Anna.x + Anna.width, Anna.y)
    Anna_brush1 = brush(10, 60, Anna.x + Anna.width, Anna.y, 0)

    global Anna_paint
    Anna_paint = paint_bar(60, 60, 20, 20)


    # Initiate background image
    global bg
    global bg_pos
    global startscrolling_x
    global startscrolling_y
    global startbackground_x
    global startbackground_y
    bg = []
    bg_pos = []
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg_pos.append([section7.waters[0].x, -HEIGHT])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), -HEIGHT])

    bg_pos.append([section7.waters[0].x, bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), bg_pos[0][1] + bg[0].get_height()])
    startscrolling_x = WIDTH / 2
    startscrolling_y = HEIGHT / 2
    startbackground_x = 0
    startbackground_y = 0


def section7_gameplay():
    global  scenechange
    global section_area
    global save_count
    global saving
    global big_boss

    section_gameplay(section7)

    if (Anna.x <= 0 and scenechange == -1):
        section_area = 10
        save_count += 1
        saving = (12, 3500 - WIDTH, HEIGHT - 300)
        scenechange = 0


def section8_init():
    # Initiate the first section
    global section8
    section8 = section()

    section8.stable_grounds.append(ground(WIDTH, 2*HEIGHT, 0, 2*HEIGHT - 200))

    # Set up the boundaries
    global start_x
    global start_y
    global end_x
    global end_y

    start_x = 0
    start_y = 0
    end_x = WIDTH
    end_y = HEIGHT

    # Inititate the player
    global Anna
    global saving
    global save_count
    Anna = player(35, 35, 0, 720)
    if (save_count > 0):
        Anna.setPos(saving[1], saving[2])

    Anna.setColor((0, 0, 255))
    Anna.hp_bars.append(hp_bar(20, 20, 100, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 150, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 200, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 250, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 300, 50))

    global Anna_brush
    global Anna_brush1
    Anna_brush = brush(60, 10, Anna.x + Anna.width, Anna.y)
    Anna_brush1 = brush(10, 60, Anna.x + Anna.width, Anna.y, 0)

    global Anna_paint
    Anna_paint = paint_bar(60, 60, 20, 20)

    # Initiate background image
    global bg
    global bg_pos
    global startscrolling_x
    global startscrolling_y
    global startbackground_x
    global startbackground_y
    bg = []
    bg_pos = []
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg_pos.append([section8.stable_grounds[0].x, -HEIGHT])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), -HEIGHT])

    bg_pos.append([section8.stable_grounds[0].x, bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), bg_pos[0][1] + bg[0].get_height()])
    startscrolling_x = WIDTH / 2
    startscrolling_y = HEIGHT / 2
    startbackground_x = 0
    startbackground_y = 0


def section8_gameplay():
    global  scenechange
    global section_area
    global big_boss

    section_gameplay(section8)

    if (Anna.x <= -Anna.width and scenechange == -1):
        section_area = 16
        scenechange = 0


def pause_screen(): ### display Surface quit error
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

    screen.blit(ps1.getText(), ps1.gettextpos())
    screen.blit(ps2.getText(), ps2.gettextpos())
    screen.blit(ps3.getText(), ps3.gettextpos())

    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:
        mx, my = pygame.mouse.get_pos()
        if mx > ps1.x and mx < ps1.x + ps1.getText().get_width() and my > ps1.y and my < ps1.y + ps1.getText().get_height(): # resume
            pauselevel = 0 # resume
            return pauselevel
        elif mx > ps2.x and mx < ps2.x + ps2.getText().get_width() and my > ps2.y and my < ps2.y + ps2.getText().get_height():
            pauselevel = 2 # key binds screen
            return pauselevel
        elif mx > ps3.x and mx < ps3.x + ps3.getText().get_width() and my > ps3.y and my < ps3.y + ps3.getText().get_height():
            pauselevel = 3 # exit
            return pauselevel

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

def section8_init():
    # Initiate the first section
    global section8
    section8 = section()

    section8.stable_grounds.append(ground(WIDTH, 2*HEIGHT, 0, 2*HEIGHT - 200))
    section8.stable_grounds.append(ground(WIDTH, 2 * HEIGHT, section8.stable_grounds[0].x + section8.stable_grounds[0].width, 2 * HEIGHT - 200))

    section8.items.append(water_fountain(200, 100, section8.stable_grounds[0].x + 1100, section8.stable_grounds[0].y - 90))

    section8.gates.append(gate(80, 80, section8.stable_grounds[0].x + 1400, section8.stable_grounds[0].y + 200))

    # Set up the boundaries
    global start_x
    global start_y
    global end_x
    global end_y

    start_x = 0
    start_y = 0
    end_x = WIDTH
    end_y = HEIGHT

    # Inititate the player
    global Anna
    global saving
    global save_count
    Anna = player(35, 35, 0, 720)
    if (save_count > 0):
        Anna.setPos(saving[1], saving[2])

    Anna.setColor((0, 0, 255))
    Anna.hp_bars.append(hp_bar(20, 20, 100, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 150, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 200, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 250, 50))
    Anna.hp_bars.append(hp_bar(20, 20, 300, 50))

    global Anna_brush
    global Anna_brush1
    Anna_brush = brush(60, 10, Anna.x + Anna.width, Anna.y)
    Anna_brush1 = brush(10, 60, Anna.x + Anna.width, Anna.y, 0)

    global Anna_paint
    Anna_paint = paint_bar(60, 60, 20, 20)

    # Initiate background image
    global bg
    global bg_pos
    global startscrolling_x
    global startscrolling_y
    global startbackground_x
    global startbackground_y
    bg = []
    bg_pos = []
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground00.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg.append(pygame.image.load('media/forestbackground01.png').convert())
    bg_pos.append([section8.stable_grounds[0].x, -HEIGHT])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), -HEIGHT])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), -HEIGHT])

    bg_pos.append([section8.stable_grounds[0].x, bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[0][0] + bg[0].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[1][0] + bg[1].get_width(), bg_pos[0][1] + bg[0].get_height()])
    bg_pos.append([bg_pos[2][0] + bg[2].get_width(), bg_pos[0][1] + bg[0].get_height()])
    startscrolling_x = WIDTH / 2
    startscrolling_y = HEIGHT / 2
    startbackground_x = 0
    startbackground_y = 0


def section8_gameplay():
    global  scenechange
    global section_area
    global big_boss
    global coins_collect
    global gate_open
    global save_count
    global saving
    global cutscenelevel

    section_gameplay(section8)

    if (section8.items[0].put_coin(pressedKey, Anna, coins_collect) == 5):
        coins_collect -= 5
        gate_open = True

    if (gate_open == True):
        section8.gates[0].setPos(section8.stable_grounds[0].x + 1600, section8.stable_grounds[0].y - 80)
        if section8.gates[0].checkcollision(section8.gates[0], Anna):
            cutscenelevel = 1
            section_area = 100



    if (Anna.x <= -Anna.width and scenechange == -1):
        section_area = 6
        save_count += 1
        saving = (6, 4*WIDTH + 1250, HEIGHT - 200)
        scenechange = 0

    if (Anna.x > WIDTH - Anna.width):
        Anna.setPos(WIDTH - Anna.width, Anna.y)


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
    global section_area
    global cutscenelevel
    text05 = text(100, 70, '-Lewis Carroll, Through the Looking Glass', 26, "Renogare", BLACK)
    x = WIDTH / 2 - text05.getText().get_width() / 2
    y = HEIGHT / 2 - text05.getText().get_height() / 2 + 175
    text05.textsetpos(x, y)
    section_area = 0
    cutscenelevel = 0

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
# --- CODE STARTS HERE --- #
running = True
pauselevel = 0

print(cutscenelevel)
while running:
    for event in pygame.event.get():  # Returns all input and triggers into an array
        if (event.type == pygame.QUIT): # If the red X was clicked
            running = False

    start_ticks = pygame.time.get_ticks()


    #intro()

    if section_area == -1 and cutscenelevel == 1:
        screen.fill(BLACK)
        if start_ticks / 1000 > 1:
            cutscene01()
        if start_ticks / 1000 > 5:
            cutscene02()
        if start_ticks / 1000 > 9:
            cutscene03()
        if start_ticks / 1000 > 14:
            cutscene04()
        if start_ticks / 1000 > 19:
            cutscene05()

    pressedKey = pygame.key.get_pressed()

    if pauselevel == 0 and section_area == 0 and cutscenelevel == 0:

        if (section_area == 0):
            section1_init()
            section_area = 1

        if (section_area == 1 and scenechange == -1):
            section1_gameplay()

        if (section_area == 2):
            section2_init()
            section_area = 3

        if (section_area == 3 and scenechange == -1):
            section2_gameplay()

        if (section_area == 4):
            section3_init()
            section_area = 5

        if (section_area == 5):
            section3_gameplay()

        if (section_area == 6):
            section4_init()
            section_area = 7

        if (section_area == 7 and scenechange == -1):
            section4_gameplay()

        if (section_area == 8):
            section5_init()
            section_area = 9

        if (section_area == 9 and scenechange == -1):
            section5_gameplay()

        if (section_area == 10):
            section6_init()
            section_area = 11

        if (section_area == 11 and scenechange == -1):
            section6_gameplay()

        if (section_area == 12):
            section7_init()
            section_area = 13

        if (section_area == 13 and scenechange == -1):
            section7_gameplay()

        if (section_area == 14):
            section8_init()
            section_area = 15

        if (section_area == 15 and scenechange == -1):
            section8_gameplay()

    if pressedKey[pygame.K_TAB]:
        pauselevel = 1
    if pauselevel == 1:
        screen.fill(BLACK)
        pause_screen()
    if pauselevel == 2:
        screen.fill(BLACK)
        keybinds_screen()
    if pauselevel == 3:
        exit()

    if cutscenelevel == 2:
        screen.fill(WHITE)
        if start_ticks / 1000 > 0:
            cutscene06()
        if start_ticks / 1000 > 6.10:
            cutscene07()
        if start_ticks / 1000 > 12.10:
            cutscene08()
        if start_ticks / 1000 > 18.10:
            cutscene09()
        if start_ticks / 1000 > 24.10:
            cutscene10()
        if start_ticks / 1000 > 30.10:
            cutscene11()
        if start_ticks / 1000 > 36.10:
            cutscene12()
        if start_ticks / 1000 > 42.10:
            cutscene13()
        if start_ticks / 1000 > 48.10:
            cutscene14()
        if start_ticks / 1000 > 54.10:
            cutscene15()
        if start_ticks / 1000 > 61.10:
            screen.fill(BLACK)

    scene_change()
    pygame.display.update()
    clock.tick(FPS) # This will pause the game until the FPS time is reached


pygame.quit()