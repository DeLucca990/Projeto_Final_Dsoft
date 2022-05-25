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
grupo_de_monitores=pygame.sprite.Group()
grupo_de_plataforma=pygame.sprite.Group()
                         #ini  #fim #gap
for pos_inicial in range (100,600,150):
    pos_x=random.randint(10,900)
    plat_movel=Plataforma(pos_x,pos_inicial)
    grupo_de_plataforma.add(plat_movel)

jogador=Personagem()
grupo_de_play.add(jogador)

#Itens relevantes: 
vidas=5
game=True
timer=0
clock=pygame.time.Clock()

#Tela inicial:
tempo_entre_imagens = 0
i = 0
lista_img_ini=['img/tela_ini1.png','img/tela_ini2.png','img/tela_ini3.png','img/tela_ini4.png']
clock=pygame.time.Clock()
timer_init = pygame.time.Clock()
intro=True

tela_i=pygame.image.load(lista_img_ini[0])
window.blit(tela_i,(0,0))
pygame.display.update()

while intro:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            intro=False
            game=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                intro=False
    clock.tick(60)
    tempo_entre_imagens += timer_init.tick()
    if tempo_entre_imagens > 250:
        tela_i=pygame.image.load(lista_img_ini[i])
        window.blit(tela_i,(0,0))
        pygame.display.update()
        i += 1
        tempo_entre_imagens = 0
        if i > 3:
            i = 0

#Loop principal:
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
        if random.random()<0.2:
            novo_quizz=Quizz(grupo_de_play,grupo_de_quizz)
        if random.random()<0.05:
            novo_ep1=Ep1(grupo_de_play,grupo_de_ep)
            novo_ep2=Ep2(grupo_de_play,grupo_de_ep)
        if random.random()<0.001:
            novo_pedro=Pedro(grupo_de_play,grupo_de_monitores)
            novo_marcio=Marcio(grupo_de_play,grupo_de_monitores)

    #Colisões:
    colisao_jogador_quizz=pygame.sprite.spritecollide(jogador,grupo_de_quizz,True,pygame.sprite.collide_mask)
    colisao_jogador_ep=pygame.sprite.spritecollide(jogador,grupo_de_ep,True,pygame.sprite.collide_mask)
    colisao_jogador_vida=pygame.sprite.spritecollide(jogador,grupo_de_monitores,True,pygame.sprite.collide_mask)
    colisao_jogador_mesa=pygame.sprite.spritecollide(jogador,grupo_de_plataforma,False)
    #Colisão plataforma móvel:
    tolerancia_colisao=10
    for plat_movel in colisao_jogador_mesa:
        if abs(jogador.rect.left - plat_movel.rect.right)<tolerancia_colisao:
            jogador.vel_x=0
            jogador.rect.left=plat_movel.rect.right
        if abs(jogador.rect.top - plat_movel.rect.bottom)<tolerancia_colisao:
            jogador.vel_y=1
        if abs(jogador.rect.bottom-plat_movel.rect.top)<tolerancia_colisao:
            jogador.rect.y-=2
            jogador.vel_y=2
            jogador.vel_x=1
            jogador.rect.x+=plat_movel.vel_x
        if abs(jogador.rect.right-plat_movel.rect.left)<tolerancia_colisao:
            jogador.vel_x=0
            jogador.rect.right=plat_movel.rect.left
    #Colisão quizz:
    if len(colisao_jogador_quizz)>0:
        vidas-=1

    #Colisão eps:
    if len(colisao_jogador_ep)>0:
        vidas-=2

    #Colisão monitores:
    if len(colisao_jogador_vida)>0:
        vidas+=1

    #Draw:
    window.fill((4,71 ,13))
    grupo_de_plataforma.draw(window)
    grupo_de_play.draw(window)
    pygame.display.update()
pygame.quit()