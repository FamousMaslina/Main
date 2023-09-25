
from pygame import *

import random


#main player class—Characters
class Character(sprite.Sprite): #in the parentheses it is indicated that the class inherits from the Sprite class
    #creating the constructor
    def __init__(self, image_path, x, y):
       sprite.Sprite.__init__(self) #mandatory calling of the constructor of the parent class
       # each sprite should store the image property—its image
       self.image = image.load(image_path)
       self.image = transform.scale(self.image, (64,64)) # resize the image
 
       # each sprite should store the rect property—the rectangle into which it is inscribed
       self.rect = self.image.get_rect() #we get a rectangle from the image
       #we set its location
       self.start_x = x
       self.start_y = y
       self.rect.x = x
       self.rect.y = y
   #method defining the sprite’s movement
    def update(self):

        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
           self.rect.x -= 5
        if keys[K_RIGHT] and self.rect.x < 740:
           self.rect.x += 5
        if keys[K_UP] and self.rect.y > 0:
           self.rect.y -= 5
        if keys[K_DOWN] and self.rect.y < 540:
           self.rect.y += 5
    def reset_position(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
class Wall(sprite.Sprite): 
    def __init__(self, image_path, x, y):
        sprite.Sprite.__init__(self) 
        self.image = image.load(image_path)
        self.image = transform.scale(self.image, (64,64)) # resize the image
        self.rect = self.image.get_rect() #we get a rectangle from the image
        #we set its location
        self.rect.x = x
        self.rect.y = y




def change_background():
    backgrounds = [
        'assets/backgrounds/city_1.png',
        'assets/backgrounds/city_2.png',
        'assets/backgrounds/city_3.png',
    ]
    
    selected_background = random.choice(backgrounds)
    background_image = image.load(selected_background)
    background_image = transform.scale(background_image, (800, 600))
    return background_image



init()
screen = display.set_mode((800, 600))
clock = time.Clock()
running = True


character = Character('assets/level/hero.png',100,100)

sprite_group = sprite.Group()
sprite_group.add(character)
sprite_group.draw(screen)


# wall1 = Wall('assets/backgrounds/cave.png',500,500)
walls = [
    Wall('assets/backgrounds/cave.png', 300, 0),
    Wall('assets/backgrounds/cave.png', 300, 64),
    Wall('assets/backgrounds/cave.png', 300, 128),
    Wall('assets/backgrounds/cave.png', 300, 192),
    Wall('assets/backgrounds/cave.png', 300, 256),
    Wall('assets/backgrounds/cave.png', 300, 320)
]
for i in range(10):
    walls.append(Wall("assets/backgrounds/cave.png", 100+i*70, 384))
sprite_group.add(walls)
background_image = change_background()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for e in event.get():
        if e.type == QUIT:
            running = False
    character.update()
    # screen.fill((0,0,0)) #comment this and see what hapen
    screen.blit(background_image, (0, 0))
    sprite_group.draw(screen)
    
    for wall in walls:
        if sprite.collide_rect(character, wall):
            character.reset_position()
            background_image = change_background()
            screen.blit(background_image, (0, 0))

    # flip() the display to put your work on screen
    display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
