from constants import SHOT_RADIUS
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen:pygame.Surface):
        pygame.draw.circle(screen, "green", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt