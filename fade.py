import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write= False, brightness=1)
i = 0

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
magenta = (255,0,255)
white = (255,255,255)
pink = (140, 47, 94)

def fade_out(colours):
    for i in range(255):
        color = (0,255,0)
        red_ratio = red[0]/50
        red_orig = red[0] 
        for i in range(1,51):
            red - red_orig + i * red_orig


