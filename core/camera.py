"""
    Camera class represents virtual camera used to view the scene. Camera
    transform affects apparent placement of the objects in rendered image of
    the scene. Each camera transformation affects scene objects in the
    opposite way mathematically: define view matrix as inverse of camera
    transform matrix.
"""

from core.object3D import Object3D
from core.matrix import Matrix
from numpy.linalg import inv # calculate inverse of a matrix


class Camera(Object3D):

    def __init__(self, angleOfView=60, aspectRatio=1, near=0.1, far=100):
        super().__init__()
        self.projectionMatrix = Matrix.makePerspective(
            angleOfView, aspectRatio, near, far)
        self.viewMatrix = Matrix.makeIdentity()

    def updateViewMatrix(self):
        # in case camera is attached to something else rather than the root
        self.viewMatrix = inv(self.getWorldMatrix())

