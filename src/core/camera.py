from OpenGL.GL import *

from src.config.settings import CAMERA_DISTANCE, ORTHO_HALF_SIZE


class Camera:
    def __init__(self, ortho_half_size: float = ORTHO_HALF_SIZE, distance: float = CAMERA_DISTANCE):
        self.ortho_half_size = ortho_half_size
        self.distance = distance

    def setup(self, width: int, height: int) -> None:
        aspect = width / height if height else 1.0
        half_height = self.ortho_half_size
        half_width = self.ortho_half_size * aspect

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-half_width, half_width, -half_height, half_height, -50.0, 50.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def resize_projection(self, width: int, height: int) -> None:
        self.setup(width, height)

    def apply_view(self, rotation_matrix) -> None:
        from src.utils.matrix_utils import flatten_column_major

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -self.distance)
        glMultMatrixf(flatten_column_major(rotation_matrix))
