import pygame

ESC1=145
ESC2=145

class Pelicano(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites=[]
        self.sprites.append(pygame.image.load('img/persona/peli_1.png'))
        self.sprites.append(pygame.image.load('img/persona/peli_2.png'))
        self.sprites.append(pygame.image.load('img/persona/peli_3.png'))
        self.sprites.append(pygame.image.load('img/persona/peli_4.png'))
        self.sprites.append(pygame.image.load('img/persona/peli_5.png'))
        self.sprites.append(pygame.image.load('img/persona/peli_6.png'))
        self.sprites.append(pygame.image.load('img/persona/peli_7.png'))
        self.sprites.append(pygame.image.load('img/persona/peli_8.png'))
        self.sprites.append(pygame.image.load('img/persona/peli_9.png'))
        self.sprites.append(pygame.image.load('img/persona/peli_10.png'))
        self.atual=0
        self.image=self.sprites[self.atual]
        self.image=pygame.transform.scale(self.image,(ESC1,ESC2))
        self.rect=self.image.get_rect()
        self.speed=2
        self.rect.x=-3
        self.rect.y=10
        self.rect.topleft=-80,10

    def update(self):
        self.rect.x+=self.speed
        self.atual=self.atual + 0.25
        if self.atual>=len(self.sprites):
            self.atual=0
        self.image=self.sprites[int(self.atual)]
        self.image=pygame.transform.scale(self.image,(ESC1,ESC2))
        if self.rect.x>1100:
            self.kill()