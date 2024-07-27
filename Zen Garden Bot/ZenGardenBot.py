from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

Pruebas = False

regadera = None

def clicky(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("q") == False:

    if regadera == None:
        
        if pyautogui.locateOnScreen("RegaderaNormal.png", confidence=0.9, region=(292,0,130,130)) != None:
            regadera = 0

            if Pruebas:
                print("Regadera Normal")

        if  pyautogui.locateOnScreen("RegaderaDorada.png", confidence=0.9, region=(292,0,130,130)) != None:
            regadera = 1

            if Pruebas:
                print("Regadera Dorada")



    if pyautogui.locateOnScreen("Abono.png", confidence=0.9) != None:
        
        if Pruebas:
            print("lo veo")
        
        Abono = locateOnScreen("Abono.png", confidence=0.9)

        if not Abono == None:

            click(475, 60)

            time.sleep(0.1)

            moveTo(Abono[0] - 50, Abono[1] + 94)

            time.sleep(0.1)

            click()

            time.sleep(0.1)




    if pyautogui.locateOnScreen("Agua.png", confidence=0.8) != None:
            
        if Pruebas:
            print("lo veo")
            
        Agua = locateOnScreen("Agua.png", confidence=0.8)

        if not Agua == None:

            click(358, 60)

            time.sleep(0.1)

            if regadera == 0:

                moveTo(Agua[0] - 50, Agua[1] + 94)


            elif regadera == 1:

                moveTo(Agua[0] - 120, Agua[1] + 170)
    
            time.sleep(0.1)

            click()

            time.sleep(0.1)


    if pyautogui.locateOnScreen("Fertilizante.png", confidence=0.9) != None:
        
        if Pruebas:
            print("lo veo")
        
        Fertilizante = locateOnScreen("Fertilizante.png", confidence=0.9)

        if not Fertilizante == None:

            click(610, 60)

            time.sleep(0.1)

            moveTo(Fertilizante[0] - 50, Fertilizante[1] + 94)

            time.sleep(0.1)

            click()

            time.sleep(0.1)



    if pyautogui.locateOnScreen("Musica.png", confidence=0.9) != None:
        
        if Pruebas:
            print("lo veo")
        
        Musica = locateOnScreen("Musica.png", confidence=0.9)

        if not Musica == None:

            click(735, 65)

            time.sleep(0.1)

            moveTo(Musica[0] - 50, Musica[1] + 94)

            time.sleep(0.1)

            click()

            time.sleep(0.1)