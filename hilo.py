#! python3
#mouseNow.py - Displays the mouse cursor's current position.
import time
import pyautogui
print('Press Ctrl-C to quit.')
try:
       while True:
         for i in  range(10): 
           pyautogui.click (1404, 314)
           time.sleep(5)
           pyautogui.click (1355, 371)
           time.sleep(5)
         pyautogui.click (1376, 419)
         time.sleep(5)
except KeyboardInterrupt:
       print('\nDone.')
