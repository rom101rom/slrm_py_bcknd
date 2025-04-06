import pygame, game

game = game.Game()


over = False


playerX_change_val = 0

while not over:
    game.screen.fill((0, 0, 0))
    game.screen.blit(game.background, (0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            over = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                playerX_change_val = -5
                game.playerX_change(playerX_change_val)
            if e.key == pygame.K_RIGHT:
                playerX_change_val = 5
                game.playerX_change(playerX_change_val)
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                playerX_change_val = 0
                game.playerX_change(playerX_change_val)

    game.playerX(playerX_change_val)
    game.player()
    pygame.display.update()
