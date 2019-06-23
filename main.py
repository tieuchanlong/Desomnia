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
from myDialogue_class import *
pygame.init() # load the pygame module commands in the program

# Display variables
TITLE = 'Hello World' # Appear in the window title
FPS = 30 # Frames per second
WIDTH = 900
HEIGHT = 500
SCREENDIM = (WIDTH, HEIGHT)

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

# Create the window
global screen
screen = pygame.display.set_mode(SCREENDIM) # Create the main surface where all other assets are placed on top
pygame.display.set_caption(TITLE) # This updates the windows title
screen.fill(BLACK) # Fill the entire surface with the chosen color. Think of fill as erase.

clock = pygame.time.Clock()  # starts a clock object to measure time

### ----------------------------------------- Initiate sounds ------------------------------------ ###
pygame.mixer.set_num_channels(20)

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
global coins_collect
global stars
global gate_open
global conversation
global cutscenelevel
global pauselevel
global start_ticks
global prog_start
global starttime
global tutoriallevel
global count
global in_cave
global instruction_screen
global delay_mouse
global easter_trigger
global easter_start

### --- Start screen variables --- ###

screenimage = []
imagecounter = -1
count = 0

for i in range(356):
    imagecounter += 1
    screenimage.append("media/startscreen/startscreen/startscreen - image" + str(imagecounter) + ".jpg")

screenimageload = []
for i in range(356):
    screenimageload.append(pygame.image.load(screenimage[i]).convert())



# ------------ Other main variables ------------------ #
big_boss = boss(300, 200, 0, 0)
big_boss.setColor((255, 0, 0))

boss_trigger = trigger(50, HEIGHT, 0, 0)
easter_trigger = trigger(50, HEIGHT, 0, 0)

flowers = []
npc2_talk = False
boss_fight = False
easter_start = False
gate_open = False

instruction_screen = image('media/lowopacity.png', 0, 0, WIDTH, HEIGHT)

conversation = dialogue()
cutscenelevel = 3
pauselevel = 0
prog_start = -1
starttime = 0
tutoriallevel = 0
in_cave = False
delay_mouse = 0

stars = []
for i in range(11):
    stars.append(drawing_piece(20, 20, -10000, -10000))

coins_collect = 0

for i in range(3):
    flowers.append(interactive_object(20, 20, 0, 0))
    flowers[i].note.setPos(flowers[i].x, flowers[i].y - 10)

section_area = -1
scenechange = -1
save_count = 1
saving = (0, 0, 300)

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
    global screen
    global delay_mouse

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
    Anna.player_pickup(pressedKey, section.instruction_points)
    Anna.player_pickup(pressedKey, flowers)
    Anna.player_pickup(pressedKey, stars)

    if (Anna.hp <= 0):
        section_area = saving[0]
        scenechange = 0

    if (conversation.dialogue_unlocked[12] == True):
        Anna.player_pickup(pressedKey, flowers)

    for i in range(len(section.items)):
        if (section.items[i].coin_check == True):
            section.items[i].coin_anim()

    star_count = 0
    for i in range(len(stars)):
        if (stars[i].collect == True):
            star_count += 1

    # Count flowers collected
    flowercount = 0
    for i in range(len(flowers)):
        if (flowers[i].collect == True):
            flowercount += 1

    Anna.flowers_text.setText(str(flowercount) + '/3')

    for i in range(len(section.items)):
        if (section.items[i].collect == True and section.items[i].check == False):
            coins_collect += 1
            section.items[i].check = True

    Anna.drawings.setText(str(star_count)+'/11')
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

    Anna.player_skill(pressedKey, Anna_paint, conversation, delay_mouse)
    Anna.player_attack(pressedKey, section, conversation, delay_mouse)
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

    for i in range(len(section.backgrounds)):
        screen.blit(section.backgrounds[i].getSurface(), section.backgrounds[i].getPos())


    # water
    for i in range(len(section.waters)):
        screen.blit(section.waters[i].getSurface(), section.waters[i].getPos())

    # grounds
    for i in range(len(section.stable_grounds)):
        screen.blit(section.stable_grounds[i].getSurface(), section.stable_grounds[i].getPos())
        for j in range(len(section.stable_grounds[i].images)):
            screen.blit(section.stable_grounds[i].images[j].getSurface(), section.stable_grounds[i].images[j].getPos())

    # moving npc
    for i in range(len(section.npc)):
        screen.blit(section.npc[i].getSurface(), section.npc[i].getPos())

    for i in range(len(section.moving_npc)):
        screen.blit(section.moving_npc[i].getSurface(), section.moving_npc[i].getPos())

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
    if (section.saving_point.note_appear == True):
        screen.blit(section.saving_point.note.getSurface(), section.saving_point.note.getPos())

    for i in range(len(stars)):
        screen.blit(stars[i].getSurface(), stars[i].getPos())

    screen.blit(Anna.getSurface(), Anna.getPos())
    if (Anna_brush.appear == True):
        screen.blit(Anna_brush.getSurface(), Anna_brush.getPos())

    if (Anna_brush1.appear == True):
        screen.blit(Anna_brush1.getSurface(), Anna_brush1.getPos())

    for i in range(len(section.items)):
        if (section.items[i].note_appear == True):
            screen.blit(section.items[i].note.getSurface(), section.items[i].note.getPos())


    for i in range(len(flowers)):
        if (flowers[i].note_appear == True):
            screen.blit(flowers[i].note.getSurface(), flowers[i].note.getPos())

    for i in range(len(section.instruction_points)):
        if (section.instruction_points[i].note_appear == True):
            screen.blit(section.instruction_points[i].note.getSurface(), section.instruction_points[i].note.getPos())

    for i in range(len(section.gates)):
        if (section.gates[i].note_appear == True):
            screen.blit(section.gates[i].note.getSurface(), section.gates[i].note.getPos())

    for i in range(len(section.control_panels)):
        if (section.control_panels[i].note_appear == True):
            screen.blit(section.control_panels[i].note.getSurface(), section.control_panels[i].note.getPos())

    for i in range(len(flowers)):
        if (flowers[i].note_appear == True):
            screen.blit(flowers[i].note.getSurface(), flowers[i].note.getPos())

    for i in range(len(section.gates)):
        if (section.gates[i].note_appear == True):
            screen.blit(section.gates[i].note.getSurface(), section.gates[i].note.getPos())

    for i in range(len(flowers)):
        if (flowers[i].note_appear == True):
            screen.blit(flowers[i].note.getSurface(), flowers[i].note.getPos())

    if (conversation.dialogue_unlocked[12] == True and conversation.dialogue_unlocked[24] == False):
        screen.blit(Anna.flowers_text.getText(), Anna.flowers_text.gettextpos())
        screen.blit(Anna.flower_UI.getSurface(), Anna.flower_UI.getPos())

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
    global screen

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
    global screen

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

    # Set up the backgrounds
    section1.stable_grounds.append(ground(200, 180, section1.stable_grounds[6].x + 200, section1.stable_grounds[6].y - 180))
    section1.stable_grounds[9].surface = pygame.image.load('media/house00.png').convert_alpha()
    section1.stable_grounds[9].surface = pygame.transform.scale(section1.stable_grounds[9].surface, (200, 180))
    section1.stable_grounds.append(ground(300, 180, section1.stable_grounds[6].x + 500, section1.stable_grounds[6].y - 180))
    section1.stable_grounds[10].surface = pygame.image.load('media/house02.png').convert_alpha()
    section1.stable_grounds[10].surface = pygame.transform.scale(section1.stable_grounds[10].surface, (300, 180))

    # Signs
    section1.stable_grounds.append(ground(60, 60, section1.stable_grounds[0].x + 100, section1.stable_grounds[0].y - 60))
    section1.stable_grounds[11].surface = pygame.image.load('media/sign_00.png').convert_alpha()
    section1.stable_grounds[11].surface = pygame.transform.scale(section1.stable_grounds[11].surface, (60, 60))

    section1.stable_grounds.append(ground(60, 60, section1.stable_grounds[6].x + 800, section1.stable_grounds[6].y - 60))
    section1.stable_grounds[12].surface = pygame.image.load('media/sign_00.png').convert_alpha()
    section1.stable_grounds[12].surface = pygame.transform.scale(section1.stable_grounds[12].surface, (60, 60))

    # Npc
    section1.moving_npc.append(moving_npc(30, 30, section1.stable_grounds[4].x + 300, section1.stable_grounds[4].y - 30))
    section1.moving_npc[0].set_rangex(section1.stable_grounds[4].x + 300, section1.stable_grounds[4].x + 600)

    section1.moving_npc.append(moving_npc(30, 30, section1.stable_grounds[4].x + 300, section1.stable_grounds[4].y - 30))
    section1.moving_npc[1].set_rangex(section1.stable_grounds[4].x + 1000, section1.stable_grounds[4].x + 1200)


    section1.npc.append(npc(30, 30, section1.stable_grounds[6].x + 100, section1.stable_grounds[6].y - 30))
    section1.npc.append(npc(30, 30, section1.stable_grounds[6].x + 300, section1.stable_grounds[6].y - 30))
    section1.npc.append(npc(30, 30, section1.stable_grounds[6].x + 500, section1.stable_grounds[6].y - 30))
    section1.npc.append(npc(30, 30, section1.stable_grounds[6].x + 700, section1.stable_grounds[6].y - 30))

    section1.moving_npc.append(moving_npc(30, 30, section1.stable_grounds[6].x + 10, section1.stable_grounds[6].y - 30, 0.1))
    section1.moving_npc[2].set_rangex(section1.stable_grounds[6].x, section1.npc[3].x - 30)


    section1.instruction_points.append(instruction_point(50, 50, section1.stable_grounds[0].x + 500, section1.stable_grounds[0].y - 50))

    # Items
    section1.items.append(interactive_object(20, 20, section1.stable_grounds[5].x + 50, section1.stable_grounds[5].y - 30))
    section1.items.append(interactive_object(20, 20, section1.stable_grounds[7].x + 200, section1.stable_grounds[7].y - 30))
    section1.items.append(interactive_object(20, 20, section1.stable_grounds[6].x + 400, section1.stable_grounds[6].y - 30))

    for i in range(len(stars)):
        stars[i].setPos(-10000, -10000)

    if (stars[0].collect == False):
        stars[0].setPos(section1.stable_grounds[4].x + 200, section1.stable_grounds[4].y - 30)

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
        print(saving)
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
    global screen
    global tutoriallevel
    global pressedKeys

    if (scenechange != 1):
        section_gameplay(section1)


    if (section1.instruction_points[0].note_appear == True):
        if (pressedKey[pygame.K_e]):
            tutoriallevel = 1

    if (Anna.x < 0):
        Anna.setPos(0, Anna.y)

    if (Anna.x >= WIDTH and scenechange == -1):
        section_area = 2
        saving = (2, 100, HEIGHT - 200)
        scenechange = 0


    screen.blit(stars[0].getSurface(), stars[0].getPos())

