from multiprocessing import Event
import pygame
from plataforma_class import *

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lado='parado direita'
        self.image=pygame.image.load('img/pulga_parado_d.png')
        self.image=pygame.transform.scale(self.image,[70,70])
        self.rect=pygame.Rect(0,600,60,60)
        self.vel_x=0
        self.vel_y=0
        self.gravidade=0.1
        self.vertical_state = 'caindo'
        
    def eventos_teclado(self,event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                self.lado='pulando'
                self.image=pygame.image.load('img/pulga_pulo.png')
                self.image=pygame.transform.scale(self.image,[70,70])
                self.vel_y=-3 
                self.vertical_state = 'pulando'

    def update(self,*args):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.lado='esquerda'
            self.image=pygame.image.load('img/pulga_esquerda.png')
            self.image=pygame.transform.scale(self.image,[70,70])
            self.vel_x =-5
            self.horizontal_state = 'left'
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.lado='direita'
            self.image=pygame.image.load('img/pulga_direita.png')
            self.image=pygame.transform.scale(self.image,[70,70])
            self.vel_x = 5
            self.horizontal_state = 'right'
        else:
            self.lado='parado direita'
            if self.vertical_state == 'caindo':
                self.image=pygame.image.load('img/pulga_parado_d.png')
                self.image=pygame.transform.scale(self.image,[70,70])
            self.vel_x=0
            self.horizontal_state = 'none'
            
        self.rect.x+=self.vel_x
        self.rect.y+=self.vel_y
        self.vel_y+=self.gravidade
        if self.vel_y>=0:
            self.vertical_state = 'caindo'

        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>590:
            self.rect.bottom=590
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>1030:
            self.rect.right=1030
            
        
            