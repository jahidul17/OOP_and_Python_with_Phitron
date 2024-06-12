import pyautogui
from time import sleep

n=int(input())
for i in range(0,n):
    for j in range(i+1):
        pyautogui.write("#",interval=0.5)
    pyautogui.press('Enter')
    sleep(3)