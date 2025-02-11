import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)
        
        first_chunk_angle = self.velocity.rotate(random_angle)
        second_chunk_angle = self.velocity.rotate(-random_angle)
        
        chunk_radius = self.radius - ASTEROID_MIN_RADIUS
        
        first_chunk = Asteroid(self.position.x, self.position.y, chunk_radius)
        first_chunk.velocity = first_chunk_angle * 1.2
        second_chunk = Asteroid(self.position.x, self.position.y, chunk_radius)        
        second_chunk.velocity = second_chunk_angle * 1.2