First thing I wanted to do was make the game interactable with in python, so I found the pyautogui through googling "gui automation" which is a term I heard in a tutorial video on creating bots for video games.

After finding out how to get windows that were opened and moving the mouse, I set up the standard for where I want to move the window to in order to keep locations consistent, and then printed out my mouse location while hovering over all the interactable things in the window. Once I got those coordinates I copied them into a map object to use for later.

Next I needed to get the data that is used in the game: pets, their abilities, their probabilities, food. All of this is available here: https://superauto.pet/api.json
and hosted by this project:
https://github.com/bencoveney/super-auto-pets-db
I needed to parse through this in order to only get relevant information.

api.json is copy and pasted from the github project. When trying to read I was getting unicode errors so I did ctrl+f for find and replacement of the unicodes, I also used vscode's regular expression option.



*I will only be doing this for the standard pack, no expansion, so I will only retrieve information from that.
There are two types of things: pets and food
for pets we want their names, stats, effect depending on tier, and probability depending on turn

for round 1 strats: https://www.reddit.com/r/superautopets/comments/qv1gzg/i_simulated_11902500_possible_round_1_matchups_in/?ref=share&ref_source=link

After getting all the data for game objects (pets and food) I needed to start reading the game screen to know what's available, so I decided to get the coordinates for the help box that comes up when you hover over a pet and then use pytesseracts ocr to read the names.

The ocr can read many names but sometimes misreads so I need to add something that can tell the best match for the string.

reading the numbers for gold+health doesn't work because their color is white with a black outline

Looking into solutions for reading numbers/bubble font using tesseract ocr

solution includes running a binary-thresh to distinguish the characters more, and for numbers there need to be specific configs set for the OCR
For trouble shooting to make sure I was creating good images I used this code snippet whenever I wanted to observe: 
# For trouble shooting
# cv2.imshow("image", bw_screen)
# cv2.waitKey(0)

In case of misreading I looked up solutions for a "string nearest match" problem and came upon this blog post:
http://norvig.com/spell-correct.html
and then modified it to work with my input

As I continue to test the reading functionality with different boards, I run into a very weird issue where "9" is sometimes read as "29". I thought it may be because of thin lines so I added dilation to thicken the lines before reading which seemed to fix the issue

I want to use a neural network (NN) for a bot to learn how to play, mainly by evaluating what a "Strong board" is.

In order to get good data for the NN I decided to read actual board states from the game, and so I added that functionality

I also need the ability to simulate fights, but this essentially means recreating the game in code. I decided to just do that but because it's a bunch of work I began getting sloppy on commenting and good design