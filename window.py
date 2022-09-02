"""
Class to create game window
date: 2022-09-01
"""
import pygame


class Window:
    """
    Window class
    Attrs:
    - screen (pygame.Surface)
    - height (int)
    - width (int)
    - background (pygame.Surface)
    - fps (int)
    - clock (pygame.time.Clock)
    - font (pygame.Font)
    Methods:
    - update(): (none)
    - get_width(): (int)
    - get_height(): (int)
    - get_screen()
    """

    def __init__(self, w, h, fps, caption):
        self.__width = w
        self.__height = h
        self.__fps = fps
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(caption)
        self.__background = pygame.Surface((w, h), pygame.SRCALPHA, 32)
        self.__background.fill((0, 0, 0))

        pygame.font.init()
        self.__font = pygame.font.SysFont('Segoe UI', 14)

    def update(self, things):
        """
        Draws everything given to method onto the screen with their x and y coords
        :param things: (tuple) surface followed by (x, y) coordinates; (surface, (x, y))
        :return: (none)
        """
        self.__screen.blit(self.__background, (0, 0))
        for thing in things:
            self.__screen.blit(thing[0], thing[1])
        self.__clock.tick(self.__fps)
        pygame.display.flip()

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_screen(self):
        return self.__screen


# EPILEPSY WARNING
if __name__ == "__main__":
    # Epilepsy Generator
    from random import randint
    pygame.init()
    screen = Window(1000, 500, 60, "Caption")
    squares = []

    while len(squares) < 200:
        x, y = randint(0, screen.get_width()), randint(0, screen.get_height())
        s = pygame.Surface((x, y), pygame.SRCALPHA, 32)
        pygame.draw.rect(s, (randint(5, 255), randint(5, 255), randint(5, 255)), pygame.Rect(0, 0, x, y),
                         randint(1, 5))
        squares.append((s, (randint(0, screen.get_width() - x), randint(0, screen.get_height() - y))))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                exit()

        screen.update(squares[randint(0, len(squares) - 1):randint(0, len(squares) - 1)])
