#Liam Collins
#4/25/18
#betterColoredWindow.py

from random import randint
from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)

def mouseClick(event):
    colors = [red,green,blue]
    Sprite(RectangleAsset(1200,800,LineStyle(1,colors[randint(0,2)]),colors[randint(0,2)]))

App().listenMouseEvent('click',mouseClick)
App().run()
