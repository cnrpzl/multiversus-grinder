from xml.etree.ElementTree import TreeBuilder
import pyautogui
import time
import random
import win32api
import win32gui
loc = pyautogui.locateOnScreen

time.sleep(3)

hwnd = win32gui.GetForegroundWindow()
win32gui.MoveWindow(hwnd, 0, 0, 640, 360, True)

character_location = {"wonderwoman":[8, 0], "lebron":[0, 1], "bugs":[2,0]}
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
    while x <= 5:
        pyautogui.press("j")
        time.sleep(0.3)
        pyautogui.press('k')
        x += 1
    


    


while True:
    select_character(character_location["bugs"])
    battle()
    rematch()