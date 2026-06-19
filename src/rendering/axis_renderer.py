# src/rendering/axis_renderer.py

from OpenGL.GL import *

class AxisRenderer:

    def draw(self):
        glBegin(GL_LINES)

        # X axis (red)
        glColor3f(1, 0, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(5, 0, 0)

        # Y axis (green)
        glColor3f(0, 1, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 5, 0)

        # Z axis (blue)
        glColor3f(0, 0, 1)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 5)

        glEnd()