def section2_init():
    # Initiate the first section
    global section2
    global endbackground2_x
    global endbackground2_y
    global screen

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

    # Set up the backgrounds
    section2.stable_grounds.append(ground(200, 180, section2.stable_grounds[1].x + 150, section2.stable_grounds[1].y - 180))
    section2.stable_grounds[15].surface = pygame.image.load('media/house00.png').convert_alpha()
    section2.stable_grounds[15].surface = pygame.transform.scale(section2.stable_grounds[15].surface, (200, 180))

    # Signs
    section2.stable_grounds.append(ground(60, 60, section2.stable_grounds[1].x + 100, section2.stable_grounds[1].y - 60))
    section2.stable_grounds[16].surface = pygame.image.load('media/sign_00.png').convert_alpha()
    section2.stable_grounds[16].surface = pygame.transform.scale(section2.stable_grounds[16].surface, (60, 60))

    section2.stable_grounds.append(ground(60, 60, section2.stable_grounds[5].x + section2.stable_grounds[5].width - 100, section2.stable_grounds[5].y - 60))
    section2.stable_grounds[17].surface = pygame.image.load('media/sign_00.png').convert_alpha()
    section2.stable_grounds[17].surface = pygame.transform.scale(section2.stable_grounds[17].surface, (60, 60))

    section2.stable_grounds.append(ground(60, 60, section2.stable_grounds[10].x + 100, section2.stable_grounds[10].y - 60))
    section2.stable_grounds[18].surface = pygame.image.load('media/sign_00.png').convert_alpha()
    section2.stable_grounds[18].surface = pygame.transform.scale(section2.stable_grounds[18].surface, (60, 60))


    section2.waters.append(water(7 * WIDTH, 2000, section2.stable_grounds[0].x, section2.stable_grounds[0].y + 100))

    endbackground2_x = section2.waters[0].x + section2.waters[0].width - 900
    endbackground2_y = section2.waters[0].y

    section2.instruction_points.append(instruction_point(50, 50, section2.stable_grounds[1].x + 200, section2.stable_grounds[1].y - 50))

    # Traps
    section2.traps.append(trap(50, section2.waters[0].height, section2.stable_grounds[5].x - 50, section2.waters[0].y))

    section2.moving_traps.append(moving_trap(300, 1000, section2.stable_grounds[0].x + 200, section2.waters[0].y + 200))
    section2.moving_traps[0].set_rangey(section2.waters[0].y + 300, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(300, 1000, section2.moving_traps[0].x + section2.moving_traps[0].width + 300, section2.waters[0].y + 200))
    section2.moving_traps[1].set_rangey(section2.waters[0].y + 300, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(300, 1000, section2.moving_traps[1].x + section2.moving_traps[1].width + 300, section2.waters[0].y + 200))
    section2.moving_traps[2].set_rangey(section2.waters[0].y + 300, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(300, 1000, section2.moving_traps[2].x + section2.moving_traps[2].width + 300, section2.waters[0].y + 200))
    section2.moving_traps[3].set_rangey(section2.waters[0].y + 300, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(300, 1000, section2.moving_traps[3].x + section2.moving_traps[3].width + 300, section2.waters[0].y + 200))
    section2.moving_traps[4].set_rangey(section2.waters[0].y + 300, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(300, 1000, section2.moving_traps[4].x + section2.moving_traps[4].width + 300, section2.waters[0].y + 200))
    section2.moving_traps[5].set_rangey(section2.waters[0].y + 300, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(300, 1000, section2.moving_traps[5].x + section2.moving_traps[5].width + 300, section2.waters[0].y + 200))
    section2.moving_traps[6].set_rangey(section2.waters[0].y + 100, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(300, 1000, section2.moving_traps[6].x + section2.moving_traps[6].width + 300, section2.waters[0].y + 200))
    section2.moving_traps[7].set_rangey(section2.waters[0].y + 200, section2.stable_grounds[0].y + 1000)

    section2.moving_traps.append(moving_trap(300, 1000, section2.moving_traps[7].x + section2.moving_traps[7].width + 300, section2.waters[0].y + 200))
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
    print(save_count)
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
    section2.moving_npc.append(moving_npc(30, 30, section2.stable_grounds[0].x + 200, section2.stable_grounds[0].y - 30))
    section2.moving_npc[0].set_rangex(section2.stable_grounds[0].x + 200, section2.stable_grounds[1].x - 130)

    section2.moving_npc.append(moving_npc(30, 30, section2.moving_npc[0].x + section2.moving_npc[0].width + 200, section2.stable_grounds[0].y - 30))
    section2.moving_npc[1].set_rangex(section2.moving_npc[1].x, section2.stable_grounds[1].x - 30)


    section2.hor_ground = 1

    section2.moving_grounds.append(moving_ground(250, 50, section2.stable_grounds[0].x + 100, section2.moving_npc[0].y - 50))
    section2.moving_grounds[0].surface = pygame.image.load('media/woodlog.png').convert_alpha()
    section2.moving_grounds[0].surface = pygame.transform.scale(section2.moving_grounds[0].surface, (section2.moving_grounds[0].width, section2.moving_grounds[0].height))
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


    # Items
    section2.items.append(interactive_object(20, 20, section2.stable_grounds[14].x + 50, section2.stable_grounds[14].y - 30))
    section2.items.append(interactive_object(20, 20, section2.stable_grounds[11].x + 50, section2.stable_grounds[11].y - 30))
    section2.items.append(interactive_object(20, 20, section2.waters[0].x + 400, section2.waters[0].y + 200))
    section2.items.append(interactive_object(20, 20, section2.stable_grounds[10].x + 100, section2.stable_grounds[10].y - 30))
    section2.items.append(interactive_object(20, 20, section2.stable_grounds[7].x + 500, section2.stable_grounds[7].y - 40))

    for i in range(len(stars)):
        stars[i].setPos(-10000, -10000)

    if (stars[1].collect == False):
        stars[1].setPos(section2.moving_traps[2].x + 20, section2.stable_grounds[0].y + section2.stable_grounds[0].height + 200)

    if (stars[10].collect == False):
        stars[10].setPos(section2.stable_grounds[6].x + 200, section2.stable_grounds[6].y - 40)


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
    global screen
    global tutoriallevel

    if (scenechange != 1):
        section_gameplay(section2)

    if (section2.instruction_points[0].note_appear == True):
        if (pressedKey[pygame.K_e]):
            tutoriallevel = 2


    # Special cases
    if (section2.moving_npc[0].x <= section2.stable_grounds[0].x):
        section2.moving_npc[1].dir = 1

    if (section2.moving_npc[0].dir != section2.moving_npc[1].dir):
        section2.moving_npc[0].dir = section2.moving_npc[1].dir
        section2.moving_grounds[0].dir = -1

    if (Anna.x >= WIDTH and scenechange == -1):
        section_area = 4
        save_count += 1
        saving = (4, 0, 565)
        scenechange = 0

    if (Anna.x <= -Anna.width and scenechange == -1):
        section_area = 0
        save_count += 1
        saving = (0, 2200 + 2*WIDTH, HEIGHT - 50)
        scenechange = 0



    screen.blit(stars[1].getSurface(), stars[1].getPos())

def section3_init(): # Add 1 more trap
    # Initiate the first section
    global section3
    global start_move
    global move_count
    global screen
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

    # Set up the backgrounds
    section3.stable_grounds.append(ground(200, 180, section3.stable_grounds[10].x + 150, section3.stable_grounds[10].y - 180))
    section3.stable_grounds[17].surface = pygame.image.load('media/house02.png').convert_alpha()
    section3.stable_grounds[17].surface = pygame.transform.scale(section3.stable_grounds[17].surface, (200, 180))

    # Signs
    section3.stable_grounds.append(ground(60, 60, section3.stable_grounds[0].x + section3.stable_grounds[0].width - 100, section3.stable_grounds[0].y - 60))
    section3.stable_grounds[18].surface = pygame.image.load('media/sign_00.png').convert_alpha()
    section3.stable_grounds[18].surface = pygame.transform.scale(section3.stable_grounds[18].surface, (60, 60))

    section3.stable_grounds.append(ground(60, 60, section3.stable_grounds[4].x + 200, section3.stable_grounds[4].y - 60))
    section3.stable_grounds[19].surface = pygame.image.load('media/sign_00.png').convert_alpha()
    section3.stable_grounds[19].surface = pygame.transform.scale(section3.stable_grounds[19].surface, (60, 60))

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
    section3.items.append(interactive_object(20, 20, section3.stable_grounds[10].x + 100, section3.stable_grounds[10].y - 30))
    section3.items.append(interactive_object(20, 20, section3.stable_grounds[10].x + 100, section3.stable_grounds[10].y - 30))
    section3.items.append(interactive_object(20, 20, section3.stable_grounds[11].x + 300, section3.stable_grounds[11].y - 30))

    for i in range(len(stars)):
        stars[i].setPos(-10000, -10000)

    if (stars[2].collect == False):
        stars[2].setPos(section3.stable_grounds[10].x + 50, section3.stable_grounds[10].y - 30)


    section3.items.append(interactive_object(50, 50, section3.stable_grounds[13].x + section3.stable_grounds[13].width - 50, section3.stable_grounds[13].y - 50))
    section3.items[4].surface = pygame.image.load('media/orb.png').convert_alpha()
    section3.items[4].coin_check = False
    section3.items[4].surface = pygame.transform.scale(section3.items[4].surface, (50, 50))

    section3.gates.append(gate(50, 60, section3.stable_grounds[8].x + 200, section3.stable_grounds[8].y - 60))

    section3.instruction_points.append(instruction_point(50, 50, section3.stable_grounds[1].x + 200, section3.stable_grounds[1].y - 50))


    section3.control_panels.append(control_panel(60, 60, section3.stable_grounds[4].x + section3.stable_grounds[13].width - 100, section3.stable_grounds[4].y - 60))
    section3.control_panels[0].surface = pygame.image.load('media/control_00.png').convert_alpha()
    section3.control_panels[0].surface = pygame.transform.scale(section3.control_panels[0].surface, (60, 60))

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
    global screen
    global tutoriallevel

    if (scenechange != 1):
        section_gameplay(section3)

    section3.gates[0].enter_gate(pressedKey, Anna)

    if (section3.instruction_points[0].note_appear == True):
        if (pressedKey[pygame.K_e]):
            tutoriallevel = 3

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


    if (section3.items[4].x <= -5000 and section3.items[4].y <= -5000):
        section3.control_panels[0].interact(pressedKey, Anna)
        if (section3.control_panels[0].active == True and move_count == 0):
            start_move = True
            section3.control_panels[0].surface = pygame.image.load('media/control_01.png').convert_alpha()
            section3.control_panels[0].surface = pygame.transform.scale(section3.control_panels[0].surface, (60, 60))

    if (start_move == True):
        section3.stable_grounds[6].setPos(section3.stable_grounds[6].x, section3.stable_grounds[6].y - 10)
        section3.stable_grounds[7].setPos(section3.stable_grounds[7].x, section3.stable_grounds[7].y - 10)
        move_count += 10

        if (move_count >= 300):
            start_move = False
            stars[2].setPos(section3.stable_grounds[7].x + 50, section3.stable_grounds[7].y - 40)

    if (section3.control_panels[0].note_appear == True):
        screen.blit(section3.control_panels[0].note.getSurface(), section3.control_panels[0].note.getPos())

    screen.blit(stars[2].getSurface(), stars[2].getPos())


