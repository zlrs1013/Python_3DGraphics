"""
     Group class represents root node of scene graph tree.
"""

from object3D import Object3D


class Group(Object3D):

    def __init__(self):
        super().__init__()