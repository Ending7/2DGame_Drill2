from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90

while(True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    if(y== 90 and x <= 800):
        x = x+2
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
    delay(0.01)
