import pygame
import sys

import settings
from level import Level


class Game:
    def __init__(self):

        # General Setup
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption('I Merely Spy')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        # Event Loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill("black")
            self.level.run()
            pygame.display.update()
            self.clock.tick(settings.FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
