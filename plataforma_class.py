import pygame

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image=pygame.image.load('img/mesa.png')
        self.image=pygame.transform.scale(self.image,[100,100])
        self.rect=pygame.Rect(600,500,50,50)