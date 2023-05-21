from pygame import *
import random
from russia import *
from player import *
from aim9x import *
init()
screen = display.set_mode((400, 700))
clock = time.Clock()
running = True
characters = sprite.Group()
characters.add(russia)
characters.add(russia2)
characters.add(russia3)
characters.add(russia4)
characters.add(russia5)
characters.add(f16)
characters.add(aim9x)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for e in event.get():
        if e.type == QUIT:
            running = False
    screen.fill((0,0,0)) #comment this and see what hapen
    characters.draw(screen)
    f16.update()
    

    # flip() the display to put your work on screen
    display.flip()
    dt = clock.tick(60) / 1000