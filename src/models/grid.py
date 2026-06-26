from __future__ import annotations

from src.models.cube import Cube


class Grid:
    def __init__(self, cubes: list[Cube]):
        self.cubes = cubes
        self._cube_by_id = {cube.cube_id: cube for cube in cubes}

    def get_all_cubes(self) -> list[Cube]:
        return list(self.cubes)

    def get_active_cubes(self) -> list[Cube]:
        return [cube for cube in self.cubes if not cube.removed]

    def get_pickable_cubes(self) -> list[Cube]:
        return [cube for cube in self.cubes if cube.selectable]

    def get_cube_by_id(self, cube_id: int) -> Cube | None:
        return self._cube_by_id.get(cube_id)

    def get_cube_at_position(self, position: tuple[int, int, int]) -> Cube | None:
        for cube in self.get_active_cubes():
            if cube.position == position:
                return cube
        return None

    def is_occupied(self, position: tuple[int, int, int], exclude: Cube | None = None) -> bool:
        for cube in self.get_active_cubes():
            if cube is exclude:
                continue
            if cube.selectable and cube.position == position:
                return True
        return False

    def update(self, dt: float) -> list[Cube]:
        finished: list[Cube] = []
        for cube in self.cubes:
            if cube.update(dt):
                finished.append(cube)
        return finished

    def remaining(self) -> int:
        return sum(1 for cube in self.cubes if not cube.removed)

    def solved(self) -> bool:
        return self.remaining() == 0
