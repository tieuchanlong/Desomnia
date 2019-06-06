
from myDialogue import *

class dialogue():
    def __init__(self):
        self.dialogueLEVEL = 0
        self.starttime = 0
        self.endtime = 0

    def dialogue0(self):
        rcdialogue1 = text(100, 70, "Lady! Help is needed over here!", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - rcdialogue1.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - rcdialogue1.getText().get_height() / 2
        rcdialogue1.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(rcdialogue1.getText(), rcdialogue1.gettextpos())

    def dialogue1(self):
        andialogue1 = text(410, 70, "You can talk !?", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - andialogue1.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - andialogue1.getText().get_height() / 2
        andialogue1.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(andialogue1.getText(), andialogue1.gettextpos())

    def dialogue2(self):
        rcdialogue2 = text(320, 60, "Creatures that can talk are not hostile", 30, "Renogare", WHITE)
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

    def dialogue3(self):
        andialogue2 = text(320, 70, "So why are you different than others?", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - andialogue2.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - andialogue2.getText().get_height() / 2
        andialogue2.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(andialogue2.getText(), andialogue2.gettextpos())

    def dialogue4(self):
        rcdialogue3 = text(360, 60, "It was a long story.", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - rcdialogue3.getText().get_width() / 2
        y = dialogueboxload.get_height() / 2 - rcdialogue3.getText().get_height() / 2
        rcdialogue3.textsetpos(x, y)

        rcdialogue3a = text(420, 85, "that I don't even remember", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - rcdialogue3a.getText().get_width() / 2
        y = 23 + dialogueboxload.get_height() / 2 - rcdialogue3a.getText().get_height() / 2
        rcdialogue3a.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(rcdialogue3.getText(), rcdialogue3.gettextpos())
        screen.blit(rcdialogue3a.getText(), rcdialogue3a.gettextpos())

    ### after returning ###

    def dialogue5(self):
        rcdialogue4 = text(350, 30, "Oh, you're still here?", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - rcdialogue4.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - rcdialogue4.getText().get_height() / 2
        rcdialogue4.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(rcdialogue4.getText(), rcdialogue4.gettextpos())

    ### Done Section ###

    def dialogue12(self):
        unk1 = text(350, 30, "(A loud screeching sound)", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - unk1.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - unk1.getText().get_height() / 2
        unk1.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(unk1.getText(), unk1.gettextpos())

    def dialogue13(self):
        andialogue6 = text(400, 30, "The poor soul is injured!", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - andialogue6.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - andialogue6.getText().get_height() / 2
        andialogue6.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(andialogue6.getText(), andialogue6.gettextpos())

    def dialogue14(self):
        andialogue7 = text(400, 30, "I need to help him!", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - andialogue7.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - andialogue7.getText().get_height() / 2
        andialogue7.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(andialogue7.getText(), andialogue7.gettextpos())

    ### After the fight

    def dialogue15(self):
        andialogue8 = text(400, 30, "Are you fine?", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - andialogue8.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - andialogue8.getText().get_height() / 2
        andialogue8.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(andialogue8.getText(), andialogue8.gettextpos())

    def dialogue16(self):
        unk2 = text(350, 30, "(A painful hum)", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - unk2.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - unk2.getText().get_height() / 2
        unk2.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(unk2.getText(), unk2.gettextpos())

    def dialogue17(self):
        andialogue9 = text(400, 30, "What should I do...", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - andialogue9.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - andialogue9.getText().get_height() / 2
        andialogue9.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(andialogue9.getText(), andialogue9.gettextpos())

    def dialogue18(self):
        nodi2 = text(350, 30, "(The creature picked up a flower)", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - nodi2.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - nodi2.getText().get_height() / 2
        nodi2.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(nodi2.getText(), nodi2.gettextpos())

    def dialogue19(self):
        andialogue10 = text(400, 30, "That's right! The flower of Luffia", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - andialogue10.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - andialogue10.getText().get_height() / 2
        andialogue10.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(andialogue10.getText(), andialogue10.gettextpos())

    def dialogue20(self):
        andialogue11 = text(400, 30, "Hold on, I will be back with those flowers", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - andialogue11.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - andialogue11.getText().get_height() / 2
        andialogue11.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(andialogue11.getText(), andialogue11.gettextpos())

    def dialogue21(self):
        unk3 = text(350, 30, "(A cheerful hum)", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - unk3.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - unk3.getText().get_height() / 2
        unk3.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(unk3.getText(), unk3.gettextpos())

    def dialogue22(self):
        nodi3 = text(350, 30, "(The creature handed you a piece of drawing)", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - nodi3.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - nodi3.getText().get_height() / 2
        nodi3.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(nodi3.getText(), nodi3.gettextpos())

    def playerflowernoti(self):
        noti1 = text(350, 30, "(2 flowers left to collect)", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - noti1.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - noti1.getText().get_height() / 2
        noti1.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(noti1.getText(), noti1.gettextpos())

    def playerflowernoti1(self):
        noti2 = text(350, 30, "(1 flower left to collect)", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - noti2.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - noti2.getText().get_height() / 2
        noti2.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(noti2.getText(), noti2.gettextpos())

    def playerflowernoti2(self):
        noti3 = text(350, 30, "I finished collecting all the flowers", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - noti3.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - noti3.getText().get_height() / 2
        noti3.textsetpos(x, y)

    def playerflowernoti3(self):
        noti4 = text(350, 30, "I finished collecting all the flowers", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - noti4.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - noti4.getText().get_height() / 2
        noti4.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(noti4.getText(), noti4.gettextpos())

    def playerflowernoti4(self):
        noti5 = text(350, 30, "Now I should get back to help him", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - noti5.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - noti5.getText().get_height() / 2
        noti5.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(noti5.getText(), noti5.gettextpos())

    def playerflowernoti5(self):
        noti5 = text(350, 30, "Now I should get back to help him", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - noti5.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - noti5.getText().get_height() / 2
        noti5.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(noti5.getText(), noti5.gettextpos())

    def npctalk(self):
        npc = text(350, 30, "Wreeegghhh...", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - npc.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - npc.getText().get_height() / 2
        npc.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(npc.getText(), npc.gettextpos())

    def bosstalk(self):
        boss = text(350, 30, "Wraaagghhh!!!", 30, "Renogare", WHITE)
        x = 50 + dialogueboxload.get_width() / 2 - boss.getText().get_width() / 2
        y = 10 + dialogueboxload.get_height() / 2 - boss.getText().get_height() / 2
        boss.textsetpos(x, y)

        screen.blit(dialogueboxload, (50, 10))
        screen.blit(boss.getText(), boss.gettextpos())

    def conv1(self):
        if self.dialogueLEVEL == 0:
            dialogue0()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 1
        if self.dialogueLEVEL == 1:
            dialogue1()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 2
        if self.dialogueLEVEL == 2:
            dialogue2()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               starttime = pygame.time.get_ticks()
              self. dialogueLEVEL = 3
        if self.dialogueLEVEL == 3:
            dialogue3()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 4
        if self.dialogueLEVEL == 4:
            dialogue4()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 5
        if self.dialogueLEVEL == 5:
            dialogue5()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()

    def conv2(self):
        if self.dialogueLEVEL == 12:
            dialogue12()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 13
        if self.dialogueLEVEL == 13:
            dialogue13()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 14
        if self.dialogueLEVEL == 14:
            dialogue14()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 15
        if self.dialogueLEVEL == 15:
            dialogue15()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 16
        if self.dialogueLEVEL == 16:
            dialogue16()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 17
        if self.dialogueLEVEL == 17:
            dialogue17()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 18
        if self.dialogueLEVEL == 18:
            dialogue18()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 19
        if self.dialogueLEVEL == 19:
            dialogue19()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 20
        if self.dialogueLEVEL == 20:
            dialogue20()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
    '''
    def flowernoti(self):
        if self.flower == 2:
            playerflowernoti()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
                self.starttime = pygame.time.get_ticks()
                self.dialogueLEVEL = 600
        if self.flower == 1 and self.dialogueLEVEL == 600:
            playerflowernoti1()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
                self.starttime = pygame.time.get_ticks()
    '''

    def conv3(self):
        if self.dialogueLEVEL == 121: # 121 is a new level because the text is new
            playerflowernoti2()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 122
        if self.dialogueLEVEL == 122:
            playerflowernoti3()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 21
        if self.dialogueLEVEL == 21:
            dialogue21()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 22
        if self.dialogueLEVEL == 22:
            dialogue22()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 23

    def npcint(self):
        if self.dialogueLEVEL == 24:
            npctalk()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 25

    def bossint(self):
        if self.dialogueLEVEL == 24:
            bosstalk()
            if pressedKeys[pygame.K_1] and endtime - self.starttime > 1000:
               self.starttime = pygame.time.get_ticks()
               self.dialogueLEVEL = 25

