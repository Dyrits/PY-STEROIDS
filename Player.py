import pygame

from CircleShape import CircleShape
from Shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.color = "white"
        self.cooldown = 0

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
        self.wrap()

    def update(self, delta):
        if self.cooldown > 0:
            self.cooldown -= delta
            self.cooldown = max(0, self.cooldown)

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
        if keys[pygame.K_SPACE]:
            if self.cooldown == 0:
                self.shoot()

    def shoot(self):
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot = Shot(self.position.x, self.position.y, velocity)
        self.cooldown = PLAYER_SHOOT_COOLDOWN

    def wrap(self):
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0