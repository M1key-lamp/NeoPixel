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
"""
the code 'fade_out'  will fade from the color that is already shown and fade into black

Args: 
color: whatever color the user wants to use they will have to type in the rgb number when calling it to fade out from the color
speed: the speed is already set and will move at a fast pace when fading out

Returns: 
int: The sum of 2 numbers

"""
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
    """
    the code 'fade_in'  will fade from fade black after fade_out is called and will fade into the chosen color

    Arg: 
    color: whatever color the user wants to use they will have to type in the rgb number when calling it to fade into the next color
    speed: the speed is already set and will move at a fast pace when fading in
    Return:
    Returns: 
        int: The sum of 2 numbers

    """

    
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


def witch_hex(fire1,fire2,speed= 0.01,tim1 = 4):
"""
This code will assume the form of a fire with a led strip while dwindling the flame lightly decreasing on btightness

Args:
 fire1: the color background of the led
 fire2: the color for the multiple blinking lights on the led
 speed: the speed of the blinking lights
 tim1:the amount of times fire2 will be blinking



"""
    
    np.fill(fire1)
    np.show()
    for i in range(tim1):
        np[random.randint(0,np.n-2)] = fire2
        np.show()
        time.sleep(speed)
def flame(ma):
    for i in range(ma):
        witch_hex(purple,orange,0.1,0.1)



def corn_maze1(color):
    """
    This code will set in the lights in a rotating order as if one chasing another

    Args:
    color: The user will be able to set the color of the dots on the led strip
    Return:
     mod: remiaining left over

    """
    count = 2
    for i in range(np.n):
        np.fill(color)
        for i in range(np.n):
            if (i + count) % 3 == 0:
                np[i] = (0,0,0)
        np.show()
        time.sleep(.05)

        count = (count + 1) % 3




def lightning(color):
    """
    This code will blink from the main color that is already set in the code and then will quickly flash multiple times to a whit and orange color

    Args:
     The user will be able to set the color of the dots on the led strip

      Return: 
      a gradient halloween color that will blink with whichever color the user chooses
     
    """
    bloodOrange = (250,30,0)
    np.fill(color)
    np.show()
    time.sleep(random.randint(2,3))
    for i in range(random.randint(1,5)):
        np.fill((white))
        np.show()
        time.sleep(random.randint(3,5)/200)
        np.fill((orange))
        np.show()
        time.sleep(random.randint(3,5)/200)
   
clr_list = [orange, purple, brown]
   
while True:
    rainbow_led = random.choice(clr_list)
    for i in range(10):
        flame(1)
        witch_hex((purple),(orange),0.01,10)
    fade_out(rainbow_led)
    fade_in(white)
    for i in range(3):
       corn_maze1((rainbow_led))
    fade_out(rainbow_led)
    fade_in(white)
    for i in range(2):
        lightning(rainbow_led)
    fade_out(black)
    
        
    

