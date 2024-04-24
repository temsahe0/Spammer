import pyautogui # open cmd pip install pyautogui
import time

time.sleep(5)

for i in range(100):
    pyautogui.typewrite("Your spam message here")
    pyautogui.press("enter") 
    