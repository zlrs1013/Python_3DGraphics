"""
    Create extensions of the base Material class that enable geometric shapes to
    be rendered as points, lines, or triangulated surfaces. A hierarchy of
    classes is used to separate the shader code and Uniform variable
    declarations from further classes that define the OpenGL render settings
    (point size, line width, etc.) and how they are to be implemented with
    OpenGL functions.
"""

from material.material import Material
from core.uniform import Uniform


class BasicMaterial(Material):

    def __init__(self):

        vertexShaderCode = """
        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;
        
        in vec3 vertexPosition;
        in vec3 vertexColor;
        out vec3 color;
        
        void main()
        {
            vec4 position = vec4(vertexPosition, 1.0);
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * 
            position;
            color = vertexColor;
        }
        """

        fragmentShaderCode = """
        uniform vec3 baseColor;
        uniform bool useVertexColors;
        in vec3 color;
        out vec4 fragColor;
        
        void main()
        {
            vec4 tempColor = vec4(baseColor, 1.0);
            
            if ( useVertexColors )
                tempColor *= vec4(color, 1.0);
                
            fragColor = tempColor;
        }
        """

        # call super class Material object
        super().__init__(vertexShaderCode, fragmentShaderCode)

        # set the default color to white 1.0
        self.uniforms["baseColor"] = Uniform(
            "vec3", [1.0, 1.0, 1.0])

        self.uniforms["useVertexColors"] = Uniform("bool", 0)

        # all uniform objects are accounted for so locate ...
        self.locateUniforms()


