import pygame
from guy import Guy
from lixo2 import Lixo2
from redGuy import RedGuy
from redGuy2 import RedGuy2
from lixo import Lixo
import random


####

pygame.init()
WIDTH = 940
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#titulo = pygame.image.load("Imagens/fundomenu.png")
jogarp = pygame.image.load("data/Imagens/jogarmarrom.png")
jogarb = pygame.image.load("data/Imagens/jogarbranco.png")
sairp = pygame.image.load("data/Imagens/SAIRp.png")
sairb = pygame.image.load("data/Imagens/SAIRb.png")
fundo = pygame.image.load("data/Imagens/fundomenu2.png")
creditob = pygame.image.load('data/Imagens/credito.png')
creditop = pygame.image.load('data/Imagens/creditop.png')
voltarb = pygame.image.load('data/Imagens/voltarbranco.png')
voltarp = pygame.image.load('data/Imagens/voltapequeno.png')
menub = pygame.image.load('data/Imagens/menub.png')
menup = pygame.image.load('data/Imagens/menup.png')

gameover = pygame.image.load('data/Imagens/testegame2.png')

porqueimagem = pygame.image.load('data/Imagens/porqueteste.png')
creditofundo = pygame.image.load('data/Imagens/teste.png')
umaEstrela = pygame.image.load('data/Imagens/1estrela.png')
duasEstrelas = pygame.image.load('data/Imagens/2estrela.png')
tresEstrelas = pygame.image.load('data/Imagens/3estrela.png')


