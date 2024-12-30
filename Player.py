import pygame

from CircleShape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.color = "white"

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        return [self.position + forward * self.radius, self.position - forward * self.radius - right, self.position - forward * self.radius + right]

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle(), 2)

    def rotate(self, delta):
        self.rotation += delta * PLAYER_TURN_SPEED

    def move(self, delta):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta

    def update(self, delta):
        keys = pygame.key.get_pressed()

        # Configuration is made for an AZERTY keyboard.
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.rotate(-delta)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate(delta)
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            self.move(delta)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            # Move backwards at half speed:
            self.move(-delta / 2)