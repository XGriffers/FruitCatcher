import pygame
import random
import sys

class FruitCatcherGame:
    def __init__(self, screen):
        self.screen = screen
        self.WIDTH, self.HEIGHT = screen.get_size()

    def play(self):
        # Load images
        background_image = pygame.image.load('background.jpg').convert()
        basket_image = pygame.image.load('basket.png').convert_alpha()
        fruit_image = pygame.image.load('fruit.png').convert_alpha()

        # Basket settings
        basket_width, basket_height = basket_image.get_size()
        basket_speed = 7
        basket = pygame.Rect(self.WIDTH // 2 - basket_width // 2, self.HEIGHT - basket_height - 10, basket_width, basket_height)

        # Fruit settings
        fruit_width, fruit_height = fruit_image.get_size()
        fruit_speed = 5
        fruits = []


        # Timer and score
        timer = pygame.time.Clock()
        score = 0

        # Main game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Move the basket
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and basket.x > 0:
                basket.x -= basket_speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d] and basket.x < self.WIDTH - basket_width:
                basket.x += basket_speed

            # Add new fruits
            if random.random() < 0.02:
                x = random.randint(0, self.WIDTH - fruit_width)
                fruits.append(pygame.Rect(x, 0, fruit_width, fruit_height))

            # Move fruits and check for collisions
            new_fruits = []
            for fruit in fruits:
                fruit.y += fruit_speed
                if fruit.colliderect(basket):
                    score += 1
                elif fruit.y < self.HEIGHT:
                    new_fruits.append(fruit)
            fruits = new_fruits

            # Draw game objects
            self.screen.blit(background_image, (0, 0))
            self.screen.blit(basket_image, basket)
            for fruit in fruits:
                self.screen.blit(fruit_image, fruit)

            # Draw score
            score_text = pygame.font.Font(None, 36).render(f'Score: {score}', True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))

            # Check for pause key press and fullscreen toggle
            keys = pygame.key.get_pressed()
            if keys[pygame.K_p] or keys[pygame.K_ESCAPE]:
                return True

            pygame.display.flip()
            timer.tick(60)
