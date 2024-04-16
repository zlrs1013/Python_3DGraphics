"""
    handle input process
    file: input.py
"""

import pygame


class Input(object):

    def __init__(self):
        # has the user quit the app
        self.quit = False

    def update(self):
        # iterate over all user input events(keyboards/mouse) that have
        # occurred since events checked

        for event in pygame.event.get():
            # quit event occurs by clicking close button
            if event.type == pygame.QUIT:
                self.quit = True
