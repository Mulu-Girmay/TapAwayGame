import OpenGL.GL as gl

from src.rendering.cube_renderer import CubeRenderer
from src.utils.color_utils import color_to_id, id_to_color


class PickingRenderer:
    def __init__(self, width: int, height: int, camera):
        self.width = width
        self.height = height
        self.camera = camera
        self.cube_renderer = CubeRenderer()

        self.fbo = gl.glGenFramebuffers(1)
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, self.fbo)

        self.texture = gl.glGenTextures(1)
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture)
        gl.glTexImage2D(
            gl.GL_TEXTURE_2D,
            0,
            gl.GL_RGB,
            self.width,
            self.height,
            0,
            gl.GL_RGB,
            gl.GL_UNSIGNED_BYTE,
            None,
        )
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
        gl.glFramebufferTexture2D(
            gl.GL_FRAMEBUFFER,
            gl.GL_COLOR_ATTACHMENT0,
            gl.GL_TEXTURE_2D,
            self.texture,
            0,
        )

        self.depth_rbo = gl.glGenRenderbuffers(1)
        gl.glBindRenderbuffer(gl.GL_RENDERBUFFER, self.depth_rbo)
        gl.glRenderbufferStorage(gl.GL_RENDERBUFFER, gl.GL_DEPTH_COMPONENT24, self.width, self.height)
        gl.glFramebufferRenderbuffer(
            gl.GL_FRAMEBUFFER,
            gl.GL_DEPTH_ATTACHMENT,
            gl.GL_RENDERBUFFER,
            self.depth_rbo,
        )

        if gl.glCheckFramebufferStatus(gl.GL_FRAMEBUFFER) != gl.GL_FRAMEBUFFER_COMPLETE:
            raise RuntimeError("Framebuffer not complete")

        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, 0)

    def pick(self, mouse_pos, grid, rotation_matrix):
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, self.fbo)
        gl.glViewport(0, 0, self.width, self.height)
        gl.glClearColor(0.0, 0.0, 0.0, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glDisable(gl.GL_BLEND)
        gl.glEnable(gl.GL_DEPTH_TEST)

        self.camera.setup(self.width, self.height)
        self.camera.apply_view(rotation_matrix)

        for cube in grid.get_pickable_cubes():
            self.cube_renderer.draw_cube(
                cube,
                picking=True,
                solid_color=id_to_color(cube.cube_id),
            )

        cube_id = self.read_pixel(mouse_pos)
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, 0)
        return cube_id

    def read_pixel(self, mouse_pos):
        x, y = mouse_pos
        gl_y = self.height - y - 1

        x = max(0, min(self.width - 1, int(x)))
        gl_y = max(0, min(self.height - 1, int(gl_y)))

        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, self.fbo)
        gl.glReadBuffer(gl.GL_COLOR_ATTACHMENT0)
        data = gl.glReadPixels(x, gl_y, 1, 1, gl.GL_RGB, gl.GL_UNSIGNED_BYTE)
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, 0)

        if isinstance(data, (bytes, bytearray)):
            r, g, b = data[0], data[1], data[2]
        else:
            pixel = data[0][0]
            r, g, b = pixel[0], pixel[1], pixel[2]

        return color_to_id(r / 255.0, g / 255.0, b / 255.0)
