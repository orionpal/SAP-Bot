import pyautogui as pag
from enum import Enum
import time

class Buttons(Enum):
    "Button coordinates from the formatted game screen"
    Arena = [500,300]
    Roll = [115,635]
    Freeze= [530,635]
    End = [830,635]
    Confirm = [830, 635]
    Field1 = [254,300]
    Field2 = [336,300]
    Field3 = [418,300]
    Field4 = [500,300]
    Field5 = [584,300]
    Shop1 = [255,465]
    Shop2 = [337,465]
    Shop3 = [418,465]
    Shop4 = [500,465]
    Shop5 = [581,465]
    Food1 = [660,465]
    Food2 = [746,465]
    Name1 = [150, 270]
    Name2 = [150, 450]
    Battle1 = [65, 445]
    Battle2 = [160, 445]
    Battle3 = [250, 445]
    Battle4 = [347, 445]
    Battle5 = [433, 445]
    Battle6 = [565, 446]
    Battle7 = [655, 446]
    Battle8 = [745, 446]
    Battle9 = [835, 446]
    Battle10 = [930, 446]

fieldButtons = [
    Buttons.Field1,
    Buttons.Field2,
    Buttons.Field3,
    Buttons.Field4,
    Buttons.Field5,
]

shopPetButtons = [
    Buttons.Shop1,
    Buttons.Shop2,
    Buttons.Shop3,
    Buttons.Shop4,
    Buttons.Shop5,
]
shopFoodButtons = [
    Buttons.Food1,
    Buttons.Food2
]
battleFieldButtons = [
    Buttons.Battle1,
    Buttons.Battle2,
    Buttons.Battle3,
    Buttons.Battle4,
    Buttons.Battle5,
    Buttons.Battle6,
    Buttons.Battle7,
    Buttons.Battle8,
    Buttons.Battle9,
    Buttons.Battle10
]

def click(button : Buttons):
    "Given a button, move cursor to those coordinates and click"
    coord = button.value
    x = coord[0]
    y = coord[1]
    pag.moveTo(x,y,0)
    pag.click()

def hover(button : Buttons):
    "Given a button, move cursor to those coordinates"
    coord = button.value
    x = coord[0]
    y = coord[1]
    pag.moveTo(x,y,0)

