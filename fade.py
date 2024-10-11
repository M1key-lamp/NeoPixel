import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write= False, brightness=.2)
i = 0

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
magenta = (255,0,255)
white = (255,255,255)

clr_list = [red, green, white]


def fade_out(color,speed):

    red_ratio = color[0]/50
    red_orig = color[0]
    green_ratio = color[1]/50
    green_orig = color[1]
    blue_ratio = color[2]/50
    blue_orig = color[2]
    for i in range(1,51):
        r = int(red_orig - i * red_ratio)
        g = int(green_orig - i * green_ratio)
        b = int(blue_orig - i * blue_ratio)
        np.fill((r,g,b))
        print(np)
        np[0]
        np.show()
        time.sleep(speed)

def fade_in(color,speed):
    red_ratio = color[0]/50
    red_orig = color[0]
    green_ratio = color[1]/50
    green_orig = color[1]
    blue_ratio = color[2]/50
    blue_orig = color[2]
    for i in range(1,51):
        r = int(red_orig + i * red_ratio)
        g = int(green_orig +i * green_ratio)
        b = int(blue_orig + i * blue_ratio)
        np.fill((r,g,b))
        np.show()
        time.sleep(speed)

while True:
    rainbow_led = random.choice(clr_list)
    fade_in(rainbow_led, 0.04)
    fade_out(rainbow_led,.04)
