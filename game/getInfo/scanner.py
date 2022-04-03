from xmlrpc.client import Boolean
from PIL import ImageGrab
import pytesseract
import cv2
import numpy as np
import time
import json

import os
import sys
sys.path.insert(0, os.pardir)
from player.clicker import *
from game.getInfo.spelling import correction

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Save pet and food data to compare ocr with
# os.chdir(os.pardir)
entityNames = []
pets = open('data/pets.json')
petsObject = json.load(pets)
foods = open('data/foods.json')
foodsObject = json.load(foods)

for name in petsObject["Pets"]:
    entityNames.append(''.join(filter(str.isalnum, name)).lower())
for name in foodsObject["Foods"]:
    entityNames.append(''.join(filter(str.isalnum, name)).lower())
entityNames.append("")

pets.close()
foods.close()

def readFieldName(button : Buttons):
    # hover mouse
    hover(button)
    coord = button.value
    x = coord[0]
    y = coord[1]

    # OCR Name
    name = OCR_Text(x-75,y-210,x+75,y-185)
    # Correct name if misread
    name = correction(name, entityNames)

    print("name: " + name)
    return name
# Since the shop has the little dice symbol the names are slightly higher than normal
def readShopName(button : Buttons):
    # hover mouse
    hover(button)
    coord = button.value
    x = coord[0]
    y = coord[1]

    # OCR Name
    name = OCR_Text(x-75,y-220,x+75,y-195)
    # Correct name if misread
    name = correction(name, entityNames)

    print("name: " + name)
    return name

def readAttack(petButton : Buttons):
    # Get button coords
    coord = petButton.value
    x = coord[0]
    y = coord[1]

     # Get image of screen
    screen = ImageGrab.grab(bbox =(x-40,y+18,x,y+57))

    # Convert to black and white
    bw_screen = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
    bw_screen = cv2.resize(bw_screen, (200,100))
    # cv2.imshow("image", bw_screen)
    # cv2.waitKey(0)
    # Use thresh binary to make numbers more distinguished
    ret,bw_screen = cv2.threshold(bw_screen,200,255,cv2.THRESH_BINARY)
    # floodfill number boundary
    processed_screen = bw_screen.astype("uint8")
    cv2.floodFill(processed_screen, None, (200-1, 50-1), 0)
    
    # dilate white pixels incase they are thin
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    processed_screen = cv2.dilate(processed_screen, kernel, iterations=1)
    # cv2.imshow("dilate", processed_screen)
    # cv2.waitKey(0)
    # flip so number is black and background is white
    processed_screen = cv2.bitwise_not(processed_screen)
    # cv2.imshow("image", processed_screen)
    # cv2.waitKey(0)
    cropped_num = processed_screen[10:90, 20:180]    
    # cv2.imshow("cropped", cropped_num)
    # cv2.waitKey(0)
    #______________________________
#     # read the image and get the dimensions
    # h, w, = cropped_num.shape

    # # run tesseract, returning the bounding boxes
    # boxes = pytesseract.image_to_boxes(
    #     cropped_num,
    #     config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789') # also include any config options you use

    # # draw the bounding boxes on the image
    # img = ""
    # for b in boxes.splitlines():
    #     b = b.split(' ')
    #     img = cv2.rectangle(cropped_num, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

    # # show annotated image and wait for keypress
    # cv2.imshow("filename", img)
    # cv2.waitKey(0)
# #____________________________________
    # run ocr with special config for number
    number = pytesseract.image_to_string(
        cropped_num,
        lang='eng',
        config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
    )
    return number
def readHealth(petButton : Buttons):
    # Get button coords
    coord = petButton.value
    x = coord[0]
    y = coord[1]

     # Get image of screen
    screen = ImageGrab.grab(bbox =(x,y+18,x+40,y+57))

    # Convert to black and white
    bw_screen = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
    bw_screen = cv2.resize(bw_screen, (200,100))
    # cv2.imshow("image", bw_screen)
    # cv2.waitKey(0)
    # Use thresh binary to make numbers more distinguished
    ret,bw_screen = cv2.threshold(bw_screen,200,255,cv2.THRESH_BINARY)
    # floodfill number boundary
    processed_screen = bw_screen.astype("uint8")
    cv2.floodFill(processed_screen, None, (0, 50-1), 0)
    # dilate white pixels incase they are thin
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    processed_screen = cv2.dilate(processed_screen, kernel, iterations=1)
    # cv2.imshow("dilate", processed_screen)
    # cv2.waitKey(0)
    # flip so number is black and background is white
    processed_screen = cv2.bitwise_not(processed_screen)
    # cv2.imshow("image", processed_screen)
    # cv2.waitKey(0)
    cropped_num = processed_screen[10:90, 20:180]    
    # cv2.imshow("cropped", cropped_num)
    # cv2.waitKey(0)
