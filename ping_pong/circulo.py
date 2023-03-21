import pygame

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
RAIO = 10

pygame.init()

tela = pygame.display.set_mode((640, 480), 0)
x = 10
velocidade_x = 0.4

y = 10
velocidade_y = 0.8

while True:
    x += velocidade_x
    y += velocidade_y

    if x + RAIO > 640:
        velocidade_x = -0.4
    if x - RAIO < 0:
        velocidade_x = 0.4
    if y + RAIO > 480:
        velocidade_y = -0.8
    if y - RAIO < 0:
        velocidade_y = 0.8

    tela.fill(PRETO)

    pygame.draw.circle(tela, AMARELO, (int(x), int(y)), RAIO, 0)

    pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()