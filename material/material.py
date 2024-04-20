"""
    Create the base Material class, which defines the overall appearance of
    geometric objects and stores uniform variable data (using the Uniform
    class) and OpenGL render settings.

    Material objects:
    Store three types of data related to rendering:
    - shader program references
    - Uniform objects
    - OpenGL render settings

    extensions of the base class
    - different materials for rendering geometric data as a collection of
    points, as a set of lines, or as a surface
    - some basic materials will implement vertex colors or uniform base colors
    - advanced materials will implement texture mapping, lighting, and other
    effects
"""

from core.openGLUtils import OpenGLUtils
from core.uniform import Uniform


class Material(object):

    def __init__(self, vertexShaderCode, fragmentShaderCode):
        self.programRef = OpenGLUtils.initializeProgram(vertexShaderCode, fragmentShaderCode)

        # store uniform objects
        self.uniforms = dict()

        # standard Uniform objects (matrices)
        # data will be passed in later
        self.uniforms["modelMatrix"] = Uniform("mat4", None)
        self.uniforms["viewMatrix"] = Uniform("mat4", None)
        self.uniforms["projectionMatrix"] = Uniform("mat4", None)

        # store OpenGL render settings
        self.settings = dict()
        self.settings["drawStyle"] = None

    # initialize all Uniform variable references
    def locateUniforms(self):
        # go through the uniform variables and call locateVariable function
        for variableName, uniformObject in self.uniforms.items():
            uniformObject.locateVariable(self.programRef, variableName)

    # configure OpenGL render settings
    # each setting will be activated differently, so implemented in extensions
    def updateRenderSettings(self):
        pass

    # convenience method for setting multiple "properties" : uniform and
    # render setting values
    def setProperties(self, properties=None):
        if properties is None:
            properties = dict()

        for name, data in properties.items():
            # update Uniforms
            if name in self.uniforms.keys():
                self.uniforms[name].data = data

            # update render settings
            elif name in self.settings.keys():
                self.settings[name] = data

            # unknown properties
            else:
                raise Exception(f"Material has no property: {name}")
