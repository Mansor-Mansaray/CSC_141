"I used this code to make a game where you can move a rocket around with the arrow keys"

import sys

import pygame

class Rocket:

    
    def __init__(self):

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Up Up & Away")
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.image.load('rocket_bit.png')  
        self.rect = self.image.get_rect()
        
       
        self.rect.center = self.screen_rect.center
        
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1

    def blitme(self):

        self.screen.blit(self.image, self.rect)


def run_game():
    pygame.init()
    rocket = Rocket()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rocket.moving_right = True
                elif event.key == pygame.K_LEFT:
                    rocket.moving_left = True
                elif event.key == pygame.K_UP:
                    rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    rocket.moving_right = False
                elif event.key == pygame.K_LEFT:
                    rocket.moving_left = False
                elif event.key == pygame.K_UP:
                    rocket.moving_up = False
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = False

        rocket.update()
        rocket.screen.fill((230, 230, 230))
        rocket.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    run_game()
