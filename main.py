import pygame

from constants import *
from Player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)
        for entity in updatable:
            entity.update(delta)
        pygame.display.flip()
        delta = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
