import pygame
from Lesson4.color.Color import *
from Lesson4.Settings import screen_width


class Player:
    def __init__(self, screen, vector, width, height):
        self.__screen = screen
        self.__vector = vector
        self.__width = width
        self.__height = height
        self.alive = True

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(
            self.__screen,
            green,
            pygame.Rect(
                (self.__vector.x, self.__vector.y, self.__width, self.__height)
            )
        )

