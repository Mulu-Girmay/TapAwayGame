from src.models.cube import Cube
from src.models.grid import Grid


LEVELS = [
    {
        "name": "Warmup",
        "cubes": [
            ((0, 0, 0), (1, 0, 0)),
            ((1, 0, 0), (1, 0, 0)),
            ((-1, 0, 0), (-1, 0, 0)),
            ((0, 1, 0), (0, 1, 0)),
            ((0, -1, 0), (0, -1, 0)),
            ((0, 0, 1), (0, 0, 1)),
            ((0, 0, -1), (0, 0, -1)),
        ],
    },
    {
        "name": "Chain",
        "cubes": [
            ((0, 0, 0), (1, 0, 0)),
            ((1, 0, 0), (1, 0, 0)),
            ((2, 0, 0), (1, 0, 0)),
            ((0, 1, 0), (0, 1, 0)),
            ((1, 1, 0), (0, 1, 0)),
            ((1, 2, 0), (0, 1, 0)),
            ((-1, 0, 0), (-1, 0, 0)),
            ((0, 0, 1), (0, 0, 1)),
        ],
    },
    {
        "name": "Stack",
        "cubes": [
            ((0, 0, 0), (0, 0, 1)),
            ((0, 0, 1), (0, 0, 1)),
            ((0, 0, 2), (0, 0, 1)),
            ((1, 0, 0), (1, 0, 0)),
            ((1, 1, 0), (1, 0, 0)),
            ((1, -1, 0), (1, 0, 0)),
            ((-1, 0, 0), (-1, 0, 0)),
            ((0, 1, 1), (0, 1, 0)),
            ((0, -1, 1), (0, -1, 0)),
        ],
    },
]


def load_level(level_index: int) -> tuple[Grid, str]:
    level = LEVELS[level_index % len(LEVELS)]
    cubes = [
        Cube(cube_id=index, position=position, direction=direction)
        for index, (position, direction) in enumerate(level["cubes"])
    ]
    return Grid(cubes), level["name"]


def level_count() -> int:
    return len(LEVELS)
