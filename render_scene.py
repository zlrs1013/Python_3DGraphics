"""
     create an application that displays a spinning cube using the graphics
     framework.

     creating an app typically requires at least 7 classes:
     - base, renderer, scene, camera, mesh, geometry, material
     - more advanced: light
"""

from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh

from geometry.boxGeometry import BoxGeometry
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

        geometry = BoxGeometry()
        material = SurfaceBasicMaterial({"useVertexColors": 1})
        self.mesh = Mesh(geometry, material)

        self.scene.add(self.mesh)

        # pull camera towards viewer
        self.camera.setPosition(0, 0, 4)

        # add a yellow box backdrop
        backGeometry = BoxGeometry(width=2, height=2, depth=0.01)
        backMaterial = SurfaceBasicMaterial({"baseColor": [1, 1, 0]})
        backdrop = Mesh(backGeometry, backMaterial)
        self.scene.add(backdrop)

    def update(self):

        # animation
        self.mesh.rotateX( 0.02 )
        self.mesh.rotateY( 0.02 )

        self.renderer.render(self.scene, self.camera)


# instantiate and run the class
Test().run()

