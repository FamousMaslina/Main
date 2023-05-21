from pygame import *
import random
from aim9x import *
from time import *
ax = 200
ay = 600

class bullet(sprite.Sprite):
    def __init__(self, image_path, x, y):
       sprite.Sprite.__init__(self) 
       self.image = image.load(image_path)
       self.image = transform.scale(self.image, (64,64)) 
 
       self.rect = self.image.get_rect() 

       self.start_x = x
       self.start_y = y
       self.rect.x = x
       self.rect.y = y

aim9x = None  
cooldown = 0  

class enemy(sprite.Sprite):
    def __init__(self, image_path, x, y):
       sprite.Sprite.__init__(self)
       self.image = image.load(image_path)
       self.image = transform.scale(self.image, (64,64)) 

       self.rect = self.image.get_rect() 

       self.start_x = x
       self.start_y = y
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
           aim9x = bullet('assets/shooter/bullet.png', self.rect.x, self.rect.y) 
           cooldown = 5 
           print("AIM9X LAUNCHED!") 

        if aim9x:
            aim9x.rect.y -= 25 
            print("rect y -=25") 

            if aim9x.rect.y < 0:  
                aim9x = None 
                print("none") 

        if cooldown > 0:
            cooldown -= 1
            print("cooldown")  

f16 = enemy('assets/shooter/f16.png', 200, 600)