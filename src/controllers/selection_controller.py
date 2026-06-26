class SelectionController:
    def __init__(self, picking_renderer):
        self.picking_renderer = picking_renderer

    def pick_cube(self, mouse_pos, grid, rotation_matrix):
        cube_id = self.picking_renderer.pick(mouse_pos, grid, rotation_matrix)
        if cube_id < 0:
            return None
        return grid.get_cube_by_id(cube_id)
