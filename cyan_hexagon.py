"""
    Learn how to create vertex array objects to manage and store the
    associations between vertex buffer data (VBOs) and attribute ("in")
    variables in a vertex shader.
    Then, create an application that uses a vertex array object and the
    Attribute class to draw a hexagon and illustrates different draw modes (
    points, lines, line loop, triangles, triangle fan). Create a second
    application that uses multiple vertex array objects to draw multiple
    shapes at once.
"""

from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *


# rendering six points in a hexagon arrangement
class Test(Base):

    def __init__(self):
        super().__init__()
        self.vertexCount = None
        self.programRef = None

    def initialize(self):
        print("Initializing Program...")

        vsCode = """
        in vec3 position;
        void main()
        {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
        }
        """

        fsCode = """
        void main()
        {
            gl_FragColor = vec4(0.0, 1.0, 1.0, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        # render settings
        glPointSize(16)
        glLineWidth(8)

        # set up VAOs (vertex array objects)
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        # set up vertex attribute
        positionData = [[0.8, 0.0, 0.0],
                        [0.4, 0.6, 0.0],
                        [-0.4, 0.6, 0.0],
                        [-0.8, 0.0, 0.0],
                        [-0.4, -0.6, 0.0],
                        [0.4, -0.6, 0.0]]

        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")

        self.vertexCount = len(positionData)

    def update(self):
        glUseProgram(self.programRef)
        # Draw mode GL_LINE_LOOP connects each dot to next dot
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)


# create an instance and run
Test().run()