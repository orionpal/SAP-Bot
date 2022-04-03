# import os
# print("par dir: " + os.pardir)
# print("cur dir: " + os.curdir)
# os.chdir(os.pardir)
# print("new cur dir: " + os.curdir)

from game.gameInfo import Game
from game.effectObjects import *

game = Game()

game.field[0] = Pet(name="duck", attack=1, health=1, level=1)
antPet = Pet("ant")
print(game.field)
if effectObjects[antPet.name].trigger==Triggers.Faint:
    effectObjects[antPet.name].effect(game,1, 1)
print(game.field)