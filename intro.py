
import pygame

class Intro(object):
    def __init__(self, game):
        self.game = game            # Rummikub
        self.getNumOfPlayers = True
        # self.numOfPlayers = getUserInput("How many players? ", onScreen = True)
        self.getNamesOfPlayers = False


    def keyPressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.introTestNumLoop == 0:
                self.introTestNum += 1
                self.introTestNumLoop += 1

    def events(self):
        for event in self.game.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(f"mx, my: {mx, my}")
                self.isIntro = False


    def doIntro(self):
        self.keyPressed()
        if self.game.introTestNumLoop > 0:
            self.game.introTestNumLoop += 1
            if self.game.introTestNumLoop >= 5:
                self.game.introTestNumLoop = 0
        self.events()


    # draws on the canvas during the intro
    def drawIntro(self):
        self.game.win.fill(rgbFromColor("yellow"))
        drawText(self.game.win, f"introTestNum: {self.game.introTestNum}", self.game.screenW/2, self.game.screenH/2)
        drawText(self.game.win, "stonks", self.game.screenW/2, self.game.screenH/30, size = 45, isBold = True)
        # name = getUserInput("How many players? ", )

