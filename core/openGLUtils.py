"""

"""

from OpenGL import GL


# static method to load/compile OpenGL shaders and link to create GPU programs


class OpenGLUtils(object):

    @staticmethod
    def initializeShader(shaderCode, shaderType):
        # specify OpenGL version and requirements
        # extension = "#extension GL_ARB_shading_language_420pack: require \n"
        shaderCode = "#version 330 \n " + shaderCode

        # create empty shader object and return the reference value
        shaderRef = GL.glCreateShader(shaderType)
        # store source code in the shader
        GL.glShaderSource(shaderRef, shaderCode)
        # compile source code stored in shader
        GL.glCompileShader(shaderRef)

        # error checking
        # query whether compilation was successful
        compileSuccess = GL.glGetShaderiv(shaderRef,
                                          GL.GL_COMPILE_STATUS)
        if not compileSuccess:
            # retrieve error message
            errorMessage = GL.glGetShaderInfoLog(shaderRef)
            # free memory used to store the shader program
            GL.glDeleteShader(shaderRef)

            # convert byte string returned to char string
            errorMessage = "\n" + errorMessage.decode("utf-8")
            # raise exception, halt the program, print error message
            raise Exception(errorMessage)

        # compilation was successful
        return shaderRef

    # link vertex shader and fragment shader together
    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):

        # compile shaders and store references
        vertexShaderRef = OpenGLUtils.initializeShader(vertexShaderCode,
                                                       GL.GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtils.initializeShader(fragmentShaderCode,
                                                         GL.GL_FRAGMENT_SHADER)

        # create program object
        programRef = GL.glCreateProgram()

        # attach previously compiled shaders
        GL.glAttachShader(programRef, vertexShaderRef)
        GL.glAttachShader(programRef, fragmentShaderRef)

        # link shaders
        GL.glLinkProgram(programRef)

        # error checking
        # query if linking was successful
        linkSuccess = GL.glGetProgramiv(programRef, GL.GL_LINK_STATUS)

        if not linkSuccess:
            # retrieve error message
            errorMessage = GL.glGetProgramInfoLog(programRef)
            # free memory used to store program
            GL.glDeleteProgram(programRef)
            # convert byte string to character string
            errorMessage = "\n" + errorMessage.decode("utf-8")
            # raise exception, halt the program, print error message
            raise Exception(errorMessage)

        # linking was successful
        return programRef

#     @staticmethod
#     def printSystemInfo():
#         print("===================================================")
#         print(f"vendor: {GL.glGetString(GL.GL_VENDOR).decode("utf-8")}")
#         print(f"Renderer: {GL.glGetString(GL.GL_RENDERER).decode("utf-8")}")
#         print(f"OpenGL version supported: "
#               f"{GL.glGetString(GL.GL_VERSION).decode("utf-8")}")
#         print(f"GLSL version supported: "
#               f""
#               f""
#               f"{GL.glGetString(GL.GL_SHADING_LANGUAGE_VERSION).decode("utf-8")}")
#         print("===================================================")
#
#
# print(OpenGLUtils().printSystemInfo())
