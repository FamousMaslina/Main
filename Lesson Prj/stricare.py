
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
class Win(Wall):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)
    def print_win():
        print("You win for now...")



def change_background():
    backgrounds = [
        'assets/backgrounds/custom/bahmut.jpg',
        'assets/backgrounds/custom/zapraozhye.jpg',
        'assets/backgrounds/custom/kharkiv.jpg',
    ]
    selected_background = random.choice(backgrounds)
    background_image = image.load(selected_background)
    background_image = transform.scale(background_image, (800, 600))
    return background_image

def change_background_win():
    selected_background = "assets/backgrounds/custom/win.png"
    background_image = image.load(selected_background)
    background_image = transform.scale(background_image, (800, 600))
    return background_image


init()
screen = display.set_mode((800, 600))
clock = time.Clock()
running = True

levels = list()

characters = sprite.Group()
character =Character('assets/backgrounds/custom/russian.jpg',100,100)
characters.add(character)
win = Win("assets/backgrounds/custom/ukr.png",400,400)
characters.add(win)

for i in range(3):
    levels.append(sprite.Group())

def rasia():
    mixer.music.load('assets/backgrounds/custom/soviet.ogg')
    mixer.music.play(-1)

# wall1 = Wall('assets/backgrounds/cave.png',500,500)
walls1 = [
    Wall('assets/backgrounds/custom/trench.jpg', 300, 0),
    Wall('assets/backgrounds/custom/trench.jpg', 300, 64),
    Wall('assets/backgrounds/custom/trench.jpg', 300, 128),
    Wall('assets/backgrounds/custom/trench.jpg', 300, 192),
    Wall('assets/backgrounds/custom/trench.jpg', 300, 256),
    Wall('assets/backgrounds/custom/trench.jpg', 300, 320)
]
levels[0].add(walls1)


walls2 = list()
for i in range(7):
    walls2.append( Wall('assets/backgrounds/custom/trench.jpg', 64+i*64, 320))
    walls2.append( Wall('assets/backgrounds/custom/trench.jpg', 64+i*64, 320-i*64))

walls3 = list()
for i in range(5):
    walls2.append( Wall('assets/backgrounds/custom/trench.jpg', 64+i*2*64, 320))
    walls2.append( Wall('assets/backgrounds/custom/trench.jpg', 320-i*64,384))


def wagner():
    selected_background = "assets/backgrounds/custom/no.png"
    background_image = image.load(selected_background)
    background_image = transform.scale(background_image, (800, 600))
    return background_image


levels[1].add(walls2)
levels[2].add(walls3)





background_image = change_background()
level_nr = 0
count = 0
print("PS: You'll not get ukraine ;)")
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for e in event.get():
        if e.type == QUIT:
            running = False
    character.update()
    if count == 10:
        import time
        background_image = wagner()
    screen.fill((0,0,0)) #comment this and see what hapen
    screen.blit(background_image, (0, 0))
    characters.draw(screen)
    levels[level_nr].draw(screen)
    
    for wall in levels[level_nr]:
        if sprite.collide_rect(character, wall):
            count += 1
            print(count)

            character.reset_position()
            background_image = change_background()
            screen.blit(background_image, (0, 0))
    if sprite.collide_rect(character, win):
        if level_nr < 2: 
            level_nr += 1
        else:
            background_image = change_background_win()
            rasia()
            screen.blit(background_image, (0, 0))
            characters.remove(win)
        character.reset_position()
    # flip() the display to put your work on screen
    display.flip()
    dt = clock.tick(60) / 1000