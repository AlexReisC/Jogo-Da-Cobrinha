import pygame
from pygame.locals import *
from sys import exit
from random import randint

BRANC0 = (255, 255, 255)

pygame.init()
# definir o volume da musica de fundo
pygame.mixer.music.set_volume(0.5)
# definir a musica de fundo
musica_fundo = pygame.mixer.music.load('smw_course_clear.wav')
# colocar a musica em loop
pygame.mixer.music.play(-1)
# som emitido quando a cobra encostar na comida
colisao = pygame.mixer.Sound('smw_coin.wav')

largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# posição que a cobra vai iniciar
x_cobra = largura // 2
y_cobra = altura // 2

velocidade = 8
x_controle = velocidade
y_controle = 0

# posição que a comida vai surgir
x_comida = randint(20, 520)
y_comida = randint(20, 460)

font = pygame.font.SysFont("Arial", 35, True, False)

pontos = 0

lista_cobra = []
comprimento_inicial = 5


def desenha_lista(lista_cobra):
    for xey in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (xey[0], xey[1], 20, 20))


def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_comida, y_comida, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = largura//2
    y_cobra = largura//2
    lista_cobra = []
    lista_cabeca = []
    x_comida = randint(40, 600)
    y_comida = randint(30, 120)
    morreu = False


while True:
    clock.tick(40)
    tela.fill(BRANC0)
    mensagem = f"Pontos: {pontos}"
    texto_pontuacao = font.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = - velocidade
                    y_controle = 0

            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0

            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    '''if pygame.key.get_pressed()[K_a]:
        a = x_cobra - 20
    if pygame.key.get_pressed()[K_d]:
        d = x_cobra + 20
    if pygame.key.get_pressed()[K_s]:
        s = y_cobra - 20
    if pygame.key.get_pressed()[K_w]:
        w = y_cobra + 20'''
    x_cobra += x_controle
    y_cobra += y_controle

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    comida = pygame.draw.rect(tela, (255, 0, 0), (x_comida, y_comida, 20, 20))

    if cobra.colliderect(comida):
        pontos += 1
        x_comida = randint(40, 600)
        y_comida = randint(30, 420)
        colisao.play()
        comprimento_inicial += 1

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    tela.blit(texto_pontuacao, (450, 40))

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    if lista_cobra.count(lista_cabeca) > 1:
        font_Game_Over = pygame.font.SysFont("Arial", 20, True, True)
        mensagem_Game_Over = "Gamer Over! Pressione 'N' para jogar novamente."
        texto_Game_Over = font_Game_Over.render(mensagem_Game_Over, True, (0, 0, 0))
        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_n:
                        reiniciar_jogo()

            tela.blit(texto_Game_Over, (150, 150))
            pygame.display.update()

    desenha_lista(lista_cobra)
    tela.blit(texto_pontuacao, (450, 40))
    pygame.display.update()