# src/core/camera.py

from OpenGL.GL import *

class Camera:
    def setup(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        # Orthographic projection (NO perspective)
        glOrtho(-10, 10, -10, 10, -20, 20)

        glMatrixMode(GL_MODELVIEW)