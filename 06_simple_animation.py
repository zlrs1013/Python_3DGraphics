"""
    Create shader programs containing uniform variables used to change the
    position and set the color of a geometric object. Then create an application
    that draws two triangles, in different positions and with different colors,
    using Uniform objects to upload values to the uniform variables in the
    shader program. Finally, expanding on this application, change the values of
    the uniform data over time to create animated effects: one triangle moves
    upward, while the other triangle shifts colors.

"""

from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *
from math import sin

# render multiple triangles efficiently by only using one buffer


class Test(Base):

    def __init__(self):
        super().__init__()
        self.programRef = None

    def initialize(self):
        print("Initializing Program...")

        vsCode = """
        in vec3 position;
        uniform vec3 translation;
        void main()
        {
            vec3 pos = position + translation;
            gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);        
        }
        """

        fsCode = """
        uniform vec3 baseColor;
        out vec4 fragColor;
        void main(){
            fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        # render settings
        glClearColor(0.6, 0.6, 0.8, 1.0)

        # vertex array object
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        # set up attribute
        positionData = [
            [0.0, 0.2, 0.0],
            [0.2, -0.2, 0.0],
            [-0.2, -0.2, 0.0]
        ]

        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")
        self.vertexCount = len(positionData)

        # set up uniform variables which will be managed separately

        # position uniforms
        self.translation1 = Uniform("vec3", [-0.5, 0.0, 0.0])
        self.translation1.locateVariable(self.programRef, "translation")

        self.translation2 = Uniform("vec3", [0.5, 0.0, 0.0])
        self.translation2.locateVariable(self.programRef, "translation")

        # color uniforms
        self.baseColor1 = Uniform("vec3", [1.0, 0.0, 0.0])
        self.baseColor1.locateVariable(self.programRef, "baseColor")

        self.baseColor2 = Uniform("vec3", [1.0, 1.0, 0.0])
        self.baseColor2.locateVariable(self.programRef, "baseColor")

        #  keep track of elapsed time
        self.time = 0

    def update(self):
        glUseProgram(self.programRef)

        # clear the color buffer
        glClear(GL_COLOR_BUFFER_BIT)
        # assume the refresh rate is 60 Hz
        self.time += 1/60

        # draw first triangle one the left
        self.translation1.data[1] = sin(self.time) / 2
        self.translation1.uploadData()
        # self.baseColor1.data[1] += 0.01
        self.baseColor1.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

        # draw second triangle
        self.baseColor2.data[2] = (sin(self.time) + 1) / 2
        self.translation2.uploadData()
        self.baseColor2.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)


# create instance of class and run
Test().run()