def section4_init():
    # Initiate the first section
    global section4
    global screen
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

    # Set up the backgrounds
    section4.stable_grounds.append(ground(250, 180, section4.stable_grounds[1].x + 200, section4.stable_grounds[1].y - 180))
    section4.stable_grounds[16].surface = pygame.image.load('media/house01.png').convert_alpha()
    section4.stable_grounds[16].surface = pygame.transform.scale(section4.stable_grounds[16].surface, (250, 180))

    # Signs
    section4.stable_grounds.append(ground(60, 60, section4.stable_grounds[0].x + section4.stable_grounds[0].width - 100,section4.stable_grounds[0].y - 60))
    section4.stable_grounds[17].surface = pygame.image.load('media/sign_00.png').convert_alpha()
    section4.stable_grounds[17].surface = pygame.transform.scale(section4.stable_grounds[17].surface, (60, 60))

    section4.waters.append(water(WIDTH - section4.stable_grounds[8].width, 1000, section4.stable_grounds[8].x + section4.stable_grounds[8].width, section4.stable_grounds[9].y + 100))
    section4.waters.append(water(5000, 500, section4.stable_grounds[9].x - 3000, section4.stable_grounds[9].y + 150))

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
    #section4.stable_enemies.append(shooting_enemy(30, 40, section4.stable_grounds[2].x + section4.stable_grounds[2].width + 4200,section4.stable_grounds[0].y - 40))

    for i in range(len(section4.stable_enemies)):
        section4.stable_enemies[i].setColor((255, 0, 0))


    # Npc
    section4.npc.append(npc(30, 30, section4.stable_grounds[9].x + section4.stable_grounds[9].width - 30, section4.stable_grounds[9].y - 30))
    section4.npc.append(npc(50, 50, section4.stable_grounds[1].x + 100, section4.stable_grounds[1].y - 50))
    section4.npc.append(npc(150, 150, section4.stable_grounds[0].x + section4.stable_grounds[0].width - 200, section4.stable_grounds[0].y - 120))

    # Items

    for i in range(len(stars)):
        stars[i].setPos(-10000, -10000)

    if (stars[3].collect == False):
        stars[3].setPos(section4.stable_grounds[12].x + 100, section4.stable_grounds[12].y - 40)

    if (stars[4].collect == False):
        stars[4].setPos(section4.stable_grounds[8].x + 150, section4.stable_grounds[8].y - 40)

    if (stars[9].collect == False):
        stars[9].setPos(section4.waters[0].x + 100, section4.waters[0].y)

    section4.items.append(interactive_object(50, 60, section4.stable_grounds[5].x + section4.stable_grounds[5].width, section4.stable_grounds[5].y - 60))
    section4.items.append(interactive_object(20, 20, section4.stable_grounds[9].x + 100, section4.stable_grounds[9].y - 30))
    section4.items.append(interactive_object(20, 20, section4.waters[0].x + 100, section4.waters[0].y + 50))

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
    global  conversation
    global screen

    section4.gates[0].enter_gate(pressedKey, Anna)
    section4.gates[1].enter_gate(pressedKey, Anna)
    section4.gates[2].enter_gate(pressedKey, Anna)

    if (scenechange != 1):
        section_gameplay(section4)


    # Talk with a random talkative creature
    if (conversation.start == False):
        section4.npc[1].npc_talk(pressedKey, Anna)
        if (conversation.dialogue_unlocked[0] == False):
            if (section4.npc[1].talk == True):
                conversation.dialogueLEVEL = 0
                section4.npc[1].talk = False
                if (conversation.start == False):
                    conversation.starttime = pygame.time.get_ticks()
                    conversation.start = True
        else:
            if (section4.npc[1].talk == True):
                conversation.dialogueLEVEL = 6
                section4.npc[1].talk = False
                if (conversation.start == False):
                    conversation.starttime = pygame.time.get_ticks()
                    conversation.start = True

    # Count flowers collected
    flowercount = 0
    for i in range(len(flowers)):
        if (flowers[i].collect == True):
            flowercount += 1

    Anna.flowers_text.setText(str(flowercount) + '/3')

    if (conversation.start == False):
        section4.npc[2].npc_talk(pressedKey, Anna)
        if (conversation.dialogue_unlocked[12] == False):
            if (section4.npc[2].talk == True):
                conversation.dialogueLEVEL = 12
                section4.npc[2].talk = False
                if (conversation.start == False):
                    conversation.starttime = pygame.time.get_ticks()
                    conversation.start = True
            # load some other dialogues
        elif (flowercount < len(flowers)):
            if (section4.npc[2].talk == True):
                conversation.dialogueLEVEL = 23
                section4.npc[2].talk = False
                if (conversation.start == False):
                    conversation.starttime = pygame.time.get_ticks()
                    conversation.start = True
            # load some dialogues
        elif (flowercount == len(flowers) and conversation.dialogue_unlocked[121] == False):
            if (section4.npc[2].talk == True):
                conversation.dialogueLEVEL = 121
                section4.npc[2].talk = False
                if (conversation.start == False):
                    conversation.starttime = pygame.time.get_ticks()
                    conversation.start = True
        else:
            if (section4.npc[2].talk == True):
                conversation.dialogueLEVEL = 24
                section4.npc[2].talk = False
                if (conversation.start == False):
                    conversation.starttime = pygame.time.get_ticks()
                    conversation.start = True

    if (conversation.dialogue_unlocked[121] == False):
        section4.npc[2].trouble_npc_anim(Anna)
    else:
        section4.npc[2].happy_npc_anim(Anna)

    section4.npc[1].talk_npc_anim(Anna)

    if (Anna.x < 0):
        Anna.setPos(0, Anna.y)

    if (flowercount < len(flowers)):
        if (Anna.x >= end_x - 100):
            Anna.x = section4.stable_grounds[1].x + section4.stable_grounds[1].width + 100
            Anna.setPos(Anna.x, Anna.y)


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

    if (Anna.x >= WIDTH - Anna.width and (flowercount == 3 or conversation.dialogue_unlocked[121] == False)):
        Anna.setPos(WIDTH - Anna.width, Anna.y)

    if (Anna.x >= WIDTH and scenechange == -1):
        section_area = 14
        save_count += 1
        saving = (14, 0, 720)
        scenechange = 0

    if (section4.npc[1].note_appear == True):
        screen.blit(section4.npc[1].note.getSurface(), section4.npc[1].note.getPos())


    if (section4.npc[2].note_appear == True):
        screen.blit(section4.npc[2].note.getSurface(), section4.npc[2].note.getPos())

    screen.blit(stars[3].getSurface(), stars[3].getPos())
    screen.blit(stars[4].getSurface(), stars[4].getPos())
    screen.blit(stars[9].getSurface(), stars[9].getPos())

def section5_init():
    # Initiate the first section
    global section5
    global flowers
    global screen

    section5 = section()

    section5.stable_grounds.append(ground(1000, 500, -500, HEIGHT - 100))
    section5.stable_grounds.append(ground(100, 50, section5.stable_grounds[0].x + section5.stable_grounds[0].width + 150, section5.stable_grounds[0].y))
    section5.stable_grounds.append(ground(100, 50, section5.stable_grounds[1].x + section5.stable_grounds[1].width + 150, section5.stable_grounds[1].y - 150))
    section5.stable_grounds.append(ground(400, 100, section5.stable_grounds[2].x + section5.stable_grounds[2].width + 150, section5.stable_grounds[2].y))
    section5.stable_grounds.append(ground(250, 60, section5.stable_grounds[3].x + section5.stable_grounds[3].width - 250,section5.stable_grounds[3].y - 60))
    section5.stable_grounds.append(ground(100, 50, section5.stable_grounds[4].x  - 250, section5.stable_grounds[4].y - 150))
    section5.stable_grounds.append(ground(100, 50, section5.stable_grounds[5].x - 250, section5.stable_grounds[5].y - 200))
    section5.stable_grounds.append(ground(400, section5.stable_grounds[0].height, section5.stable_grounds[0].x - 1200, section5.stable_grounds[0].y))

    for i in range(len(section5.stable_grounds)):
        section5.stable_grounds[i].surface = pygame.image.load('media/caveground.png').convert_alpha()
        section5.stable_grounds[i].surface = pygame.transform.scale(section5.stable_grounds[i].surface, (section5.stable_grounds[i].width, min(section5.stable_grounds[i].height, 300)))


    # Signs
    section5.stable_grounds.append(ground(60, 60, section5.stable_grounds[0].x + section5.stable_grounds[0].width - 100, section5.stable_grounds[0].y - 60))
    section5.stable_grounds[8].surface = pygame.image.load('media/sign_00.png').convert_alpha()
    section5.stable_grounds[8].surface = pygame.transform.scale(section5.stable_grounds[8].surface, (60, 60))

    # Bonfire
    section5.stable_grounds.append(ground(100, 150, section5.stable_grounds[0].x + 160,section5.stable_grounds[0].y - 130))
    section5.stable_grounds.append(ground(100, 150, section5.stable_grounds[0].x + 510, section5.stable_grounds[0].y - 130))

    section5.stable_grounds.append(ground(200, 200, section5.stable_grounds[0].x + section5.stable_grounds[0].width - 400,section5.stable_grounds[0].y - 200))
    section5.stable_grounds[11].surface = pygame.image.load('media/hut.png').convert_alpha()
    section5.stable_grounds[11].surface = pygame.transform.scale(section5.stable_grounds[11].surface, (200, 200))

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

    section5.waters.append(water(section5.stable_grounds[0].x - section5.stable_grounds[7].x - section5.stable_grounds[7].width + 1400, 500, section5.stable_grounds[7].x, section5.stable_grounds[7].y + 200))

    # NPC
    section5.npc.append(npc(50, 50, section5.stable_grounds[0].x + 100, section5.stable_grounds[0].y - 50))
    section5.npc.append(npc(50, 50, section5.stable_grounds[0].x + 300, section5.stable_grounds[0].y - 50))
    section5.npc.append(npc(50, 50, section5.stable_grounds[0].x + 480, section5.stable_grounds[0].y - 50))
    section5.npc.append(npc(50, 50, section5.stable_grounds[0].x + 650, section5.stable_grounds[0].y - 50))

    # Items
    section5.items.append(interactive_object(20, 20, section5.stable_grounds[4].x + 50, section5.stable_grounds[4].y - 30))
    section5.items.append(interactive_object(20, 20, section5.stable_grounds[0].x + 400, section5.stable_grounds[0].y - 30))
    section5.items.append(interactive_object(20, 20, section5.stable_grounds[7].x + section5.stable_grounds[7].width + 100, section5.stable_grounds[7].y + 200))

    for i in range(len(stars)):
        stars[i].setPos(-10000, -10000)

    if (stars[5].collect == False):
        stars[5].setPos(section5.stable_grounds[6].x + 50, section5.stable_grounds[6].y - 40)

    if (stars[6].collect == False):
        stars[6].setPos(section5.stable_grounds[6].x + 50, section5.stable_grounds[6].y - 40)


    flowers[0].setPos(section5.stable_grounds[7].x + 50, section5.stable_grounds[7].y - 60)
    flowers[0].note.setPos(flowers[0].x, flowers[0].y - 40)
    flowers[0].surface = pygame.image.load('media/flower.png').convert_alpha()

    flowers[1].setPos(section5.stable_grounds[5].x + 50, section5.stable_grounds[5].y - 60)
    flowers[1].note.setPos(flowers[1].x, flowers[1].y - 40)
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
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
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
    global screen

    if (npc2_talk == True):
        flowers[0].interact(pressedKey, Anna)
        flowers[1].interact(pressedKey, Anna)

    if (scenechange != 1):
        section_gameplay(section5)

    section5.stable_grounds[9].bonfire_anim()
    section5.stable_grounds[10].bonfire_anim()

    for i in range(len(section5.npc)):
        section5.npc[i].crazy_npc_anim()

    section5.gates[0].enter_gate(pressedKey, Anna)

    if (section5.gates[0].active == True and scenechange == -1):
        section_area = 6
        save_count += 1
        saving = (6, 3600, HEIGHT - 900)
        scenechange = 0


    screen.blit(flowers[0].getSurface(), flowers[0].getPos())
    screen.blit(flowers[1].getSurface(), flowers[1].getPos())
    screen.blit(stars[5].getSurface(), stars[5].getPos())
    screen.blit(stars[6].getSurface(), stars[6].getPos())

