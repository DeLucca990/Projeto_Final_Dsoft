import pygame

class Personagem(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.lado='direita'
        self.image=pygame.image.load('img/pulga_direita.png')
        self.image=pygame.transform.scale(self.image,[80,80])
        self.rect=pygame.Rect(0,395,100,100)
    
    def update(self, *args):
        #Lógica
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
        elif keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= 5
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += 5

        if self.rect.top<0:
            self.rect.top=0
        elif self.rect.bottom>620:
            self.rect.bottom=620
        elif self.rect.left<-20:
            self.rect.left=-20
        elif self.rect.right>1060:
            self.rect.right=1060