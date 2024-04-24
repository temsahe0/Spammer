import pyautogui # open cmd pip install pyautogui
import time

time.sleep(5)

while True:
    pyautogui.typewrite("Your spam message here")
    pyautogui.press("enter")