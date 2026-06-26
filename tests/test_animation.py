import pathlib
import sys
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


from levels.level_loader import LEVELS, load_level
from levels.path_checker import can_exit
from src.controllers.animation_controller import AnimationController
from src.models.cube import Cube
from src.models.grid import Grid


class TapAwayLogicTests(unittest.TestCase):
    def test_blocked_cube_cannot_exit(self):
        grid = Grid(
            [
                Cube(0, (0, 0, 0), (1, 0, 0)),
                Cube(1, (1, 0, 0), (1, 0, 0)),
            ]
        )

        self.assertFalse(can_exit(grid.get_cube_by_id(0), grid))
        self.assertTrue(can_exit(grid.get_cube_by_id(1), grid))

    def test_animation_removes_cube(self):
        cube = Cube(0, (0, 0, 0), (1, 0, 0))
        controller = AnimationController()

        self.assertTrue(controller.add_animation(cube))
        self.assertEqual(cube.state, "moving")

        controller.update(2.0)

        self.assertEqual(cube.state, "removed")
        self.assertFalse(controller.busy)

    def test_level_loader_returns_playable_grid(self):
        grid, name, subtitle = load_level(0)

        self.assertTrue(name)
        self.assertTrue(subtitle)
        self.assertGreater(grid.remaining(), 0)
        self.assertGreater(len(grid.get_pickable_cubes()), 0)

    def test_all_levels_are_solvable(self):
        for index in range(len(LEVELS)):
            grid, _, _ = load_level(index)
            progress = True
            safety = 0

            while progress and not grid.solved() and safety < 200:
                progress = False
                for cube in list(grid.get_pickable_cubes()):
                    if can_exit(cube, grid):
                        cube.start_exit()
                        cube.state = "removed"
                        progress = True
                        safety += 1
                        break

            self.assertTrue(grid.solved(), msg=f"Level {index} did not solve")


if __name__ == "__main__":
    unittest.main()
