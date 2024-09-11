import pygame
from constants import SHOT_RADIUS, PLAYER_SHOT_SPEED

class Shot(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)
        self.rect = self.image.get_rect(center=(x, y))
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 1).rotate(direction) * PLAYER_SHOT_SPEED

    def update(self, delta_time):
        self.position += self.velocity * delta_time
        self.rect.center = self.position
