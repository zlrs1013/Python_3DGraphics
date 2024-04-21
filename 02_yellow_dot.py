"""

"""
from core.base import Base
from core.openGLUtils import OpenGLUtils
from OpenGL import GL


# render a single point
class Test(Base):

    def __init__(self):
        super().__init__()
        self.programRef = None

    def initialize(self):
        print("Initializing program.")

        ### create GPU program ###

        # vertex shader code
        vsCode = """
        void main()
        {
            gl_Position = vec4(0.0, 0.5, -0.5, 1);
        }
        """

        # fragment shader code
        fsCode = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        # send code to GPU, compile, store program reference
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        # render settings (optional)
        GL.glPointSize(36)

    def update(self):
        # select program to use when rendering
        GL.glUseProgram(self.programRef)

        # renders geometric object(s) using program
        GL.glDrawArrays(GL.GL_POINTS, 0, 1)


# create instance of class and run it
Test().run()
