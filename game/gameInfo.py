import time
import os
import sys
import json
from game.pet import *
from player.bot import *

#os.chdir(os.pardir)
turnDataFile = open('data/pets.json')
turnData = petsObject = json.load(turnDataFile)

turnDataFile.close()



class Game():
    def __init__(self):
        self.gold = 10 # every turn start with 10 gold
        self.health = 10 # start every game with 10 health
        self.wins = 0 # start every game with 0 wins
        self.turn = 1 # start turn 1
        self.field = [Pet()]*5 # start with "None" Pets
        self.fieldScore = 0 # score of current field
        self.petShop = [Pet()]*5 # available shop?
        self.foodShop = [] # available shop?
        self.activeTriggers = [None]*5 # keeps track of whether or not we should check our field pets for effects like onSummon or onBuy
        # map of active effects
        # key should be trigger
        # value should be array of tuples: (level, func)
        self.effects = {}

    #when something dies, do a quick check of it's name in effectobjects for Triggers.faint
    #then also do

    def readShop(self):
        shopPetSlots = turnData[self.turn]["animalShopSlots"]
        shopFoodSlots = turnData[self.turn]["foodShopSlots"]
        for i in range(shopPetSlots):
            self.petShop.append(getPet(shopPetButtons[i]))
        for i in range(shopFoodSlots):
            self.foodShop.append(getPet(shopFoodButtons[i]))
    
    def endTurn(self):
        # End Turn
        click(Buttons.End)
        time.sleep(1)
        # Click until we finish fight
        while (readGold()==''):
            click(Buttons.Arena)
        # Update variables
        self.turn += 1
        