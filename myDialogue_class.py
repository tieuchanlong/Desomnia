import pygame

WHITE = (255, 255, 255)

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


class dialogue():
    def __init__(self):
        self.dialogueLEVEL = -1
        self.starttime = 0
        self.endtime = 0
        self.dialogueboxload = (pygame.image.load("media/dialoguebox01.png").convert_alpha())
        self.start = False
        self.dialogue_unlocked = []
        for i in range(200):
            self.dialogue_unlocked.append(False)

    def dialogue0(self, screen):
        rcdialogue1 = text(100, 70, "Talkative Creature: Young lady! Why are you wandering around here?", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - rcdialogue1.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - rcdialogue1.getText().get_height() / 2
        rcdialogue1.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(rcdialogue1.getText(), rcdialogue1.gettextpos())

    def dialogue1(self, screen):
        andialogue1 = text(410, 70, "Anna: You can talk !?", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - andialogue1.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - andialogue1.getText().get_height() / 2
        andialogue1.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(andialogue1.getText(), andialogue1.gettextpos())

    def dialogue2(self, screen):
        rcdialogue2 = text(320, 60, "Talkative Creature: You find that strange?", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - rcdialogue2.getText().get_width() / 2
        y = self.dialogueboxload.get_height() / 2 - rcdialogue2.getText().get_height() / 2
        rcdialogue2.textsetpos(x, y)

        rcdialogue2a = text(420, 85, "Maybe it is...", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - rcdialogue2a.getText().get_width() / 2
        y = 23 + self.dialogueboxload.get_height() / 2 - rcdialogue2a.getText().get_height() / 2
        rcdialogue2a.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(rcdialogue2.getText(), rcdialogue2.gettextpos())
        screen.blit(rcdialogue2a.getText(), rcdialogue2a.gettextpos())

    def dialogue3(self, screen):
        andialogue2 = text(320, 70, "Anna: So why are you different than others?", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - andialogue2.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - andialogue2.getText().get_height() / 2
        andialogue2.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(andialogue2.getText(), andialogue2.gettextpos())

    def dialogue4(self, screen):
        rcdialogue3 = text(360, 60, "Talkative Creature: It is a long story...", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - rcdialogue3.getText().get_width() / 2
        y = self.dialogueboxload.get_height() / 2 - rcdialogue3.getText().get_height() / 2
        rcdialogue3.textsetpos(x, y)

        rcdialogue3a = text(420, 85, "...that I don't even remember", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - rcdialogue3a.getText().get_width() / 2
        y = 23 + self.dialogueboxload.get_height() / 2 - rcdialogue3a.getText().get_height() / 2
        rcdialogue3a.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(rcdialogue3.getText(), rcdialogue3.gettextpos())
        screen.blit(rcdialogue3a.getText(), rcdialogue3a.gettextpos())

    ### after returning ###

    def dialogue5(self, screen):
        rcdialogue4 = text(350, 30, "Talkative Creature: Be safe out there!", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - rcdialogue4.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - rcdialogue4.getText().get_height() / 2
        rcdialogue4.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(rcdialogue4.getText(), rcdialogue4.gettextpos())

    ### Done Section ###

    def dialogue12(self, screen):
        unk1 = text(350, 30, "Creature: (A loud screeching sound)", 30, "Renogare", WHITE)
        self.dialogue_unlocked[12] = True
        x = 50 + self.dialogueboxload.get_width() / 2 - unk1.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - unk1.getText().get_height() / 2
        unk1.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(unk1.getText(), unk1.gettextpos())

    def dialogue13(self, screen):
        andialogue6 = text(400, 30, "Anna: (The poor soul is injured!)", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - andialogue6.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - andialogue6.getText().get_height() / 2
        andialogue6.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(andialogue6.getText(), andialogue6.gettextpos())

    def dialogue14(self, screen):
        andialogue7 = text(400, 30, "Anna: (I need to help him!)", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - andialogue7.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - andialogue7.getText().get_height() / 2
        andialogue7.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(andialogue7.getText(), andialogue7.gettextpos())

    ### After the fight

    def dialogue15(self, screen):
        andialogue8 = text(400, 30, "Anna: Are you fine?", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - andialogue8.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - andialogue8.getText().get_height() / 2
        andialogue8.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(andialogue8.getText(), andialogue8.gettextpos())

    def dialogue16(self, screen):
        unk2 = text(350, 30, "Creature: (A painful hum)", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - unk2.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - unk2.getText().get_height() / 2
        unk2.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(unk2.getText(), unk2.gettextpos())

    def dialogue17(self, screen):
        andialogue9 = text(400, 30, "Anna: What should I do...", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - andialogue9.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - andialogue9.getText().get_height() / 2
        andialogue9.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(andialogue9.getText(), andialogue9.gettextpos())

    def dialogue18(self, screen):
        nodi2 = text(350, 30, "(The creature picked up a flower)", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - nodi2.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - nodi2.getText().get_height() / 2
        nodi2.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(nodi2.getText(), nodi2.gettextpos())

    def dialogue19(self, screen):
        andialogue10 = text(400, 30, "Anna: So you need this flower to heal?", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - andialogue10.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - andialogue10.getText().get_height() / 2
        andialogue10.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(andialogue10.getText(), andialogue10.gettextpos())

    def dialogue20(self, screen):
        andialogue11 = text(400, 30, "Anna: Hold on, I will be back with those flowers", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - andialogue11.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - andialogue11.getText().get_height() / 2
        andialogue11.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(andialogue11.getText(), andialogue11.gettextpos())

    def dialogue21(self, screen):
        unk3 = text(350, 30, "(A cheerful hum)", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - unk3.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - unk3.getText().get_height() / 2
        unk3.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(unk3.getText(), unk3.gettextpos())

    def dialogue22(self, screen):
        nodi3 = text(350, 30, "(The creature open the waterway for Anna)", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - nodi3.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - nodi3.getText().get_height() / 2
        nodi3.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(nodi3.getText(), nodi3.gettextpos())

    def dialogue23(self, screen):
        nodi3 = text(350, 30, "Creature: Umu...", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - nodi3.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - nodi3.getText().get_height() / 2
        nodi3.textsetpos(x, y)
        self.start = False

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(nodi3.getText(), nodi3.gettextpos())

    def dialogue24(self, screen):
        nodi3 = text(350, 30, "Creature: Umu! Umu!", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - nodi3.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - nodi3.getText().get_height() / 2
        nodi3.textsetpos(x, y)
        self.start = False

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(nodi3.getText(), nodi3.gettextpos())

    def playerflowernoti(self, screen):
        noti1 = text(350, 30, "(2 flowers left to collect)", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - noti1.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - noti1.getText().get_height() / 2
        noti1.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(noti1.getText(), noti1.gettextpos())

    def playerflowernoti1(self, screen):
        noti2 = text(350, 30, "(1 flower left to collect)", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - noti2.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - noti2.getText().get_height() / 2
        noti2.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(noti2.getText(), noti2.gettextpos())

    def playerflowernoti2(self, screen):
        noti3 = text(350, 30, "I finished collecting all the flowers", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - noti3.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - noti3.getText().get_height() / 2
        noti3.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(noti3.getText(), noti3.gettextpos())

    def playerflowernoti3(self, screen):
        noti4 = text(350, 30, "I finished collecting all the flowers", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - noti4.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - noti4.getText().get_height() / 2
        noti4.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(noti4.getText(), noti4.gettextpos())

    def playerflowernoti4(self, screen):
        noti5 = text(350, 30, "Now I should get back to help him", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - noti5.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - noti5.getText().get_height() / 2
        noti5.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(noti5.getText(), noti5.gettextpos())

    def npctalk(self, screen):
        npc = text(350, 30, "Wreeegghhh...", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - npc.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - npc.getText().get_height() / 2
        npc.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(npc.getText(), npc.gettextpos())

    def dialogue25(self, screen):
        boss = text(350, 30, "Wraaagghhh!!!", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - boss.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - boss.getText().get_height() / 2
        boss.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(boss.getText(), boss.gettextpos())

    def dialogue26(self, screen):
        boss = text(350, 30, "Woah!! What is that?", 30, "Renogare", WHITE)
        x = 50 + self.dialogueboxload.get_width() / 2 - boss.getText().get_width() / 2
        y = 10 + self.dialogueboxload.get_height() / 2 - boss.getText().get_height() / 2
        boss.textsetpos(x, y)

        screen.blit(self.dialogueboxload, (50, 10))
        screen.blit(boss.getText(), boss.gettextpos())

    def conv1(self, pressedKeys, screen):
        self.endtime = pygame.time.get_ticks()
        mousepressed = pygame.mouse.get_pressed()
        if self.dialogueLEVEL == 0:
            self.dialogue0(screen)
            self.dialogue_unlocked[0] = True
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 1
        if self.dialogueLEVEL == 1:
            self.dialogue1(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 2
        if self.dialogueLEVEL == 2:
            self.dialogue2(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
                self.starttime = pygame.time.get_ticks()
                self. dialogueLEVEL = 3
        if self.dialogueLEVEL == 3:
            self.dialogue3(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 4
        if self.dialogueLEVEL == 4:
            self.dialogue4(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = -1
               self.start = False

    def conv2(self, pressedKeys, screen):
        self.endtime = pygame.time.get_ticks()
        mousepressed = pygame.mouse.get_pressed()
        if self.dialogueLEVEL == 12:
            self.dialogue12(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 13
        if self.dialogueLEVEL == 13:
            self.dialogue13(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 14
        if self.dialogueLEVEL == 14:
            self.dialogue14(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 15
        if self.dialogueLEVEL == 15:
            self.dialogue15(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 16
        if self.dialogueLEVEL == 16:
            self.dialogue16(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 17
        if self.dialogueLEVEL == 17:
            self.dialogue17(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 18
        if self.dialogueLEVEL == 18:
            self.dialogue18(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 19
        if self.dialogueLEVEL == 19:
            self.dialogue19(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 20
        if self.dialogueLEVEL == 20:
            self.dialogue20(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
                self.starttime = pygame.time.get_ticks()
                self.dialogueLEVEL = -1
                self.start = False

    def conv3(self, pressedKeys, screen):
        self.endtime = pygame.time.get_ticks()
        mousepressed = pygame.mouse.get_pressed()
        if self.dialogueLEVEL == 23:
            self.dialogue23(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
                self.starttime = pygame.time.get_ticks()
                self.dialogueLEVEL = -1
                self.start = False

    def conv4(self, pressedKeys, screen):
        if self.dialogueLEVEL == 121:  # 121 is a new level because the text is new
            self.playerflowernoti2(screen)
            self.dialogue_unlocked[121] = True
            if pressedKeys[pygame.K_1] and self.endtime - self.starttime > 1000:
                self.starttime = pygame.time.get_ticks()
                self.dialogueLEVEL = 122
        if self.dialogueLEVEL == 122:
            self.playerflowernoti3(screen)
            if pressedKeys[pygame.K_1] and self.endtime - self.starttime > 1000:
                self.starttime = pygame.time.get_ticks()
                self.dialogueLEVEL = 21
        if self.dialogueLEVEL == 21:
            self.dialogue21(screen)
            if pressedKeys[pygame.K_1] and self.endtime - self.starttime > 1000:
                self.starttime = pygame.time.get_ticks()
                self.dialogueLEVEL = 22
        if self.dialogueLEVEL == 22:
            self.dialogue22(screen)
            if pressedKeys[pygame.K_1] and self.endtime - self.starttime > 1000:
                self.starttime = pygame.time.get_ticks()
                self.dialogueLEVEL = -1
                self.start = False

    def conv5(self, pressedKeys, screen):
        self.endtime = pygame.time.get_ticks()
        mousepressed = pygame.mouse.get_pressed()
        if self.dialogueLEVEL == 24:
            self.dialogue24(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
                self.starttime = pygame.time.get_ticks()
                self.dialogueLEVEL = -1
                self.start = False

    def conv6(self, pressedKeys, screen):
        self.endtime = pygame.time.get_ticks()
        mousepressed = pygame.mouse.get_pressed()
        if self.dialogueLEVEL == 6:
            self.dialogue5(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
                self.starttime = pygame.time.get_ticks()
                self.dialogueLEVEL = -1
                self.start = False

    def conv7(self, pressedKeys, screen):
        mousepressed = pygame.mouse.get_pressed()
        if self.dialogueLEVEL == 25:  # 121 is a new level because the text is new
            self.dialogue25(screen)
            self.dialogue_unlocked[25] = True
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
                self.starttime = pygame.time.get_ticks()
                self.dialogueLEVEL = 26
        if self.dialogueLEVEL == 26:
            self.dialogue26(screen)
            if (mousepressed[0] == 1 or mousepressed[1] == 1 or mousepressed[2] == 1) and self.endtime - self.starttime > 1000:
                self.starttime = pygame.time.get_ticks()
                self.dialogueLEVEL = -1

