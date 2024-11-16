# Used the code for this section to put in a video game character of
# my choice while changing the background color.

import sys

import pygame

class Spawn:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Spawn Redemption")
        self.bg_color = (55, 206, 35)

        self.image = pygame.image.load('spawn_bit.png')
        self.image_rect = self.image.get_rect()  
        self.image_rect.center = self.screen.get_rect().center 

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.screen.blit(self.image, self.image_rect)
            pygame.display.flip()

if __name__ == '__main__':
    ai = Spawn()
    ai.run_game()