import board
from neopixel import NeoPixel
import time
import random


np = NeoPixel(board.D2,30,auto_write=False,brightness=.3)

orange = (250, 60, 0)
brown = (130, 40, 10)
purple = (140, 0, 197)
white = (255,255,255)
black = (0,0,0)
pink = (255,100,50)
blue = (0,0,200)



def chase1(colors):
    for i in range(np.n):
        np[i] = colors[i%len(colors)]
        np.show()
        time.sleep(0.04)

def reverse_wipe(colors):
    for i in range(np.n):
        i = i * -1
        np[i] = colors[i%len(colors)]
        np.show()
        time.sleep(0.04)
             

while True:
    chase1(blue)
    reverse_wipe(white)

