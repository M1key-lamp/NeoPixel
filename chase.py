import board
from neopixel import NeoPixel
import time



np = NeoPixel(board.D2,30,auto_write=False,brightness=.4)



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

       
while True:
        chase1((255,100,120))
