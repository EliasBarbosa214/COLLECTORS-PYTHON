import pygame
import random

class Lixo2(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('data/Imagens/Refri3.png')
        self.image = pygame.transform.scale(self.image, [50, 60])
        self.rect = pygame.Rect(50, 60, 50, 60)

        self.rect.x = random.randint(0, 890)
        self.rect.y = random.randint(120, 500)

        ############################################################

        if self.rect.top < 0:
            self.rect.top = 0

        elif self.rect.bottom > 650:
            self.rect.bottom = 680