# src/core/renderer.py

from OpenGL.GL import *

from src.rendering.cube_renderer import CubeRenderer
from src.rendering.axis_renderer import AxisRenderer


class Renderer:

    def __init__(self):
        self.cube = CubeRenderer()
        self.axis = AxisRenderer()

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Move camera slightly back
        glTranslatef(0, 0, -8)

        self.axis.draw()

        # draw cube in center
        self.cube.draw_cube()