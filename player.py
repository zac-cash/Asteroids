from circleshape import *
from constants import * 

class Player(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rotation = 0
        super().__init__(x,y,PLAYER_RADIUS)
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return (a, b, c)
    
    def draw(self,screen):
        pygame.draw.polygon(screen, RGB_WHITE, self.triangle(), 2)


