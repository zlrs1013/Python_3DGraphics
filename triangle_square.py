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


# rendering a triangle and a square
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

        # set up VAOs (vertex array objects) for the triangle
        self.vaoTri = glGenVertexArrays(1)
        glBindVertexArray(self.vaoTri)

        # set up vertex attribute
        positionDataTri = [[-0.5, 0.8, 0.0],
                        [-0.2, 0.2, 0.0],
                        [-0.8, 0.2, 0.0]]

        positionAttributeTri = Attribute("vec3", positionDataTri)
        # set up variable association that'll be stored in the VAO that's
        # currently bound
        positionAttributeTri.associateVariable(self.programRef, "position")

        self.vertexCount = len(positionDataTri)

        # set up square
        self.vaoSq = glGenVertexArrays(1)
        glBindVertexArray(self.vaoSq)

        # set up vertex attribute
        positionDataSq = [[0.8, 0.8, 0.0],
                           [0.8, 0.2, 0.0],
                           [0.2, 0.2, 0.0],
                          [0.2, 0.8, 0.0]]

        positionAttributeSq = Attribute("vec3", positionDataSq)
        # set up variable association that'll be stored in the VAO that's
        # currently bound
        positionAttributeSq.associateVariable(self.programRef, "position")

        self.vertexCount = len(positionDataSq)

    def update(self):
        glUseProgram(self.programRef)
        # Draw mode GL_LINE_LOOP connects each dot to next dot
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)


# create an instance and run
Test().run()