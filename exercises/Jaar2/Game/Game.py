import pygame
from Jaar2.Game.color.Color import *
from Jaar2.Game.Settings import screen_height, screen_width
from Jaar2.Game.player.Player import Player
from Jaar2.Game.vector.Vector import Vector


class Game:
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode([screen_width, screen_height])
        self.__clock = pygame.time.Clock()
        self.__player = Player(self.__screen, Vector((screen_width / 2) - 25, (screen_height / 2) - 25), 50, 50)
        # self.__player = Player(self.__screen, Vector(0, 0), 50, 50)

    @staticmethod
    def __quit_program():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True

    def update(self):
        self.__player.update()

    def draw(self):
        self.__player.draw()

    def run(self):
        run_game = True
        while run_game:
            self.__screen.fill(white)
            self.update()
            self.draw()

            run_game = self.__quit_program()

            pygame.display.update()
            self.__clock.tick(90)
        quit()


game = Game()
game.run()

