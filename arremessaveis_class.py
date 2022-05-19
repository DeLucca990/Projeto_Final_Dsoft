import pygame
import random

class Quizz(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.image=pygame.image.load('img/quizz.png')
        self.image=pygame.transform.scale(self.image,[50,50])
        self.rect=pygame.Rect(50,50,100,100)
        self.speed= 1 + random.random()*2
        self.rect.y= 0 - random.randint(1,200)
        self.rect.x= random.randint(1,1000)

    def update(self, *args):
        self.rect.y += self.speed

        if self.rect.bottom>600:
            self.kill()
            
