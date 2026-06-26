from OpenGL.GL import *

from src.config.settings import CUBE_SIZE


class CubeRenderer:
    def __init__(self):
        self.half = CUBE_SIZE / 2.0
        self.palette = [
            (0.92, 0.46, 0.35),
            (0.46, 0.70, 0.96),
            (0.46, 0.86, 0.62),
            (0.96, 0.79, 0.38),
            (0.82, 0.55, 0.94),
            (0.36, 0.82, 0.82),
            (0.94, 0.58, 0.74),
            (0.79, 0.79, 0.79),
        ]

    def draw_cube(self, cube, picking: bool = False, selected: bool = False, solid_color=None):
        x, y, z = cube.world_position

        glPushMatrix()
        glTranslatef(x, y, z)
        glScalef(CUBE_SIZE, CUBE_SIZE, CUBE_SIZE)

        if picking:
            color = solid_color if solid_color is not None else (1.0, 1.0, 1.0)
            self._draw_solid(color)
        else:
            self._draw_shaded(cube, selected=selected)
            self._draw_outline(selected=selected)
            self._draw_direction_marker(cube.direction)

        glPopMatrix()

    def _draw_shaded(self, cube, selected: bool = False):
        base = self.palette[cube.cube_id % len(self.palette)]
        factor = 1.18 if selected else 1.0
        front = self._shade(base, 1.06 * factor)
        back = self._shade(base, 0.72 * factor)
        left = self._shade(base, 0.82 * factor)
        right = self._shade(base, 0.90 * factor)
        top = self._shade(base, 1.22 * factor)
        bottom = self._shade(base, 0.64 * factor)

        glBegin(GL_QUADS)

        glColor3f(*front)
        glVertex3f(-self.half, -self.half,  self.half)
        glVertex3f( self.half, -self.half,  self.half)
        glVertex3f( self.half,  self.half,  self.half)
        glVertex3f(-self.half,  self.half,  self.half)

        glColor3f(*back)
        glVertex3f(-self.half, -self.half, -self.half)
        glVertex3f(-self.half,  self.half, -self.half)
        glVertex3f( self.half,  self.half, -self.half)
        glVertex3f( self.half, -self.half, -self.half)

        glColor3f(*left)
        glVertex3f(-self.half, -self.half, -self.half)
        glVertex3f(-self.half, -self.half,  self.half)
        glVertex3f(-self.half,  self.half,  self.half)
        glVertex3f(-self.half,  self.half, -self.half)

        glColor3f(*right)
        glVertex3f(self.half, -self.half, -self.half)
        glVertex3f(self.half,  self.half, -self.half)
        glVertex3f(self.half,  self.half,  self.half)
        glVertex3f(self.half, -self.half,  self.half)

        glColor3f(*top)
        glVertex3f(-self.half, self.half, -self.half)
        glVertex3f(-self.half, self.half,  self.half)
        glVertex3f(self.half, self.half,  self.half)
        glVertex3f(self.half, self.half, -self.half)

        glColor3f(*bottom)
        glVertex3f(-self.half, -self.half, -self.half)
        glVertex3f(self.half, -self.half, -self.half)
        glVertex3f(self.half, -self.half,  self.half)
        glVertex3f(-self.half, -self.half,  self.half)

        glEnd()

    def _draw_solid(self, color):
        glBegin(GL_QUADS)
        glColor3f(*color)

        glVertex3f(-self.half, -self.half,  self.half)
        glVertex3f( self.half, -self.half,  self.half)
        glVertex3f( self.half,  self.half,  self.half)
        glVertex3f(-self.half,  self.half,  self.half)

        glVertex3f(-self.half, -self.half, -self.half)
        glVertex3f(-self.half,  self.half, -self.half)
        glVertex3f( self.half,  self.half, -self.half)
        glVertex3f( self.half, -self.half, -self.half)

        glVertex3f(-self.half, -self.half, -self.half)
        glVertex3f(-self.half, -self.half,  self.half)
        glVertex3f(-self.half,  self.half,  self.half)
        glVertex3f(-self.half,  self.half, -self.half)

        glVertex3f(self.half, -self.half, -self.half)
        glVertex3f(self.half,  self.half, -self.half)
        glVertex3f(self.half,  self.half,  self.half)
        glVertex3f(self.half, -self.half,  self.half)

        glVertex3f(-self.half, self.half, -self.half)
        glVertex3f(-self.half, self.half,  self.half)
        glVertex3f(self.half, self.half,  self.half)
        glVertex3f(self.half, self.half, -self.half)

        glVertex3f(-self.half, -self.half, -self.half)
        glVertex3f(self.half, -self.half, -self.half)
        glVertex3f(self.half, -self.half,  self.half)
        glVertex3f(-self.half, -self.half,  self.half)

        glEnd()

    def _draw_outline(self, selected: bool = False):
        color = (1.0, 0.95, 0.35) if selected else (0.12, 0.12, 0.14)
        glColor3f(*color)
        glLineWidth(2.0 if selected else 1.1)

        glBegin(GL_LINES)
        edges = [
            ((-self.half, -self.half, -self.half), (self.half, -self.half, -self.half)),
            ((self.half, -self.half, -self.half), (self.half, self.half, -self.half)),
            ((self.half, self.half, -self.half), (-self.half, self.half, -self.half)),
            ((-self.half, self.half, -self.half), (-self.half, -self.half, -self.half)),
            ((-self.half, -self.half, self.half), (self.half, -self.half, self.half)),
            ((self.half, -self.half, self.half), (self.half, self.half, self.half)),
            ((self.half, self.half, self.half), (-self.half, self.half, self.half)),
            ((-self.half, self.half, self.half), (-self.half, -self.half, self.half)),
            ((-self.half, -self.half, -self.half), (-self.half, -self.half, self.half)),
            ((self.half, -self.half, -self.half), (self.half, -self.half, self.half)),
            ((self.half, self.half, -self.half), (self.half, self.half, self.half)),
            ((-self.half, self.half, -self.half), (-self.half, self.half, self.half)),
        ]
        for start, end in edges:
            glVertex3f(*start)
            glVertex3f(*end)
        glEnd()
        glLineWidth(1.0)

    def _draw_direction_marker(self, direction):
        dx, dy, dz = direction
        glColor3f(0.1, 0.1, 0.1)
        glLineWidth(3.0)
        glBegin(GL_LINES)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(dx * self.half * 0.75, dy * self.half * 0.75, dz * self.half * 0.75)
        glEnd()
        glLineWidth(1.0)

    def _shade(self, color, factor):
        r, g, b = color
        return (
            min(1.0, r * factor),
            min(1.0, g * factor),
            min(1.0, b * factor),
        )
