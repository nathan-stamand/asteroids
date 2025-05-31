from circleshape import CircleShape
import constants as C
import pygame

class Shot(CircleShape):
    def __init__(self, position, rotation):
        super().__init__(position[0], position[1], C.SHOT_RADIUS)
        self.rotation = rotation
        self.velocity = pygame.Vector2(0, 1) * C.PLAYER_SHOOT_SPEED
        
    def draw(self, screen):
        return pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity.rotate(self.rotation) * dt