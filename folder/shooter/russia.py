from pygame import *
import random
 
class enemy(sprite.Sprite): #in the parentheses it is indicated that the class inherits from the Sprite class
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

rx = random.randint(0, 390)
ry = random.randint(0, 25)
russia = enemy('assets/shooter/su57.png', rx, ry)
rx = random.randint(0, 390)
ry = random.randint(0, 25)
russia2 = enemy('assets/shooter/su57.png', rx, ry)
rx = random.randint(0, 390)
ry = random.randint(0, 25)
russia3 = enemy('assets/shooter/su57.png', rx, ry)
rx = random.randint(0, 390)
ry = random.randint(0, 25)
russia4 = enemy('assets/shooter/su57.png', rx, ry)
rx = random.randint(0, 390)
ry = random.randint(0, 25)
russia5 = enemy('assets/shooter/su57.png', rx, ry)
rx = random.randint(0, 400)
ry = random.randint(0, 25)
russia6 = enemy('assets/shooter/su57.png', rx, ry)

