import pygame
from shot import Shot
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from circle_shape import CircleShape
from constants import PLAYER_SHOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, size=40, color=(255, 255, 255)):
        CircleShape.__init__(self, x, y, size / 2)
        pygame.sprite.Sprite.__init__(self)
        self.position = pygame.Vector2(x, y)
        self.radius = size / 2
        self.velocity = pygame.Vector2(0, 0)
        self.size = size
        self.color = color
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.rotation = 0
        self.timer = 0

    def update(self, dt):
        self.move(dt)
        self.rotate(dt)
        self.rect.center = self.position
        if self.timer > 0:
            self.timer = max(0, self.timer - dt)


    def draw(self, screen):
        surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        height = self.size * (3**0.5) / 2

        points = [
            (self.size / 2, 0),
            (0, height),
            (self.size, height)
        ]

        pygame.draw.polygon(surface, self.color, points)

        rotated_surface = pygame.transform.rotate(surface, -self.rotation)
        rect = rotated_surface.get_rect(center=self.position)
        screen.blit(rotated_surface, rect)

    def rotate(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_RIGHT]:
            self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation = self.rotation % 360

    def move(self, dt):
        keys = pygame.key.get_pressed()
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if keys[pygame.K_UP]:
            self.position -= forward * PLAYER_SPEED * dt
        if keys[pygame.K_DOWN]:
            self.position += forward * PLAYER_SPEED * dt

    def shoot(self, all_sprites, shots_group):
        if self.timer <= 0:
            direction_angle = self.rotation
            new_shot = Shot(self.position.x, self.position.y, direction_angle)
            all_sprites.add(new_shot)
            shots_group.add(new_shot)
            self.timer = PLAYER_SHOOT_COOLDOWN

    def handle_input(self, all_sprites, shots_group):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.shoot(all_sprites, shots_group)
