from asyncore import read
from pickle import FALSE
import pyautogui as pag
import time

from sympy import E
from player.clicker import *
from player.bot import *
from game.getInfo.scanner import *
from game.gameInfo import *
from strats.stats import *
from brain.simulate import *


# Before starting make sure game is open and focused so it can be clicked on
def formatGameWindow():
    "Get \"Super Auto Pets\" window, focus it, resize it to 1000x700, and move it to top left corner"
    window = pag.getWindowsWithTitle("Super Auto Pets")[0]
    window.activate()
    window.resizeTo(1000,700)
    window.moveTo(0,0)

canplay = False
global game
try:
    formatGameWindow()
    # Initialize a new game, this object will hold general information
    # for button in fieldButtons:
    #     readFieldName(button)
    #     readStats(button)
    # for button in shopPetButtons:
    #     readShopName(button)
    #     readStats(button)
    # for button in shopFoodButtons:
    #     readShopName(button)
    # readLeftEdgeName()
    # readStats(battleFieldButtons[0], True)
    # for buttonIndex ixn range(1, len(battleFieldButtons)-1):
    #     readName(battleFieldButtons[buttonIndex])
    #     readStats(battleFieldButtons[buttonIndex], True)
    # readRightEdgeName()
    # readStats(battleFieldButtons[9], True)

    readFood(Buttons.Field5)
    game = Game()
    strategy = StatStrategy(game)
    simulate(game)
    #canplay = True
    
except E:
    print("could not find game window")
    print(E)

while canplay:
    strategy.makeTurn()
    canplay = False

def saveBoardData():

    pass