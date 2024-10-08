import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write= False, brightness=0.3)
i = 0

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
magenta = (255,0,255)


clr_list = (red, green, blue, yellow, cyan, magenta)
while True:
    for i in range(np.n):
        np[i] = random.choice(clr_list)
    np.show()
    time.sleep(.1)
