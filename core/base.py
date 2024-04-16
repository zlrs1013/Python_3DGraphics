"""

    file:base.py
"""

import pygame
import sys  # for terminating the app once it runs
from core.input import Input


class Base(object):
    # define constructor function
    def __init__(self):
        # initialize all pygame modules
        pygame.init()

        # set width and height of the window
        screenSize = (512, 512)

        # indicate rendering options. | combines the two constants
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL

        # create and display the window
        self.screen = pygame.display.set_mode(screenSize, displayFlags)

        # set window title text
        pygame.display.set_caption("Graphics Window")

        # determines if main loop is active
        self.running = True

        # manage time-related data and operations
        self.clock = pygame.time.Clock()

        # manage user input
        self.input = Input()

    # implement by extending the class
    def initialize(self):
        pass

    # implement by extending class
    def update(self):
        pass

    #
    def run(self):
        # startup
        self.initialize()
        # main loop
        while self.running:
            # process input
            self.input.update()

            if self.input.quit:
                self.running = False

            # update
            self.update()

            # render
            # display image in front buffer on screen
            pygame.display.flip()

            # pause if necessary to achieve 60 FPS
            self.clock.tick(60)

        # shut down
        pygame.quit()
        sys.exit()
