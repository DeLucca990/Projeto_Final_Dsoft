import pygame
import random

class Quizz(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.image=pygame.image.load('img/quizz.png')
        self.image=pygame.transform.scale(self.image,[25,25])
        self.rect=pygame.Rect(50,50,100,100)
        self.speed= 1 + random.random()*2
        self.rect.y= 0 - random.randint(1,200)
        self.rect.x= random.randint(1,1000)

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.bottom>700:
            self.kill()
            
class Ep1(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.image=pygame.image.load('img/ep1.png')
        self.image=pygame.transform.scale(self.image,[25,25])
        self.rect=pygame.Rect(50,50,100,100)
        self.speed= 1 + random.random()*2
        self.rect.y= 0 - random.randint(1,200)
        self.rect.x= random.randint(1,1000)

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.bottom>700:
            self.kill()

class Ep2(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.image=pygame.image.load('img/ep2.png')
        self.image=pygame.transform.scale(self.image,[25,25])
        self.rect=pygame.Rect(50,50,100,100)
        self.speed= 1 + random.random()*2
        self.rect.y= 0 - random.randint(1,200)
        self.rect.x= random.randint(1,1000)

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.bottom>700:
            self.kill()
    
class Marcio(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.image=pygame.image.load('img/marcio.png')
        self.image=pygame.transform.scale(self.image,[25,25])
        self.rect=pygame.Rect(50,50,100,100)
        self.speed= 1 + random.random()*2
        self.rect.y= 0 - random.randint(1,200)
        self.rect.x= random.randint(1,1000)

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.bottom>700:
            self.kill()

class Pedro(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.image=pygame.image.load('img/pedro.png')
        self.image=pygame.transform.scale(self.image,[25,25])
        self.rect=pygame.Rect(50,50,100,100)
        self.speed= 1 + random.random()*2
        self.rect.y= 0 - random.randint(1,200)
        self.rect.x= random.randint(1,1000)

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.bottom>700:
            self.kill()