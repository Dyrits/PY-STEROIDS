import pygame

from constants import SHOT_RADIUS
from CircleShape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.color = "white"
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def update(self, delta):
        self.position += self.velocity * delta