import pyautogui
from time import sleep

#You have 10 seconds!
def typewhile(message):
    sleep(10)
    while True:
        pyautogui.typewrite(message)
        pyautogui.press("enter")


msgs = input('Enter the text: ')
typewhile(msgs)
