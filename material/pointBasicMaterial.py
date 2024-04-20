"""
    The OpenGL render settings needed for point basic material is
    - "drawStyle": GL_POINTS
    - "pointSize": integer
    - "roundedPoints": boolean
"""

from material.basicMaterial import BasicMaterial
from OpenGL.GL import *


class PointBasicMaterial(BasicMaterial):

    def __init__(self, properties={}):
        # set up everything by initializing BasicMaterial super class
        # load up shader code and store and locate the uniforms
        super().__init__()

        # render vertices as points
        self.settings["drawStyle"] = GL_POINTS
        # width and height of points
        self.settings["pointSize"] = 8
        # draw points as rounded ?
        self.settings["roundedPoints"] = True

        # once all render settings default are set up
        # modify as needed
        self.setProperties(properties)

    def updateRenderSettings(self):

        glPointSize(self.settings["pointSize"])

        if self.settings["roundedPoints"]:
            glEnable(GL_POINT_SMOOTH)
        else:
            glDisable(GL_POINT_SMOOTH)

