import pygame, player

pygame.init()

player = player.Player()

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load('assets/background.png')
        self.caption = pygame.display.set_caption("Space Invader")
        self.icon = pygame.image.load('assets/ufo.png')
        self.icon = pygame.display.set_icon(self.icon)

    def player(self):
        self.screen.blit(player.playerImg, (player.playerX, player.playerY))
    
    def playerX_change(self, val):
        player.playerX_change(val)


    def playerX(self, val_x):
        player.playerX += val_x
        if player.playerX <= 0:
            player.playerX = 0
        elif player.playerX >=736:
            player.playerX = 736


        



