import pygame
import sys
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
shots_group = pygame.sprite.Group()
def main():
    pygame.init()

    screen_width, screen_height = 800, 600
    player_radius = 15
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, player_radius)
    updatable.add(player)
    drawable.add(player)
    all_sprites.add(player)

    x, y, radius = 100, 150, 20
    asteroid = Asteroid(x, y, radius)
    asteroids.add(asteroid)
    updatable.add(asteroid)
    drawable.add(asteroid)
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    running = True
    while running:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif  event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_SPACE:
                     player.shoot(all_sprites, shots_group)

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                running = False
        for asteroid in asteroids:
            for bullet in shots_group:
                if pygame.sprite.collide_rect(asteroid, bullet):
                    asteroid.kill()
                    bullet.kill()

        updatable.update(dt)
        shots_group.update(dt)

        screen.fill((0, 0, 0))

        drawable.draw(screen)
        shots_group.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()



































































































































