from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen:pygame.Surface):
        pygame.draw.circle(screen, "red", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt