import pygame
import sys

class MainMenu:
    def __init__(self, screen):
        self.screen = screen

    def show(self):
        while True:
            self.screen.fill((0, 0, 0))
            self._draw_text('Press SPACE to start', 36, (255, 255, 255), 250, 300)
            self._draw_text('Press ESC to quit', 36, (255, 255, 255), 275, 350)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return 'start'
                    elif event.key == pygame.K_ESCAPE:
                        return 'quit'

    def _draw_text(self, text, font_size, color, x, y):
        font = pygame.font.Font(None, font_size)
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_obj, text_rect)



class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.WIDTH, self.HEIGHT = screen.get_size()
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()

    def show(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return "quit"

            # Draw pause menu
            self._draw_text('PAUSED', 48, (255, 255, 255), self.WIDTH // 2, self.HEIGHT // 2 - 100)
            self._draw_text('Press ESC to quit', 36, (255, 255, 255), self.WIDTH // 2, self.HEIGHT // 2)

            pygame.display.flip()
            self.clock.tick(60)

    def _draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)


