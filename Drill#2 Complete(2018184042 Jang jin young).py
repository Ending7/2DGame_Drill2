#2018184042 장진영 Drill#2 
from pico2d import *
import math
   
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
val = 270
while(True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x,y)
    if(y == 90 and x <= 800):
        x = x+2
        y = 90
        if(x == 400):
            while(val != 630):
                clear_canvas_now()
                grass.draw_now(400, 30)
                character.draw_now(400 + 400*(math.cos(val / 360 * 2 * math.pi)), 360 +270*(math.sin(val / 360 * 2 * math.pi)) )
                val = val + 1
                delay(0.01)
            val = 270
            x = 400
            y = 90
           
    elif(y <= 600 and x >= 800 ):
        x = 800
        y = y+2
    elif(y>=600 and x>= 0):
        x = x-2
        y = 600
    elif(y>=0 and x<= 0):
        x = 0
        y = y-2

    
    delay(0.001)

   
