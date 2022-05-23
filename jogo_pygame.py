import pygame
import random
from personagens_class import *
from arremessaveis_class import Quizz
from plataforma_class import *

#Iniciando o Game:
pygame.init()

LARGURA=1024
ALTURA=600

window=pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Dsoft Kong')

#Objetos:
grupo_de_play=pygame.sprite.Group()
grupo_de_arre=pygame.sprite.Group()
grupo_de_plataforma=pygame.sprite.Group()

for pos_inicial in range (100,400,300):
    plat_movel=Plataforma(pos_inicial)
    grupo_de_plataforma.add(plat_movel)

plat_fix=Plataforma2()
grupo_de_plataforma.add(plat_fix)

jogador=Personagem()
grupo_de_play.add(jogador)

game=True
timer=0
clock=pygame.time.Clock()
while game:
    clock.tick(60)

    #Eventos:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        jogador.eventos_teclado(event)

    #Update Lógica:
    grupo_de_play.update()
    grupo_de_plataforma.update()
    timer+=1
    if timer>30:
        timer=0
        if random.random()<0.3:
            novo_quizz=Quizz(grupo_de_play,grupo_de_arre)

    #Colisões:
    colisao_jogador_arre=pygame.sprite.spritecollide(jogador,grupo_de_arre,True,pygame.sprite.collide_mask)
    colisao_jogador_mesa=pygame.sprite.spritecollide(jogador,grupo_de_plataforma,False,pygame.sprite.collide_mask)
    for plataforma in colisao_jogador_mesa:
        if jogador.horizontal_state=='left':
            jogador.rect.x+=2
        if jogador.horizontal_state == 'right':
            jogador.rect.x-=2
        if jogador.vertical_state == 'caindo':
            jogador.rect.y-=2
            jogador.vel_y=2
            jogador.rect.x+=plataforma.vel_x

    #Draw:
    window.fill((4,71 ,13))
    grupo_de_plataforma.draw(window)
    grupo_de_play.draw(window)
    pygame.display.update()
pygame.quit()