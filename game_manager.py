import sys
import pygame
from settings import Settings


class GameManager:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Game")
        self.bg_color = self.settings.bg_color

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


if __name__ == '__main__':
    gm = GameManager()
    gm.run_game()
