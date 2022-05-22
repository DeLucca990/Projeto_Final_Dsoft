from multiprocessing import Event
import pygame

class Personagem(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.lado='parado direita'
        self.image=pygame.image.load('img/pulga_parado_d.png')
        self.image=pygame.transform.scale(self.image,[80,80])
        self.rect=pygame.Rect(0,600,100,100)
        self.vel_x=0
        self.vel_y=0
        self.gravidade=0.1
        self.intencao_pos=list(self.rect.center)


    def eventos_teclado(self,event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                self.lado='direita'
                self.image=pygame.image.load('img/pulga_direita.png')
                self.image=pygame.transform.scale(self.image,[80,80])
                self.vel_x=5
            if event.key==pygame.K_a or event.key==pygame.K_LEFT:
                self.lado='esquerda'
                self.image=pygame.image.load('img/pulga_esquerda.png')
                self.image=pygame.transform.scale(self.image,[80,80])
                self.vel_x=-5
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                self.lado='parado direita'
                self.image=pygame.image.load('img/pulga_parado_d.png')
                self.image=pygame.transform.scale(self.image,[80,80])
                self.vel_x=0
            if event.key==pygame.K_a or event.key==pygame.K_LEFT:
                self.lado='parado esquerda'
                self.image=pygame.image.load('img/pulga_parado_e.png')
                self.image=pygame.transform.scale(self.image,[80,80])
                self.vel_x=0
            if event.key==pygame.K_SPACE:
                self.lado='pulando'
                self.image=pygame.image.load('img/pulga_pulo.png')
                self.image=pygame.transform.scale(self.image,[80,80])
                self.vel_y=-5 

    def update(self,*args):
        self.vel_y+=self.gravidade
        self.intencao_pos[0]+=self.vel_x
        self.intencao_pos[1]+=self.vel_y

        if self.rect.top<0:
            self.rect.top=0
        elif self.rect.bottom>620:
            self.rect.bottom=620
        elif self.rect.left<0:
            self.rect.left=0
        elif self.rect.right>1060:
            self.rect.right=1060
        
        
            