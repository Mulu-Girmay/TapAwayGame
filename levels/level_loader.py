from src.models.cube import Cube
from src.models.grid import Grid


LEVELS = [
    {
        "name": "Warmup",
        "subtitle": "A compact opener with one obvious escape line at a time.",
        "cubes": [
            ((0, 0, 0), (1, 0, 0)),
            ((1, 0, 0), (1, 0, 0)),
            ((2, 0, 0), (1, 0, 0)),
            ((0, 1, 0), (0, 1, 0)),
            ((0, 2, 0), (0, 1, 0)),
            ((0, -1, 0), (0, -1, 0)),
            ((0, 0, 1), (0, 0, 1)),
        ],
    },
    {
        "name": "Lanes",
        "subtitle": "Two independent lanes, one horizontal and one vertical.",
        "cubes": [
            ((-2, 0, 0), (1, 0, 0)),
            ((-1, 0, 0), (1, 0, 0)),
            ((0, 0, 0), (1, 0, 0)),
            ((1, 0, 0), (1, 0, 0)),
            ((0, -2, 0), (0, 1, 0)),
            ((0, -1, 0), (0, 1, 0)),
            ((0, 1, 0), (0, 1, 0)),
            ((0, 2, 0), (0, 1, 0)),
            ((-1, 1, 0), (-1, 0, 0)),
        ],
    },
    {
        "name": "Stack",
        "subtitle": "A vertical column with side exits that open up in sequence.",
        "cubes": [
            ((0, 0, -1), (0, 0, 1)),
            ((0, 0, 0), (0, 0, 1)),
            ((0, 0, 1), (0, 0, 1)),
            ((0, 0, 2), (0, 0, 1)),
            ((1, 0, 0), (1, 0, 0)),
            ((2, 0, 0), (1, 0, 0)),
            ((-1, 0, 0), (-1, 0, 0)),
            ((0, 1, 1), (0, 1, 0)),
            ((0, 2, 1), (0, 1, 0)),
        ],
    },
    {
        "name": "Crossfire",
        "subtitle": "Three little arms intersecting around the center block.",
        "cubes": [
            ((-2, 0, 0), (1, 0, 0)),
            ((-1, 0, 0), (1, 0, 0)),
            ((0, 0, 0), (1, 0, 0)),
            ((1, 0, 0), (1, 0, 0)),
            ((0, -2, 0), (0, 1, 0)),
            ((0, -1, 0), (0, 1, 0)),
            ((0, 1, 0), (0, 1, 0)),
            ((0, 2, 0), (0, 1, 0)),
            ((0, 0, -2), (0, 0, 1)),
            ((0, 0, -1), (0, 0, 1)),
            ((0, 0, 1), (0, 0, 1)),
        ],
    },
    {
        "name": "Spiral",
        "subtitle": "A denser board that forces you to read the outer shell first.",
        "cubes": [
            ((-2, -1, 0), (1, 0, 0)),
            ((-1, -1, 0), (1, 0, 0)),
            ((0, -1, 0), (1, 0, 0)),
            ((1, -1, 0), (1, 0, 0)),
            ((1, 0, 0), (0, 1, 0)),
            ((1, 1, 0), (0, 1, 0)),
            ((0, 1, 0), (-1, 0, 0)),
            ((-1, 1, 0), (-1, 0, 0)),
            ((-1, 0, 0), (0, -1, 0)),
            ((0, 0, 0), (0, 0, 1)),
            ((0, 0, 1), (0, 0, 1)),
            ((0, 0, 2), (0, 0, 1)),
        ],
    },
    {
        "name": "Finale",
        "subtitle": "The largest board in the set, mixing three axes and deeper chains.",
        "cubes": [
            ((-3, 0, 0), (1, 0, 0)),
            ((-2, 0, 0), (1, 0, 0)),
            ((-1, 0, 0), (1, 0, 0)),
            ((0, 0, 0), (1, 0, 0)),
            ((1, 0, 0), (1, 0, 0)),
            ((2, 0, 0), (1, 0, 0)),
            ((0, -2, 0), (0, 1, 0)),
            ((0, -1, 0), (0, 1, 0)),
            ((0, 1, 0), (0, 1, 0)),
            ((0, 2, 0), (0, 1, 0)),
            ((0, 0, -2), (0, 0, 1)),
            ((0, 0, -1), (0, 0, 1)),
            ((0, 0, 1), (0, 0, 1)),
            ((0, 0, 2), (0, 0, 1)),
            ((1, 1, 0), (1, 0, 0)),
            ((2, 1, 0), (1, 0, 0)),
        ],
    },
]


def _build_grid(level_index: int) -> tuple[Grid, dict]:
    level = LEVELS[level_index % len(LEVELS)]
    cubes = [
        Cube(cube_id=index, position=position, direction=direction)
        for index, (position, direction) in enumerate(level["cubes"])
    ]
    return Grid(cubes), level


def load_level(level_index: int) -> tuple[Grid, str, str]:
    grid, level = _build_grid(level_index)
    return grid, level["name"], level["subtitle"]


def level_count() -> int:
    return len(LEVELS)
