import pygame
import random

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Main")
pygame.init()

x = 50
y = 50
width = 40
height = 40
speed = 5
run = True

class Character(pygame.sprite.Sprite):
    #creating the constructor
    def __init__(self, image_path, x, y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(image_path)
       self.image = pygame.transform.scale(self.image, (64,64))
 
       self.rect = self.image.get_rect()
       self.start_x = x
       self.start_y = y
       self.rect.x = x
       self.rect.y = y
    def update(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
           self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.x < 740:
           self.rect.x += 5
        if keys[pygame.K_UP] and self.rect.y > 0:
           self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.y < 540:
           self.rect.y += 5
    def reset_position(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
class Wall(pygame.sprite.Sprite): 
    def __init__(self, image_path, x, y):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Win(pygame.sprite.Sprite): 
    def __init__(self, image_path, x, y):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def change_background():
    backgrounds = [
        'assets/backgrounds/custom/afgdesert.jpg',
        'assets/backgrounds/custom/iraqdesert.jpg'
    ]
    background_path = random.choice(backgrounds)
    background_image = pygame.image.load(background_path)
    background_image = pygame.transform.scale(background_image, (800, 600))
    return background_image

#def block(): #nu merge
    #pygame.draw.rect(window,(255,0,0),(x,y,width,height))

character = Character('assets/heroes/soldier/ussSoldier.png',100,100)

sprite_group = pygame.sprite.Group()
sprite_group.add(character)
sprite_group.draw(window)

lvl1 = True
lvl2 = False

walls = [
    Wall('assets/backgrounds/cave.png', 300, 0),
    Wall('assets/backgrounds/cave.png', 300, 64),
    Wall('assets/backgrounds/cave.png', 300, 128),
    Wall('assets/backgrounds/cave.png', 300, 192),
    Wall('assets/backgrounds/cave.png', 300, 256),
    Wall('assets/backgrounds/cave.png', 300, 320),
    Wall('assets/backgrounds/cave.png', 300, 384),
    Wall('assets/backgrounds/cave.png', 362, 384),
    Wall('assets/backgrounds/cave.png', 424, 384),
    Wall('assets/backgrounds/cave.png', 486, 384),
    Wall('assets/backgrounds/cave.png', 550, 384),

]
walls2 = [
    Wall('assets/backgrounds/cave.png', 300, 0),
    Wall('assets/backgrounds/cave.png', 300, 64),
    Wall('assets/backgrounds/cave.png', 300, 128),
    Wall('assets/backgrounds/cave.png', 300, 192),
    Wall('assets/backgrounds/cave.png', 300, 256),
    Wall('assets/backgrounds/cave.png', 300, 320)

]

win1 = [
    Win('assets/level/trophy-1.png', 630, 384)
]
win2 = [
    Win('assets/level/trophy-1.png', 630, 300)
]


if lvl1 == True:
    sprite_group.remove(win2)
    sprite_group.remove(walls2)
    sprite_group.add(win1)
    sprite_group.add(walls)
elif lvl2 == True:
    sprite_group.remove(win1)
    sprite_group.remove(walls)
    sprite_group.add(win2)
    sprite_group.add(walls2)
background_image = change_background()


print("lvl1", lvl1)
print("lvl2", lvl2)
while run:
    pygame.time.delay(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    window.blit(background_image, (0, 0)) # blit the background image first

    character.update()
    sprite_group.draw(window)
    if lvl1 == True:
        for wall in walls:
            if pygame.sprite.collide_rect(character, wall):
                character.reset_position()
                background_image = change_background() # choose a new background image
        for nxt in win1:
            if pygame.sprite.collide_rect(character, nxt):
                character.reset_position()
                background_image = change_background() # choose a new background image
                lvl1 = False
                lvl2 = True
                print("lvl1", lvl1)
                print("lvl2", lvl2)
                if lvl2 == True:
                    sprite_group.remove(win1)
                    sprite_group.remove(walls)
                    sprite_group.add(win2)
                    sprite_group.add(walls2)
                    for wall in walls2:
                        if pygame.sprite.collide_rect(character, wall):
                            character.reset_position()
                            background_image = change_background() # choose a new background image
                        sprite_group.draw(window)
                        for nxt in win1:
                            if pygame.sprite.collide_rect(character, nxt):
                                character.reset_position()
                                background_image = change_background() # choose a new background image
                                lvl2 = False

    pygame.display.flip()

    clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000
pygame.quit()