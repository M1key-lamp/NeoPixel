import board
from neopixel import NeoPixel
import time
import random
np = NeoPixel(board.D2, 30, auto_write= False, brightness=0.3)

def background():
    np.fill((20,30,50))
    np.show()

value = 0

background()

def flash(flash):
    np.fill(flash)
    np.show()
    time.sleep(random.randint(2,3))
    for i in range(random.randint(1,5)):
        time.sleep(random.randint(3,5))
        np.fill((22,20,200))
        np.show()
        time.sleep(random.randint(4,5))
        
        
                                  
                                
                                
while True:
    background()
    flash((255,2,230))
