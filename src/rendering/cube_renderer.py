# src/rendering/cube_renderer.py

from OpenGL.GL import *

class CubeRenderer:

    def draw_cube(self):
        glBegin(GL_QUADS)

        # FRONT (red)
        glColor3f(1, 0, 0)
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        glVertex3f( 0.5,  0.5,  0.5)
        glVertex3f(-0.5,  0.5,  0.5)

        # BACK (green)
        glColor3f(0, 1, 0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5,  0.5, -0.5)
        glVertex3f( 0.5,  0.5, -0.5)
        glVertex3f( 0.5, -0.5, -0.5)

        # LEFT (blue)
        glColor3f(0, 0, 1)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f(-0.5,  0.5,  0.5)
        glVertex3f(-0.5,  0.5, -0.5)

        # RIGHT (yellow)
        glColor3f(1, 1, 0)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5,  0.5, -0.5)
        glVertex3f(0.5,  0.5,  0.5)
        glVertex3f(0.5, -0.5,  0.5)

        # TOP (magenta)
        glColor3f(1, 0, 1)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f(-0.5, 0.5,  0.5)
        glVertex3f( 0.5, 0.5,  0.5)
        glVertex3f( 0.5, 0.5, -0.5)

        # BOTTOM (cyan)
        glColor3f(0, 1, 1)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        glVertex3f(-0.5, -0.5,  0.5)

        glEnd()