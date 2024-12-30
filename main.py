import pygame

from constants import *
from Player import Player
from Bubble import Bubble
from BubbleField import BubbleField
from Shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    bubbles = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Bubble.containers = (bubbles, updatable, drawable)
    BubbleField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = BubbleField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)
        for entity in updatable:
            entity.update(delta)
        for bubble in bubbles:
            if player.collide(bubble):
                print("Game Over!")
                return
            for shot in shots:
                if bubble.collide(shot):
                    bubble.split()
                    shot.kill()
                    break
        pygame.display.flip()
        delta = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
