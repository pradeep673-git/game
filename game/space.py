
import pygame
import sys
from setting import Settings
from ship import Ship
from bullet import Bullet
from enemy import Enemy   

class AlienInvasion:
    def __init__(self):

        self.settings = Settings()

        pygame.init()
        pygame.display.set_caption("My Alien Invasion")
        self.screen = pygame.display.set_mode(self.settings.window_size)

        self.ship = Ship(self)

        self.bullet = pygame.sprite.Group()

        self.enemy = Enemy(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                print(self.ship.image_rect.right)
                print(self.ship.screen_rect.right)
                if(event.key == pygame.K_LEFT and self.ship.image_rect.left > 20):
                   self.ship.move_left = True 
                if(event.key == pygame.K_RIGHT and self.ship.image_rect.right < 880):
                   self.ship.move_right = True 
                if event.key == pygame.K_SPACE :
                    self.fire_bullet()
  
    def fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullet.add(new_bullet)

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.draw_ship()
        self.ship.move_ship()
        self.enemy.draw_ship()
        self.bullet.update()
        pygame.display.flip()
        for Bullet in self.bullet.sprites():
            Bullet.draw_bullet()
        pygame.display.flip()

    def run_game(self):
        while True:
            self.check_events();
            self.update_screen();
            for bullet in self.bullet.copy():
                if bullet.bullet_rect.bottom <=0:
                    self.bullet.remove(bullet)
            
            if self.enemy.image_rect.bottom == self.bullet.bullet_rect.top:
                self.enemy.remove(Enemy)
            self.update_screen()

game = AlienInvasion()
game.run_game()
