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
pygame.display.set_caption('Dessoft Kong')

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
font = pygame.font.Font('img/itens/PressStart2P.ttf',24)
game=True
timer=0
clock=pygame.time.Clock()

#Placar de pontos:
pontos=0
def exibir_pontuacao(msg,tamanho,cor):
    fonte=pygame.font.Font('img/itens/PressStart2P.ttf',tamanho)
    mensagem=f'Score:{msg}'
    texto_formatado=fonte.render(mensagem,True,cor)
    return texto_formatado

#Tela inicial:
tempo_entre_imagens = 0
i = 0
lista_img_ini=['img/telas/tela_ini1.png','img/telas/tela_ini2.png','img/telas/tela_ini3.png','img/telas/tela_ini4.png']
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

#print(pygame.font.get_fonts())
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
        if random.random()<0.01:
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
            jogador.vel_x=2
            jogador.rect.x+=plat_movel.vel_x
        if abs(jogador.rect.right-plat_movel.rect.left)<tolerancia_colisao:
            jogador.vel_x=0
            jogador.rect.right=plat_movel.rect.left

    #Movimento do cenário:
    if jogador.rect.top<=ALTURA/2.5:
        jogador.rect.y+=abs(jogador.vel_y)
        for plat in grupo_de_plataforma:
            plat.rect.y+=abs(jogador.vel_y)
            if plat.rect.top>=ALTURA:
                plat.kill()
                pontos+=10

    while len(grupo_de_plataforma)<4:
        larg=random.randrange(50,100)
        p=Plataforma(random.randrange(10,900-larg),random.randrange(-75,-30))
        grupo_de_plataforma.add(p)
    
    #Colisão quizz:
    if len(colisao_jogador_quizz)>0:
        jogador.obter_dano(100)

    #Colisão eps:
    if len(colisao_jogador_ep)>0:
        jogador.obter_dano(300)

    #Colisão monitores:
    if len(colisao_jogador_vida)>0:
        jogador.obter_vida(200)
    
    #Zerar pontos:
    if jogador.rect.bottom==590:
        pontos=0
    #Fonte
    text = font.render(f'LP:{int(jogador.porcentagem_vida)}', True, (255,255,255))
    text_rect = (20,40)
    texto_pontos=exibir_pontuacao(pontos,24,(240, 159, 10))

    #Draw:
    window.fill((4,71 ,13))
    grupo_de_plataforma.draw(window)
    grupo_de_play.draw(window)
    pygame.draw.rect(window, (255,0,0), (10,10,jogador.vida_atual/jogador.vida_ratio,25))
    pygame.draw.rect(window,(255,255,255),(10,10,jogador.comprimento_barra_vida,25),4)
    window.blit(texto_pontos,(780,10))
    window.blit(text,text_rect)
    pygame.display.update()
pygame.quit()