

from rummy import *
from settings import *

def main():
    numStartTiles = 14
    goOutNum = 30
    settings = Settings(numStartTiles, goOutNum)
    Rum = Rummy(settings)
    Rum.play()


if __name__ == '__main__':
    main()




