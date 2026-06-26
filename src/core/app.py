import pygame
from pygame.locals import DOUBLEBUF, OPENGL

from OpenGL.GL import *

from levels.level_loader import level_count, load_level
from levels.path_checker import can_exit
from src.config.settings import BACKGROUND_COLOR, FPS, WINDOW_HEIGHT, WINDOW_WIDTH
from src.controllers.animation_controller import AnimationController
from src.controllers.input_controller import InputController
from src.controllers.rotation_controller import RotationController
from src.controllers.selection_controller import SelectionController
from src.core.camera import Camera
from src.core.renderer import Renderer
from src.models.game_state import GameState
from src.rendering.picking_renderer import PickingRenderer


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)

        glEnable(GL_DEPTH_TEST)
        glClearColor(*BACKGROUND_COLOR)

        self.camera = Camera()
        self.rotation = RotationController()
        self.animation = AnimationController()
        self.game_state = GameState()

        self.grid, self.level_name = load_level(0)
        self.game_state.reset_for_level(0, self.level_name, self.grid.remaining())
        self.selected_cube = None

        self.renderer = Renderer(self.camera)
        self.picking_renderer = PickingRenderer(WINDOW_WIDTH, WINDOW_HEIGHT, self.camera)
        self.selection = SelectionController(self.picking_renderer)
        self.input = InputController(self.rotation, self.handle_pick, self.restart_level, self.next_level)

        self.clock = pygame.time.Clock()
        self.running = True
        self._update_caption()

    def handle_pick(self, mouse_pos):
        if self.game_state.won:
            return

        cube = self.selection.pick_cube(mouse_pos, self.grid, self.rotation.matrix)
        if cube is None:
            return

        if can_exit(cube, self.grid):
            if self.animation.add_animation(cube):
                self.selected_cube = cube
                self.game_state.record_move()

    def restart_level(self):
        self.grid, self.level_name = load_level(self.game_state.level_index)
        self.animation = AnimationController()
        self.rotation.reset()
        self.selected_cube = None
        self.game_state.reset_for_level(self.game_state.level_index, self.level_name, self.grid.remaining())
        self._update_caption()

    def next_level(self):
        next_index = (self.game_state.level_index + 1) % level_count()
        self.grid, self.level_name = load_level(next_index)
        self.animation = AnimationController()
        self.rotation.reset()
        self.selected_cube = None
        self.game_state.reset_for_level(next_index, self.level_name, self.grid.remaining())
        self._update_caption()

    def _update_caption(self):
        status = "Solved" if self.game_state.won else "Playing"
        pygame.display.set_caption(
            f"Tap Away | Level {self.game_state.level_index + 1}: {self.level_name} | "
            f"Moves {self.game_state.moves} | Remaining {self.game_state.remaining} | {status}"
        )

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.input.process(event)

            self.animation.update(dt)
            self.game_state.sync_remaining(self.grid.remaining())

            if self.selected_cube is not None and self.selected_cube.removed:
                self.selected_cube = None

            self.renderer.render(self.grid, self.rotation.matrix, selected_cube=self.selected_cube)
            self._update_caption()
            pygame.display.flip()

        pygame.quit()
