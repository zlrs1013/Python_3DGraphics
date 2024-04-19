"""
    Learn about why uniform variables are useful, the OpenGL functions needed to
    upload uniform data to the GPU, and create a Uniform class to manage these
    tasks.
"""

from OpenGL.GL import *


class Uniform(object):

    def __init__(self, dataType, data):

        # type of data
        # int | bool | float | vec2 | vec3 | vec4 | mat4
        self.dataType = dataType

        # data to be sent to uniform variable
        self.data = data

        # reference for variable location in program
        # this reference will be updated between each draw call
        self.variableRef = None

    # get and store reference to uniform variable
    def locateVariable(self, programRef, variableName):

        # returns reference to uniform variable named variableName in program
        # programRef
        self.variableRef = glGetUniformLocation(programRef, variableName)

    # store data in the uniform variable
    def uploadData(self):

        # if the variable does not exist, then exit
        if self.variableRef == -1:
            return

        if self.dataType == "int":
            glUniform1i(self.variableRef, self.data)

        elif self.dataType == "bool":
            glUniform1i(self.variableRef, self.data)

        elif self.dataType == "float":
            glUniform1f(self.variableRef, self.data)

        # when input data is more than one, they need to be sent separately
        elif self.dataType == "vec2":
            glUniform2f(self.variableRef, self.data[0], self.data[1])

        elif self.dataType == "vec3":
            glUniform3f(self.variableRef, self.data[0], self.data[1],
                        self.data[2])

        elif self.dataType == "vec4":
            glUniform4f(self.variableRef, self.data[0], self.data[1],
                        self.data[2], self.data[3])

        elif self.dataType == "mat4":
            # openGL expect the matrix arranged column by column
            #  we need to transpose the row major matrix by pass the
            #  constance GL_TRUE
            glUniformMatrix4fv(self.variableRef, 1, GL_TRUE, self.data)

        else:
            raise Exception(f"Unknown uniform data type: {self.dataType}")
