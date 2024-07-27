from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


# X:  885 Y:  500 RGB: (  0,   0,   0)
# X:  778 Y:  500 RGB: (  0,   0,   0)
# X:  675 Y:  500 RGB: (  0,   0,   0)
# X:  575 Y:  500 RGB: (  0,   0,   0)

def clicky(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("q") == False:

    if pyautogui.pixel(875, 500)[0] == 0:
        clicky(885, 500)

    if pyautogui.pixel(775, 500)[0] == 0:
        clicky(775, 500)

    if pyautogui.pixel(675, 500)[0] == 0:
        clicky(675, 500)

    if pyautogui.pixel(575, 500)[0] == 0:
        clicky(575, 500)