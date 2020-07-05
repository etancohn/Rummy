
import pygame
from termcolor import colored, cprint

# drawText : window * string * int * int -> None
# creates text at position (x,y) on the pygame window
def drawText(win, msg, x, y, color = (0,0,0), font = 'arial', size = 30, 
             isBold = False, isItalic = False, centered = True):
    screenW, screenH = pygame.display.get_surface().get_size()
    font = pygame.font.SysFont(font, size, isBold, isItalic)
    text = font.render(msg, 1, color)
    if centered:
        win.blit(text, (x - (text.get_rect().width/2), y - (text.get_rect().height/2)))
    else:
        win.blit(text, x, y)


# gets user input. Outside the class, you need to use the drawUserInput() method 
# to draw the prompt and user input. You need to make the attribute 'onScreen' 
# equal False when 'enter' is pressed, and add keyboard presses to 'userInput'
# if onScreen is True.
class GetUserInput(object):
    def __init__(self, prompt, x, y, onScreen = True):
        self.prompt = prompt            # prompt message
        self.x = x                      # x coordinate of prompt
        self.y = y                      # y coordinate of prompt
        self.userInput = ""             # user input
        self.onScreen = onScreen        # text should be drawn

    def drawUserInput(self, win, color = (0,0,0), font = 'arial', size = 30,
                      isBold = False, isItalic = False, centered = False):
        if self.onScreen:
            drawText(win, self.prompt + self.userInput, self.x, self.y, color = color,
                     font = font, size = size, isBold = isBold, isItalic = isItalic, 
                     centered = centered)




# To print in a color:
    # cprint (<text>, <color>)

# to get a colored string:
    # <name> = colored(<text>, <color>)

# background color optional parameter: <on_color>


# rgbFromColor : string -> int * int * int
# rgbFromColor(s) => returns the rgb tuple value of s
def rgbFromColor(s):
    if s == "white":
        return (255,255,255)
    elif s == "black":
        return (0,0,0)
    elif s == "red":
        return (255,0,0)
    elif s == "orange":
        return (255,128,0)
    elif s == "yellow":
        return (255,255,0)
    elif s == "green":
        return (0,255,0)
    elif s == "cyan":
        return (0,255,255)
    elif s == "blue":
        return (0,0,255)
    elif s == "purple":
        return (127,0,255)
    elif s == "pink":
        return (255,0,255)
    elif s == "gray":
        return (128,128,128)
    else:
        print(f"Not a valid color: {s}")
        return (0,0,0)







