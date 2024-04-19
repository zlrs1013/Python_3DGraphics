"""
    Mesh class stores transformation matrix, vao (which connects geometry and
    material instances), geometry and material instance, visibility(boolean)
    variable
    Set up the association between vertex buffers (geometry) and shader
    variables (material).
"""

from object3D import Object3D
from OpenGL.GL import *


class Mesh(Object3D):

    def __init__(self, geometry, material):
        super().__init__()

        self.geometry = geometry
        self.material = material

        # should this object be rendered
        self.visibility = True

        # set up association between attributes in the geometry and shader
        # variables in material
        self.vaoRef = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRef)

        for variableName, attributeObject in geometry.attributes.items():
            attributeObject.associateVariable(material.programRef, variableName)

        # unbind the vertex array object
        glBindVertexArray(0)

