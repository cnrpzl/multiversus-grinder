import pyautogui
import time
import win32gui
import logging
from datetime import datetime
import keyboard


##GLOBALS
# Initalizing total gold as -7 because updating gold happens at perk selection screen, aka before a game finishes 
total_gold = -7
challenges_complete = 0
now = datetime.now().strftime("%m_%d_%Y_%H-%M-%S") # current date and time
logging.basicConfig(filename=f'mv-grinder-{now}.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level="DEBUG")
loc = pyautogui.locateOnScreen
stop = False
#END GLOBALS

#function that stops script on key press
def stop_script(event):
    global stop
    stop = True
    print(stop)
    logging.debug(f"Stop script triggered. Stop: {stop}")

keyboard.hook_key("f2", stop_script)

#character dictionary, key is the character name, value is a list (x, y) where x = left/rigpht (negative is right) and y = up
character_location = {"wonderwoman":[8, 0], 
                    "lebron":[0, 1], 
                    "bugs":[2,0], 
                    "harley":[1, 1], 
                    "superman":[7, 0], 
                    "irongiant":[6, 0], 
                    "steven":[5, 0], 
                    "reindog":[4, 0], 
                    "velma":[3, 0], 
                    "tomjerry":[1, 0],
                    "arya":[2, 1],
                    "finn":[3, 1],
                    "jake":[4, 1],
                    "garnet":[5, 1],
                    "taz":[6, 1],
                    "batman":[7, 1],
                    "shaggy":[8, 1],
                    "morty":[0, 0],
                    "random":[-1, 1]}


#This function almost never runs and probably isn't necessary but it's here. 
# It's meant to scan for the "Enter multiversus button" after disconnects.
def enter_mv():
    enter_button = loc("./enter-mv.png")
    if enter_button != None:
        pyautogui.press("space")
        logging.debug("enter MV triggered")
        time.sleep(7)

#looks for orange check in character selection screen, if it detects it, then click on it. 
# Trying to be careful with this, don't want to reroll all challenges over and over
def accept_challenge_rewards():
    global challenges_complete
    challenge_check = loc("./challenge-check.png", confidence=0.8)
    while challenge_check != None:
        pyautogui.moveTo(challenge_check)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        logging.debug("Challenge completed, accepting rewards...")
        time.sleep(1)
        challenges_complete += 1
        logging.info(f"Challenge completition detected: {challenges_complete}")
        challenge_check = loc("./challenge-check.png")

#Navigates to bot game 2v2's from the main menu
def main_menu():
    menu_button = loc("./main-menu-button.png")
    if menu_button != None:
        logging.debug("main menu triggered")
        pyautogui.press("v")
        time.sleep(0.5)
        pyautogui.press("up")
        time.sleep(0.2)
        pyautogui.press("up")
        time.sleep(0.2)
        pyautogui.press("up")
        time.sleep(0.2)
        pyautogui.press("left")
        time.sleep(0.5)
        pyautogui.press("space")
        time.sleep(0.5)
        pyautogui.press("v")
        time.sleep(5)

#Character selection function, takes x, y coords (0, 0 is morty, although they're backwards anyway, 
# i should switch right to be positive and left to be negative) as an argument. 
def select_character(location):
    menu_cog = loc("./select-cog.png")
    if menu_cog != None:
        logging.debug("select_char triggered")
        for x in range(0, 3):
            accept_challenge_rewards()
            time.sleep(0.2)
        for x in range(0, 10):
            pyautogui.press("down")
            time.sleep(0.1)

        for x in range(0, 10):
            pyautogui.press("right")
            time.sleep(0.1)
        
        for x in range(0, location[1]):
            pyautogui.press("up")
            time.sleep(0.2)
        
        if location[0] < 0:
            for x in range(0, location[0] * -1):
                pyautogui.press("right")
                time.sleep(0.2)
        else:
            for x in range(0, location[0]):
                pyautogui.press("left")
                time.sleep(0.2)
            
        pyautogui.press("space")
        time.sleep(0.5)
        pyautogui.press("v")
        select_perks()

#Code waits until it detects perks after character selection. Perks will be auto-equipped and confirmed
def select_perks():
    global total_gold
    perks = loc("./perks.png", confidence=0.8)
    while perks == None:
        time.sleep(0.5)
        perks = loc("./perks.png", confidence=0.8)
    if perks != None:
        pyautogui.moveTo(perks[0], perks[1])
        time.sleep(1)
        pyautogui.click()
        logging.debug("select perks triggered")
        for x in range(0, 5):
            pyautogui.press("down")
            time.sleep(0.3)
            pyautogui.press("v")
        total_gold += 7
        print(f"Total gold earned: {total_gold}")
        logging.info(f"Total gold earned: {total_gold}")
        time.sleep(8)

#Self explainatiory, looks for rematch / victory images, if it detects them, press V to rematch. 
def rematch():
    rematch = loc("./rematch.png", confidence=0.8)
    victory = loc("./victory.png", confidence=0.8)
    if rematch != None or victory != None:
        logging.debug("rematch_triggered")
        time.sleep(0.3)
        pyautogui.press("v")

#Super simple 'battle' function, just spams j and k and d for basic, special, and dodges. 
# I'm sure someone could make a better function but it serves it's purpose and gets most challenges done. 
def battle():
    logging.debug("battle")
    x = 0
    while x <= 2:
        pyautogui.press("j")
        time.sleep(0.2)
        pyautogui.press("k")
        time.sleep(0.2)
        pyautogui.press("d")
        time.sleep(0.2)
        pyautogui.press("d")
        time.sleep(0.2)
        pyautogui.press("j")
        time.sleep(0.2)
        pyautogui.press("j")
        time.sleep(0.2)
        pyautogui.press("d")
        time.sleep(0.2)
        pyautogui.press("d")
        time.sleep(0.2)
        pyautogui.press("d")
        x+= 1

#Main Loop, character selection is input based, and it's important to select the MultiVersus window to get hwnd, it allows resizing of the window. If somebody knows how to do this without having to alt tab into multi versus manually, let me know. 
try:
    character_selection = input("Select character by name: ")
    print("Switch to MultiVersus window and press f1.")
    print("F2 will stop script execution.")
    keyboard.wait('f1')
    hwnd = win32gui.GetForegroundWindow()
    win32gui.MoveWindow(hwnd, 0, 0, 640, 360, True)
    time.sleep(1)
    while True and stop != True:
        enter_mv()
        main_menu()
        select_character(character_location[character_selection.lower()])
        battle()
        rematch()
except Exception as e:
    print(e)
    logging.exception(e)
    time.sleep(35)
    exit(1)