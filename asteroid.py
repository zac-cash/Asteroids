import pygame
import random
from circleshape import *
from constants import * 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt 
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20.0,30.0)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(angle *-1)

        new_astroid1 = Asteroid(self.position.x,self.position.y, new_radius)
        new_astroid1.velocity = vector1 * 1.2
        new_astroid2 = Asteroid(self.position.x,self.position.y, new_radius)
        new_astroid2.velocity = vector2 * 1.2



        
        
