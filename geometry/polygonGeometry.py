"""
    the Polygon Geometry class that can generate data to render a regular polygon
    with any number of sides and radius. Use the parametric equation of a circle
    to generate the vertex position data, and add vertex color data so that
    each triangle appears distinct.
"""

from geometry.geometry import Geometry
from math import sin, cos, pi


class PolygonGeometry(Geometry):

    def __init__(self, sides=3, radius=1):

        super().__init__()

        # calculate the base angle
        A = 2 * pi / sides
        positionData = []
        colorData = []

        for n in range(sides):
            positionData.append(
                [0, 0, 0]
            )
            positionData.append(
                [radius * cos(n * A), radius * sin(n * A), 0]
            )
            positionData.append(
                [radius * cos((n + 1) * A), radius * sin((n + 1) * A), 0]
            )

            colorData.append([1, 1, 1])
            colorData.append([1, 0.5, 0])
            colorData.append([1, 1, 0])

        self.addAttribute("vec3", "vertexPosition", positionData)
        self.addAttribute("vec3", "vertexColor", colorData)

        self.countVertices()
