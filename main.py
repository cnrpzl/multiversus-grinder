import random
from xml.etree.ElementTree import TreeBuilder
import pyautogui
import time
import win32gui
import threading
import keyboard
loc = pyautogui.locateOnScreen
# event = threading.Event()

# def stop():
#     event.set()
#     print("stop")

# keyboard.add_hotkey("f9", stop)
time.sleep(7)

hwnd = win32gui.GetForegroundWindow()
win32gui.MoveWindow(hwnd, 0, 0, 640, 360, True)

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
                    "arya":[3, 1],
                    "finn":[4, 1],
                    "jake":[5, 1],
                    "garnet":[6, 1],
                    "taz":[7, 1],
                    "batman":[8, 1],
                    "shaggy":[9, 1],
                    "morty":[0, 0]}


def enter_mv():
    enter_button = loc("./enter-mv.png")
    if enter_button != None:
        pyautogui.press("space")
        print("enter MV triggered")
        time.sleep(7)


def main_menu():
    menu_button = loc("./main-menu-button.png")
    if menu_button != None:
        print("main menu triggered")
        for x in range(0, 10):
            pyautogui.press("down")
            time.sleep(0.1)
        for x in range(0, 10):
            pyautogui.press("left")
            time.sleep(0.1)
        
        pyautogui.press("right")
        time.sleep(0.2)
        pyautogui.press("v")
        time.sleep(0.2)
        pyautogui.press("up")
        time.sleep(0.2)
        pyautogui.press("up")
        time.sleep(0.2)
        pyautogui.press("up")
        time.sleep(0.2)
        pyautogui.press("left")
        time.sleep(0.2)
        pyautogui.press("space")
        time.sleep(0.2)
        pyautogui.press("v")
        time.sleep(5)

def select_character(location):
    menu_cog = loc("./select-cog.png")
    if menu_cog != None:
        print("select_char triggered")
        for x in range(0, 10):
            pyautogui.press("down")
            time.sleep(0.1)

        for x in range(0, 10):
            pyautogui.press("right")
            time.sleep(0.1)
        
        for x in range(0, location[0]):
            pyautogui.press("left")
            time.sleep(0.1)
        
        for x in range(0, location[1]):
            pyautogui.press("up")
            time.sleep(0.1)
            
        pyautogui.press("space")
        time.sleep(0.1)
        pyautogui.press("v")
        select_perks()

def select_perks():
    perks = loc("./perks.png", confidence=0.8)
    while perks == None:
        time.sleep(0.5)
        perks = loc("./perks.png", confidence=0.8)
    if perks != None:
        pyautogui.moveTo(perks[0], perks[1])
        time.sleep(1)
        pyautogui.click()
        print("select perks triggered")
        for x in range(0, 5):
            pyautogui.press("down")
            time.sleep(0.3)
            pyautogui.press("v")
        time.sleep(8)

def post_game():
    perks = loc("./next-post.png", confidence=0.8)
    while perks == None:
        time.sleep(0.5)
        perks = loc("./perks.png", confidence=0.8)
    if perks != None:
        for x in range(0, 4):
            pyautogui.press("down")
            time.sleep(0.1)
        pyautogui.press("v")
        time.sleep(0.3)
        pyautogui.press("v")

def rematch():
    rematch = loc("./rematch.png", confidence=0.8)
    victory = loc("./victory.png", confidence=0.8)
    if rematch != None or victory != None:
        print("rematch_triggered")
        time.sleep(0.3)
        pyautogui.press("v")


def battle():
    print("battle")
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

    


    


while True:
    enter_mv()
    main_menu()
    select_character(character_location["morty"])
    battle()
    rematch()