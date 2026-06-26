from OpenGL.GL import *


class AxisRenderer:
    def draw(self):
        glLineWidth(2.0)
        glBegin(GL_LINES)

        glColor3f(0.95, 0.25, 0.25)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(4.0, 0.0, 0.0)

        glColor3f(0.3, 0.95, 0.3)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 4.0, 0.0)

        glColor3f(0.35, 0.55, 1.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 4.0)

        glEnd()
        glLineWidth(1.0)
