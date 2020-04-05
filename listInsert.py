from pyautogui import *
from time import sleep
from tkinter import Tk

K = Tk()
try:
    t = K.clipboard_get().split('\n')
    print("Получен список\n", t)
    for i in reversed(range(3)):
        sleep(1)
        print(i+1)

    for i in t:
        K.clipboard_clear()
        K.clipboard_append(i)
        click()
        hotkey('ctrl', 'v')
        sleep(0.1)
        press('enter')
        sleep(0.1)
except:
    print("Буфер пуст")
    sleep(3)