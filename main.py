from constants import *
import pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pygame window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()
def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)











































if __name__ == "__main__":
    main()




































































































































