
from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *

# move a triangle around the screen with the arrow keys

class Test(Base):

    def initialize(self):

        print("initializing program...")

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
                out vec4 fragColor;
                void main(){
                    fragColor = vec4(1.0, 1.0, 0.0, 1.0);
                }
                """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        # vertex array object
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        # attributes
        positionData = [
            [0.0, 0.2, 0.0],
            [0.2, -0.2, 0.0],
            [-0.2, -0.2, 0.0]
        ]

        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")

        self.vertexCount = len(positionData)

        # set up uniforms
        self.translationUniform = Uniform("vec3", [0.0, 0.0, 0.0])
        self.translationUniform.locateVariable(self.programRef, "translation")


    def update(self):

        glUseProgram(self.programRef)
        glClear(GL_COLOR_BUFFER_BIT)

        # amount to move triangle
        distance = 0.01
        if self.input.isKeyPressed("left"):
            self.translationUniform.data[0] -= distance

        if self.input.isKeyPressed("right"):
            self.translationUniform.data[0] += distance

        if self.input.isKeyPressed("up"):
            self.translationUniform.data[1] += distance

        if self.input.isKeyPressed("down"):
            self.translationUniform.data[1] -= distance

        self.translationUniform.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

# create instance of class and run
Test().run()
