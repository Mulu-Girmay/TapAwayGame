def check_win(self, grid):
    if len(grid.get_active_cubes()) == 0:
        self.won = True