import pygame

class Personagem(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.lado='parado'
        self.image=pygame.image.load('img/pulga_parado.png')
        self.image=pygame.transform.scale(self.image,[80,80])
        self.rect=pygame.Rect(0,600,100,100)
        self.pulo=False
        self.posy_inicial=600

    def pular(self):
        self.pulo=True
    
    def update(self, *args):
        #Lógica
        if self.pulo==True:
            if self.rect.y<=400:
                self.pulo=False
            self.rect.y-=5
        else:
            if self.rect.y<self.posy_inicial:
                self.rect.y+=5
            else:
                self.rect.y=self.posy_inicial
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.lado='esquerda'
            self.image=pygame.image.load('img/pulga_esquerda.png')
            self.image=pygame.transform.scale(self.image,[80,80])
            self.rect.x -= 5
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.lado='direita'
            self.image=pygame.image.load('img/pulga_direita.png')
            self.image=pygame.transform.scale(self.image,[80,80])
            self.rect.x += 5
        else:
            self.lado='parado'
            self.image=pygame.image.load('img/pulga_parado.png')
            self.image=pygame.transform.scale(self.image,[80,80])
            
        if self.rect.top<0:
            self.rect.top=0
        elif self.rect.bottom>620:
            self.rect.bottom=620
        elif self.rect.left<50:
            self.rect.left=50
        elif self.rect.right>1060:
            self.rect.right=1060
            