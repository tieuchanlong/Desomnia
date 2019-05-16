class section:
    def __init__(self):
        self.moving_enemies = []
        self.stable_enemies = []
        self.stable_grounds = []
        self.moving_grounds = []
        self.waters = []
        self.stairs = []
        self.items = []
        self.npc = []
        self.moving_npc = []
        self.hor_ground = 0

    def move_x(self, distance):
        for i in range(len(self.moving_enemies)):
            self.moving_enemies[i].move_range = (self.moving_enemies[i].move_range[0] + distance, self.moving_enemies[i].move_range[1] + distance)
            self.moving_enemies[i].setPos(self.moving_enemies[i].x + distance, self.moving_enemies[i].y)

        for i in range(len(self.stable_grounds)):
            self.stable_grounds[i].setPos(self.stable_grounds[i].x + distance, self.stable_grounds[i].y)

        for i in range(len(self.stairs)):
            self.stairs[i].setPos(self.stairs[i].x + distance, self.stairs[i].y)

        for i in range(len(self.items)):
            self.items[i].setPos(self.items[i].x + distance, self.items[i].y)

        for i in range(len(self.npc)):
            self.npc[i].setPos(self.npc[i].x + distance, self.npc[i].y)

        for i in range(len(self.moving_npc)):
            self.moving_npc[i].setPos(self.moving_npc[i].x + distance, self.moving_npc[i].y)
            self.moving_npc[i].set_rangex(self.moving_npc[i].move_range[0] + distance, self.moving_npc[i].move_range[1] + distance)

        for i in range(len(self.waters)):
            self.waters[i].setPos(self.waters[i].x + distance, self.waters[i].y)

        for i in range(len(self.moving_grounds)):
            self.moving_grounds[i].setPos(self.moving_grounds[i].x + distance, self.moving_grounds[i].y)
            self.moving_grounds[i].set_rangex(self.moving_grounds[i].move_rangex[0] + distance, self.moving_grounds[i].move_rangex[1] + distance)

    def move_y(self, distance):
        for i in range(len(self.moving_enemies)):
            self.moving_enemies[i].setPos(self.moving_enemies[i].x, self.moving_enemies[i].y + distance)

        for i in range(len(self.stable_grounds)):
            self.stable_grounds[i].setPos(self.stable_grounds[i].x, self.stable_grounds[i].y + distance)

        for i in range(len(self.stairs)):
            self.stairs[i].setPos(self.stairs[i].x, self.stairs[i].y + distance)

        for i in range(len(self.items)):
            self.items[i].setPos(self.items[i].x, self.items[i].y + distance)

        for i in range(len(self.npc)):
            self.npc[i].setPos(self.npc[i].x, self.npc[i].y + distance)

        for i in range(len(self.moving_npc)):
            self.moving_npc[i].setPos(self.moving_npc[i].x, self.moving_npc[i].y + distance)

        for i in range(len(self.waters)):
            self.waters[i].setPos(self.waters[i].x, self.waters[i].y + distance)

        for i in range(len(self.moving_grounds)):
            self.moving_grounds[i].setPos(self.moving_grounds[i].x, self.moving_grounds[i].y + distance)
            self.moving_grounds[i].set_rangey(self.moving_grounds[i].move_rangey[0] + distance, self.moving_grounds[i].move_rangey[1] + distance)