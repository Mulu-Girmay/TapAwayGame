from OpenGL.GL import *

from src.config.settings import WINDOW_HEIGHT, WINDOW_WIDTH
from src.rendering.axis_renderer import AxisRenderer
from src.rendering.cube_renderer import CubeRenderer


class Renderer:
    def __init__(self, camera):
        self.camera = camera
        self.cube_renderer = CubeRenderer()
        self.axis_renderer = AxisRenderer()

    def render(self, grid, rotation_matrix, selected_cube=None):
        glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.camera.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.camera.apply_view(rotation_matrix)

        self.axis_renderer.draw()

        selected_id = selected_cube.cube_id if selected_cube is not None else None
        for cube in grid.get_active_cubes():
            self.cube_renderer.draw_cube(
                cube,
                selected=(selected_id == cube.cube_id),
            )
