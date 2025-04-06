import pygame


pygame.init()

over = False
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('assets/background.png')


caption = pygame.display.set_caption("Space Invader")
icon = pygame.image.load('assets/ufo.png')
icon = pygame.display.set_icon(icon)




playerImg = pygame.image.load('assets/player.png')
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))

while not over:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            over = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                playerX_change = -5
            if e.key == pygame.K_RIGHT:
                playerX_change = 5
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                playerX_change = 0
    
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    player(playerX, playerY)
    
    pygame.display.update()