def section6_init():
    # Initiate the first section
    global section6
    global screen

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
    section6.stable_grounds.append(ground(200, 50, section6.stable_grounds[11].x + section6.stable_grounds[11].width - 300, section6.stable_grounds[11].y - 300))
    section6.stable_grounds.append(ground(200, 50, section6.stable_grounds[11].x + section6.stable_grounds[11].width - 700, section6.stable_grounds[11].y - 450))
    section6.stable_grounds.append(ground(200, 50, section6.stable_grounds[11].x + section6.stable_grounds[11].width - 1000, section6.stable_grounds[11].y - 300))
    section6.stable_grounds.append(ground(200, 50, section6.stable_grounds[11].x + section6.stable_grounds[11].width - 1300, section6.stable_grounds[11].y - 150))


    for i in range(len(section6.stable_grounds)):
        section6.stable_grounds[i].surface = pygame.image.load('media/caveground.png').convert_alpha()
        section6.stable_grounds[i].surface = pygame.transform.scale(section6.stable_grounds[i].surface, (section6.stable_grounds[i].width, min(section6.stable_grounds[i].height, 300)))


    # Signs
    section6.stable_grounds.append(ground(60, 60, section6.stable_grounds[4].x + section6.stable_grounds[4].width - 50, section6.stable_grounds[4].y - 60))
    section6.stable_grounds[17].surface = pygame.image.load('media/sign_00.png').convert_alpha()
    section6.stable_grounds[17].surface = pygame.transform.flip(section6.stable_grounds[17].surface, 1, 0)
    section6.stable_grounds[17].surface = pygame.transform.scale(section6.stable_grounds[17].surface, (60, 60))

    section6.stable_grounds.append(ground(1500, 100, section6.stable_grounds[11].x, section6.stable_grounds[11].y + 600))
    section6.stable_grounds[18].surface = pygame.image.load('media/caveground.png').convert_alpha()
    section6.stable_grounds[18].surface = pygame.transform.scale(section6.stable_grounds[18].surface, (section6.stable_grounds[18].width, min(section6.stable_grounds[18].height, 300)))

    section6.stable_grounds.append(ground(60, 60, section6.stable_grounds[18].x + 100,section6.stable_grounds[18].y - 60))
    section6.stable_grounds[19].surface = pygame.image.load('media/sign_01.png').convert_alpha()
    section6.stable_grounds[19].surface = pygame.transform.flip(section6.stable_grounds[19].surface, 1, 0)
    section6.stable_grounds[19].surface = pygame.transform.scale(section6.stable_grounds[19].surface, (60, 60))


    section6.waters.append(water(1000, HEIGHT, section6.stable_grounds[4].x + section6.stable_grounds[4].width, section6.stable_grounds[4].y + 200))


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
    boss_trigger = trigger(50, 3*HEIGHT, section6.stable_grounds[11].x + section6.stable_grounds[11].width - 800, section6.stable_grounds[11].y - 3*HEIGHT)

    global easter_trigger
    easter_trigger = trigger(50, abs(section6.stable_grounds[18].y - section6.stable_grounds[11].y - section6.stable_grounds[11].height), section6.stable_grounds[18].x + section6.stable_grounds[18].width - 300, section6.stable_grounds[11].y + section6.stable_grounds[11].height)

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
    section6.moving_enemies.append(jumping_enemy(150, 150, section6.stable_grounds[0].x, section6.stable_grounds[0].y - 150))
    section6.moving_enemies[0].set_rangex(section6.stable_grounds[0].x, section6.stable_grounds[5].x)
    section6.moving_enemies.append(jumping_enemy(150, 150, section6.stable_grounds[6].x - 60, section6.stable_grounds[0].y - 150))
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
    for i in range(len(stars)):
        stars[i].setPos(-10000, -10000)

    if (stars[7].collect == False):
        stars[7].setPos(section6.stable_grounds[2].x - 100, section6.stable_grounds[6].y - 150)

    section6.items.append(interactive_object(20, 20, section6.stable_grounds[12].x + 1000, section6.stable_grounds[12].y - 30))
    section6.items.append(interactive_object(20, 20, section6.stable_grounds[5].x + 50, section6.stable_grounds[5].y - 30))
    section6.items.append(interactive_object(20, 20, section6.stable_grounds[1].x + 50, section6.stable_grounds[1].y - 30))
    section6.items.append(interactive_object(20, 20, section6.stable_grounds[12].x + 500, section6.stable_grounds[12].y - 30))

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
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
    bg.append(pygame.image.load('media/cavebackground2.png').convert())
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
    global screen
    global conversation

    if (npc2_talk == True):
        flowers[2].interact(pressedKey, Anna)

    if (scenechange != 1):
        section_gameplay(section6)

    section6.gates[0].enter_gate(pressedKey, Anna)

    # Boss fight
    global boss_trigger


    if (boss_trigger.checkcollision(boss_trigger, Anna)):
        if (pygame.mixer.Channel(12).get_busy() == False):
            pygame.mixer.Channel(12).play(pygame.mixer.Sound('media/boss_theme.wav'), 1)
            pygame.mixer.Channel(11).stop()
            pygame.mixer.Channel(12).set_volume(0.05)

        boss_fight = True
        boss_trigger.setPos(-10000, -10000)
        if (conversation.dialogue_unlocked[25] == False):
            conversation.dialogueLEVEL = 25

    if (boss_fight == True and conversation.dialogueLEVEL == -1 and conversation.dialogue_unlocked[25] == True):
        big_boss.boss_attack(Anna)
        big_boss.boss_die()
    else:
        big_boss.boss_idle_ani()

    if (boss_fight == True and big_boss.hp > 0):
        if (Anna.x > section6.stable_grounds[7].x + section6.stable_grounds[7].width - Anna.width):
            Anna.setPos(section6.stable_grounds[7].x + section6.stable_grounds[7].width - Anna.width, Anna.y)

    if (big_boss.hp <= 0):
        pygame.mixer.Channel(12).stop()
        if (pygame.mixer.Channel(11).get_busy() == False):
            pygame.mixer.Channel(11).play(pygame.mixer.Sound('media/cave1.wav'), 1)
            pygame.mixer.Channel(11).set_volume(0.05)

    if (big_boss.hp <= 0 and flowers[2].collect == False):
        flowers[2].setPos(section6.stable_grounds[11].x + 200, section6.stable_grounds[11].y - 50)
        flowers[2].note.setPos(flowers[2].x, flowers[2].y - 40)
        screen.blit(flowers[2].getSurface(), flowers[2].getPos())


    # Easter Egg
    if (Anna.checkcollision(Anna, easter_trigger) and easter_trigger.x >= -5000):
        easter_trigger.setPos(-10000, -10000)
        easter_start = True

    '''if (easter_start == True):
        # Make the strange Npc runs away'''



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

    if (Anna.x < 0):
        Anna.setPos(0, Anna.y)


    screen.blit(big_boss.getSurface(), big_boss.getPos())

    for i in range(len(big_boss.rocks)):
        screen.blit(big_boss.rocks[i].getSurface(), big_boss.rocks[i].getPos())

    screen.blit(stars[7].getSurface(), stars[7].getPos())


def section7_init():
    # Initiate the first section
    global section7
    global screen

    section7 = section()

    section7.waters.append(water(2*WIDTH, 2*HEIGHT, -WIDTH, 0))
    section7.waters.append(water(2 * WIDTH, 2 * HEIGHT, section7.waters[0].x + section7.waters[0].width, 0))


    # Items
    for i in range(len(stars)):
        stars[i].setPos(-10000, -10000)

    if (stars[8].collect == False):
        stars[8].setPos(section7.waters[0].x + 100, section7.waters[0].y + 1000)

    for i in range(20):
        section7.items.append(interactive_object(20, 20, section7.waters[0].x + random.randrange(1700), section7.waters[0].y + random.randrange(800)))

        while True:
            check = True
            for j in range(i):
                if (i != j and section7.items[i].checkcollision(section7.items[i], section7.items[j])):
                    section7.items[i].setPos(section7.waters[0].x + random.randrange(1500), section7.waters[0].y + random.randrange(400))
                    check = False
                    break

            if (check == True):
                break

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
    global screen

    if (scenechange != 1):
        section_gameplay(section7)

    if (Anna.x <= 0 and scenechange == -1):
        section_area = 10
        save_count += 1
        saving = (12, 3500 - WIDTH, HEIGHT - 300)
        scenechange = 0


def section8_init():
    # Initiate the first section
    global section8
    global screen

    section8 = section()

    section8.stable_grounds.append(ground(WIDTH, 2*HEIGHT, 0, 2*HEIGHT - 200))
    section8.stable_grounds.append(ground(WIDTH, 2 * HEIGHT, section8.stable_grounds[0].x + section8.stable_grounds[0].width, 2 * HEIGHT - 200))

    # Signs
    section8.stable_grounds.append(ground(100, 100, section8.stable_grounds[1].x + section8.stable_grounds[1].width - 800, section8.stable_grounds[1].y - 100))
    section8.stable_grounds[2].surface = pygame.image.load('media/sign_02.png').convert_alpha()
    section8.stable_grounds[2].surface = pygame.transform.scale(section8.stable_grounds[2].surface, (100, 100))

    section8.items.append(water_fountain(200, 180, section8.stable_grounds[0].x + 1100, section8.stable_grounds[0].y - 170))

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


    # Items
    for i in range(len(stars)):
        stars[i].setPos(-10000, -10000)

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
    global screen
    global cutscenelevel

    if (scenechange != 1):
        section_gameplay(section8)

    section8.items[0].fountain_anim()

    if (section8.items[0].put_coin(pressedKey, Anna, coins_collect, screen) == 5):
        coins_collect -= 15
        gate_open = True

    if (gate_open == True):
        section8.gates[0].setPos(section8.stable_grounds[0].x + 1600, section8.stable_grounds[0].y - 80)
        cutscenelevel = 2

    if (Anna.x <= -Anna.width and scenechange == -1):
        section_area = 6
        save_count += 1
        saving = (6, 4*WIDTH + 1250, HEIGHT - 200)
        scenechange = 0

    if (Anna.x > WIDTH - Anna.width):
        Anna.setPos(WIDTH - Anna.width, Anna.y)


# Extra scenes
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
            delay_mouse = 0
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

# Intro cutscenes
def cutscene01():
    global start_ticks
    global prog_start
    global delay_mouse

    text01 = text(100, 70, '"In a Wonderland they lie, Dreaming as the days go by,', 28, "Renogare", BLACK)
    x = WIDTH / 2 - text01.getText().get_width() / 2
    y = HEIGHT / 2 - text01.getText().get_height() / 2 -200
    text01.textsetpos(x, y)
    start_ticks = pygame.time.get_ticks()


    if (start_ticks - prog_start)/1000 > 1.1:
        text01.textsetColor(cs)
    if (start_ticks - prog_start)/1000 > 1.25:
        text01.textsetColor(cs0)
    if (start_ticks - prog_start)/1000 > 1.4:
        text01.textsetColor(cs1)
    if (start_ticks - prog_start)/1000 > 1.55:
        text01.textsetColor(cs2)
    if (start_ticks - prog_start)/1000 > 1.7:
        text01.textsetColor(cs3)
    if (start_ticks - prog_start)/1000 > 1.85:
        text01.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 25.1:
        text01.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 25.25:
        text01.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 25.4:
        text01.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 25.55:
        text01.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 25.7:
        text01.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 25.85:
        text01.textsetColor(BLACK)

    screen.blit(text01.getText(), text01.gettextpos())


    text02 = text(100, 70, 'Dreaming as the summers die,', 28, "Renogare", BLACK)
    x = WIDTH / 2 - text02.getText().get_width() / 2
    y = HEIGHT / 2 - text02.getText().get_height() / 2 - 150
    text02.textsetpos(x, y)
    start_ticks = pygame.time.get_ticks()


    if (start_ticks - prog_start) / 1000 > 5.1:
        text02.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 5.25:
        text02.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 5.4:
        text02.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 5.55:
        text02.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 5.7:
        text02.textsetColor(cs3)
    if (start_ticks - prog_start)/ 1000 > 5.85:
        text02.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 25.1:
        text02.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 25.25:
        text02.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 25.4:
        text02.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 25.55:
        text02.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 25.7:
        text02.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 25.85:
        text02.textsetColor(BLACK)


    screen.blit(text02.getText(), text02.gettextpos())


    text03 = text(100, 70, 'Ever drifting down the stream, Lingering in the golden gleam, ', 28, "Renogare", BLACK)
    x = WIDTH / 2 - text03.getText().get_width() / 2
    y = HEIGHT / 2 - text03.getText().get_height() / 2 - 100
    text03.textsetpos(x, y)
    start_ticks = pygame.time.get_ticks()


    if (start_ticks - prog_start) / 1000 > 9.1:
        text03.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 9.25:
        text03.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 9.4:
        text03.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 9.55:
        text03.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 9.7:
        text03.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 9.85:
        text03.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 25.1:
        text03.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 25.25:
        text03.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 25.4:
        text03.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 25.55:
        text03.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 25.7:
        text03.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 25.85:
        text03.textsetColor(BLACK)


    screen.blit(text03.getText(), text03.gettextpos())


    text04 = text(100, 70, 'Life, what is it but a dream?"', 28, "Renogare", BLACK)
    x = WIDTH / 2 - text04.getText().get_width() / 2
    y = HEIGHT / 2 - text04.getText().get_height() / 2 - 50
    text04.textsetpos(x, y)

    start_ticks = pygame.time.get_ticks()


    if (start_ticks - prog_start) / 1000 > 14.1:
        text04.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 14.25:
        text04.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 14.4:
        text04.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 14.55:
        text04.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 14.7:
        text04.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 14.85:
        text04.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 25.1:
        text04.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 25.25:
        text04.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 25.4:
        text04.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 25.55:
        text04.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 25.7:
        text04.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 25.85:
        text04.textsetColor(BLACK)


    screen.blit(text04.getText(), text04.gettextpos())


    global section_area
    global cutscenelevel

    text05 = text(100, 70, '-Lewis Carroll, Through the Looking Glass', 26, "Renogare", BLACK)
    x = WIDTH / 2 - text05.getText().get_width() / 2
    y = HEIGHT / 2 - text05.getText().get_height() / 2 + 175
    text05.textsetpos(x, y)

    start_ticks = pygame.time.get_ticks()


    if (start_ticks - prog_start) / 1000 > 19.1:
        text05.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 19.25:
        text05.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 19.4:
        text05.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 19.55:
        text05.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 19.7:
        text05.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 19.85:
        text05.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 25.1:
        text05.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 25.25:
        text05.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 25.4:
        text05.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 25.55:
        text05.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 25.7:
        text05.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 25.85:
        text05.textsetColor(BLACK)
        section_area = 0
        cutscenelevel = 0
        prog_start = -1


    screen.blit(text05.getText(), text05.gettextpos())

    text19 = text(100, 70, 'Click anywhere to continue', 30, "Renogare", BLACK)
    text19.textsetColor(WHITE)
    text19.textsetpos(WIDTH - text19.getText().get_width() - 20, HEIGHT - text19.getText().get_height() - 20)

    screen.blit(text19.getText(), text19.gettextpos())


