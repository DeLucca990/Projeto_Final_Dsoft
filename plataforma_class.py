import pygame
from personagens_class import *

class Plataforma(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('img/itens/mesa_final.png')
        self.image=pygame.transform.scale(self.image,[100,45])
        self.rect=pygame.Rect(pos_x,pos_y,80,45)
        self.vel_x=3
    def update(self,*args):
        if self.rect.x>=900 or self.rect.x<10:
            self.vel_x*=-1
        self.rect.left+=self.vel_x

