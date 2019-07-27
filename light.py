#!/usr/bin/env python3

from sense_hat import SenseHat
s = SenseHat()   
from random import random
import time

x = 0
y = 0

#Color Description   RGB Values  
#Violet  148, 0, 211 #9400D3 
#Indigo  75, 0, 130  #4B0082 
#Blue    0, 0, 255   #0000FF 
#Green   0, 255, 0   #00FF00 
#Yellow  255, 255, 0 #FFFF00 
#Orange  255, 127, 0 #FF7F00 
#Red 255, 0 , 0  #FF0000 

colors_r = [255, 255, 255,   0,   0,  75, 148,   0]
colors_g = [  0, 127, 255, 255,   0,   0,   0,   0]
colors_b = [  0,   0,   0,   0, 255, 130, 211,   0]
colors_length = len(colors_r)

do_random = False

r = 0 #colors_r[0]
g = 0 #colors_g[0]
b = 0 #colors_b[0]

i = -1

last_press_time = 0

s.clear()

while True:
    e = s.stick.wait_for_event()
    print(x, y, r, g, b)
    print(e)
    print(e.direction)
    if e.action is "released": continue
    if e.direction is "middle":
        curr_press_time = time.time()
        if curr_press_time - last_press_time < 0.2:
            s.clear()
            continue
        else:
            if do_random:
                r = round(random() * 255)
                g = round(random() * 255)
                b = round(random() * 255)
            else:
                i += 1
                if i >= colors_length:
                    i = 0
                r = colors_r[i]
                g = colors_g[i]
                b = colors_b[i]
        last_press_time = curr_press_time
    elif e.direction is "right":
        if x == 7:
            x = 0
        else:
            x += 1
    elif e.direction is "left":
        if x == 0:
            x = 7
        else:
            x -= 1
    elif e.direction is "down":
        if y == 7:
            y = 0
        else:
            y += 1
    elif e.direction is "up":
        if y == 0:
            y = 7
        else:
            y -= 1
    s.set_pixel(x, y, r, g, b)