# Outtro
### outro\\

def cutscene02():
    global start_ticks
    global prog_start

    text06 = text(100, 70, "You're home! Welcome back.", 32, "Renogare", WHITE)
    x = WIDTH / 2 - text06.getText().get_width() / 2
    y = HEIGHT / 2 - text06.getText().get_height() / 2

    text06.textsetpos(x, y)


    if (start_ticks - prog_start) / 1000 > 1.1:
        text06.textsetColor(WHITE)
    if (start_ticks - prog_start) / 1000 > 1.25:
        text06.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 1.4:
        text06.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 1.55:
        text06.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 1.7:
        text06.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 1.85:
        text06.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 2.10:
        text06.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 > 5.1:
        text06.textsetColor(BLACK)
    if (start_ticks - prog_start) / 1000 > 5.25:
        text06.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 5.4:
        text06.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 5.55:
        text06.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 5.7:
        text06.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 5.85:
        text06.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 6.10:
        text06.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 1.1 and (start_ticks - prog_start) / 1000 <= 6.10:
        screen.blit(text06.getText(), text06.gettextpos())

    text07 = text(100, 70, '...', 40, "Renogare", WHITE)
    x = WIDTH / 2 - text07.getText().get_width() / 2
    y = HEIGHT / 2 - text07.getText().get_height() / 2
    text07.textsetpos(x, y)


    if (start_ticks - prog_start) / 1000 > 8.1:
        text07.textsetColor(WHITE)
    if (start_ticks - prog_start) / 1000 > 8.25:
        text07.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 8.4:
        text07.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 8.55:
        text07.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 8.7:
        text07.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 8.85:
        text07.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 9.10:
        text07.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 > 11.1:
        text07.textsetColor(BLACK)
    if (start_ticks - prog_start) / 1000 > 11.25:
        text07.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 11.4:
        text07.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 11.55:
        text07.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 11.7:
        text07.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 11.85:
        text07.textsetColor(cs3)
    if (start_ticks - prog_start)/ 1000 > 12.10:
        text07.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 8.1 and (start_ticks - prog_start) / 1000 <= 12.10:
        screen.blit(text07.getText(), text07.gettextpos())

    text08 = text(100, 70, 'We miss you so much', 40, "Renogare", WHITE)
    x = WIDTH / 2 - text08.getText().get_width() / 2
    y = HEIGHT / 2 - text08.getText().get_height() / 2
    text08.textsetpos(x, y)


    if (start_ticks - prog_start) / 1000 > 14.1:
        text08.textsetColor(WHITE)
    if (start_ticks - prog_start) / 1000 > 14.25:
        text08.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 14.4:
        text08.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 14.55:
        text08.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 14.7:
        text08.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 14.85:
        text08.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 15.10:
        text08.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 > 18.1:
        text08.textsetColor(BLACK)
    if (start_ticks - prog_start) / 1000 > 18.25:
        text08.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 18.4:
        text08.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 18.55:
        text08.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 18.7:
        text08.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 18.85:
        text08.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 18.10:
        text08.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 14.1 and (start_ticks - prog_start) / 1000 <= 18.10:
        screen.blit(text08.getText(), text08.gettextpos())


    text09 = text(100, 70, '...', 40, "Renogare", WHITE)
    x = WIDTH / 2 - text09.getText().get_width() / 2
    y = HEIGHT / 2 - text09.getText().get_height() / 2
    text09.textsetpos(x, y)

    if (start_ticks - prog_start) / 1000 > 20.1:
        text09.textsetColor(WHITE)
    if (start_ticks - prog_start) / 1000 > 20.25:
        text09.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 20.4:
        text09.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 20.55:
        text09.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 20.7:
        text09.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 20.85:
        text09.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 21.10:
        text09.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 > 23.1:
        text09.textsetColor(BLACK)
    if (start_ticks - prog_start) / 1000 > 23.25:
        text09.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 23.4:
        text09.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 23.55:
        text09.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 23.7:
        text09.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 23.85:
        text09.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 24.10:
        text09.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 20.1 and (start_ticks - prog_start) / 1000 <= 24.10:
        screen.blit(text09.getText(), text09.gettextpos())


    text10 = text(100, 70, 'We think of you everyday', 40, "Renogare", WHITE)
    x = WIDTH / 2 - text10.getText().get_width() / 2
    y = HEIGHT / 2 - text10.getText().get_height() / 2
    text10.textsetpos(x, y)


    if (start_ticks - prog_start) / 1000 > 26.1:
        text10.textsetColor(WHITE)
    if (start_ticks - prog_start) / 1000 > 26.25:
        text10.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 26.4:
        text10.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 26.55:
        text10.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 26.7:
        text10.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 26.85:
        text10.textsetColor(cs)
    if (start_ticks - prog_start)/ 1000 > 27.10:
        text10.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 > 29.1:
        text10.textsetColor(BLACK)
    if (start_ticks - prog_start) / 1000 > 29.25:
        text10.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 29.4:
        text10.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 29.55:
        text10.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 29.7:
        text10.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 29.85:
        text10.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 30.10:
        text10.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 26.1 and (start_ticks - prog_start) / 1000 <= 30.10:
        screen.blit(text10.getText(), text10.gettextpos())


    text11 = text(100, 70, 'Thinking you might come and play with us...', 40, "Renogare", WHITE)
    x = WIDTH / 2 - text11.getText().get_width() / 2
    y = HEIGHT / 2 - text11.getText().get_height() / 2
    text11.textsetpos(x, y)


    if (start_ticks - prog_start) / 1000 > 32.1:
        text11.textsetColor(WHITE)
    if (start_ticks - prog_start) / 1000 > 32.25:
        text11.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 32.4:
        text11.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 32.55:
        text11.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 32.7:
        text11.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 32.85:
        text11.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 33.10:
        text11.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 > 35.1:
        text11.textsetColor(BLACK)
    if (start_ticks - prog_start) / 1000 > 35.25:
        text11.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 35.4:
        text11.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 35.55:
        text11.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 35.7:
        text11.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 35.85:
        text11.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 36.10:
        text11.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 32.1 and (start_ticks - prog_start) / 1000 <= 36.10:
        screen.blit(text11.getText(), text11.gettextpos())

    text12 = text(100, 70, '...', 40, "Renogare", WHITE)
    x = WIDTH / 2 - text12.getText().get_width() / 2
    y = HEIGHT / 2 - text12.getText().get_height() / 2
    text12.textsetpos(x, y)

    if (start_ticks - prog_start) / 1000 > 38.1:
        text12.textsetColor(WHITE)
    if (start_ticks - prog_start) / 1000 > 38.25:
        text12.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 38.4:
        text12.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 38.55:
        text12.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 38.7:
        text12.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 38.85:
        text12.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 39.10:
        text12.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 > 41.1:
        text12.textsetColor(BLACK)
    if (start_ticks - prog_start) / 1000 > 41.25:
        text12.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 41.4:
        text12.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 41.55:
        text12.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 41.7:
        text12.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 41.85:
        text12.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 42.10:
        text12.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 38.1 and (start_ticks - prog_start) / 1000 <= 42.10:
        screen.blit(text12.getText(), text12.gettextpos())

    text13 = text(100, 70, "Don't you leave me ever again!", 40, "Renogare", WHITE)
    x = WIDTH / 2 - text13.getText().get_width() / 2
    y = HEIGHT / 2 - text13.getText().get_height() / 2
    text13.textsetpos(x, y)


    if (start_ticks - prog_start) / 1000 > 44.1:
        text13.textsetColor(WHITE)
    if (start_ticks - prog_start) / 1000 > 44.25:
        text13.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 44.4:
        text13.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 44.55:
        text13.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 44.7:
        text13.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 44.85:
        text13.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 45.10:
        text13.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 > 47.1:
        text13.textsetColor(BLACK)
    if (start_ticks - prog_start) / 1000 > 47.25:
        text13.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 47.4:
        text13.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 47.55:
        text13.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 47.7:
        text13.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 47.85:
        text13.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 48.10:
        text13.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 44.1 and (start_ticks - prog_start) / 1000 <= 48.10:
        screen.blit(text13.getText(), text13.gettextpos())

    text14 = text(100, 70, '...', 40, "Renogare", WHITE)
    x = WIDTH / 2 - text14.getText().get_width() / 2
    y = HEIGHT / 2 - text14.getText().get_height() / 2
    text14.textsetpos(x, y)


    if (start_ticks - prog_start) / 1000 > 50.1:
        text14.textsetColor(WHITE)
    if (start_ticks - prog_start) / 1000 > 50.25:
        text14.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 50.4:
        text14.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 50.55:
        text14.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 50.7:
        text14.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 50.85:
        text14.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 51.10:
        text14.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 > 53.1:
        text14.textsetColor(BLACK)
    if (start_ticks - prog_start) / 1000 > 53.25:
        text14.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 53.4:
        text14.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 53.55:
        text14.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 53.7:
        text14.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 53.85:
        text14.textsetColor(cs3)
    if (start_ticks - prog_start)/ 1000 > 55.10:
        text14.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 50.1 and (start_ticks - prog_start) / 1000 <= 55.10:
        screen.blit(text14.getText(), text14.gettextpos())

    global section_area
    global cutscenelevel

    text15 = text(100, 70, 'I miss you so much, I miss you so much, I miss-', 40, "Renogare", WHITE)
    x = WIDTH / 2 - text15.getText().get_width() / 2
    y = HEIGHT / 2 - text15.getText().get_height() / 2
    text15.textsetpos(x, y)


    if (start_ticks - prog_start) / 1000 > 57.1:
        text15.textsetColor(WHITE)
    if (start_ticks - prog_start) / 1000 > 57.25:
        text15.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 57.4:
        text15.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 57.55:
        text15.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 57.7:
        text15.textsetColor(cs0)
    if (start_ticks - prog_start)/ 1000 > 57.85:
        text15.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 58.10:
        text15.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 > 60.1:
        text15.textsetColor(BLACK)
    if (start_ticks - prog_start) / 1000 > 60.25:
        text15.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 60.4:
        text15.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 60.55:
        text15.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 60.7:
        text15.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 60.85:
        text15.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 61.10:
        text15.textsetColor(WHITE)
        cutscenelevel = 4
        section_area = -1
        prog_start = -1

    if (start_ticks - prog_start) / 1000 > 57.1 and (start_ticks - prog_start) / 1000 <= 61.10:
        screen.blit(text15.getText(), text15.gettextpos())

