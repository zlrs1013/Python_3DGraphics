"""
    Geometry class defines the overall shape of geometric objects and stores
    vertex-related properties (position and color for now) with attribute
    objects. Then create and extension of this class representing rectangular
    shapes.
"""


class Geometry(object):

    def __init__(self):
        # no need to import attribute class. since base class creates
        # attributes. so create a dict to store attribute objects
        self.attributes = dict()

        # number of vertices
        self.vertexCount = None

    def countVertices(self):
        # the number of vertices is the length of any attribute object's
        # array of data
        attrib = list(self.attributes.values())[0]
        self.vertexCount = len(attrib.data)
