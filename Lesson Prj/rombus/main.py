from pygame import *
import random
import time as tm
from romans import *
from tree import *
import pygame as pyg


clock = time.Clock()

FPS = 60
init()
screen = display.set_mode((800, 300))
clock = pyg.time.Clock()
display.set_caption('Romanian Forest Industry Simulator')
Icon = image.load('folder/rombus/icon.jpg')
display.set_icon(Icon)
running = True
#bullet = Bullet('assets/shooter/bullet.png', 20)
roman = Character('folder/rombus/romand.png', 50, 170)
tree = Character2('folder/rombus/tree.png', 650, 170)
tree2 = Character2('folder/rombus/tree.png', 600, 170)
tree3 = Character2('folder/rombus/tree.png', 700, 170)
garage = Character2('folder/rombus/garage2.png', 0, 170)
flag = Character2('folder/rombus/flag2.png', 685, 25)

characters = sprite.Group()

characters.add(roman)
characters.add(tree)
characters.add(tree2)
characters.add(tree3)
characters.add(garage)
characters.add(flag)

mixer.music.load('folder/rombus/theme.mp3')
mixer.music.play(-1)


cooldown = 0

while running:
    for event in pyg.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((135, 206, 235))
    
    characters.update(screen)  # Update the characters group
    sumc = 0
    sumc2 = 0
    sumc3 = 0
    sumF = 0
    if sprite.collide_rect(roman, tree):
        sumc = random.randint(250, 3000)
        print("1",sumc)
        sfx2 = mixer.Sound('folder/rombus/saw.mp3')
        sfx2.play(0)
    elif sprite.collide_rect(roman, tree):
        sumc2 = random.randint(250, 3000)
        print("2",sumc2)
        sfx2 = mixer.Sound('folder/rombus/saw.mp3')
        sfx2.play(0)
    elif sprite.collide_rect(roman, tree):
        sumc3 = random.randint(250, 3000)
        print("3", sumc3)
        sfx2 = mixer.Sound('folder/rombus/saw.mp3')
        sfx2.play(0)
    elif sprite.collide_rect(roman, garage):
        sumF = sumc+sumc2+sumc3
        print(sumF)
        sfx = mixer.Sound('folder/rombus/cash.mp3')
        sfx.play(0)

    
    characters.draw(screen)

    display.flip()
    display.update()
    dt = clock.tick(60) / 1000

quit()