
import pygame
from pygameHelpers import *
from intro import *

class Rummy(object):
    def __init__(self, settings):
        self.settings = settings        # instance of Settings()
        self.numOfPlayers = None
        self.players = []
        self.run = True                 # run the mainloop
        self.screenW = 800              # pygame window width
        self.screenH = 800              # pygame window height
        self.clock = None               # pygame clock (gets set in self.play())
        self.fps = 30                   # frames per second
        self.win = None                 # pygame window (gets set in self.play())
        self.isIntro = True
        self.state = None
        self.introTestNum, self.introTestNumLoop = 0, 0       # for testing in the intro
        self.events = None              # pygame events

    def doIntro(self):
        keys = pygame.key.get_pressed()
        if self.introTestNumLoop > 0:
            self.introTestNumLoop += 1
            if self.introTestNumLoop >= 5:
                self.introTestNumLoop = 0
        if keys[pygame.K_SPACE]:
            if self.introTestNumLoop == 0:
                self.introTestNum += 1
                self.introTestNumLoop += 1
        for event in self.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(f"mx, my: {mx, my}")
                self.isIntro = False

    # draws on the canvas during the intro
    def drawIntro(self):
        self.win.fill(rgbFromColor("yellow"))
        drawText(self.win, f"introTestNum: {self.introTestNum}", self.screenW/2, self.screenH/2)
        drawText(self.win, "stonks", self.screenW/2, self.screenH/30, size = 45, isBold = True)
        # name = getUserInput("How many players? ", )

    # draws on the canvas during the game
    def drawGameMode(self):
        self.win.fill(rgbFromColor("green"))
        makeText(self.win, "NOT stonks", self.screenW/2, self.screenH/30, size = 45, isBold = True)

    # updates the canvas (every function/method that updates the canvas is contained here)
    def redrawGameWindow(self):
        if self.isIntro:
            self.drawIntro()
        else:
            self.drawGameMode()
        pygame.display.update()

    def doGameMode(self):
        pass


    # contains the main pygame loop
    def mainLoop(self):
        while self.run:
            self.clock.tick(self.fps)
            self.events = pygame.event.get()
            # for event in pygame.event.get():
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.run = False
            if self.isIntro:
                self.intro = Intro(self)
                self.doIntro()
            else:
                self.doGameMode()
            self.redrawGameWindow()

    
    # initializes pygame, initiates the mainloop, and closes pygame after the game is over
    def play(self):
        pygame.init()
        self.win = pygame.display.set_mode((self.screenW, self.screenH))
        pygame.display.set_caption("Rummikub")
        self.clock = pygame.time.Clock()
        self.mainLoop()
        pygame.quit()




