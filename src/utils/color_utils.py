def id_to_color(index: int) -> tuple:
    """
    Convert a cube index (0..) into an RGB color with components in [0.0, 1.0].
    Cube 0 -> (0,0,0) is reserved for "no cube". Cube 1 -> (1/255,0,0) ...
    """
    # Use index+1 so that background (index = -1) becomes black (0,0,0)
    i = index + 1
    return (
        (i & 0xFF) / 255.0,
        ((i >> 8) & 0xFF) / 255.0,
        ((i >> 16) & 0xFF) / 255.0
    )

def color_to_id(r: float, g: float, b: float) -> int:
    
    # Convert an RGB color (each in [0,1]) back to cube index.
    # Returns -1 if the color is black (background / no cube).
    # Convert to integer 0..255
    ri = int(round(r * 255))
    gi = int(round(g * 255))
    bi = int(round(b * 255))
    # Rebuild original index (stored as index+1)
    i = ri + (gi << 8) + (bi << 16)
    return i - 1   # -1 means no cube / background
