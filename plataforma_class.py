from cmath import rect
import pygame

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image=pygame.image.load('img/mesa.png')
        self.image=pygame.transform.scale(self.image,[100,100])
        self.rect=pygame.Rect(10,150,200,50)
        self.vel_y=3   
    def update(self,*args):
        if self.rect.x>=900 or self.rect.x<10:
            self.vel_y*=-1
        self.rect.left+=self.vel_y

class Plataforma2(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image=pygame.image.load('img/mesa.png')
        self.image=pygame.transform.scale(self.image,[100,100])
        self.rect=pygame.Rect(600,500,50,50)