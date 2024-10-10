import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write= False, brightness=.2)
i = 0

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

def fade_out(color):

    red_ratio = color[0]/50
    red_orig = color[0]
    green_ratio = color[1]/50
    green_orig = color[1]
    blue_ratio = color[2]/50
    blue_orig = color[1]
    for i in range(1,51):
        red = int(red_orig - i * red_ratio)
        g = int(green_orig - i * green_ratio)
        b = int(blue_orig - i * blue_ratio)
        np.fill((red,g,b))
        np.show()
        time.sleep(.05)

def fade_in(color):

    red_ratio = color[0]/50
    red_orig = color[0]
    green_ratio = color[1]/50
    green_orig = color[1]
    blue_ratio = color[2]/50
    blue_orig = color[1]
    for i in range(1,51):
        red = int(red_orig + i * red_ratio)
        g = int(green_orig +i * green_ratio)
        b = int(blue_orig + i * blue_ratio)
        np.fill((red,g,b))
        np.show()
        time.sleep(.05)
while True:
    fade_in((255,0,0))
    fade_in((0,200,0))
