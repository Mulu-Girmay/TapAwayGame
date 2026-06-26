def id_to_color(index: int) -> tuple[float, float, float]:
    """
    Convert a cube id into a unique RGB color.
    """

    value = index + 1
    return (
        (value & 0xFF) / 255.0,
        ((value >> 8) & 0xFF) / 255.0,
        ((value >> 16) & 0xFF) / 255.0,
    )


def color_to_id(r: float, g: float, b: float) -> int:
    """
    Convert a picking color back into a cube id.
    """

    ri = int(round(r * 255))
    gi = int(round(g * 255))
    bi = int(round(b * 255))
    value = ri + (gi << 8) + (bi << 16)
    return value - 1
