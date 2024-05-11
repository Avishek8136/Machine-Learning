import random

# @python.coder_

import pyautogui as pg

import time

animal=('monkey','donkey')

time.sleep(8)

for i in range(200):
    a=random.choice(animal)
    pg.write("You are a "+a)
    pg.press("Enter")
