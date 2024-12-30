import random

import pygame

from CircleShape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = "white"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, delta):
        self.position += self.velocity * delta

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        velocities = [self.velocity.rotate(angle), self.velocity.rotate(-angle)]
        radius = max(self.radius - ASTEROID_MIN_RADIUS, ASTEROID_MIN_RADIUS)
        for velocity in velocities:
            asteroid = Asteroid(self.position.x, self.position.y, radius)
            asteroid.velocity = velocity * 1.2
