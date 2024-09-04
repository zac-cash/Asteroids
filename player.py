import pygame
from circleshape import *
from constants import *
from shot import * 

class Player(CircleShape):
    def __init__(self, x, y):
        self.rotation = 0
        super().__init__(x,y,PLAYER_RADIUS)
        self.shoot_cooldown = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return (a, b, c)
    
    def draw(self,screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED* dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        self.shoot_cooldown -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
    
    def shoot(self):
        if self.shoot_cooldown > 0:
            return
        self.shoot_cooldown += PLAYER_SHOOT_COOLDOWN
        bullet = Shot(self.position.x,self.position.y,SHOT_RADIUS)
        bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        



