from pygame import *
import random
init()
window = display.set_mode((800, 600))
display.set_caption("Mazeeee")
x = 400
y = 560
width = 40
height = 40
speed = 2
run = True
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
while run:
    time.delay(10)
    for e in event.get():
        if e.type == QUIT:
            run = False
    keys = key.get_pressed()

    if keys[K_LEFT] and x > 0:
        x -= speed
    if keys[K_RIGHT] and x < 760:
        x += speed
    if keys[K_UP] and y > 0:
        y -= speed
    if keys[K_DOWN] and y < 560:
        y += speed
    character.update()
    # screen.fill((0,0,0)) #comment this and see what hapen
    screen.blit(background_image, (0, 0))
    sprite_group.draw(screen)
    
    for wall in walls:
        if sprite.collide_rect(character, wall):
            character.reset_position()
            background_image = change_background()
            screen.blit(background_image, (0, 0))
    draw.rect(window,(123,18,53),(x,y,width,height))
    display.update()
quit()