#______________________________
#     # read the image and get the dimensions
    # h, w, = cropped_num.shape

    # # run tesseract, returning the bounding boxes
    # boxes = pytesseract.image_to_boxes(
    #     cropped_num,
    #     config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789') # also include any config options you use

    # # draw the bounding boxes on the image
    # img = ""
    # for b in boxes.splitlines():
    #     b = b.split(' ')
    #     img = cv2.rectangle(cropped_num, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

    # # show annotated image and wait for keypress
    # cv2.imshow("filename", img)
    # cv2.waitKey(0)
# #____________________________________
    # run ocr with special config for number
    number = pytesseract.image_to_string(
        cropped_num,
        lang='eng',
        config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
    )
    return number
def readStats(petButton : Buttons):
    attack = readAttack(petButton)
    health = readHealth(petButton)

    print("attack: " + attack)
    print("health: " + health)
    return (attack, health)

def readFood(petButton : Buttons):
    "read food that a pet has equipped"
    hover(petButton)
    coord = petButton.value
    x = coord[0]
    y = coord[1]

    name = OCR_Text(x+135,y-195,x+195,y-175)
    name = correction(name, entityNames)

def readGold():
    gold = OCR_Number(55,45,95,80)
    #print("gold: " + gold)
    return gold

def readPlayerHealth():
    playerHealth = OCR_Number(150,45,185,80)
    print("player health: " + playerHealth)
    pass

def readWins():
    wins = OCR_Number(240,45,265,80)
    print("wins: " + wins)
    pass

def OCR_Text(x1,y1,x2,y2):
    # screen grab text box
    screen = ImageGrab.grab(bbox =(x1,y1,x2,y2))
    cv2.imshow("image", np.array(screen))
    cv2.waitKey(0)
    # Convert to black and white
    bw_screen = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
    bw_screen = cv2.resize(bw_screen, (300,100))
    
    cv2.imshow("image", bw_screen)
    cv2.waitKey(0)

    # Use thresh binary to make numbers more distinguished
    ret,bw_screen = cv2.threshold(bw_screen,127,255,cv2.THRESH_BINARY)
    
    # ocr for name
    name = pytesseract.image_to_string(
        bw_screen, 
        lang ='eng'
    )
    name = ''.join(filter(str.isalnum, name))
    name = name.lower()
    return name

def OCR_Number(x1,y1,x2,y2):
    # Get image of screen
    screen = ImageGrab.grab(bbox =(x1,y1,x2,y2))

    # Convert to black and white
    bw_screen = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
    bw_screen = cv2.resize(bw_screen, (200,100))

    cv2.imshow("image", bw_screen)
    cv2.waitKey(0)

    # Use thresh binary to make numbers more distinguished
    ret,bw_screen = cv2.threshold(bw_screen,200,255,cv2.THRESH_BINARY)

    cv2.imshow("image", bw_screen)
    cv2.waitKey(0)
    # Floodfill parts that are not numbers
    processed_screen = bw_screen.astype("uint8")
    # first floodfill to get general shapes
    cv2.floodFill(processed_screen, None, (0, 0), 255)
    cv2.imshow("image", processed_screen)
    cv2.waitKey(0)
    # flip pixel values so that only numbers are black
    processed_screen = cv2.bitwise_not(processed_screen)
    cv2.imshow("image", processed_screen)
    cv2.waitKey(0)
    # second floodfill to blend background and border
    cv2.floodFill(processed_screen, None, (0, 0), 255)
    cv2.imshow("image", processed_screen)
    cv2.waitKey(0)

    # Config necessary to read digits instead of characters
    number = pytesseract.image_to_string(
        processed_screen,
        lang='eng',
        config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
    )

    # if the number is 2 digits it breaks the boundary and must go through a different process
    if number=="":
        processed_screen = bw_screen.astype("uint8")
        cv2.imshow("image", processed_screen)
        cv2.waitKey(0)
        cv2.floodFill(processed_screen, None, (200-1, 50-1), 0)
        cv2.imshow("image", processed_screen)
        cv2.waitKey(0)
        processed_screen = cv2.bitwise_not(processed_screen)
        cv2.imshow("image", processed_screen)
        cv2.waitKey(0)
        

    return number

def readLeftEdgeName():
    "Specifically for reading left most pet's name in battle"
    button = Buttons.Battle1
    # hover mouse
    hover(button)
    coord = button.value
    x = coord[0]
    y = coord[1]

    # OCR Name
    name = OCR_Text(x,y-207,x+150,y-182)
    # Correct name if misread
    name = correction(name, entityNames)
    
    print("name: " + name)
    return name
    
def readRightEdgeName():
    "Specifically for reading right most pet's name in battle"
    button = Buttons.Battle10
    # hover mouse
    hover(button)
    coord = button.value
    x = coord[0]
    y = coord[1]

    # OCR Name
    name = OCR_Text(x-150,y-207,x,y-182)
    # Correct name if misread
    name = correction(name, entityNames)

    print("name: " + name)
    return name

