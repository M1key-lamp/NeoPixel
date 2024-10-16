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
white = (255,255,55)


clr_list = (red, green)
def sparkling_glitter(sparkle,sparkle2,speed,tim1):
    np.fill(sparkle)
    np.show()
    for i in range(tim1):
        np[random.randint(0,np.n-2)] = sparkle2
        np.show()
        time.sleep(speed)
while True:
    sparkling_glitter((32,2,30),(240,110,240),0,4)
