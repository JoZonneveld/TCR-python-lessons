import pygame
from Lesson4.color.Color import *
from Lesson4.Settings import screen_width, screen_height

class Player:
    def __init__(self, screen, vector, width, height):
        self.__screen = screen
        self.__vector = vector
        self.__width = width
        self.__height = height
        self.alive = True

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.__vector.x -= 10

            if self.__vector.x < 0:
                self.__vector.x = 0

        if keys[pygame.K_RIGHT]:
            self.__vector.x += 10

            if self.__vector.x > screen_width - self.__width:
                self.__vector.x = (screen_width - self.__width)

        if keys[pygame.K_UP]:
            self.__vector.y -= 10

            if self.__vector.y < 0:
                self.__vector.y = 0

        if keys[pygame.K_DOWN]:
            self.__vector.y += 10

            if self.__vector.y > screen_height - self.__height:
                self.__vector.y = (screen_height - self.__height)

    def draw(self):
        pygame.draw.rect(
            self.__screen,
            green,
            pygame.Rect(
                (self.__vector.x, self.__vector.y, self.__width, self.__height)
            )
        )

