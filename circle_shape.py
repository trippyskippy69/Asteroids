import pygame

class CircleShape:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.position = pygame.Vector2(x, y)

    def check_collision(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)
