
from termcolor import colored, cprint


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


