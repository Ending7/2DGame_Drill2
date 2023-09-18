from pico2d import *
import math

math.sin(270 / 360 * 2 * math.pi)
         
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

val = 270
while(True):
    
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400 + 400*(math.cos(val / 360 * 2 * math.pi)), 360 +270*(math.sin(val / 360 * 2 * math.pi)) )
    val = val + 1
    delay(0.01)
