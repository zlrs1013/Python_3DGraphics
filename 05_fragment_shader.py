"""
    Learn how to use shader variables with the type qualifiers "in" and "out" to
    pass data from the vertex shader to the fragment shader. Create an
    application that draws six vertices as points, each with a different color.
    Then experiment with different draw modes to see that the vertex data
    (colors) is interpolated for each pixel within the geometric shapes.

"""

from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *


# rendering six points in a hexagon arrangement; use vertex colors
class Test(Base):

    def __init__(self):
        super().__init__()
        self.vertexCount = None
        self.programRef = None

    def initialize(self):
        print("Initializing Program...")

        vsCode = """
        in vec3 position;
        in vec3 vertexColor;
        out vec3 color;
        void main()
        {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
            color = vertexColor;
        }
        """

        fsCode = """
        in vec3 color;
        void main()
        {
            gl_FragColor = vec4(color.r, color.g, color.b, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        # render settings
        glPointSize(16)
        glLineWidth(8)

        # set up VAOs (vertex array objects)
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        # set up vertex attribute for position
        positionData = [[0.8, 0.0, 0.0],
                        [0.4, 0.6, 0.0],
                        [-0.4, 0.6, 0.0],
                        [-0.8, 0.0, 0.0],
                        [-0.4, -0.6, 0.0],
                        [0.4, -0.6, 0.0]]

        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")

        self.vertexCount = len(positionData)

        # set up vertex attribute for color
        colorData = [
            [1.0, 0.0, 0.0],
            [1.0, 0.5, 0.0],
            [1.0, 1.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [0.5, 0.0, 1.0]
        ]

        colorAttribute = Attribute("vec3", colorData)
        colorAttribute.associateVariable(self.programRef, "vertexColor")

    def update(self):
        glUseProgram(self.programRef)

        # test different draw modes
        # interpolation takes a weighted average of the color at each vertex
        # in general, a pixel closer to an orange vertex would be rendered more
        # orange

        # glDrawArrays(GL_POINTS, 0, self.vertexCount)
        # glDrawArrays(GL_LINES, 0, self.vertexCount)
        # glDrawArrays(GL_LINE_LOOP, 0, self.vertexCount)
        # glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)


# create an instance and run
Test().run()
