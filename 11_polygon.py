"""
     render a polygon geometry
"""

from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh

from geometry.polygonGeometry import PolygonGeometry
from material.surfaceBasicMaterial import SurfaceBasicMaterial


# render a scene
class Test(Base):

    def __init__(self):
        super().__init__()
        self.mesh = None
        self.camera = None
        self.scene = None
        self.renderer = None

    def initialize(self):
        print("Initializing Program ... ")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera()
        # pull camera towards viewer
        self.camera.setPosition(0, 0, 4)

        geometry = PolygonGeometry(sides=7)
        material = SurfaceBasicMaterial({"useVertexColors": 1})
        self.mesh = Mesh(geometry, material)

        self.scene.add(self.mesh)

    def update(self):
        self.renderer.render(self.scene, self.camera)


# instantiate and run the class
Test().run()
