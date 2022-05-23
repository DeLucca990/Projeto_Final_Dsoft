import pygame
import random
from personagens_class import *
from arremessaveis_class import *
from plataforma_class import *

#Iniciando o Game:
pygame.init()

LARGURA=1024
ALTURA=600

window=pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Dsoft Kong')

#Objetos:
grupo_de_play=pygame.sprite.Group()
grupo_de_ep=pygame.sprite.Group()
grupo_de_quizz=pygame.sprite.Group()
grupo_de_vida=pygame.sprite.Group()
grupo_de_plataforma=pygame.sprite.Group()
                         #ini  #fim #gap
for pos_inicial in range (50,1000,150):
    pos_x=random.randint(10,900)
    plat_movel=Plataforma(pos_x,pos_inicial)
    grupo_de_plataforma.add(plat_movel)


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
    if timer>20:
        timer=0
        if random.random()<0.3:
            novo_quizz=Quizz(grupo_de_play,grupo_de_quizz)
        if random.random()<0.1:
            novo_ep1=Ep1(grupo_de_play,grupo_de_ep)
            novo_ep2=Ep2(grupo_de_play,grupo_de_ep)
        if random.random()<0.001:
            novo_pedro=Pedro(grupo_de_play,grupo_de_vida)
            novo_marcio=Marcio(grupo_de_play,grupo_de_vida)

    #Colisões:
    colisao_jogador_quizz=pygame.sprite.spritecollide(jogador,grupo_de_quizz,True,pygame.sprite.collide_mask)
    colisao_jogador_ep=pygame.sprite.spritecollide(jogador,grupo_de_ep,True,pygame.sprite.collide_mask)
    colisao_jogador_vida=pygame.sprite.spritecollide(jogador,grupo_de_vida,True,pygame.sprite.collide_mask)
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
        if jogador.vertical_state=='pulando':
            jogador.rect.y+=-2
            jogador.vel_y=+2

    #Draw:
    window.fill((4,71 ,13))
    grupo_de_plataforma.draw(window)
    grupo_de_play.draw(window)
    pygame.display.update()
pygame.quit()