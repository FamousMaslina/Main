from pygame import *
import random
from time import *
from russia import *
from player import *
import pygame as pyg

class Bullet(sprite.Sprite):
    def __init__(self, image_path, x, y):
        sprite.Sprite.__init__(self) 
        self.image = image.load(image_path)
        self.image = transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemy(sprite.Sprite):
    def __init__(self, image_path, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(image_path)
        self.image = transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        global aim9x, cooldown

        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5
        if keys[K_RIGHT] and self.rect.x < 1300:
            self.rect.x += 5
        if keys[K_SPACE] and self.rect.x < 1300 and cooldown <= 0:
            aim9x = Bullet('assets/shooter/bullet.png', self.rect.x, self.rect.y)
            cooldown = 5
            print("AIM9X LAUNCHED!")

        if aim9x:
            aim9x.rect.y -= 25
            print("aim9x.rect.y -= 25")

            if aim9x.rect.y < 0:
                aim9x = None
                print("aim9x = None")

        if cooldown > 0:
            cooldown -= 1
            print("cooldown")

init()
screen = display.set_mode((400, 700))
clock = pyg.time.Clock()
running = True

characters = sprite.Group()
characters.add(russia)
characters.add(russia2)
characters.add(russia3)
characters.add(russia4)
characters.add(russia5)
characters.add(f16)

aim9x = None
cooldown = 0

while running:
    for event in pyg.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((0, 0, 0))

    if aim9x:
        characters.add(aim9x)

    characters.update()

    if aim9x and aim9x.rect.y < 0:
        aim9x = None

    characters.draw(screen)

    display.flip()
    dt = clock.tick(60) / 1000

quit()