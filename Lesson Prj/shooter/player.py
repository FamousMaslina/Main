from pygame import *
import random
from aim9x import *
import time as tm
from russia import *
ax = 200
ay = 600

cooldown = None
count = 0
class Character(sprite.Sprite): #in the parentheses it is indicated that the class inherits from the Sprite class
    #creating the constructor
   bullets = sprite.Group()


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
   def shoot(self):
      self.bullets.add(Bullet(self.rect.x,self.rect.y))

   #method defining the sprite’s movement
   def update(self, screen):
      keys = key.get_pressed()
      if keys[K_LEFT] and self.rect.x > 0:
         self.rect.x -= 5
      if keys[K_RIGHT] and self.rect.x < 740:
         self.rect.x += 5
      if keys[K_SPACE]:
         self.shoot()
         sfx = mixer.Sound('assets/shooter/bullet2.mp3')
         sfx.play(0)

      self.bullets.update()
      self.bullets.draw(screen) 
         
      for bullet in self.bullets:
         if bullet.getY() < -100:
              bullet.kill()
         elif sprite.collide_rect(bullet, russia):
            print("russia ")
            russia.kill()
            russia.rect = Rect(0, 0, 0, 0)
            bullet.kill()
         elif sprite.collide_rect(bullet, russia2):
            print("russia 2")
            russia2.kill()
            russia12.rect = Rect(0, 0, 0, 0)
            bullet.kill()
         elif sprite.collide_rect(bullet, russia3):
            print("russia 3")
            russia3.kill()
            russia3.rect = Rect(0, 0, 0, 0)
            bullet.kill()
         elif sprite.collide_rect(bullet, russia4):
            print("russia 4")
            russia4.kill()
            russia4.rect = Rect(0, 0, 0, 0)
            bullet.kill()
         elif sprite.collide_rect(bullet, russia5):
            russia5.kill()
            russia5.rect = Rect(0, 0, 0, 0)
            print("russia 5")
            bullet.kill()

         elif sprite.collide_rect(bullet, russia6):
            print("russia 6")
            russia6.kill()
            russia6.rect = Rect(0, 0, 0, 0)
            bullet.kill()
         elif sprite.collide_rect(bullet, russia7):
            print("russia 7")
            russia7.kill()
            russia7.rect = Rect(0, 0, 0, 0)
            bullet.kill()
         elif sprite.collide_rect(bullet, russia8):
            print("russia 8")
            russia8.kill()
            russia8.rect = Rect(0, 0, 0, 0)
            bullet.kill()
         elif sprite.collide_rect(bullet, russia9):
            print("russia 9")
            russia9.kill()
            russia9.rect = Rect(0, 0, 0, 0)
            bullet.kill()
         elif sprite.collide_rect(bullet, russia10):
            russia10.kill()
            russia10.rect = Rect(0, 0, 0, 0)
            print("russia 10")
            bullet.kill()

         elif sprite.collide_rect(bullet, russia11):
            print("russia 11")
            russia11.kill()
            russia11.rect = Rect(0, 0, 0, 0)
            bullet.kill()
         elif sprite.collide_rect(bullet, russia12):
            russia12.kill()
            russia12.rect = Rect(0, 0, 0, 0)
            print("russia 12")
            bullet.kill()

   def reset_position(self):
      self.rect.x = self.start_x
      self.rect.y = self.start_y