"""
    surfaceBasicMaterials use triangles by default to render
    The OpenGL render settings needed for surface basic material is
    - "drawStyle": GL_TRIANGLES
    - "doubleSide": bool
    - "wireframe: bool
    - "lineWidth": int
"""

from material.basicMaterial import BasicMaterial
from OpenGL.GL import *


class SurfaceBasicMaterial(BasicMaterial):

    def __init__(self, properties={}):
        # set up everything by initializing BasicMaterial super class
        # load up shader code and store and locate the uniforms
        super().__init__()

        # render vertices as triangles by default
        self.settings["drawStyle"] = GL_TRIANGLES
        # to improve performance, only render the front side (vertices are
        # specified in ccw order). for simple rendering we can use doubleside
        self.settings["doubleSide"] = True
        # render as wireframe?
        self.settings["wireframe"] = False
        # line thickness
        self.settings["lineWidth"] = 4

        self.setProperties(properties)

    def updateRenderSettings(self):

        if self.settings["doubleSide"]:
            glDisable(GL_CULL_FACE)
        else:
            glEnable(GL_CULL_FACE)

        if self.settings["wireframe"]:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        glLineWidth(self.settings["lineWidth"])
