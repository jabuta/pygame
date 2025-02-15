from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen:pygame.Surface):
        pygame.draw.circle(screen, "red", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        a1 = self.velocity.rotate(angle)
        a2 = self.velocity.rotate(-angle)

        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, radius)

        asteroid1.velocity = a1 * 1.2
        asteroid2.velocity = a2 * 1.2


