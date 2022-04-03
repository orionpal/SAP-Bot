from player.clicker import *

# TODO: integrate Game object into functions
def pickName():
    " Pick first 2 options for team name"
    click(Buttons.Name1)
    click(Buttons.Name2)

def buyShop(shopButton : Buttons, fieldButton : Buttons):
    " Buy from shopButton and place on fieldButton"
    click(shopButton)
    click(fieldButton)

def sellPet(fieldButton : Buttons):
    " Sell Pet from fieldButton position"
    click(fieldButton)
    click(Buttons.Freeze) # freeze button is same location as sell button

def freezeShop(shopButton : Buttons):
    " Freeze item on shopButton"
    click(shopButton)
    click(Buttons.Freeze)

def fieldPlace(fieldButton1 : Buttons, fieldButton2 : Buttons):
    " Move Pet from fieldButton1 to fieldButton2 "
    # if pet is of same name then you need to hover first
    click(fieldButton1)
    click(fieldButton2)

def reroll():
    click(Buttons.Roll)