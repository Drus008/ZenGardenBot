from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

Pruebas = False

#1226   134
#1176   228

while keyboard.is_pressed("q") == False:

    if pyautogui.locateOnScreen("Fertilizante.png", confidence=0.9) != None:
        
        if Pruebas:
            print("lo veo")
        
        Fertilizante = locateOnScreen("Fertilizante.png", confidence=0.9)

        click(610, 60)

        time.sleep(1)

        moveTo(Fertilizante[0] - 50, Fertilizante[1] + 94)

        time.sleep(0.5)

        click()



    else:

        if Pruebas:

            print("no veo")

    time.sleep(2)