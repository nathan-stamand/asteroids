from circleshape import CircleShape
import pygame
import constants as C
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= C.ASTEROID_MIN_RADIUS:
            return
        x, y = self.position
        
        rotation = random.uniform(20, 50)
        asteroid1 = Asteroid(x, y, self.radius - C.ASTEROID_MIN_RADIUS)
        asteroid1.velocity = self.velocity.rotate(rotation) * C.ASTEROID_SPLIT_VELOCITY_MULTIPLIER
        asteroid2 = Asteroid(x, y, self.radius - C.ASTEROID_MIN_RADIUS)
        asteroid2.velocity = self.velocity.rotate(-rotation) * C.ASTEROID_SPLIT_VELOCITY_MULTIPLIER