from myObject import *

class section:
    def __init__(self):
        self.moving_enemies = []
        self.stable_enemies = []
        self.stable_grounds = []
        self.moving_grounds = []
        self.waters = []
        self.items = []
        self.npc = []
        self.moving_npc = []
        self.traps = []
        self.moving_traps = []
        self.hor_ground = 0
        self.bullets = []
        self.throw_stuffs = []
        self.gates = []
        self.control_panels = []
        self.saving_point = save_point(100, 20, 0, 0)
        self.instruction_points = []

    def move_x(self, distance):
        self.saving_point.setPos(self.saving_point.x + distance, self.saving_point.y)

        for i in range(len(self.stable_enemies)):
            self.stable_enemies[i].setPos(self.stable_enemies[i].x + distance, self.stable_enemies[i].y)

        for i in range(len(self.moving_enemies)):
            self.moving_enemies[i].move_range = (self.moving_enemies[i].move_range[0] + distance, self.moving_enemies[i].move_range[1] + distance)
            self.moving_enemies[i].setPos(self.moving_enemies[i].x + distance, self.moving_enemies[i].y)

        for i in range(len(self.stable_grounds)):
            self.stable_grounds[i].setPos(self.stable_grounds[i].x + distance, self.stable_grounds[i].y)
            for j in range(len(self.stable_grounds[i].images)):
                self.stable_grounds[i].images[j].setPos(self.stable_grounds[i].images[j].x + distance, self.stable_grounds[i].images[j].y)


        for i in range(len(self.items)):
            self.items[i].setPos(self.items[i].x + distance, self.items[i].y)

        for i in range(len(self.instruction_points)):
            self.instruction_points[i].setPos(self.instruction_points[i].x + distance, self.instruction_points[i].y)

        for i in range(len(self.gates)):
            self.gates[i].setPos(self.gates[i].x + distance, self.gates[i].y)

        for i in range(len(self.control_panels)):
            self.control_panels[i].setPos(self.control_panels[i].x + distance, self.control_panels[i].y)

        for i in range(len(self.bullets)):
            self.bullets[i].setPos(self.bullets[i].x + distance, self.bullets[i].y)

        for i in range(len(self.throw_stuffs)):
            self.throw_stuffs[i].setPos(self.throw_stuffs[i].x + distance, self.throw_stuffs[i].y)

        for i in range(len(self.npc)):
            self.npc[i].setPos(self.npc[i].x + distance, self.npc[i].y)

        for i in range(len(self.moving_npc)):
            self.moving_npc[i].setPos(self.moving_npc[i].x + distance, self.moving_npc[i].y)
            self.moving_npc[i].set_rangex(self.moving_npc[i].move_range[0] + distance, self.moving_npc[i].move_range[1] + distance)

        for i in range(len(self.waters)):
            self.waters[i].setPos(self.waters[i].x + distance, self.waters[i].y)

        for i in range(len(self.traps)):
            self.traps[i].setPos(self.traps[i].x + distance, self.traps[i].y)

        for i in range(len(self.moving_traps)):
            self.moving_traps[i].setPos(self.moving_traps[i].x + distance, self.moving_traps[i].y)

        for i in range(len(self.moving_grounds)):
            self.moving_grounds[i].setPos(self.moving_grounds[i].x + distance, self.moving_grounds[i].y)
            self.moving_grounds[i].set_rangex(self.moving_grounds[i].move_rangex[0] + distance, self.moving_grounds[i].move_rangex[1] + distance)

    def move_y(self, distance):
        self.saving_point.setPos(self.saving_point.x, self.saving_point.y + distance)

        for i in range(len(self.stable_enemies)):
            self.stable_enemies[i].setPos(self.stable_enemies[i].x, self.stable_enemies[i].y + distance)

        for i in range(len(self.moving_enemies)):
            self.moving_enemies[i].setPos(self.moving_enemies[i].x, self.moving_enemies[i].y + distance)

        for i in range(len(self.stable_grounds)):
            self.stable_grounds[i].setPos(self.stable_grounds[i].x, self.stable_grounds[i].y + distance)
            for j in range(len(self.stable_grounds[i].images)):
                self.stable_grounds[i].images[j].setPos(self.stable_grounds[i].images[j].x, self.stable_grounds[i].images[j].y + distance)

        for i in range(len(self.items)):
            self.items[i].setPos(self.items[i].x, self.items[i].y + distance)

        for i in range(len(self.instruction_points)):
            self.instruction_points[i].setPos(self.instruction_points[i].x, self.instruction_points[i].y + distance)

        for i in range(len(self.gates)):
            self.gates[i].setPos(self.gates[i].x, self.gates[i].y + distance)

        for i in range(len(self.control_panels)):
            self.control_panels[i].setPos(self.control_panels[i].x, self.control_panels[i].y + distance)

        for i in range(len(self.bullets)):
            self.bullets[i].setPos(self.bullets[i].x, self.bullets[i].y + distance)

        for i in range(len(self.throw_stuffs)):
            self.throw_stuffs[i].setPos(self.throw_stuffs[i].x, self.throw_stuffs[i].y + distance)

        for i in range(len(self.npc)):
            self.npc[i].setPos(self.npc[i].x, self.npc[i].y + distance)

        for i in range(len(self.moving_npc)):
            self.moving_npc[i].setPos(self.moving_npc[i].x, self.moving_npc[i].y + distance)

        for i in range(len(self.waters)):
            self.waters[i].setPos(self.waters[i].x, self.waters[i].y + distance)

        for i in range(len(self.traps)):
            self.traps[i].setPos(self.traps[i].x, self.traps[i].y + distance)

        for i in range(len(self.moving_traps)):
            self.moving_traps[i].set_rangey(self.moving_traps[i].move_range[0] + distance, self.moving_traps[i].move_range[1] + distance)
            self.moving_traps[i].setPos(self.moving_traps[i].x, self.moving_traps[i].y + distance)

        for i in range(len(self.moving_grounds)):
            self.moving_grounds[i].setPos(self.moving_grounds[i].x, self.moving_grounds[i].y + distance)
            self.moving_grounds[i].set_rangey(self.moving_grounds[i].move_rangey[0] + distance, self.moving_grounds[i].move_rangey[1] + distance)