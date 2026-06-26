def can_exit(cube, grid) -> bool:
    """
    A cube can exit when no other active cube sits in front of it on the
    direction axis.
    """

    if not cube.selectable:
        return False

    ox, oy, oz = cube.position
    dx, dy, dz = cube.direction

    if (dx, dy, dz) == (0, 0, 0):
        return False

    for other in grid.get_active_cubes():
        if other is cube:
            continue

        x, y, z = other.position

        if dx and y == oy and z == oz and (x - ox) * dx > 0:
            return False

        if dy and x == ox and z == oz and (y - oy) * dy > 0:
            return False

        if dz and x == ox and y == oy and (z - oz) * dz > 0:
            return False

    return True
