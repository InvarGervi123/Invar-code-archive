import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
LIGHT_GRAY = (200, 200, 200)
CYAN = (0, 255, 255)
DARK_CYAN = (0, 150, 150)
BLACK = (0, 0, 0)

# Параметры здоровья
MAX_HEALTH = 100
HEALTH_BAR_WIDTH = 300
HEALTH_BAR_HEIGHT = 30
HEALTH_BAR_SEGMENTS = 10
SEGMENT_GAP = 5
BORDER_WIDTH = 2

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Health Bar Example")
clock = pygame.time.Clock()

# Здоровье игрока
health = MAX_HEALTH

# Функция для отрисовки полосы здоровья в стиле Assassin's Creed
def draw_health_bar(surface, x, y, health):
    segment_width = (HEALTH_BAR_WIDTH - (HEALTH_BAR_SEGMENTS - 1) * SEGMENT_GAP) / HEALTH_BAR_SEGMENTS
    current_segments = int((health / MAX_HEALTH) * HEALTH_BAR_SEGMENTS)

    # Рисуем фон полосы
    pygame.draw.rect(surface, GRAY, (x, y, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))

    # Рисуем декоративную подложку
    pygame.draw.rect(surface, DARK_CYAN, (x - BORDER_WIDTH, y - BORDER_WIDTH, 
                                          HEALTH_BAR_WIDTH + BORDER_WIDTH * 2, HEALTH_BAR_HEIGHT + BORDER_WIDTH * 2), 
                     border_radius=10)

    # Рисуем сегменты здоровья с эффектом свечения
    for i in range(HEALTH_BAR_SEGMENTS):
        segment_x = x + i * (segment_width + SEGMENT_GAP)
        if i < current_segments:
            pygame.draw.rect(surface, CYAN, (segment_x, y, segment_width, HEALTH_BAR_HEIGHT), border_radius=5)
            pygame.draw.rect(surface, LIGHT_GRAY, (segment_x + 2, y + 2, segment_width - 4, HEALTH_BAR_HEIGHT - 4), 
                             border_radius=5)
        else:
            pygame.draw.rect(surface, GRAY, (segment_x, y, segment_width, HEALTH_BAR_HEIGHT), border_radius=5)

    # Рисуем рамку для всей полосы
    pygame.draw.rect(surface, BLACK, (x - BORDER_WIDTH, y - BORDER_WIDTH, 
                                      HEALTH_BAR_WIDTH + BORDER_WIDTH * 2, HEALTH_BAR_HEIGHT + BORDER_WIDTH * 2), 
                     BORDER_WIDTH, border_radius=10)

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление здоровьем для теста
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        health = min(MAX_HEALTH, health + 1)
    if keys[pygame.K_DOWN]:
        health = max(0, health - 1)

    # Отрисовка
    screen.fill(WHITE)
    draw_health_bar(screen, 250, 50, health)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()