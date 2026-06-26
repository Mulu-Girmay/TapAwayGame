def can_exit(cube, grid):

    x, y, z = cube.position
    dx, dy, dz = cube.direction

    for other in grid.get_active_cubes():

        if other == cube:
            continue

        if other.position == (x+dx, y+dy, z+dz):
            return False

    return True