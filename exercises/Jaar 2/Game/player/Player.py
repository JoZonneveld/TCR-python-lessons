import pygame
from Lesson4.color.Color import *
from Lesson4.Settings import screen_width, screen_height, player_speed
from Lesson4.player.projectile.Projectile import Projectile
from Lesson4.vector.Vector import Vector


class Player:
    def __init__(self, screen, vector, width, height):
        self.__screen = screen
        self.__vector = vector
        self.__width = width
        self.__height = height
        self.alive = True
        self.__projectiles = []

    def __movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.__vector.x -= player_speed
            if self.__vector.x < 0:
                self.__vector.x = 0

        if keys[pygame.K_RIGHT]:
            self.__vector.x += player_speed

            if self.__vector.x > screen_width - self.__width:
                self.__vector.x = (screen_width - self.__width)

        if keys[pygame.K_UP]:
            self.__vector.y -= player_speed

            if self.__vector.y < 0:
                self.__vector.y = 0

        if keys[pygame.K_DOWN]:
            self.__vector.y += player_speed

            if self.__vector.y > screen_height - self.__height:
                self.__vector.y = (screen_height - self.__height)

    def __create_projectile(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.__projectiles.append(Projectile(self.__screen, 'up', Vector(self.__vector.x + 20, self.__vector.y + 20)))

        if keys[pygame.K_a]:
            self.__projectiles.append(Projectile(self.__screen, 'left', Vector(self.__vector.x + 20, self.__vector.y + 20)))

        if keys[pygame.K_s]:
            self.__projectiles.append(Projectile(self.__screen, 'down', Vector(self.__vector.x + 20, self.__vector.y + 20)))

        if keys[pygame.K_d]:
            self.__projectiles.append(Projectile(self.__screen, 'right', Vector(self.__vector.x + 20, self.__vector.y + 20)))

    def update(self):
        self.__movement()
        self.__create_projectile()

        for projectile in self.__projectiles:
            if projectile.alive:
                projectile.update()
            else:
                self.__projectiles.remove(projectile)

    def draw(self):
        for projectile in self.__projectiles:
            projectile.draw()
        pygame.draw.rect(
            self.__screen,
            green,
            pygame.Rect(
                (self.__vector.x, self.__vector.y, self.__width, self.__height)
            )
        )



