from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from datetime import datetime

Pruebas = False


def clicky(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed("q") == False:

    if pyautogui.locateOnScreen("Caracol.jpg", grayscale=True, confidence=0.5) != None:
        

        Stinky = locateOnScreen("Caracol.jpg", grayscale=True, confidence=0.5)

        print(Stinky)

        if not Stinky == None:

            clicky(Stinky[0] + 30, Stinky[1] + 30)

            time.sleep(0.5)

            moveTo(500, 500)

            print("OK")

            time.sleep(0.5)


    else:
        if Pruebas:

            print("no veo")

    time.sleep(3)