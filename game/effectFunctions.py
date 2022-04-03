"Library of effects that are not quite so simple"

from enum import Enum
from typing import Callable
from game.gameInfo import Game
import random
from game.pet import *
"Library of names+effects at bottom"
class Triggers(Enum):
    Buy = "Buy"
    Sell = "Sell"
    Faint = "Faint"
    Attack = "Attack"
    Damaged = "Damaged"
    Summon = "Summon"
    EndRound = "EndRound"
    StartRound = "StartRound"
    StartBattle = "StartBattle"
    Level = "Level"

class Effect():
    def __init__(self, effect : Callable, trigger : Triggers):
        self.effect = effect
        self.trigger = trigger

def summon(game : Game, pet : Pet, position):
    #If game has any active summon effects, apply them:
    if Triggers.Summon in game.activeTriggers:
        for effectPair in game.effects[Triggers.Summon]:
            effectPair[0](pet, effectPair[1])

    #Summoning should first try to summon into the designated position"
    if game.field[position].isNone():
        game.field[position] = pet
        return
    #If another pet is present, try to push it forward, along with other adjacent pets, into vacant spots to make room"
    i = position
    while i<4:
        i += 1
        # if we find an empty spot
        if game.field[i].isNone():
            # begin moving pets forward 
            while i>position:
                game.field[i] = game.field[i-1]
                i -= 1
            # actually summon pet
            game.field[i] = pet
            return
    # if no empty spots found forward, look backward
    while i>0:
        i -= 1
        if game.field[i].isNone():
            while i<position:
                game.field[i] = game.field[i+1]
                i += 1
            game.field[i] = pet
            return
    #if no space is present, do nothing"
    return

def ant(game : Game, pet : Pet, level):
    "Randomly give unit +2/1"
    activeBoard = [p for p in game.field if not p.isNone()]
    if len(activeBoard)==0:
        return
    chosenOne = random.sample(activeBoard, 1)[0]
    chosenOne.addAttack(2*level)
    chosenOne.addHealth(1*level)

def beaver(game : Game, pet : Pet, level):
    "Give 2 random pets +1 health"
    activeBoard = [p for p in game.field if not p.isNone()]
    if len(activeBoard)==0: return
    if len(activeBoard)==1:# just give him the 1 health
        activeBoard[0].addHealth(1*level)
    chosenOnes = random.sample(activeBoard, 2)
    chosenOnes[0].addHealth(1*level)
    chosenOnes[1].addHealth(1*level)
    
def cricket(game : Game, position, level): 
    pet = Pet(name="zombiecricket", attack=1*level, health=1*level, level=1)
    summon(game, pet, position)

def duck(game : Game, level):
    for p in game.petShop:
        if not p.isNone(): p.addHealth(1*level)

def fish(game : Game, level):
    for p in game.field:
        if not p.isNone():
            p.addAttack(1*(level-1))
            p.addHealth(1*(level-1))

def horse(pet : Pet, level):   
    pet.addAttack(1*level)

def mosquito(enemyGame : Game, level):
    activeBoard = [p for p in enemyGame.field if not p.isNone()]
    chosenOnes = random.sample(activeBoard, level)
    for p in chosenOnes:
        p.addHealth(-1)
    
def otter(game : Game, level):
    pass
def pig(game : Game):
    pass
def crab(game : Game):
    pass
def dodo(game : Game):
    pass
def dog(game : Game):
    pass
def elephant(game : Game):
    pass
def flamingo(game : Game):
    pass
def hedgehog(game : Game):
    pass
def peacock(game : Game):
    pass
def rat(game : Game):
    pass
def shrimp(game : Game):
    pass
def spider(game : Game):
    pass
def swan(game : Game):
    pass
def badger(game : Game):
    pass
def blowfish(game : Game):
    pass
def camel(game : Game):
    pass
def giraffe(game : Game):
    pass
def kangaroo(game : Game):
    pass
def ox(game : Game):
    pass
def rabbit(game : Game):
    pass
def sheep(game : Game):
    pass
def snail(game : Game):
    pass
def turtle(game : Game):
    pass
def whale(game : Game):
    pass
def bison(game : Game):
    pass
def deer(game : Game):
    pass
def dolphin(game : Game):
    pass
def hippo(game : Game):
    pass
def monkey(game : Game):
    pass
def penguin(game : Game):
    pass
def rooster(game : Game):
    pass
def skunk(game : Game):
    pass
def squirrel(game : Game):
    pass
def worm(game : Game):
    pass
def cow(game : Game):
    pass
def crocodile(game : Game):
    pass
def parrot(game : Game):
    pass
def rhino(game : Game):
    pass
def scorpion(game : Game):
    pass
def seal(game : Game):
    pass
def shark(game : Game):
    pass
def turkey(game : Game):
    pass
def cat(game : Game):
    pass
def boar(game : Game):
    pass
def dragon(game : Game):
    pass
def fly(game : Game):
    pass
def gorilla(game : Game):
    pass
def leopard(game : Game):
    pass
def mammoth(game : Game):
    pass
def snake(game : Game):
    pass
def tiger(game : Game):
    pass
def apple(game : Game):
    pass
def honey(game : Game):
    pass
def cupcake(game : Game):
    pass
def meatbone(game : Game):
    pass
def sleepingpill(game : Game):
    pass
def garlic(game : Game):
    pass
def saladbowl(game : Game):
    pass
def cannedfood(game : Game):
    pass
def pear(game : Game):
    pass
def chili(game : Game):
    pass
def chocolate(game : Game):
    pass
def sushi(game : Game):
    pass
def melon(game : Game):
    pass
def mushroom(game : Game):
    pass
def pizza(game : Game):
    pass
def steak(game : Game):
    pass
