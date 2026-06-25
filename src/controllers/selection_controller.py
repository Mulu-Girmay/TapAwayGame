# class SelectionController: 
#     def init(self, grid): 
#         self.grid = grid 
#     def pick_cube(self, mouse_pos): 
#         x, y = mouse_pos 
# # placeholder logic (real version uses OpenGL readPixels) 
#     return self.grid.get_cube_at_index(0)

# src/controllers/selection_controller.py

from src.rendering.picking_renderer import PickingRenderer
from src.utils.color_utils import id_to_color, color_to_id

class SelectionController:
    def __init__(self, grid, screen_width: int, screen_height: int):
        self.grid = grid
        self.picking_renderer = PickingRenderer(screen_width, screen_height)

    def pick_cube(self, mouse_pos: tuple[int, int]) -> int:
        # mouse_pos: (x, y) in window coordinates (top‑left origin).
        # Returns the index of the cube under the cursor, or -1 if none.
        x, y = mouse_pos
        # First, render all cubes into the picking buffer
        # We need a list of cubes – get from grid
        cubes = self.grid.get_all_cubes()   # you must implement this
        self.picking_renderer.render_picking(cubes, self.grid)

        # Then read the pixel under the mouse
        index = self.picking_renderer.read_pixel(x, y)
        return index
