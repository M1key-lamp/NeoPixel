import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write= False, brightness=0.3)
i = 0

red = (255,30,0)

orange = (250, 60, 0)



def fire(fire1,fire2,speed,tim1):
    np.fill(fire1)
    np.show()
    for i in range(tim1):
        np[random.randint(0,np.n-2)] = fire2
        np.show()
        time.sleep(speed)
def flame(ma):
    for i in range(ma):
        fire(red,orange,0.1,0.1)
while True:
    flame(1) 
    fire((255, 50, 0),(255, 20, 0),0.01,4)
