import sys
import os

while True:
    try:
        from pyautogui import *
        import pyautogui
        import time
        import keyboard
        import random
        import win32api, win32con

        time.sleep(2)

        def click(x,y):
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

        #Color of center: (255, 219, 195)

        while keyboard.is_pressed('q') == False:

            sdx = 0

            posDL = pyautogui.locateOnScreen('dlbutton.png', confidence =.9)

            if posDL != None:
                time.sleep(1)
                posDL = pyautogui.locateOnScreen('dlbutton.png', confidence =.9)
                click(posDL.left + 10, posDL.top + 10)

                time.sleep(2)
        #Un-comment this section if you want this script to automatically download from the Nexusmods page
                # while sdx == 0:
                #     posSD = pyautogui.locateOnScreen('sdbutton.png', confidence =.9)
                #     if posSD != None:
                #         sdx = 1
                #         click(posSD.left, posSD.top)

                time.sleep(6)        

            time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}. Restarting script...")
        time.sleep(5)
        #Change the file paths to you file paths
        os.chdir('C:/Path/to/Directory/that/contains/the/py/script')
        os.system('python VortexBot.py')
