"""
    The OpenGL render settings needed for line basic material is
    - "drawStyle": GL_LINE_STRIP, GL_LINE_LOOP, GL_LINES
    - "lineType": "connected", "loop", "segments"
    - "lineWidth": integer
"""

from material.basicMaterial import BasicMaterial
from OpenGL.GL import *


class LineBasicMaterial(BasicMaterial):

    def __init__(self, properties={}):
        # set up everything by initializing BasicMaterial super class
        # load up shader code and store and locate the uniforms
        super().__init__()

        # there are many different ways to group vertices into lines
        # render vertices as continuous by default
        self.settings["drawStyle"] = GL_LINE_STRIP
        # line type: "connected" | "loop" | "segments"
        self.settings["lineType"] = "connected"
        # line thickness
        self.settings["lineWidth"] = 4

        self.setProperties(properties)

    def updateRenderSettings(self):

        glLineWidth(self.settings["lineWidth"])

        if self.settings["lineType"] == "connected":
            self.settings["drawStyle"] = GL_LINE_STRIP
        elif self.settings["lineType"] == "loop":
            self.settings["drawStyle"] = GL_LINE_LOOP
        elif self.settings["lineType"] == "segments":
            self.settings["drawStyle"] = GL_LINES
        else:
            raise Exception(f"Unknown line style: {self.settings["lineType"]}")