def Jogo():
    largura = 940
    altura = 600
    fundojogo = pygame.image.load('data/Imagens/cidade2.jpg')
    # fundojogo = pygame.transform.scale(fundojogo, [940, 600])

    # Object Grupo
    objectGroup = pygame.sprite.Group()
    redguy2Group = pygame.sprite.Group()
    redguyGroup = pygame.sprite.Group()
    lixoGroup = pygame.sprite.Group()
    shootGroup = pygame.sprite.Group()
    lixoGroup2 = pygame.sprite.Group()

    guy = Guy(objectGroup)
    
    #som = pygame.image.load('data/Imagens/som.png')
    #somp = pygame.image.load('data/Imagens/somp.png')


    # Timer
    timer_relogio = 0
    tempo_segundo = 0

    font = pygame.font.SysFont('Arial Black', 50)
    texto = font.render(':', True, (255, 255, 255))
    pos_texto = texto.get_rect()
    pos_texto.center = (120, 67)

    pos_relogio = (10, 10)

    # Pontos
    pontos = 0
    tamanho = pygame.font.SysFont('Arial Black', 50)
    text = tamanho.render('Pontuação: ' + str(pontos), True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (460, 20)

    # Jogo
    display = pygame.display.set_mode([largura, altura])
    pygame.display.set_caption('Collectors')

    # Music
    pygame.mixer.music.load('data/MusicSons/jogomusica.ogg')
    pygame.mixer.music.play(-1)

    # Sounds
    # shoot = pygame.mixer.Sound('MusicSons/8bit_gunloop_explosion.wav')
    colid = pygame.mixer.Sound('data/MusicSons/game-over2.wav')
    coletou = pygame.mixer.Sound('data/MusicSons/appear-online.ogg')

    # Teclas
    sair = True
    clock = pygame.time.Clock()
    timer = 20
    number = 10

    if __name__ == "__main__":
        while sair:
            clock.tick(20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False

                    # elif event.type == pygame.KEYDOWN:
                    #    if event.key == pygame.K_SPACE:
                    #        shoot.play()

            if (timer_relogio < 25):
                timer_relogio += 1

            else:
                tempo_segundo += 1
                texto = font.render(':' + str(tempo_segundo), True, (255, 255, 255))
                timer_relogio = 0

            # Update
            objectGroup.update()

            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    RedGuy(objectGroup, redguyGroup)
                    print('New Inimigo!')

            timer += 1
            if pontos > 3:
                if timer > 30:
                    timer = 0
                    if random.random() < 0.4:
                        RedGuy2(objectGroup, redguy2Group)
                        print('New Inimigo 2!')

            collision = pygame.sprite.spritecollide(guy, redguyGroup, False, pygame.sprite.collide_mask)

            collision2 = pygame.sprite.spritecollide(guy, redguy2Group, False, pygame.sprite.collide_mask)

            if collision2:
                print('Game OVER!')
                sair = False
                colid.play()
                gameOver(pontos, tempo_segundo, 940, 600)

            if collision:
                print('Game OVER!')
                sair = False
                colid.play()
                gameOver(pontos, tempo_segundo, 940, 600)


            timer += 1
            if timer > 30:
                if random.random() < 0.2:
                    newLixo = Lixo(objectGroup, lixoGroup)
                    print('New Lixo!')

            colect = pygame.sprite.spritecollide(guy, lixoGroup, True, pygame.sprite.collide_mask)

            if colect:
                print('Coletou')
                pontos = pontos + 2
                text = tamanho.render('Pontuação: ' + str(pontos), True, (255, 255, 255))
                coletou.play()

            if timer > 30:
                if random.random() < 0.2:
                    newLixo2 = Lixo2(objectGroup, lixoGroup2)
                    print('New Lixo!')

            colect2 = pygame.sprite.spritecollide(guy, lixoGroup2, True, pygame.sprite.collide_mask)

            if colect2:
                print('Coletou')
                pontos = pontos + 1
                text = tamanho.render('Pontuação: ' + str(pontos), True, (255, 255, 255))
                coletou.play()

            # if sair == False:
            # Draw



            relogioimg = pygame.image.load('data/Imagens/relogio3.png')
            display.blit(fundojogo, (0, 0))  # Background
            display.blit(texto, pos_texto)
            display.blit(relogioimg, pos_relogio)
           #screen.blit(som, (870, 15))
            display.blit(text, textRect)
            objectGroup.draw(display)
            pygame.display.update()

            '''while pygame.event.wait() or pygame.event.get():

                mouse = pygame.mouse.get_pos()
                if 870 + 50 > mouse[0] > 870 and 15 + 50 > mouse[1] > 15:
                    screen.blit(som, (870, 15))
                    if pygame.mouse.get_pressed()[0]:
                        pygame.mixer.music.load('data/MusicSons/sons/musica de fundo/Find Your Way Beat - Nana Kwabena.mp3')
                        pygame.mixer.music.play(-1)

                else:
                    screen.blit(somp,(870, 15))
                    pygame.mixer.load()
                    if 870 + 50 > mouse[0] > 870 and 15 + 50 > mouse[1] > 15:
                       screen.blit(somp, (870, 15))
                    if pygame.mouse.get_pressed()[0]:
                        pygame.mixer.music.load('data/MusicSons/sons/musica de fundo/Find Your Way Beat - Nana Kwabena.mp3')
                        pygame.mixer.music.play(-1)
'''

def porque():
    pygame.mixer.music.load('data/MusicSons/menumusica.ogg')
    pygame.mixer.music.play(-1)
    screen.fill((0,0,0))
    screen.blit(porqueimagem, (0,0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    screen.blit(jogarp, (150, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    screen.blit(sairp, (500, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 150 + 308 > mouse[0] > 150 and 500 + 112 > mouse[1] > 500:
            screen.blit(jogarb, (150, 500))
            if pygame.mouse.get_pressed()[0]:
                Jogo()


        else:
            screen.blit(jogarp, (150, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if 500 + 215 > mouse[0] > 500 and 500 + 83 > mouse[1] > 500:
            screen.blit(sairb, (500, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()

        else:
            screen.blit(sairp, (500, 500))

        pygame.display.flip()


def credito():
    pygame.mixer.music.load('data/MusicSons/menumusica.ogg')
    pygame.mixer.music.play(-1)
    screen.fill((0,0,0))
    screen.blit(creditofundo, (0, 0))
    screen.blit(voltarp, (130, 400))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 130 + 147 > mouse[0] > 130 and 400 + 148 > mouse[1] > 400:
            screen.blit(voltarb, (130, 400))
            if pygame.mouse.get_pressed()[0]:
                screen.fill((0, 0, 0))
                menu()


        else:
            screen.blit(voltarp, (130, 400))

        pygame.display.flip()


def gameOver(pontos, tempo_segundo, largura, altura):
    global timer
    pygame.display.set_mode((940, 600))  # Define o tamanho da janela
    pygame.display.set_caption('Collectors')
    pygame.mixer.music.load('data/MusicSons/8.mp3')
    pygame.mixer.music.play(-1)
    gameover2 = True
    while gameover2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        screen.fill((0, 0, 0)) # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
        screen.blit(gameover, (0, 0))  # plano de fundo da tela game over
        screen.blit(jogarp, (605, 200))
        screen.blit(sairp, (605, 450))
        screen.blit(menup, (605, 325))


        if 10 > pontos >= 0:
            screen.blit(umaEstrela, (80, 30))

            tamanho = pygame.font.SysFont('Arial Black', 30)
            text = tamanho.render(str(pontos) + ' Ponto(s) ', True, (196, 121, 8))
            textRect = text.get_rect()
            textRect.center = (290, 253)
            screen.blit(text, textRect)

            font = pygame.font.SysFont('Arial Black', 30)
            texto = font.render(str(tempo_segundo) + 's', True, (196, 121, 8))
            pos_texto = texto.get_rect()
            pos_texto.center = (280,357)
            screen.blit(texto, pos_texto)


        elif 20 >= pontos >= 10 :
            screen.blit(duasEstrelas, (80, 35))

            tamanho = pygame.font.SysFont('Arial Black', 30)
            text = tamanho.render(str(pontos) + ' Ponto(s) ', True, (196, 121, 8))
            textRect = text.get_rect()
            textRect.center = (290, 253)
            screen.blit(text, textRect)

            font = pygame.font.SysFont('Arial Black', 30)
            texto = font.render(str(tempo_segundo) + 's', True, (196, 121, 8))
            pos_texto = texto.get_rect()
            pos_texto.center = (300, 357)
            screen.blit(texto, pos_texto)

        elif pontos >= 21:
            screen.blit(tresEstrelas, (80, 35))

            tamanho = pygame.font.SysFont('Arial Black', 30)
            text = tamanho.render(str(pontos) + ' Ponto(s) ', True, (196, 121, 8))
            textRect = text.get_rect()
            textRect.center = (290, 270)
            screen.blit(text, textRect)

            font = pygame.font.SysFont('Arial Black', 30)
            texto = font.render(str(tempo_segundo) + 's', True, (196, 121, 8))
            pos_texto = texto.get_rect()
            pos_texto.center = (300, 375)
            screen.blit(texto, pos_texto)

        pygame.display.update()

        while pygame.event.wait() or pygame.event.get():

            mouse = pygame.mouse.get_pos()
            if 605 + 308 > mouse[0] > 605 and 200 + 112 > mouse[1] > 200:
                screen.blit(jogarb, (605, 200))
                if pygame.mouse.get_pressed()[0]:
                    Jogo()

            else:
                screen.blit(jogarp, (605, 200))

            if 605 + 215 > mouse[0] > 605 and 450 + 83 > mouse[1] > 450:
                screen.blit(sairb, (605, 450))
                if pygame.mouse.get_pressed()[0]:
                    quit()

            else:
                screen.blit(sairp, (605, 450))

            if 605 + 215 > mouse[0] > 605 and 325 + 83 > mouse[1] > 325:
                screen.blit(menub, (605, 325))
                if pygame.mouse.get_pressed()[0]:
                    menu()

            else:
                screen.blit(menup, (605, 325))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.flip()





def menu():
    pygame.mixer.music.load('data/MusicSons/menumusica.ogg')
    pygame.mixer.music.play(-1)
    screen.blit(fundo, (0, 0))
    #screen.blit(titulo, (WIDTH / 4, 50))
    screen.blit(jogarp, (60, 200))
    #screen.blit(jogarb,(WIDTH /3,600))
    screen.blit(sairp, (600, 650))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 60 + 308 > mouse[0] > 60 and 200 + 112 > mouse[1] > 200:
            screen.blit(jogarb, (60, 200))
            if pygame.mouse.get_pressed()[0]:
                porque()


        else:
            screen.blit(jogarp, (60, 200))

        if 60 + 215 > mouse[0] > 60 and 325 + 83 > mouse[1] > 325:
            screen.blit(creditob, (60, 325))
            if pygame.mouse.get_pressed()[0]:
                screen.fill((0,0,0))
                credito()
        else:
            screen.blit(creditop, (60, 325))


        if 60 + 215 > mouse[0] > 60 and 450 + 83 > mouse[1] > 450:
            screen.blit(sairb, (60, 450))
            if pygame.mouse.get_pressed()[0]:
                quit()

        else:
            screen.blit(sairp, (60, 450))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()


menu()
quit()