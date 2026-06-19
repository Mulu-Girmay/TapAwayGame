# src/core/app.py

import pygame
from pygame.locals import *

from OpenGL.GL import *

from src.core.renderer import Renderer
from src.core.camera import Camera
from src.config.settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS


class App:

    def __init__(self):
        pygame.init()

        pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            DOUBLEBUF | OPENGL
        )

        glEnable(GL_DEPTH_TEST)

        self.camera = Camera()
        self.camera.setup()

        self.renderer = Renderer()

        self.clock = pygame.time.Clock()
        self.running = True

        print("App started successfully")

    def run(self):

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.renderer.render()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()