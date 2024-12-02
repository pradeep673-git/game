import pygame
from setting import Settings

class Enemy:
    def __init__(self, game):

        self.settings = Settings()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load(r"C:\Users\HAI\OneDrive\Pictures\Saved Pictures\enemy_ship2.bmp")
        self.image_rect = self.image.get_rect()

        self.image_rect.midtop = self.screen_rect.midtop



    def draw_ship(self):
        self.screen.blit(self.image, self.image_rect)
    
