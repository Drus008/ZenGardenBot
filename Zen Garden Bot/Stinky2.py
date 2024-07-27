from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from datetime import datetime


#250 795
# 1665 915

Pruebas = False


def clicky(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

tiempos = []

tiemposErroneos = []

tiempo_inicial = datetime.now()

while keyboard.is_pressed("q") == False:



    if pyautogui.locateOnScreen("Caracol.jpg", grayscale=True, confidence=0.5, region=(10,795,1900,120)) != None:
        


        Stinky = locateOnScreen("Caracol.jpg", grayscale=True, confidence=0.5, region=(10,795,1900,120))

        print(Stinky)

        if not Stinky == None:

            clicky(Stinky[0] + 30, Stinky[1] + 30)

            tiempo_final = datetime.now()

            time.sleep(0.5)

            moveTo(500, 500)

            print("Encontrado")

            diferencia_tiempo = (tiempo_final - tiempo_inicial).total_seconds()

            print(diferencia_tiempo)

            if diferencia_tiempo > 120 or diferencia_tiempo < 350:

                tiempos.append(diferencia_tiempo)

                tiempo_inicial = datetime.now()

            else:

                tiemposErroneos.append(diferencia_tiempo)


        else:
            print("No encontrado")


    else:
        if Pruebas:

            print("no veo")

    time.sleep(5)

n = 0

t = 0

for x in tiempos:

    n = n + 1

    t = t + x

media = t / n

print(tiempos)

print(n)

print(media)

print(tiemposErroneos)