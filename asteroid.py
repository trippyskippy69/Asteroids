from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random
class Asteroid(CircleShape, pygame.sprite.Sprite):
    containers = ()

    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(1, 0)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=(x, y))


    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return


        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid1.velocity = new_velocity1 * 1.2
        new_asteroid2.velocity = new_velocity2 * 1.2

        Asteroid.containers.add(new_asteroid1)
        Asteroid.containers.add(new_asteroid2)
