import pygame
from pygame.locals import *
#from ping_pong.circulo import velocidade_x

branco = (255, 255, 255)
preto = (0, 0, 0)
largura = 720
altura = 480
raio = 10

pygame.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

borda_esq_x = 0
borda_esq_y = altura
borda_di_x = largura
borda_di_y = altura

x_bola = largura // 2
y_bola = altura // 2
velocidade_x = 0.6
velocidade_y = 0.8

x_raquete1 = 0
y_raquete1 = altura // 3
r1_velocidade_y = 0.5

x_raquete2 = largura - 10
y_raquete2 = altura // 3
velo_r = 0.5

font = pygame.font.SysFont("Arial", 20, True, False)
gols1 = 0
gols2 = 0


while True:
    clock.tick()
    tela.fill(branco)
    nome_jog = f"Jogador 1 vs Jogador 2"
    placar = f"{gols1} x {gols2} "
    texto_placar = font.render(placar, True, (0, 0, 0))
    texto_nome = font.render(nome_jog, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    #movendo a raquete 2
    if pygame.key.get_pressed()[K_s]:
        y_raquete1 += velo_r
    if pygame.key.get_pressed()[K_w]:
        y_raquete1 -= velo_r

    if y_raquete2 + (y_raquete2/2) > altura:
        y_raquete2 -= velo_r
    if y_raquete2 < 0:
        y_raquete2 += velo_r

    #movendo a raquete 1
    if pygame.key.get_pressed()[K_UP]:
        y_raquete2 -= velo_r
    if pygame.key.get_pressed()[K_DOWN]:
        y_raquete2 += velo_r

    if y_raquete1 + (y_raquete1/2) > altura:
        y_raquete1 -= velo_r
    if y_raquete1 < 0:
        y_raquete1 += velo_r


    #movendo a bola
    x_bola += velocidade_x
    y_bola += velocidade_y
    if x_bola + raio > largura:
        gols1 += 1
        x_bola = largura//2
    if x_bola - raio < 0:
        gols2 += 1
        x_bola = largura//2
    if y_bola + raio > altura:
        velocidade_y = -0.8
    if y_bola - raio < 0:
        velocidade_y = 0.8



    bola = pygame.draw.circle(tela, preto, (x_bola, y_bola), raio, 0)
    raquete1 = pygame.draw.rect(tela, preto, (x_raquete1, y_raquete1, 10, 100))
    raquete2 = pygame.draw.rect(tela, preto, (x_raquete2, y_raquete2, 10, 100))

    if bola.colliderect(raquete2):
        velocidade_x = -0.6
    if bola.colliderect(raquete1):
        velocidade_x = 0.6


    tela.blit(texto_nome, (250, 10))
    tela.blit(texto_placar,(340, 35))
    pygame.display.update()

