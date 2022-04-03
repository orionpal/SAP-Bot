from tkinter import Button
from game.getInfo.scanner import *
from player.clicker import *
from player.bot import *

tier1 = ["ant", "beaver", "cricket", "Duck", "Fish", "Horse", "Mosquito", "Otter", "Pig"]

shopButtons = [
    Buttons.Shop1,
    Buttons.Shop2,
    Buttons.Shop3,
    Buttons.Shop4,
    Buttons.Shop5,
]

def turn1():
    priority = {
        "fish" : 1,
        "otter" : 1,
        "cricket" : 2,
        "mosquito" : 3,
        "ant" : 4,
        "beaver" : 5,
        "pig" : 6,
        "horse" : 7,
        "duck" : 8
    }
    shop = []
    shop.append(readName(Buttons.Shop1))
    shop.append(readName(Buttons.Shop2))
    shop.append(readName(Buttons.Shop3))

    otter = False
    for pet in shop:
        index = shop.indexOf(pet)
        if pet=="fish":
            buyShop(shopButtons[index])

