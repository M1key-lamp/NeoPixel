import board
from neopixel import NeoPixel
import time
import random


np = NeoPixel(board.D2,30,auto_write=False,brightness=.3)



orange = (250, 60, 0)
brown = (109, 37, 0)
purple = (140, 0, 197)
white = (255,255,255)


def fade_out(color, speed= 0.04):

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
        
        np[0]
        np.show()
        time.sleep(speed)

def fade_in(color,speed= 0.25):
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

def fire(fire1,fire2,speed,tim1):
    np.fill(fire1)
    np.show()
    for i in range(tim1):
        np[random.randint(0,np.n-2)] = fire2
        np.show()
        time.sleep(speed)
def flame(ma):
    for i in range(ma):
        fire(purple,orange,0.1,0.1)



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
    bloodOrange = (250,30,0)
    np.fill(color)
    np.show()
    time.sleep(random.randint(2,3))
    for i in range(random.randint(1,5)):
        np.fill((white))
        np.show()
        time.sleep(random.randint(3,5)/100)
        np.fill((orange))
        np.show()
        time.sleep(random.randint(3,5)/100)
   
clr_list = [orange, purple, brown]
   
while True:
    rainbow_led = random.choice(clr_list)
    for i in range(5):
        chase1((rainbow_led))
    fade_out(purple)
    fade_in(orange)
    for i in range:
        flame(2)
        fire((255, 50, 0),(255, 20, 0),0.01,10)
        
    

