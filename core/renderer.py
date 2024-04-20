"""
    Rendered class, which performs general OpenGL initialization tasks,
    and contains a function named render, which takes a Scene and a Camera
    object as input, and performs all rendering related tasks from earlier
    examples.
"""

from OpenGL.GL import *
from core.mesh import Mesh



class Renderer(object):

    def __init__(self, clearColor=None):
        if clearColor is None:
            clearColor = [0, 0, 0]
        glEnable(GL_DEPTH_TEST)
        glClearColor(clearColor[0], clearColor[1], clearColor[2], 1.0)

    def render(self, scene, camera):
        # clear buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # update camera view
        camera.updateViewMatrix()

        # extract a list of Mesh objects from the scene
        descendentList = scene.getDescendentList()
        # filter the mesh list
        meshFilter = lambda x: isinstance(x, Mesh)
        # create a list of mesh object
        meshList = list(filter(meshFilter, descendentList))

        for mesh in meshList:
            # if mesh is not visible, continue to next object in list
            if not mesh.visibility:
                continue

            glUseProgram(mesh.material.programRef)

            # bind VAO
            glBindVertexArray(mesh.vaoRef)

            # update uniform matrices
            mesh.material.uniforms["modelMatrix"].data = mesh.getWorldMatrix()
            mesh.material.uniforms["viewMatrix"].data = camera.viewMatrix
            mesh.material.uniforms["projectionMatrix"].data = (
                camera.projectionMatrix)

            # upload all data from all uniforms to the GPU
            # update uniforms stored in material
            for variableName, uniformObject in mesh.material.uniforms.items():
                uniformObject.uploadData()
            # update render settings
            mesh.material.updateRenderSettings()

            glDrawArrays( mesh.material.settings["drawStyle"], 0,
                          mesh.geometry.vertexCount )




