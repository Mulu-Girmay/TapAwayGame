# src/rendering/picking_renderer.py

import OpenGL.GL as gl
import numpy as np
from src.utils.color_utils import id_to_color, color_to_id

class PickingRenderer:
    
    # Off-screen renderer that draws cubes with unique colour IDs.
    # After drawing, you can query a pixel to find which cube is there.
    

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        # Create a framebuffer object
        self.fbo = gl.glGenFramebuffers(1)
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, self.fbo)

        # Create a texture to store the colour data
        self.texture = gl.glGenTextures(1)
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture)
        gl.glTexImage2D(
            gl.GL_TEXTURE_2D, 0, gl.GL_RGB,
            self.width, self.height, 0,
            gl.GL_RGB, gl.GL_UNSIGNED_BYTE, None
        )
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
        gl.glFramebufferTexture2D(
            gl.GL_FRAMEBUFFER, gl.GL_COLOR_ATTACHMENT0,
            gl.GL_TEXTURE_2D, self.texture, 0
        )

        # Also need a depth buffer (optional but good practice)
        self.depth_rbo = gl.glGenRenderbuffers(1)
        gl.glBindRenderbuffer(gl.GL_RENDERBUFFER, self.depth_rbo)
        gl.glRenderbufferStorage(gl.GL_RENDERBUFFER, gl.GL_DEPTH_COMPONENT24,
                                 self.width, self.height)
        gl.glFramebufferRenderbuffer(gl.GL_FRAMEBUFFER, gl.GL_DEPTH_ATTACHMENT,
                                     gl.GL_RENDERBUFFER, self.depth_rbo)

        # Check completeness
        if gl.glCheckFramebufferStatus(gl.GL_FRAMEBUFFER) != gl.GL_FRAMEBUFFER_COMPLETE:
            raise RuntimeError("Framebuffer not complete!")
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, 0)   # unbind

    def render_picking(self, cubes, grid):
        # 
        # Render all cubes into the off‑screen FBO with their ID colours.
        # cubes: list of Cube objects that have a method `render_id_colour()`
        #        (which should set the colour using id_to_color(cube.index))
        # grid:   not directly used here, but could provide transformation.
        # 
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, self.fbo)
        gl.glViewport(0, 0, self.width, self.height)

        gl.glClearColor(0.0, 0.0, 0.0, 1.0)   # background = black → index -1
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        # Enable depth test (so cubes behind are hidden)
        gl.glEnable(gl.GL_DEPTH_TEST)

        # Set orthographic projection (since this is an orthographic puzzle)
        # You'll need to adjust these values to match your game's camera.
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        # Example: ortho from (-10,10) in X and Y, near=0.1 far=100
        gl.glOrtho(-10, 10, -10, 10, 0.1, 100)

        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        # Set camera position (e.g., looking down Z axis)
        gl.gluLookAt(0, 0, 5,  0, 0, 0,  0, 1, 0)

        # Now draw each cube with its picking colour
        for cube in cubes:
            # Set colour from cube.index
            r, g, b = id_to_color(cube.index)
            gl.glColor3f(r, g, b)
            # Render the cube geometry (assume cube.draw() uses current colour)
            cube.draw()   # you must implement cube.draw() to draw its mesh

        # Restore normal rendering target
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, 0)

    def read_pixel(self, x: int, y: int) -> int:
        # 
        # Return the cube index at pixel (x, y) in window coordinates.
        # y is typically inverted: OpenGL (0,0) is bottom‑left, window (0,0) is top‑left.
        # So we need to flip y.
        # 
        # Flip y: window y → OpenGL y
        gl_y = self.height - y

        # Bind the FBO to read from it
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, self.fbo)
        gl.glReadBuffer(gl.GL_COLOR_ATTACHMENT0)
        
            # Read a single pixel
        data = gl.glReadPixels(x, gl_y, 1, 1, gl.GL_RGB, gl.GL_FLOAT)
        # data is a numpy array of shape (1,1,3) with floats in [0,1]
        pixel = data[0][0]   # (r, g, b)
        r, g, b = pixel

        index = color_to_id(r, g, b)
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, 0)
        return index   # -1 if no cube

