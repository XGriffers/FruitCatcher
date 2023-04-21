import pygame
from game import FruitCatcherGame
from menu import MainMenu, PauseMenu

def main():
    pygame.init()

    # Set up display
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Fruit Catcher')

    main_menu = MainMenu(screen)
    pause_menu = PauseMenu(screen)
    game = FruitCatcherGame(screen)

    running = True
    while running:
        action = main_menu.show()
        if action == 'start':
            while True:
                game_over = game.play()
                if game_over:
                    pause_action = pause_menu.show()
                    if pause_action == 'quit':
                        break
                else:
                    break
        elif action == 'quit':
            running = False

    pygame.quit()

if __name__ == '__main__':
    main()
