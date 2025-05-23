import os, sys
import pygame

datas=[
    ('resources/sound/*', 'resources/sound'),
    ('resources/sprites/*', 'resources/sprites'),
    ('resources/textures/*', 'resources/textures')
],


# מאתר את הנתיב הנכון גם כשהקובץ ארוז בתוך EXE
BASE_PATH = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
image_path = os.path.join(BASE_PATH, "resources", "sprites", "player.png")

# טען את הקובץ
player_image = pygame.image.load(image_path)
