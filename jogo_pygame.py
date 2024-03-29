import pygame
import random
import gc
from personagens_class import *
from arremessaveis_class import *
from plataforma_class import *
from easteregg_class import *
import sys

tudo=True
while tudo:
    #Iniciando o Game:
    pygame.init()
    pygame.mixer.init()
    LARGURA=1024
    ALTURA=600

    window=pygame.display.set_mode((LARGURA,ALTURA))
    pygame.display.set_caption('Dessoft Kong')

    #Objetos:
    pelicas=Pelicano()
    grupo_de_ee=pygame.sprite.Group()
    grupo_de_play=pygame.sprite.Group()
    grupo_de_ep=pygame.sprite.Group()
    grupo_de_quizz=pygame.sprite.Group()
    grupo_de_monitores=pygame.sprite.Group()
    grupo_de_plataforma=pygame.sprite.Group()
                            #ini  #fim #gap
    for pos_inicial in range (100,700,150):
        pos_x=random.randint(10,900)
        plat_movel=Plataforma(pos_x,pos_inicial)
        grupo_de_plataforma.add(plat_movel)

    #Itens relevantes:
    font = pygame.font.Font('img/itens/PressStart2P.ttf',24)
    fundo=pygame.image.load('img/telas/img_fundo.png')
    game=True
    selecao=True
    intro=True
    tutorial=True
    pre_jogo=True
    over = True
    jogo = True
    space_press=0
    timer=0
    clock=pygame.time.Clock()

    #Sounds
    vida = pygame.mixer.Sound('sons/Ganhando_vida.mp3')
    dano_ep = pygame.mixer.Sound('sons/maluco_doente.mp3')
    game_over = pygame.mixer.Sound('sons/game_over.mp3')
    hora_do_show = pygame.mixer.Sound('sons/hora_do_show.mp3')
    eita = pygame.mixer.Sound('sons/eita.mp3')
    vai_da_nao = pygame.mixer.Sound('sons/vai_da_nao.mp3')

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
    timer_init = pygame.time.Clock()
    tela_i=pygame.image.load(lista_img_ini[i])
    window.blit(tela_i,(0,0))
    pygame.display.update()

    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_SPACE:
                    intro=False
        clock.tick(60)
        tempo_entre_imagens += timer_init.tick()
        if tempo_entre_imagens > 300:
            tela_i=pygame.image.load(lista_img_ini[i])
            window.blit(tela_i,(0,0))
            pygame.display.update()
            i += 1
            tempo_entre_imagens = 0
            if i > 3:
                i = 0

    #Tela Tutorial:
    tempo_entre_img_tut = 0
    t = 0
    lista_img_tut=['img/telas/tut_1.png','img/telas/tut_2.png','img/telas/tut_3.png','img/telas/tut_4.png','img/telas/tut_5.png',
    'img/telas/tut_6.png','img/telas/tut_7.png','img/telas/tut_8.png','img/telas/tut_9.png','img/telas/tut_10.png','img/telas/tut_11.png',
    'img/telas/tut_12.png','img/telas/tut_13.png','img/telas/tut_14.png','img/telas/tut_15.png','img/telas/tut_16.png',
    'img/telas/tut_17.png']
    timer_tut = pygame.time.Clock()
    tela_i_tut=pygame.image.load(lista_img_tut[t])
    window.blit(tela_i_tut,(0,0))
    pygame.display.update()

    while tutorial:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_SPACE:
                    tutorial=False
        clock.tick(60)
        tempo_entre_img_tut += timer_tut.tick()
        bora =True
        if t == 6 or t == 9 or t == 12:
            if tempo_entre_img_tut > 3000:
                tela_i_tut=pygame.image.load(lista_img_tut[t])
                window.blit(tela_i_tut,(0,0))
                pygame.display.update()
                t += 1
                tempo_entre_img_tut = 0
                if t > 16:
                    t = 0

        else:
            if tempo_entre_img_tut > 500:
                tela_i_tut=pygame.image.load(lista_img_tut[t])
                window.blit(tela_i_tut,(0,0))
                pygame.display.update()
                t += 1
                tempo_entre_img_tut = 0
                if t == 17:
                    tutorial=False

    #Tela seleção de personagem:
    tempo_entre_img_sel = 0
    w = 0
    lista_img_selecao=['img/telas/sel_1.png','img/telas/sel_2.png','img/telas/sel_3.png','img/telas/sel_4.png','img/telas/sel_5.png',
    'img/telas/sel_6.png','img/telas/sel_7.png','img/telas/sel_8.png','img/telas/sel_9.png','img/telas/sel_10.png','img/telas/sel_11.png',
    'img/telas/sel_12.png']
    timer_sel = pygame.time.Clock()
    tela_i_sel=pygame.image.load(lista_img_selecao[w])
    window.blit(tela_i_sel,(0,0))
    pygame.display.update()

    while selecao:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_1:
                    jogador=Personagem_r()
                    grupo_de_play.add(jogador)
                    selecao=False
                if event.key==pygame.K_2:
                    jogador=Personagem_p()
                    grupo_de_play.add(jogador)
                    selecao=False
                if event.key==pygame.K_3:
                    jogador=Personagem_f()
                    grupo_de_play.add(jogador)
                    selecao=False
        clock.tick(60)
        tempo_entre_img_sel += timer_sel.tick()
        if tempo_entre_img_sel >500:
            tela_i_sel=pygame.image.load(lista_img_selecao[w])
            window.blit(tela_i_sel,(0,0))
            pygame.display.update()
            w += 1
            tempo_entre_img_sel = 0
            if w > 11:
                w = 0

    #Pré jogo:
    tempo_entre_img_pre = 0
    p = 0
    lista_img_pre=['img/telas/pre_1.png','img/telas/pre_2.png','img/telas/pre_3.png','img/telas/pre_4.png','img/telas/pre_5.png',
    'img/telas/pre_6.png','img/telas/img_fundo.png']
    timer_pre = pygame.time.Clock()
    tela_i_pre=pygame.image.load(lista_img_pre[p])
    window.blit(tela_i_pre,(0,0))
    pygame.display.update()

    while pre_jogo:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        clock.tick(60)
        tempo_entre_img_pre += timer_pre.tick()
        if tempo_entre_img_pre > 400:
            tela_i_pre=pygame.image.load(lista_img_pre[p])
            window.blit(tela_i_pre,(0,0))
            pygame.display.update()
            p += 1
            tempo_entre_img_pre = 0
            if p ==7:
                pre_jogo=False
        
    #Musica de Fundo
    pygame.mixer.music.load('sons/musica_de_fundo.mp3')
    pygame.mixer.music.play(-1)

    hora_do_show.play()

    #Loop principal:
    while game:
        clock.tick(60) 
        #Eventos:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    space_press+=1
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if space_press<=3:
                jogador.eventos_teclado(event)

        #Update Lógica:
        grupo_de_ee.update()
        grupo_de_play.update()
        grupo_de_plataforma.update()
        timer+=1
        if timer>20:
            timer=0
            if random.random()<0.2:
                novo_quizz=Quizz(grupo_de_play,grupo_de_quizz)
            if random.random()<0.08:
                novo_ep1=Ep1(grupo_de_play,grupo_de_ep)
                novo_ep2=Ep2(grupo_de_play,grupo_de_ep)
            if random.random()<0.01:
                novo_pedro=Pedro(grupo_de_play,grupo_de_monitores)
                novo_marcio=Marcio(grupo_de_play,grupo_de_monitores)
        #Colisões
        colisao_jogador_quizz=pygame.sprite.spritecollide(jogador,grupo_de_quizz,True,pygame.sprite.collide_mask)
        colisao_jogador_ep=pygame.sprite.spritecollide(jogador,grupo_de_ep,True,pygame.sprite.collide_mask)
        colisao_jogador_vida=pygame.sprite.spritecollide(jogador,grupo_de_monitores,True,pygame.sprite.collide_mask)
        colisao_jogador_mesa=pygame.sprite.spritecollide(jogador,grupo_de_plataforma,False)

        #Colisão plataforma móvel:
        if colisao_jogador_mesa:
            space_press=0
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
                    pontos+=20

        while len(grupo_de_plataforma)<4:
            larg=random.randrange(50,100)
            p=Plataforma(random.randrange(10,900-larg),random.randrange(-75,-30))
            grupo_de_plataforma.add(p)
        
        #Colisão quizz:
        if len(colisao_jogador_quizz)>0:
            jogador.obter_dano(100)
            eita.play()

            
        #Colisão eps:
        if len(colisao_jogador_ep)>0:
            jogador.obter_dano(300)
            dano_ep.play()

        #Colisão monitores:
        if len(colisao_jogador_vida)>0:
            jogador.obter_vida(200)
            vida.play()
        
        if jogador.porcentagem_vida >50:
            nao = True
        if jogador.porcentagem_vida <=50:
            if nao == True:
                vai_da_nao.play()
                nao = False

        #Easter egg    
        if pontos!=1000:
            isso=True
        if pontos==1000:
            if isso==True:
                pelicas=Pelicano()
                grupo_de_ee.add(pelicas)
                isso=False

        #Zerar pontos:
        if jogador.rect.bottom==590:
            pontos=0
            space_press=0

        #Personagem morre:
        if jogador.porcentagem_vida==0:
            pygame.mixer.music.stop()
            eita.stop()
            vida.stop()
            vai_da_nao.stop()
            dano_ep.stop()
            game_over.play()
            game=False
        
        #Fonte
        text = font.render(f'HP:{int(jogador.porcentagem_vida)}', True, (0,0,0))
        text_rect = (330,12)
        texto_pontos=exibir_pontuacao(pontos,24,(255, 255, 255))

        #Draw:
        window.blit(fundo,(0,0))
        grupo_de_plataforma.draw(window)
        grupo_de_play.draw(window)

        #Cor Barra de Vida
        if jogador.porcentagem_vida ==100 or jogador.porcentagem_vida == 90 or jogador.porcentagem_vida == 80:
            pygame.draw.rect(window, (31, 235, 12), (10,10,jogador.vida_atual/jogador.vida_ratio,25))
        if jogador.porcentagem_vida == 70 or jogador.porcentagem_vida == 60:
            pygame.draw.rect(window, (232, 218, 16), (10,10,jogador.vida_atual/jogador.vida_ratio,25))
        if jogador.porcentagem_vida == 50 or jogador.porcentagem_vida == 40 :
            pygame.draw.rect(window, (232, 132, 12), (10,10,jogador.vida_atual/jogador.vida_ratio,25))
        if jogador.porcentagem_vida == 30 or jogador.porcentagem_vida == 20 or jogador.porcentagem_vida == 10 or jogador.porcentagem_vida == 0:
            pygame.draw.rect(window, (255,0,0), (10,10,jogador.vida_atual/jogador.vida_ratio,25))
        pygame.draw.rect(window,(255,255,255),(10,10,jogador.comprimento_barra_vida,25),4)
        window.blit(texto_pontos,(780,68))
        window.blit(text,text_rect)
        grupo_de_ee.draw(window)
        pygame.display.update()

    #Tela de game over
    def exibir_pontuacao_final_tex(msg,tamanho,cor):
        fonte=pygame.font.Font('img/itens/PressStart2P.ttf',tamanho)
        mensagem='Final Score'
        texto_formatado=fonte.render(mensagem,True,cor)
        return texto_formatado
    def exibir_pontuacao_final_pont(msg,tamanho,cor):
        fonte=pygame.font.Font('img/itens/PressStart2P.ttf',tamanho)
        mensagem=f'{msg}'
        texto_formatado=fonte.render(mensagem,True,cor)
        return texto_formatado

    texto_pontos_final_tex=exibir_pontuacao_final_tex(pontos,20,(0, 0, 0))
    texto_pontos_final_pont=exibir_pontuacao_final_pont(pontos,45,(0,0,0))

    tempo_entre_img_fim = 0
    f = 0
    lista_img_fim=['img/telas/over_1.png','img/telas/over_2.png','img/telas/over_3.png','img/telas/over_4.png','img/telas/over_5.png',
    'img/telas/over_6.png']
    timer_fim = pygame.time.Clock()
    tela_i_fim=pygame.image.load(lista_img_fim[f])
    window.blit(tela_i_fim,(0,0))
    pygame.display.update()

    while over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_SPACE:
                    game=True
                    selecao=True
                    intro=True
                    tutorial=True
                    pre_jogo=True
                    over = False
                    gc.collect()
                    tudo = True
        clock.tick(60)
        tempo_entre_img_fim += timer_fim.tick()
        if tempo_entre_img_fim > 300:
            tela_i_fim=pygame.image.load(lista_img_fim[f])
            window.blit(tela_i_fim,(0,0))
            window.blit(texto_pontos_final_tex,(775,220))
            window.blit(texto_pontos_final_pont,(820,265))
            pygame.display.update()
            f += 1
            tempo_entre_img_fim = 0
            if f > 5:
                f = 0
pygame.quit()