"""
    USe the pygame class to monitor for discrete input (keydown, keyup) and
    continuous input (keypressed).
    handle input process
    file: input.py
"""

import pygame


class Input(object):

    def __init__(self):
        # has the user quit the app
        self.quit = False

        # list to store key states
        # down, up: discrete events, last for one iteration
        # pressed: continuous event, between down and up events
        self.keyDownList = []
        self.keyPressedList = []
        self.keyUpList = []

    def update(self):
        # iterate over all user input events(keyboards/mouse) that have
        # occurred since events checked

        # reset discrete key states
        self.keyUpList = []
        self.keyDownList = []

        for event in pygame.event.get():
            # quit event occurs by clicking close button
            if event.type == pygame.QUIT:
                self.quit = True

            # check for discrete key down and up events
            # get name of key from event and append to or remove from
            # corresponding lists
            elif event.type == pygame.KEYDOWN:
                keyName = pygame.key.name(event.key)
                self.keyDownList.append(keyName)
                self.keyPressedList.append(keyName)

#           # key up
            elif event.type == pygame.KEYUP:
                keyName = pygame.key.name(event.key)
                self.keyPressedList.remove(keyName)
                self.keyUpList.append(keyName)

    # functions to query key states
    def isKeyDown(self, keyName):
        return keyName in self.keyDownList

    def isKeyPressed(self, keyName):
        return keyName in self.keyPressedList

    def isKeyUp(self, keyName):
        return keyName in self.keyUpList

