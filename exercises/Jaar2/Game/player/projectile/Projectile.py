import pygame

from Jaar2.Game.Settings import projectile_speed, screen_width, screen_height
from Jaar2.Game.color.Color import red


class Projectile:
    def __init__(self, screen, movement, vector):
        self.screen = screen
        self.movement = movement
        self.width = 30
        self.height = 10
        self.vector = vector
        self.alive = True

        if movement == 'up' or movement == 'down':
            self.width = 10
            self.height = 30

    def update(self):
        if self.movement == 'up':
            self.vector.y -= projectile_speed
        elif self.movement == 'down':
            self.vector.y += projectile_speed
        elif self.movement == 'right':
            self.vector.x += projectile_speed
        elif self.movement == 'left':
            self.vector.x -= projectile_speed

        if (
                self.vector.x <= 0 - self.width or
                self.vector.x >= screen_width or
                self.vector.y <= 0 - self.height or
                self.vector.y >= screen_height):
            self.alive = False

    def draw(self):
        pygame.draw.rect(
            self.screen,
            red,
            pygame.Rect(
                (self.vector.x, self.vector.y, self.width, self.height)
            )
        )
