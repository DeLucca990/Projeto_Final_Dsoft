import pygame
import random
from personagens_class import Personagem
from arremessaveis_class import Quizz

#Iniciando o Game:
pygame.init()

LARGURA=1024
ALTURA=600

window=pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Dsoft Kong')

#Objetos:
grupo_de_objeto=pygame.sprite.Group()

jogador=Personagem(grupo_de_objeto)
arremessa_quizz=Quizz(grupo_de_objeto)

game=True
timer=0
clock=pygame.time.Clock()
while game:
    clock.tick(60)

    #Eventos:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                jogador.pular()
    #Update Lógica:
    grupo_de_objeto.update()
    timer+=1
    if timer>30:
        timer=0
        if random.random()<0.3:
            novo_quizz=Quizz(grupo_de_objeto)
    #Draw:
    window.fill((255,255 ,255))
    grupo_de_objeto.draw(window)
    pygame.display.update()

pygame.quit()