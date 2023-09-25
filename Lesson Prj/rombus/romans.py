from pygame import *
import random
import time as tm
ax = 200
ay = 600

cooldown = None
count = 0
class Character(sprite.Sprite): #in the parentheses it is indicated that the class inherits from the Sprite class
    #creating the constructor


    def __init__(self, image_path, x, y):
        sprite.Sprite.__init__(self) #mandatory calling of the constructor of the parent class
        # each sprite should store the image property—its image
        self.image = image.load(image_path)
        self.image = transform.scale(self.image, (128,128)) # resize the image
 
        # each sprite should store the rect property—the rectangle into which it is inscribed
        self.rect = self.image.get_rect() #we get a rectangle from the image
        #we set its location
        self.start_x = x
        self.start_y = y
        self.rect.x = x
        self.rect.y = y

    def update(self, screen):
      keys = key.get_pressed()
      if keys[K_LEFT] and self.rect.x > 0:
         self.rect.x -= 1
      if keys[K_RIGHT] and self.rect.x < 740:
         self.rect.x += 1

    def reset_position(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y