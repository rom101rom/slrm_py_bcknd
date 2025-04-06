import pygame



class Player():
    def __init__(self):
        self.playerImg = pygame.image.load('assets/player.png')
        self.playerX = 370
        self.playerY = 480
        self.playerX_change_val = 0
        

    def playerX_change(self, val):
        self.playerX_change_val += val