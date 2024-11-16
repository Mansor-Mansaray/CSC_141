# made a sideways shooting pygame using if and elif statments
# to move the ship and using define fuctions to make and shoot bullets.

import sys

import pygame

class Ship:


    def __init__(self, game):
        
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()


        self.image = pygame.image.load('fighter_rocket_bit.png')
        self.rect = self.image.get_rect()

      
        self.rect.midleft = self.screen_rect.midleft

      
        self.y = float(self.rect.y)

     
        self.moving_up = False
        self.moving_down = False

    def update(self):
      
        if self.moving_up and self.rect.top > 0:
            self.y -= 1.5
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1.5

        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Bullet(pygame.sprite.Sprite):

    def __init__(self, game):
 
        super().__init__()
        self.screen = game.screen
        self.color = (60, 60, 60)
        self.speed = 1.5

        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = game.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):

        self.x += self.speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class SidewaysShooter:


    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Sideways Shooter")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
     
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _check_events(self):
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
   
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill((230, 230, 230))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

if __name__ == '__main__':
  
    game = SidewaysShooter()
    game.run_game()
