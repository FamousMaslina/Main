from pygame import *
import random
import time as tm
from russia import *
from player import *
import pygame as pyg


clock = time.Clock()

FPS = 60
init()
screen = display.set_mode((400, 700))
clock = pyg.time.Clock()
running = True
#bullet = Bullet('assets/shooter/bullet.png', 20)
f16 = Character('assets/shooter/f16.png', 200, 600)

characters = sprite.Group()

characters.add(russia)
characters.add(russia2)
characters.add(russia3)
characters.add(russia4)
characters.add(russia5)
characters.add(russia6)
characters.add(russia7)
characters.add(russia8)
characters.add(russia9)
characters.add(russia10)
characters.add(russia11)
characters.add(russia12)
characters.add(f16)


mixer.music.load('assets/shooter/theme.mp3')
mixer.music.play(-1)


cooldown = 0

while running:
    for event in pyg.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((135, 206, 235))
    #f16.update()
    characters.update(screen)


    characters.draw(screen)
    #if sprite.collide_rect(Bullet, russia):
        #count += 1
        #print(count)

    display.flip()
    display.update()
    dt = clock.tick(60) / 1000
    #delay = 2 
    #delay_ticks = int(delay * FPS)  
    #time.delay(delay_ticks)
quit()