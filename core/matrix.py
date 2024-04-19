"""
    The Matrix class that can be used to generate translation, rotation,
    scale, and perspective projection matrices. Update the Uniform class to
    work with matrix data. Create a test application that enables the user to
    move a triangle around the with translations and rotations, both global
    and local.
"""

import numpy as np
from math import sin, cos, tan, pi


class Matrix(object):

    @staticmethod
    def makeIdentity():
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]).astype(float)

    @staticmethod
    def makeTranslation(x, y, z):
        return np.array([
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]
        ]).astype(float)

    @staticmethod
    def makeRotationX(angle):
        c = cos(angle)
        s = sin(angle)
        return np.array([
            [1, 0, 0, 0],
            [0, c, -s, 0],
            [0, s, c, 0],
            [0, 0, 0, 1]
        ]).astype(float)

    @staticmethod
    def makeRotationY(angle):
        c = cos(angle)
        s = sin(angle)
        return np.array([
            [c, 0, s, 0],
            [0, 1, 0, 0],
            [-s, 0, c, 0],
            [0, 0, 0, 1]
        ]).astype(float)

    @staticmethod
    def makeRotationZ(angle):
        c = cos(angle)
        s = sin(angle)
        return np.array([
            [c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]).astype(float)

    @staticmethod
    def makeScale(s):
        # a uniform scaling
        return np.array([
            [s, 0, 0, 0],
            [0, s, 0, 0],
            [0, 0, s, 0],
            [0, 0, 0, 1]
        ]).astype(float)

    @staticmethod
    def makePerspective(angleOfView=60, aspectRatio=1, near=0.01,
                        far=100):
        # convert angle of view to radians
        a = angleOfView * (pi / 180)
        d = 1.0 / tan(a / 2)
        r = aspectRatio
        b = (far + near) / (near - far)
        c = 2 * far * near / (near - far)

        return np.array([
            [d / r, 0, 0, 0],
            [0, d, 0, 0],
            [0, 0, b, c],
            [0, 0, -1, 0]
        ]).astype(float)
