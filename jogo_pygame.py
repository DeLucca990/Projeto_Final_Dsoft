import pygame

pygame.init()

LARGURA=1024
ALTURA=600

window=pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Dsoft Kong')

game=True

while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
    
    window.fill((120, 11, 13))
    pygame.display.update()

pygame.quit()