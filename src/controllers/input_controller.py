import math

import pygame

from src.config.settings import DRAG_THRESHOLD


class InputController:
    def __init__(self, rotation_controller, on_pick, on_restart, on_next_level):
        self.rotation_controller = rotation_controller
        self.on_pick = on_pick
        self.on_restart = on_restart
        self.on_next_level = on_next_level
        self.drag_start_pos = None
        self.last_pos = None
        self.dragging = False

    def process(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.drag_start_pos = event.pos
            self.last_pos = event.pos
            self.dragging = False

        elif event.type == pygame.MOUSEMOTION and self.drag_start_pos is not None:
            if self.last_pos is None:
                self.last_pos = event.pos

            dx = event.pos[0] - self.last_pos[0]
            dy = event.pos[1] - self.last_pos[1]

            distance = math.dist(self.drag_start_pos, event.pos)
            if self.dragging or distance >= DRAG_THRESHOLD:
                self.dragging = True
                self.rotation_controller.rotate(dx, dy)

            self.last_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.drag_start_pos is not None and not self.dragging:
                self.on_pick(event.pos)

            self.drag_start_pos = None
            self.last_pos = None
            self.dragging = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.on_restart()
            elif event.key == pygame.K_n:
                self.on_next_level()
