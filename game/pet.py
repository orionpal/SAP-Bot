import os
import sys
sys.path.insert(0, os.pardir)
from player.clicker import *
from game.getInfo.scanner import *

class Pet():
    def __init__(self,
            name=None,
            attack=None,
            health=None,
            food=None,
            level=None):
        self.name = name
        self.attack = attack
        self.health = health
        self.food = food
        self.level = level
    def __repr__(self):
        if self.isNone():
            return "Empty\n"
        return f'name: {self.name}\nattack: {self.attack}\nhealth: {self.health}\nfood: {self.food}\nlevel: {self.level}\n'

    def isNone(self):
        return self.name==None
    
    def addAttack(self, attack):
        self.attack += attack
        return True
    def addHealth(self, health):
        "Can use negative numbers to subtract health from damage, returns False if they die"
        self.health += health
        # If you die, you become a "None" pet
        if self.health <= 0:
            self = Pet()
            return False
        return True


def getPet(button : Buttons):
    name = readName(button)
    stats = readStats(button, False)
    return Pet(name, stats[0], stats[1])