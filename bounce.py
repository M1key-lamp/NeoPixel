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


def larson(background, fground, num, spd):
    pixel = 0
    direction = 1
    count = 0
    while count < num:
        np.fill(background)
        np.show()
        np[pixel - 1]
        np[pixel] = fground
        np.show()
        time.sleep(spd)
        pixel += direction 
        if (pixel >= (np.n -1) or pixel <= 0):
            direction *= -1
            count += 1
        
      
      
while True:
    larson(purple, blue,2,0.03)
    


        
        
        
    