def cutscene03():
    global start_ticks
    global prog_start

    text01 = text(WIDTH/2, 400, 'To be continued', 50, "Renogare", BLACK)
    text01.textsetpos(WIDTH/2 - text01.getText().get_width()/2, HEIGHT/2 - text01.getText().get_height())


    if (start_ticks - prog_start)/1000 > 1.1:
        text01.textsetColor(cs)
    if (start_ticks - prog_start)/1000 > 1.25:
        text01.textsetColor(cs0)
    if (start_ticks - prog_start)/1000 > 1.4:
        text01.textsetColor(cs1)
    if (start_ticks - prog_start)/1000 > 1.55:
        text01.textsetColor(cs2)
    if (start_ticks - prog_start)/1000 > 1.7:
        text01.textsetColor(cs3)
    if (start_ticks - prog_start)/1000 > 1.85:
        text01.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 5.1:
        text01.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 5.25:
        text01.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 5.4:
        text01.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 5.55:
        text01.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 5.7:
        text01.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 5.85:
        text01.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 5.85:
        screen.blit(text01.getText(), text01.gettextpos())


    text02 = text(100, 70, 'Producers', 28, "Renogare", BLACK)
    text02.textsetpos(WIDTH / 2 - text02.getText().get_width()/2, HEIGHT / 2 - text02.getText().get_height())


    if (start_ticks - prog_start) / 1000 > 9.1:
        text02.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 9.25:
        text02.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 9.4:
        text02.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 9.55:
        text02.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 9.7:
        text02.textsetColor(cs3)
    if (start_ticks - prog_start)/ 1000 > 9.85:
        text02.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 13.1:
        text02.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 13.25:
        text02.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 13.4:
        text02.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 13.55:
        text02.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 13.7:
        text02.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 13.85:
        text02.textsetColor(BLACK)

    textt02 = text(100, 70, 'LONG TIEU and WAYNE SETO', 50, "Renogare", BLACK)
    textt02.textsetpos(WIDTH / 2 - textt02.getText().get_width()/2, text02.y + text02.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 9.1:
        textt02.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 9.25:
        textt02.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 9.4:
        textt02.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 9.55:
        textt02.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 9.7:
        textt02.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 9.85:
        textt02.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 13.1:
        textt02.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 13.25:
        textt02.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 13.4:
        textt02.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 13.55:
        textt02.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 13.7:
        textt02.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 13.85:
        textt02.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 13.85 and (start_ticks - prog_start) / 1000 > 5.85:
        screen.blit(text02.getText(), text02.gettextpos())
        screen.blit(textt02.getText(), textt02.gettextpos())


    text03 = text(100, 70, 'Pixel Arts', 28, "Renogare", BLACK)
    text03.textsetpos(WIDTH / 2 - text03.getText().get_width()/2, HEIGHT / 2 - text03.getText().get_height())


    if (start_ticks - prog_start) / 1000 > 17.1:
        text03.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 17.25:
        text03.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 17.4:
        text03.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 17.55:
        text03.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 17.7:
        text03.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 17.85:
        text03.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 21.1:
        text03.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 21.25:
        text03.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 21.4:
        text03.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 21.55:
        text03.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 21.7:
        text03.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 21.85:
        text03.textsetColor(BLACK)

    textt03 = text(100, 70, 'LONG TIEU', 50, "Renogare", BLACK)
    textt03.textsetpos(WIDTH / 2 - textt03.getText().get_width()/2, text03.y + text03.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 17.1:
        textt03.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 17.25:
        textt03.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 17.4:
        textt03.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 17.55:
        textt03.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 17.7:
        textt03.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 17.85:
        textt03.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 21.1:
        textt03.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 21.25:
        textt03.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 21.4:
        textt03.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 21.55:
        textt03.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 21.7:
        textt03.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 21.85:
        textt03.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 21.85 and (start_ticks - prog_start) / 1000 > 17.85:
        screen.blit(text03.getText(), text03.gettextpos())
        screen.blit(textt03.getText(), textt03.gettextpos())


    text04 = text(100, 70, 'Background Arts', 28, "Renogare", BLACK)
    text04.textsetpos(WIDTH / 2 - text04.getText().get_width()/2, HEIGHT / 2 - text04.getText().get_height())


    if (start_ticks - prog_start) / 1000 > 25.1:
        text04.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 25.25:
        text04.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 25.4:
        text04.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 25.55:
        text04.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 25.7:
        text04.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 25.85:
        text04.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 29.1:
        text04.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 29.25:
        text04.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 29.4:
        text04.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 29.55:
        text04.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 29.7:
        text04.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 29.85:
        text04.textsetColor(BLACK)


    textt04 = text(100, 70, 'WAYNE SETO', 50, "Renogare", BLACK)
    textt04.textsetpos(WIDTH / 2 - textt04.getText().get_width()/2, text04.y + text04.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 25.1:
        textt04.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 25.25:
        textt04.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 25.4:
        textt04.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 25.55:
        textt04.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 25.7:
        textt04.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 25.85:
        textt04.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 29.1:
        textt04.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 29.25:
        textt04.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 29.4:
        textt04.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 29.55:
        textt04.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 29.7:
        textt04.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 29.85:
        textt04.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 29.85 and (start_ticks - prog_start) / 1000 > 25.85:
        screen.blit(text04.getText(), text04.gettextpos())
        screen.blit(textt04.getText(), textt04.gettextpos())



    text05 = text(100, 70, 'Map Design', 26, "Renogare", BLACK)
    text05.textsetpos(WIDTH / 2 - text05.getText().get_width()/2, HEIGHT / 2 - text05.getText().get_height())


    if (start_ticks - prog_start) / 1000 > 33.1:
        text05.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 33.25:
        text05.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 33.4:
        text05.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 33.55:
        text05.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 33.7:
        text05.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 33.85:
        text05.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 37.1:
        text05.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 37.25:
        text05.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 37.4:
        text05.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 37.55:
        text05.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 37.7:
        text05.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 37.85:
        text05.textsetColor(BLACK)


    textt05 = text(100, 70, 'LONG TIEU', 50, "Renogare", BLACK)
    textt05.textsetpos(WIDTH / 2 - textt05.getText().get_width()/2, text05.y + text05.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 29.1:
        textt05.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 29.25:
        textt05.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 29.4:
        textt05.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 29.55:
        textt05.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 29.7:
        textt05.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 29.85:
        textt05.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 37.1:
        textt05.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 37.25:
        textt05.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 37.4:
        textt05.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 37.55:
        textt05.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 37.7:
        textt05.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 37.85:
        textt05.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 37.85 and (start_ticks - prog_start) / 1000 > 33.85:
        screen.blit(text05.getText(), text05.gettextpos())
        screen.blit(textt05.getText(), textt05.gettextpos())

    text06 = text(100, 70, 'Presentation', 26, "Renogare", BLACK)
    text06.textsetpos(WIDTH / 2 - text06.getText().get_width()/2, HEIGHT / 2 - text06.getText().get_height())

    if (start_ticks - prog_start) / 1000 > 41.1:
        text06.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 41.25:
        text06.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 41.4:
        text06.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 41.55:
        text06.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 41.7:
        text06.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 41.85:
        text06.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 45.1:
        text06.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 45.25:
        text06.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 45.4:
        text06.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 45.55:
        text06.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 45.7:
        text06.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 45.85:
        text06.textsetColor(BLACK)

    textt06 = text(100, 70, 'WAYNE SETO', 50, "Renogare", BLACK)
    textt06.textsetpos(WIDTH / 2 - textt06.getText().get_width()/2, text06.y + text06.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 41.1:
        textt06.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 41.25:
        textt06.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 41.4:
        textt06.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 41.55:
        textt06.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 41.7:
        textt06.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 41.85:
        textt06.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 45.1:
        textt06.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 45.25:
        textt06.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 45.4:
        textt06.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 45.55:
        textt06.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 45.7:
        textt06.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 45.85:
        textt06.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 45.85 and (start_ticks - prog_start) / 1000 > 41.85:
        screen.blit(text06.getText(), text06.gettextpos())
        screen.blit(textt06.getText(), textt06.gettextpos())


    text07 = text(100, 70, 'Images Source', 26, "Renogare", BLACK)
    text07.textsetpos(WIDTH / 2 - text07.getText().get_width() / 2, HEIGHT / 2 - text07.getText().get_height())

    if (start_ticks - prog_start) / 1000 > 49.1:
        text07.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 49.25:
        text07.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 49.4:
        text07.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 49.55:
        text07.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 49.7:
        text07.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 49.85:
        text07.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 53.1:
        text07.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 53.25:
        text07.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 53.4:
        text07.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 53.55:
        text07.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 53.7:
        text07.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 53.85:
        text07.textsetColor(BLACK)

    textt07 = text(100, 70, 'GOOGLE', 50, "Renogare", BLACK)
    textt07.textsetpos(WIDTH / 2 - textt07.getText().get_width()/2, text07.y + text07.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 49.1:
        textt07.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 49.25:
        textt07.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 49.4:
        textt07.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 49.55:
        textt07.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 49.7:
        textt07.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 49.85:
        textt07.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 53.1:
        textt07.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 53.25:
        textt07.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 53.4:
        textt07.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 53.55:
        textt07.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 53.7:
        textt07.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 53.85:
        textt07.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 49.85 and (start_ticks - prog_start) / 1000 > 53.85:
        screen.blit(text07.getText(), text07.gettextpos())
        screen.blit(textt07.getText(), textt07.gettextpos())

    text08 = text(100, 70, 'Start Screen Music', 26, "Renogare", BLACK)
    text08.textsetpos(WIDTH / 2 - text08.getText().get_width() / 2, HEIGHT / 2 - text08.getText().get_height())

    if (start_ticks - prog_start) / 1000 > 57.1:
        text08.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 57.25:
        text08.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 >57.4:
        text08.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 57.55:
        text08.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 57.7:
        text08.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 57.85:
        text08.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 61.1:
        text08.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 61.25:
        text08.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 61.4:
        text08.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 61.55:
        text08.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 61.7:
        text08.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 61.85:
        text08.textsetColor(BLACK)

    textt08 = text(100, 70, 'The Long Dark Theme', 50, "Renogare", BLACK)
    textt08.textsetpos(WIDTH / 2 - textt08.getText().get_width()/2, text08.y + text08.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 57.1:
        textt08.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 57.25:
        textt08.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 57.4:
        textt08.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 57.55:
        textt08.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 57.7:
        textt08.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 57.85:
        textt08.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 61.1:
        textt08.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 61.25:
        textt08.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 61.4:
        textt08.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 61.55:
        textt08.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 61.7:
        textt08.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 61.85:
        textt08.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 61.85 and (start_ticks - prog_start) / 1000 > 57.85:
        screen.blit(text08.getText(), text08.gettextpos())
        screen.blit(textt08.getText(), textt07.gettextpos())


    text09 = text(100, 70, 'Ambient Music', 26, "Renogare", BLACK)
    text09.textsetpos(WIDTH / 2 - text09.getText().get_width() / 2, HEIGHT / 2 - text09.getText().get_height())

    if (start_ticks - prog_start) / 1000 > 65.1:
        text09.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 65.25:
        text09.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 65.4:
        text09.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 65.55:
        text09.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 65.7:
        text09.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 65.85:
        text09.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 69.1:
        text09.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 69.25:
        text09.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 69.4:
        text09.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 69.55:
        text09.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 69.7:
        text09.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 69.85:
        text09.textsetColor(BLACK)

    textt09 = text(100, 70, 'Night Forest Sound', 50, "Renogare", BLACK)
    textt09.textsetpos(WIDTH / 2 - textt09.getText().get_width()/2, text09.y + text09.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 65.1:
        textt09.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 65.25:
        textt09.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 65.4:
        textt09.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 65.55:
        textt09.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 65.7:
        textt09.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 65.85:
        textt09.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 69.1:
        textt09.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 69.25:
        textt09.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 69.4:
        textt09.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 69.55:
        textt09.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 69.7:
        textt09.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 69.85:
        textt09.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 65.85 and (start_ticks - prog_start) / 1000 > 69.85:
        screen.blit(text09.getText(), text09.gettextpos())
        screen.blit(textt09.getText(), textt09.gettextpos())

    text10 = text(100, 70, 'Movement Sounds', 26, "Renogare", BLACK)
    text10.textsetpos(WIDTH / 2 - text10.getText().get_width() / 2, HEIGHT / 2 - text10.getText().get_height())

    if (start_ticks - prog_start) / 1000 > 73.1:
        text10.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 73.25:
        text10.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 73.4:
        text10.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 73.55:
        text10.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 73.7:
        text10.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 73.85:
        text10.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 77.1:
        text10.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 77.25:
        text10.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 77.4:
        text10.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 77.55:
        text10.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 77.7:
        text10.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 77.85:
        text10.textsetColor(BLACK)

    textt10 = text(100, 70, 'https://www.youtube.com', 50, "Renogare", BLACK)
    textt10.textsetpos(WIDTH / 2 - textt10.getText().get_width()/2, text10.y + text10.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 73.1:
        textt10.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 73.25:
        textt10.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 73.4:
        textt10.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 73.55:
        textt10.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 73.7:
        textt10.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 73.85:
        textt10.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 77.1:
        textt10.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 77.25:
        textt10.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 77.4:
        textt10.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 77.55:
        textt10.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 77.7:
        textt10.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 77.85:
        textt10.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 73.85 and (start_ticks - prog_start) / 1000 > 77.85:
        screen.blit(text10.getText(), text10.gettextpos())
        screen.blit(textt10.getText(), textt10.gettextpos())

    text11 = text(100, 70, 'Pause Screen Music', 26, "Renogare", BLACK)
    text11.textsetpos(WIDTH / 2 - text11.getText().get_width() / 2, HEIGHT / 2 - text11.getText().get_height())

    if (start_ticks - prog_start) / 1000 > 81.1:
        text11.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 81.25:
        text11.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 81.4:
        text11.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 81.55:
        text11.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 81.7:
        text11.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 81.85:
        text11.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 85.1:
        text11.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 85.25:
        text11.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 85.4:
        text11.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 85.55:
        text11.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 85.7:
        text11.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 85.85:
        text11.textsetColor(BLACK)

    textt11 = text(100, 70, 'GRIS OST - Mae', 50, "Renogare", BLACK)
    textt11.textsetpos(WIDTH / 2 - textt11.getText().get_width()/2, text11.y + text11.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 81.1:
        textt11.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 81.25:
        textt11.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 81.4:
        textt11.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 81.55:
        textt11.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 81.7:
        textt11.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 81.85:
        textt11.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 85.1:
        textt11.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 85.25:
        textt11.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 85.4:
        textt11.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 85.55:
        textt11.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 85.7:
        textt11.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 85.85:
        textt11.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 85.85 and (start_ticks - prog_start) / 1000 > 81.85:
        screen.blit(text11.getText(), text11.gettextpos())
        screen.blit(textt11.getText(), textt11.gettextpos())

    text12 = text(100, 70, 'Credit Scene Music', 26, "Renogare", BLACK)
    text12.textsetpos(WIDTH / 2 - text12.getText().get_width() / 2, HEIGHT / 2 - text12.getText().get_height())

    if (start_ticks - prog_start) / 1000 > 89.1:
        text12.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 89.25:
        text12.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 89.4:
        text12.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 89.55:
        text12.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 89.7:
        text12.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 89.85:
        text12.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 93.1:
        text12.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 93.25:
        text12.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 93.4:
        text12.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 93.55:
        text12.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 93.7:
        text12.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 93.85:
        text12.textsetColor(BLACK)

    textt12 = text(100, 70, 'GRIS OST - In Your Hands', 50, "Renogare", BLACK)
    textt12.textsetpos(WIDTH / 2 - textt12.getText().get_width()/2, text12.y + text12.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 89.1:
        textt12.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 89.25:
        textt12.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 89.4:
        textt12.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 89.55:
        textt12.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 89.7:
        textt12.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 89.85:
        textt12.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 93.1:
        textt12.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 93.25:
        textt12.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 93.4:
        textt12.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 93.55:
        textt12.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 93.7:
        textt12.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 93.85:
        textt12.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 93.85 and (start_ticks - prog_start) / 1000 > 89.85:
        screen.blit(text12.getText(), text12.gettextpos())
        screen.blit(textt12.getText(), textt12.gettextpos())

    text13 = text(100, 70, 'Outro Sound', 26, "Renogare", BLACK)
    text13.textsetpos(WIDTH / 2 - text13.getText().get_width() / 2, HEIGHT / 2 - text13.getText().get_height())

    if (start_ticks - prog_start) / 1000 > 97.1:
        text13.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 97.25:
        text13.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 97.4:
        text13.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 97.55:
        text13.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 97.7:
        text13.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 97.85:
        text13.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 101.1:
        text13.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 101.25:
        text13.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 101.4:
        text13.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 101.55:
        text13.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 101.7:
        text13.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 101.85:
        text13.textsetColor(BLACK)

    textt13 = text(100, 70, 'https://www.youtube.com', 50, "Renogare", BLACK)
    textt13.textsetpos(WIDTH / 2 - textt13.getText().get_width()/2, text13.y + text13.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 97.1:
        textt13.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 97.25:
        textt13.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 97.4:
        textt13.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 97.55:
        textt13.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 97.7:
        textt13.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 97.85:
        textt13.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 101.1:
        textt13.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 101.25:
        textt13.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 101.4:
        textt13.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 101.55:
        textt13.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 101.7:
        textt13.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 101.85:
        textt13.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 101.85 and (start_ticks - prog_start) / 1000 > 97.85:
        screen.blit(text13.getText(), text13.gettextpos())
        screen.blit(textt13.getText(), textt13.gettextpos())

    text14 = text(100, 70, 'with thanks to', 26, "Renogare", BLACK)
    text14.textsetpos(WIDTH / 2 - text14.getText().get_width() / 2, HEIGHT / 2 - text14.getText().get_height())

    if (start_ticks - prog_start) / 1000 > 105.1:
        text14.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 105.25:
        text14.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 105.4:
        text14.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 105.55:
        text14.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 105.7:
        text14.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 105.85:
        text14.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 109.1:
        text14.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 109.25:
        text14.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 109.4:
        text14.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 109.55:
        text14.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 109.7:
        text14.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 109.85:
        text14.textsetColor(BLACK)

    textt14 = text(100, 70, 'our teacher Michael Zhang', 50, "Renogare", BLACK)
    textt14.textsetpos(WIDTH / 2 - textt14.getText().get_width()/2, text14.y + text14.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 105.1:
        textt14.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 105.25:
        textt14.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 105.4:
        textt14.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 105.55:
        textt14.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 105.7:
        textt14.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 105.85:
        textt14.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 109.1:
        textt14.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 109.25:
        textt14.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 109.4:
        textt14.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 109.55:
        textt14.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 109.7:
        textt14.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 109.85:
        textt14.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 109.85 and (start_ticks - prog_start) / 1000 > 105.85:
        screen.blit(text14.getText(), text14.gettextpos())
        screen.blit(textt14.getText(), textt14.gettextpos())


    text15 = text(100, 70, 'Programming IDE', 26, "Renogare", BLACK)
    text15.textsetpos(WIDTH / 2 - text15.getText().get_width() / 2, HEIGHT / 2 - text15.getText().get_height())

    if (start_ticks - prog_start) / 1000 > 113.1:
        text15.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 113.25:
        text15.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 113.4:
        text15.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 113.55:
        text15.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 113.7:
        text15.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 113.85:
        text15.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 117.1:
        text15.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 117.25:
        text15.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 117.4:
        text15.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 117.55:
        text15.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 117.7:
        text15.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 117.85:
        text15.textsetColor(BLACK)

    textt15 = text(100, 70, 'PYCHARM COMMUNITY', 50, "Renogare", BLACK)
    textt15.textsetpos(WIDTH / 2 - textt15.getText().get_width()/2, text15.y + text15.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 113.1:
        textt15.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 113.25:
        textt15.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 113.4:
        textt15.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 113.55:
        textt15.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 113.7:
        textt15.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 113.85:
        textt15.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 117.1:
        textt15.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 117.25:
        textt15.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 117.4:
        textt15.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 117.55:
        textt15.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 117.7:
        textt15.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 117.85:
        textt15.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 117.85 and (start_ticks - prog_start) / 1000 > 113.85:
        screen.blit(text15.getText(), text15.gettextpos())
        screen.blit(textt15.getText(), textt15.gettextpos())

    text16 = text(100, 70, 'Pixel Drawing Site', 26, "Renogare", BLACK)
    text16.textsetpos(WIDTH / 2 - text16.getText().get_width() / 2, HEIGHT / 2 - text16.getText().get_height())

    if (start_ticks - prog_start) / 1000 > 121.1:
        text16.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 121.25:
        text16.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 121.4:
        text16.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 121.55:
        text16.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 121.7:
        text16.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 121.85:
        text16.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 125.1:
        text16.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 125.25:
        text16.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 125.4:
        text16.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 125.55:
        text16.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 125.7:
        text16.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 125.85:
        text16.textsetColor(BLACK)

    textt16 = text(100, 70, 'https://www.piskelapp.com', 50, "Renogare", BLACK)
    textt16.textsetpos(WIDTH / 2 - textt16.getText().get_width()/2, text16.y + text16.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 121.1:
        textt16.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 121.25:
        textt16.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 121.4:
        textt16.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 121.55:
        textt16.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 121.7:
        textt16.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 121.85:
        textt16.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 125.1:
        textt16.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 125.25:
        textt16.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 125.4:
        textt16.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 125.55:
        textt16.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 125.7:
        textt16.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 125.85:
        textt16.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 125.85 and (start_ticks - prog_start) / 1000 > 121.85:
        screen.blit(text16.getText(), text16.gettextpos())
        screen.blit(textt16.getText(), textt16.gettextpos())


    text17 = text(100, 70, 'Graphics Editor', 26, "Renogare", BLACK)
    text17.textsetpos(WIDTH / 2 - text17.getText().get_width() / 2, HEIGHT / 2 - text17.getText().get_height())

    if (start_ticks - prog_start) / 1000 > 129.1:
        text17.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 129.25:
        text17.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 129.4:
        text17.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 129.55:
        text17.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 129.7:
        text17.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 129.85:
        text17.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 133.1:
        text17.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 133.25:
        text17.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 133.4:
        text17.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 133.55:
        text17.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 133.7:
        text17.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 133.85:
        text17.textsetColor(BLACK)

    textt17 = text(100, 70, 'Adobe Photoshop', 50, "Renogare", BLACK)
    textt17.textsetpos(WIDTH / 2 - textt17.getText().get_width()/2, text17.y + text17.getText().get_height() + 10)

    if (start_ticks - prog_start) / 1000 > 129.1:
        textt17.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 129.25:
        textt17.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 129.4:
        textt17.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 129.55:
        textt17.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 129.7:
        textt17.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 129.85:
        textt17.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 133.1:
        textt17.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 133.25:
        textt17.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 133.4:
        textt17.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 133.55:
        textt17.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 133.7:
        textt17.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 133.85:
        textt17.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 133.85 and (start_ticks - prog_start) / 1000 > 129.85:
        screen.blit(text17.getText(), text17.gettextpos())
        screen.blit(textt17.getText(), textt17.gettextpos())

    text18 = text(100, 70, 'THANKS FOR PLAYING!', 50, "Renogare", BLACK)
    text18.textsetpos(WIDTH / 2 - text18.getText().get_width() / 2, HEIGHT/2 - text18.getText().get_height()/2)

    if (start_ticks - prog_start) / 1000 > 137.1:
        text18.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 137.25:
        text18.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 137.4:
        text18.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 137.55:
        text18.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 137.7:
        text18.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 137.85:
        text18.textsetColor(WHITE)

    if (start_ticks - prog_start) / 1000 > 141.1:
        text18.textsetColor(cs3)
    if (start_ticks - prog_start) / 1000 > 141.25:
        text18.textsetColor(cs2)
    if (start_ticks - prog_start) / 1000 > 141.4:
        text18.textsetColor(cs1)
    if (start_ticks - prog_start) / 1000 > 141.55:
        text18.textsetColor(cs0)
    if (start_ticks - prog_start) / 1000 > 141.7:
        text18.textsetColor(cs)
    if (start_ticks - prog_start) / 1000 > 141.85:
        text18.textsetColor(BLACK)

    if (start_ticks - prog_start) / 1000 <= 141.85 and (start_ticks - prog_start) / 1000 > 137.85:
        screen.blit(text18.getText(), text18.gettextpos())

    text19 = text(100, 70, 'Click anywhere to continue', 30, "Renogare", BLACK)
    text19.textsetColor(WHITE)
    text19.textsetpos(WIDTH - text19.getText().get_width() - 20, HEIGHT - text19.getText().get_height() - 20)

    if (start_ticks - prog_start) / 1000 > 5.85:
        screen.blit(text19.getText(), text19.gettextpos())


# Tutorial Sections
def tutorialmove():
    global instruction_screen

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

    screen.blit(instruction_screen.getSurface(), instruction_screen.getPos())
    screen.blit(tit01.getText(), tit01.gettextpos())
    screen.blit(tut01.getText(), tut01.gettextpos())
    screen.blit(tut02.getText(), tut02.gettextpos())
    screen.blit(tut03.getText(), tut03.gettextpos())
    screen.blit(tut04.getText(), tut04.gettextpos())
    screen.blit(tut05.getText(), tut05.gettextpos())
    screen.blit(exit01.getText(), exit01.gettextpos())

def tutorialatt():
    global instruction_screen

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

    tut09 = text(100, 70, "The third click aka combo can throw a cat ", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut09.getText().get_width() / 2
    y = HEIGHT / 2 - tut09.getText().get_height() / 2 + 50
    tut09.textsetpos(x, y)

    exit02 = text(100, 70, "Press [ ESC ] to EXIT INTERACTION PAGE", 35, "Renogare", WHITE)
    x = WIDTH / 2 - exit02.getText().get_width() / 2
    y = HEIGHT / 2 - exit02.getText().get_height() / 2 + 200
    exit02.textsetpos(x, y)

    screen.blit(instruction_screen.getSurface(), instruction_screen.getPos())
    screen.blit(tit2.getText(), tit2.gettextpos())
    screen.blit(tut06.getText(), tut06.gettextpos())
    screen.blit(tut07.getText(), tut07.gettextpos())
    screen.blit(tut08.getText(), tut08.gettextpos())
    screen.blit(tut09.getText(), tut09.gettextpos())
    screen.blit(exit02.getText(), exit02.gettextpos())

def tutorialspeatt():
    global instruction_screen

    tit3 = text(100, 70, "SPECIAL ATTACK TUTORIAL", 50, "Renogare", WHITE)
    x = WIDTH / 2 - tit3.getText().get_width() / 2
    y = HEIGHT / 2 - tit3.getText().get_height() / 2 - 200
    tit3.textsetpos(x, y)

    tut10 = text(100, 70, "Press [ MOUSE RIGHT-CLICK ] to initial special attack", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut10.getText().get_width() / 2
    y = HEIGHT / 2 - tut10.getText().get_height() / 2 - 100
    tut10.textsetpos(x, y)

    tut11 = text(100, 70, "It will stun the enemy", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut11.getText().get_width() / 2
    y = HEIGHT / 2 - tut11.getText().get_height() / 2 - 50
    tut11.textsetpos(x, y)

    tut12 = text(100, 70, "It will use up all the paintnergy", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut12.getText().get_width() / 2
    y = HEIGHT / 2 - tut12.getText().get_height() / 2
    tut12.textsetpos(x, y)

    tut13 = text(100, 70, "Press [ E ] to interact with the environment", 35, "Renogare", WHITE)
    x = WIDTH / 2 - tut13.getText().get_width() / 2
    y = HEIGHT / 2 - tut13.getText().get_height() / 2 + 50
    tut13.textsetpos(x, y)

    exit01 = text(100, 70, "Press [ ESC ] to EXIT INTERACTION PAGE", 35, "Renogare", WHITE)
    x = WIDTH / 2 - exit01.getText().get_width() / 2
    y = HEIGHT / 2 - exit01.getText().get_height() / 2 + 200
    exit01.textsetpos(x, y)

    screen.blit(instruction_screen.getSurface(), instruction_screen.getPos())
    screen.blit(tit3.getText(), tit3.gettextpos())
    screen.blit(tut10.getText(), tut10.gettextpos())
    screen.blit(tut11.getText(), tut11.gettextpos())
    screen.blit(tut12.getText(), tut12.gettextpos())
    screen.blit(tut13.getText(), tut13.gettextpos())
    screen.blit(exit01.getText(), exit01.gettextpos())


# --- CODE STARTS HERE --- #
running = True

while running:
    for event in pygame.event.get():  # Returns all input and triggers into an array
        if (event.type == pygame.QUIT): # If the red X was clicked
            running = False

        if event.type == pygame.KEYDOWN and section_area == -1 and cutscenelevel == 3:
            cutscenelevel = 1

        if (event.type == pygame.MOUSEBUTTONDOWN and cutscenelevel == 4 and (start_ticks - prog_start/1000 > 5.85)):
            cutscenelevel = 3
            prog_start = -1
            section_area = -1

        if (event.type == pygame.MOUSEBUTTONDOWN and cutscenelevel == 1 and (start_ticks - prog_start / 1000 > 1.85)):
            section_area = 0
            cutscenelevel = 0
            prog_start = -1
            delay_mouse = 0


    pressedKey = pygame.key.get_pressed()
    delay_mouse += 1

    if (scenechange == 0):
        for i in range(20):
            pygame.mixer.Channel(i).stop()


    # ----------------- Main gameplay --------------------
    if pauselevel == 0 and section_area >= 0 and cutscenelevel == 0 and tutoriallevel == 0:
        #print(save_count)
        if (section_area != 9 and section_area != 11 and section_area != 13):
            in_cave = False
        else:
            in_cave = True


        if (in_cave == False):
            if (pygame.mixer.Channel(3).get_busy() == False):
                pygame.mixer.Channel(3).play(pygame.mixer.Sound('media/ambient.wav'), 1)
                pygame.mixer.Channel(3).set_volume(0.02)
            pygame.mixer.Channel(11).stop()
        else:
            if (pygame.mixer.Channel(11).get_busy() == False):
                pygame.mixer.Channel(11).play(pygame.mixer.Sound('media/cave1.wav'), 1)
                pygame.mixer.Channel(11).set_volume(0.1)
            pygame.mixer.Channel(3).stop()

        for i in range(20):
            if (pygame.mixer.Channel(i).get_busy() == True and i != 3 and i != 11 and i != 1 and i != 2 and i != 5 and i != 6 and i != 7 and i != 8 and i != 12 and i != 13 and i != 14 and i != 15):
                    pygame.mixer.Channel(i).stop()


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

    # --------------------- Pause screen ----------------------- #
    if pressedKey[pygame.K_TAB] and scenechange == -1:
        pauselevel = 1
    if pauselevel == 1:
        if (pygame.mixer.Channel(4).get_busy() == False):
            pygame.mixer.Channel(4).play(pygame.mixer.Sound('media/pause.wav'), 1)
            pygame.mixer.Channel(4).set_volume(0.6)

        for i in range(20):
            if (pygame.mixer.Channel(i).get_busy() == True and i != 4):
                pygame.mixer.Channel(i).stop()

        screen.fill(BLACK)
        pause_screen()

    if pauselevel == 2:
        screen.fill(BLACK)
        keybinds_screen()
    if pauselevel == 3:
        exit()


    # ----------------------- Intro ------------------- #
    start_ticks = pygame.time.get_ticks()

    if section_area == -1 and cutscenelevel == 1:
        if (prog_start == -1):
            prog_start = pygame.time.get_ticks()
        screen.fill(BLACK)
        cutscene01()

    # --------------------------- Outtro -------------------- #
    if cutscenelevel == 2:
        for i in range(20):
            if (pygame.mixer.Channel(i).get_busy() == True and i != 9):
                pygame.mixer.Channel(i).stop()

        if (pygame.mixer.Channel(9).get_busy() == False):
            pygame.mixer.Channel(9).play(pygame.mixer.Sound('media/outro.wav'), 1)
            #pygame.mixer.Channel(9).set_volume(0.7)

        if (prog_start == -1):
            prog_start = pygame.time.get_ticks()

        screen.fill(WHITE)
        cutscene02()
        if start_ticks / 1000 > 61.10:
            screen.fill(BLACK)


    # ----------------------------- Start menu ----------------- #
    if (cutscenelevel == 3):
        for i in range(20):
            if (pygame.mixer.Channel(i).get_busy() == True and i != 0):
                pygame.mixer.Channel(i).stop()

        if (pygame.mixer.Channel(0).get_busy() == False):
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('media/menu.wav'), 1)

        screen.blit(screenimageload[count], (0, 0))
        count += 1
        if (count > 355):
            count = 0

    # ------------------------------ Credit Scene --------------------------- #
    if (cutscenelevel == 4):
        for i in range(20):
            if (pygame.mixer.Channel(i).get_busy() == True and i != 10):
                pygame.mixer.Channel(i).stop()

        if (pygame.mixer.Channel(10).get_busy() == False):
            pygame.mixer.Channel(10).play(pygame.mixer.Sound('media/credit_scene.wav'), 1)
            pygame.mixer.Channel(9).set_volume(0.6)

        if (prog_start == -1):
            prog_start = pygame.time.get_ticks()

        screen.fill(BLACK)
        cutscene03()

    # ------------ Instruction section ------------ #
    endtime = pygame.time.get_ticks()

    if tutoriallevel == 1:
        for i in range(20):
            pygame.mixer.Channel(i).stop()

        tutorialmove()
        if pressedKey[pygame.K_ESCAPE] and endtime - starttime > 1000:
            starttime = pygame.time.get_ticks()
            tutoriallevel = 0

    if tutoriallevel == 2:
        for i in range(20):
            pygame.mixer.Channel(i).stop()

        tutorialatt()
        if pressedKey[pygame.K_ESCAPE] and endtime - starttime > 1000:
            starttime = pygame.time.get_ticks()
            tutoriallevel = 0

    if tutoriallevel == 3:
        for i in range(20):
            pygame.mixer.Channel(i).stop()

        tutorialspeatt()
        if pressedKey[pygame.K_ESCAPE] and endtime - starttime > 1000:
            starttime = pygame.time.get_ticks()
            tutoriallevel = 0

    # Conversation for section 4
    conversation.conv1(pressedKey, screen)
    conversation.conv2(pressedKey, screen)
    conversation.conv3(pressedKey, screen)
    conversation.conv4(pressedKey, screen)
    conversation.conv5(pressedKey, screen)
    conversation.conv6(pressedKey, screen)
    conversation.conv7(pressedKey, screen)

    scene_change()
    pygame.display.update()
    clock.tick(FPS) # This will pause the game until the FPS time is reached


pygame.quit()