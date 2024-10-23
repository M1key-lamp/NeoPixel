import board
from neopixel import NeoPixel
import time
import random


np = NeoPixel(board.D2,30,auto_write=False,brightness=.6)

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



def chase1(color):
    count = 0
    for i in range(np.n):
        np.fill(color)
        for i in range(np.n):
            if (i + count) % 3 == 0:
                np[i] = (0,0,0)
        np.show()
        time.sleep(.05)

        count = (count + 1) % 3



def lightning(color):
    bloodOrange = (40,0,0)
    np.fill(color)
    np.show()
    time.sleep(random.randint(2,3))
    for i in range(random.randint(1,5)):
        np.fill((0,0,230))
        np.show()
        time.sleep(random.randint(3,5)/100)
        np.fill((20,0,0))
        np.show()
        time.sleep(random.randint(4,5)/100)
   
   
   
while True:
    chase1((200,200,0))
    fade_out()
