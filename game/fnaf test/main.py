import pygame
import random
import sys

pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Five Nights at Freddy's")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Animatronic class
class Animatronic(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = random.randint(1, 3)

    def move(self):
        self.rect.x += self.speed

        if self.rect.left > WIDTH:
            self.rect.right = 0

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Game initialization
all_sprites = pygame.sprite.Group()

# Create animatronics
animatronics = pygame.sprite.Group()
for _ in range(3):
    animatronic = Animatronic(RED, random.randint(0, WIDTH), random.randint(0, HEIGHT), 50, 50)
    animatronics.add(animatronic)
    all_sprites.add(animatronic)

# Create player
player = Player(WHITE, WIDTH // 2, HEIGHT - 50, 50, 50)
all_sprites.add(player)

# Main game loop
clock = pygame.time.Clock()
power = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.rect.left > 0:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT] and player.rect.right < WIDTH:
        player.rect.x += 5

    # Animatronics movement
    animatronics.update()

    # Check collisions with player
    if pygame.sprite.spritecollide(player, animatronics, False):
        power -= 1

    # Player actions
    if keys[pygame.K_c]:
        print("You checked the cameras.")
        # Implement camera checking logic here
    elif keys[pygame.K_d]:
        print("You closed the door.")
        # Implement door closing logic here
    elif keys[pygame.K_p]:
        print("You conserved power.")
        # Implement power conservation logic here

    # Draw background
    screen.fill(WHITE)

    # Draw sprites
    all_sprites.draw(screen)

    # Display power
    font = pygame.font.Font(None, 36)
    power_text = font.render(f"Power: {power}", True, RED)
    screen.blit(power_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

    # Check for game over condition
    if power <= 0:
        print("Game over. The animatronics got you!")
        pygame.quit()
        sys.exit()
